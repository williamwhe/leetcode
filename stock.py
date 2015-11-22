class Solution(object):
    def maxProfit(self, k, prices):
        if k>=len(prices)/2: return self.onlyone(prices)
        dp=[]
        for i in xrange(k+1): dp.append([0]*len(prices))
        for i in xrange(1,k+1):
            tmp=-prices[0]
            for j in xrange(1,len(prices)):
                dp[i][j]=max(dp[i][j-1],prices[j]+tmp)
                tmp=max(tmp,dp[i-1][j-1]-prices[j])
        print dp
        return dp[-1][-1]

    def onlyone(self, prices):
        retval=0
        for i in xrange(1,len(prices)):
            if prices[i]>prices[i-1]: retval+=prices[i]-prices[i-1]
        return retval

print Solution().maxProfit(3,[2,3,6,9,3,5,1,9,8,3])