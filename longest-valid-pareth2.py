class Solution(object):
    def longestValidParentheses(self, s):
        retval,dp=0,[0]*len(s)
        for i in xrange(1,len(s)):
            if s[i]==")":
                if s[i-1]=="(":
                    dp[i]=dp[i-2]+2
                elif i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=="(":
                    if dp[i-1]>0:
                        dp[i]=dp[i-1]+2+dp[i-dp[i-1]-2]
                retval=max(retval,dp[i])
        return retval

print Solution().longestValidParentheses("(())")
print Solution().longestValidParentheses("()(())")