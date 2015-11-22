class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums)<s: return 0
        if sum(nums)==s: return len(nums)

print Solution().minSubArrayLen(7,[2,3,1,2,4,3])