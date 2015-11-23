import pdb

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
    	if len(strs) == 0:
    		return ""
    	res = strs[0]
        for str in strs[1:]:
        	res = self.commonPrefix(res, str)
        	if res == "":
        		return ""
        return res

    def commonPrefix(self, a, b):
    	res = ""
    	i = 0
    	while i < len(a) and i < len(b):
    		if a[i] == b[i]:
    			res += a[i]
    		else:
    			break
    		i += 1
    	return res

s = Solution()
arr = ["aca","cba"]
print s.longestCommonPrefix(arr)
arr = ["ab", "abc", "abcd"]
print s.longestCommonPrefix(arr)