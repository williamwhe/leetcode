import pdb

class Solution:
    # @return a string
    def countAndSay(self, n):
        num = "1"
        for i in range(1, n):
        	num = self.next(num)
        return num

    def next(self, num):
    	#pdb.set_trace()
    	res = ""
    	prev = num[0]
    	cnt = 1
    	for i in range(1, len(num)):
    		if num[i] == prev:
    			cnt += 1
    		else:
    			res += str(cnt)
    			res += num[i-1]
    			prev = num[i]
    			cnt = 1
    	res += str(cnt)
    	res += num[-1]
    	return res

s = Solution()
print s.countAndSay(1)	#1
print s.countAndSay(2)	#11
print s.countAndSay(3)	#21
print s.countAndSay(4)	#1211
print s.countAndSay(5)	#111221