import sys

class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums)<1: return 0
        retval,dp=1,[sys.maxint]*len(nums)
        for i in xrange(len(nums)):
            for j in xrange(i+1):
                if nums[i]>dp[j]: continue
                dp[j]=nums[i]
                retval=max(retval,j+1)
                break
        return retval

print Solution().lengthOfLIS([2,2])
print Solution().lengthOfLIS([10,9,2,5,3,7,101,18])