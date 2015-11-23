import copy

class Solution(object):
    def combinationSum3(self, k, n):
        retval = []
        self.dfs(k, n, 1, [], retval)
        return retval
    
    def dfs(self, k, n, s, tmp, retval):
        ##print "try", tmp, k, n, s
        if k==0 and n==0:
            ##print "ok", tmp
            retval.append(copy.copy(tmp))
            return
        if n < s or k==0 or n==0:
            return
        for i in range(s, n+1):
            if i > 9:
                continue
            tmp.append(i)
            self.dfs(k-1, n-i, i+1, tmp, retval)
            tmp.pop()
            
s=Solution()
print s.combinationSum3(3,15)