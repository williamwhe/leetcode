class Solution(object):
    def rob(self, nums):
        if len(nums)==1: return nums[0]
        return max(self.gao(nums[:-1]),self.gao(nums[1:]))

    def gao(self, nums):
        if len(nums)==0:
            return 0
        dp=[0]*len(nums)
        for i in range(len(nums)):
            if i>1:
                tmp=max(dp[i-2]+nums[i],dp[i-1])
            elif i>0:
                tmp=dp[i-1]
            else:
                tmp=0
            dp[i]=max(nums[i],tmp)
        return dp[-1]

print Solution().rob([2,1,5,6,2,3,9])