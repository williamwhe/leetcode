import math

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        if nums[0] != 0:
            return 0
        if nums[-1] != len(nums):
            return len(nums)
        alln=math.factorial(nums[-1])
        missn=1
        for ele in nums:
            if ele>0:
                missn*=ele
        return alln//missn