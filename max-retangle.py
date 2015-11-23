import sys

class Solution(object):
    def maximalRectangle(self, matrix):
        if matrix is None: return 0
        retval,dp,nrow,ncol=0,[],len(matrix),len(matrix[0])
        if nrow==0: return 0
        for i in xrange(nrow):
            tmp,cnt=[],0
            for j in xrange(ncol):
                cnt=0 if matrix[i][j]=="0" else cnt+1
                tmp.append(cnt)
            dp.append(tmp)
        for j in xrange(ncol):
            mincol,mincon=sys.maxint,0
            for i in xrange(nrow):
                if dp[i][j]==0 and mincon>0:
                    mincol,mincon,retval=sys.maxint,0,max(retval, mincol*mincon)
                elif dp[i][j]>0:
                    mincol,mincon=min(mincol, dp[i][j]),mincon+1
            if mincon>0: retval=max(retval, mincol*mincon)
        return retval

print Solution().maximalRectangle(["01101","11010","01110","11110","11111","00000"])
# print Solution().maximalRectangle(["01","10"])
# print Solution().maximalRectangle(["011","110","011"])
# print Solution().maximalRectangle(["011","011","100"])