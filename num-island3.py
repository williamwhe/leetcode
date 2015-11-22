class Solution(object):
    def __init__(self):
        self.dx = [-1,0,0,1]
        self.dy = [0,1,-1,0]

    def numIslands(self, grid):
        if grid is None or len(grid)==0 or len(grid[0])==0: return 0
        islands,self.nrow,self.ncol=0,len(grid),len(grid[0])
        wgrid=[list(line) for line in grid]
        for i in xrange(self.nrow):
            for j in xrange(self.ncol):
                if wgrid[i][j]=='1':
                    self.gao(wgrid,i,j)
                    islands+=1
        return islands

    def gao(self, grid, i, j):
        grid[i][j]='x'
        for d in xrange(4):
            if i+self.dy[d]<self.nrow and i+self.dy[d]>=0 and j+self.dx[d]<self.ncol and j+self.dx[d]>=0 and grid[i+self.dy[d]][j+self.dx[d]]=='1':
                self.gao(grid,i+self.dy[d],j+self.dx[d])

# print Solution().numIslands(["10110010111101011110","01001010111111011011","10010101011011100110","01100110111100100011","11010010001010111011","00001011001001011110","10111101101101110010","01100010010111001101","00001101001101001010","00111010101110111110","10101110111010101011","00111101110100011101","11100000110111011110","00111001001111110110","00011000011010011111","01110100111110111001","00001111000010000110","11111111110110111111","01001001111110101111","00111110001111110110"])
print Solution().numIslands(["111111","100001","101101","100001","111111"])
print Solution().numIslands(["10111","10101","11101"])
print Solution().numIslands(["111","010","111"])
print Solution().numIslands(["10"])
print Solution().numIslands(["1","1"])
print Solution().numIslands(["10","01"])
print Solution().numIslands(["11110","11010","11000","00000"])
print Solution().numIslands(["11000","11000","00100","00011"])