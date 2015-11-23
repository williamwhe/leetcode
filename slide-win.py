class Solution(object):
    def maxSlidingWindow(self, nums, k):
        retval=[]
        if len(nums)==0 or k==0: return retval
        for i in xrange(len(nums)-k+1):
            retval.append(max(nums[i:i+k]))
        return retval

print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)