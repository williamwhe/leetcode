import collections

class Solution(object):
    def minSubArrayLen(self, s, nums):
        if sum(nums)<s: return 0
        retval,tsum,tmp=len(nums)+1,0,collections.deque()
        for i in xrange(len(nums)):
            tsum+=nums[i]
            tmp.append(nums[i])
            leftmost=-1
            while tsum>=s and len(tmp)>1:
                leftmost=tmp.popleft()
                tsum-=leftmost
            if leftmost!=-1 and tsum<s:
                tmp.appendleft(leftmost)
                tsum+=leftmost
            if tsum>=s:
                retval=min(retval,len(tmp))
        return retval

print Solution().minSubArrayLen(4,[1,4,4])
print Solution().minSubArrayLen(11,[1,2,3,4,5])
print Solution().minSubArrayLen(7,[2,3,1,2,4,3])