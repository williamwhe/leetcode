class Solution(object):
    def __init__(self):
        self.maps=[]
        self.retval=[]

    def solveNQueens(self, n):
        if len(self.maps)==n:
            self.retval.append(self.makestr(n))
            return
        for i in xrange(n):
            self.maps.append(i)
            if self.valid():
                self.solveNQueens(n)
            self.maps.pop()
        return self.retval

    def valid(self):
        if len(self.maps)<=1:
            return True
        pivot=len(self.maps)-1
        y=self.maps[-1]
        for i in xrange(pivot):
            if self.maps[-1]==self.maps[i]:
                return False
            if pivot-i==abs(self.maps[i]-y):
                return False
        return True

    def makestr(self,n):
        elem="."*n
        matrix=[]
        for i in xrange(n):
            matrix.append(list(elem))
        for i in xrange(n):
            matrix[i][self.maps[i]]='Q'
        retval=[]
        for m in matrix:
            retval.append("".join(m))
        return retval

print Solution().solveNQueens(5)