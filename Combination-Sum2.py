import pdb

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        c=sorted(candidates)
        res=set()
        self.dfs(c,[],target,0,res)
        return list(map(list,res))
        
    def dfs(self, c, tmp, target, start, res):
        if target==0:
            res.add(tuple(tmp))
            return
        if start >= len(c) or c[start]>target:
            return
        for i in range(start,len(c)):
            if c[i]>target:
                break
            self.dfs(c,tmp+[c[i]],target-c[i],i+1,res)

s=Solution()
print s.combinationSum2([1], 2)