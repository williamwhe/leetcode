import copy

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        prev = [1,1]
        res = [[1],[1,1]]
        for i in range(2, numRows):
            curr = [1]
            for j in range(1, len(prev)):
                curr.append(prev[j-1]+prev[j])
            curr.append(1)
            res.append(curr)
            prev = copy.copy(curr)
        return res

s = Solution()
print s.generate(88)