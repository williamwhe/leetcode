import copy

class NumMatrix(object):
    def __init__(self, matrix):
        self.dp=copy.deepcopy(matrix)
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if i==0 and j==0: continue
                if i==0:
                    self.dp[i][j]+=self.dp[i][j-1]
                    continue
                if j==0:
                    self.dp[i][j]+=self.dp[i-1][j]
                    continue
                self.dp[i][j]+=self.dp[i][j-1]+self.dp[i-1][j]-self.dp[i-1][j-1]
        print self.dp

    def sumRegion(self, row1, col1, row2, col2):
        if row1==0 and col1==0: return self.dp[row2][col2]
        if row1==0: return self.dp[row2][col2]-self.dp[row2][col1-1]
        if col1==0: return self.dp[row2][col2]-self.dp[row1-1][col2]
        return self.dp[row2][col2]-self.dp[row1-1][col2]-self.dp[row2][col1-1]+self.dp[row1-1][col1-1]

nm=NumMatrix([[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],[1, 2, 0, 1, 5],[4, 1, 0, 1, 7],[1, 0, 3, 0, 5]])
print nm.sumRegion(0,0,0,0)
print nm.sumRegion(2, 1, 4, 3)# -> 8
print nm.sumRegion(1, 1, 2, 2)# -> 11
print nm.sumRegion(1, 2, 2, 4)# -> 12