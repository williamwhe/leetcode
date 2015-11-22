class Solution(object):
    def numDecodings(self, s):
        if s=="": return 0
        n=len(s)
        dp=[0]*(n+1)
        dp[-1],dp[-2]=1,0 if s[-1]=='0' else 1
        for i in xrange(n-2,-1,-1):
            # if s[i:i+2]=="00": return 0
            if s[i]=='0': continue
            dp[i]=dp[i+1]+dp[i+2] if int(s[i:i+2])<=26 else dp[i+1]
        print dp
        return dp[0]

print Solution().numDecodings("100")
print Solution().numDecodings("101")