class Solution(object):
    def numIslands(self, grid):
        if grid is None or len(grid)==0 or len(grid[0])==0: return 0
        retval,nrow,ncol=set(),len(grid),len(grid[0])
        self.id=[-1]*nrow*ncol
        for i in xrange(nrow):
            for j in xrange(ncol):
                idx=i*ncol+j
                if grid[i][j]=="0": continue
                self.id[idx]=idx
                if i>0 and self.find((i-1)*ncol+j)!=-1: self.id[idx]=min(self.id[idx],self.find((i-1)*ncol+j))
                if i<nrow-1 and self.find((i+1)*ncol+j)!=-1: self.id[idx]=min(self.id[idx],self.find((i+1)*ncol+j))
                if j>0 and self.find(i*ncol+j-1)!=-1: self.id[idx]=min(self.id[idx],self.find(i*ncol+j-1))
                if j<ncol-1 and self.find(i*ncol+j+1)!=-1: self.id[idx]=min(self.id[idx],self.find(i*ncol+j+1))
        for j in xrange(ncol-1,-1,-1):
            for i in xrange(nrow-1,-1,-1):
                idx=i*ncol+j
                if self.id[idx]==-1: continue
                if i>0 and self.find((i-1)*ncol+j)!=-1: self.id[idx]=min(self.id[idx],self.find((i-1)*ncol+j))
                if i<nrow-1 and self.find((i+1)*ncol+j)!=-1: self.id[idx]=min(self.id[idx],self.find((i+1)*ncol+j))
                if j>0 and self.find(i*ncol+j-1)!=-1: self.id[idx]=min(self.id[idx],self.find(i*ncol+j-1))
                if j<ncol-1 and self.find(i*ncol+j+1)!=-1: self.id[idx]=min(self.id[idx],self.find(i*ncol+j+1))
        # for i in xrange(nrow):
        #     print self.id[i*ncol:(i+1)*ncol]
        for i in self.id:
            if i>-1: retval.add(self.find(i))
        return len(retval)

    def find(self, p):
        while p!=self.id[p] and p!=-1: p=self.id[p]
        return p

    def union(self, p, q):
        proot=self.find(p)
        qroot=self.find(q)
        if proot==qroot: return;
        if qroot==-1 or proot<qroot: self.id[qroot]=self.id[proot]
        elif proot==-1 or qroot<proot: self.id[proot]=self.id[qroot]

print Solution().numIslands(["10110010111101011110","01001010111111011011","10010101011011100110","01100110111100100011","11010010001010111011","00001011001001011110","10111101101101110010","01100010010111001101","00001101001101001010","00111010101110111110","10101110111010101011","00111101110100011101","11100000110111011110","00111001001111110110","00011000011010011111","01110100111110111001","00001111000010000110","11111111110110111111","01001001111110101111","00111110001111110110"])
# print Solution().numIslands(["111111","100001","101101","100001","111111"])
# print Solution().numIslands(["10111","10101","11101"])
# print Solution().numIslands(["111","010","111"])
# print Solution().numIslands(["10"])
# print Solution().numIslands(["1","1"])
# print Solution().numIslands(["10","01"])
# print Solution().numIslands(["11110","11010","11000","00000"])
# print Solution().numIslands(["11000","11000","00100","00011"])