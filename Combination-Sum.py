import pdb

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        c=list(set(candidates))
        c.sort()
        res=[]
        self.dfs(c,[],target,0,res)
        return res
        
    def dfs(self, c, tmp, target, start, res):
        if target==0:
            res.append(tmp)
            return
        if c[start]>target:
            return
        for i in range(start,len(c)):
            if c[i]>target:
                break
            self.dfs(c,tmp+[c[i]],target-c[i],i,res)

s=Solution()
print s.combinationSum([1],1)