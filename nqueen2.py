class Solution(object):
    def __init__(self):
        self.maps=[]
        self.count=0

    def totalNQueens(self, n):
        if len(self.maps)==n:
            self.count+=1
            print "OK", self.maps
            return
        for i in xrange(n):
            self.maps.append(i)
            #print "append:", i, "vector:", self.maps
            if self.valid():
                self.totalNQueens(n)
            self.maps.pop()
        return self.count

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

s=Solution()
print s.totalNQueens(4)