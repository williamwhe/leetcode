class Solution(object):
    def fourSum(self, nums, target):
        i,retval=0,[]
        nums.sort()
        if sum(nums[:4])>target or sum(nums[len(nums)-4:])<target: return retval
        while i<len(nums)-3:
            j=i+1
            while j<len(nums)-2:
                start,end=j+1,len(nums)-1
                while start<end:
                    if nums[i]+nums[j]+nums[start]+nums[end]==target:
                        retval.append([nums[i],nums[j],nums[start],nums[end]])
                        start+=1
                        end-=1
                        while start<end and nums[start]==nums[start-1]: start+=1
                        while start<end and nums[end]==nums[end+1]: end-=1
                    elif nums[i]+nums[j]+nums[start]+nums[end]<target:
                        start+=1
                        while start<end and nums[start]==nums[start-1]: start+=1
                    elif nums[i]+nums[j]+nums[start]+nums[end]>target:
                        end-=1
                        while start<end and nums[end]==nums[end+1]: end-=1
                j+=1
                while j<len(nums)-2 and nums[j]==nums[j-1]: j+=1
            i+=1
            while i<len(nums)-3 and nums[i]==nums[i-1]: i+=1
        return retval

print Solution().fourSum([1,0,-1,0,-2,2],0)