class Solution(object):
    def hIndex(self, citations):
        low = 0
        n = len(citations)
        high = n-1
        if n == 0:
            return 0
        while low < high and n > 1:
            mid = (low + high) // 2
            if n - mid == citations[mid]:
                low=mid
                break
            if n - mid < citations[mid]:
                high = mid
            else:
                low = mid+1
        return min(n-low, citations[low])
    
s=Solution()
print s.hIndex([1,2,2])
print s.hIndex([0])
print s.hIndex([100])
print s.hIndex([0,0])