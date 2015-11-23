class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        B = [A[0]]
        max = A[0]
        for i in range(1, len(A)):
            curr = A[i] if A[i] > A[i] + B[i-1] else A[i] + B[i-1]
            B.append(curr)
            if curr > max:
                max = curr
        return max

print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])