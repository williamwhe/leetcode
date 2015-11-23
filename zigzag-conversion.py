import pdb

class Solution:
    # @return a string
    def convert(self, s, nRows):
        arr = [""]*nRows
        i = curr = 0
        prev = -1
        for i in range(len(s)):
        	arr[curr] += s[i]
        	j = self.pos(curr, prev, nRows)
        	prev = curr
        	curr = j
        return "".join(arr)

    def pos(self, curr, prev, nRows):
    	if nRows < 2:
    		return 0
    	if curr == 0:
    		return 1
    	elif curr == nRows-1:
    		return nRows-2
    	elif curr > prev:
    		return curr+1
    	else:
    		return curr-1

s = Solution()
print s.convert("pnkuybqbwmvskxjmcspjztmtfmnxvlemaogarwbnizhuwtgalykmrygzktwhgctjsblkxnz", 26)
print s.convert("AB", 1)
print s.convert("PAYPALISHIRING", 3)
print s.convert("PAYPALISHIRING", 4)