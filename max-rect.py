class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or len(matrix)==0 or len(matrix[0])==0: return 0
        count,retval,dp=0,0,[]
        for i in xrange(len(matrix)):
            tmp=[]
            for j in xrange(len(matrix[0])):
                tmp.append(int(matrix[i][j]))
            dp.append(tmp)
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if i> 0 and dp[i][j]==1:
                    dp[i][j]=dp[i-1][j]+1
                    retval=max(retval,dp[i][j])
            retval=max(retval,self.maxhist(dp[i]))
        return retval

    def maxhist(self, height):
        i,retval,s=0,0,[]
        while i<len(height):
            while len(s)>0 and height[i]<height[s[-1]]:
                tmp=height[s.pop()]*(i if len(s)==0 else i-s[-1]-1)
                retval=max(retval,tmp)
            s.append(i)
            i+=1
        while len(s)>0:
            tmp=height[s.pop()]*(len(height) if len(s)==0 else len(height)-s[-1]-1)
            retval=max(retval,tmp)
        return retval

print Solution().maximalRectangle(["10100","10111","11111","10010"])
print Solution().maximalRectangle(["1010","1011","1011","1111"])
print Solution().maximalRectangle(["110101","010011","111101","111101"])
print Solution().maximalRectangle(["01","10"])
print Solution().maximalRectangle(["110","011","110"])