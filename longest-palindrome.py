class Solution(object):
    def longestValidParentheses(self, s):
        retval,dp=0,[-1]*len(s)
        for i in xrange(1,len(s)):
            if dp[i-1]==-1 and s[i]!=s[i-1]:
                dp[i]=i-1
            elif dp[i-1]>-1:
                if dp[i-1]>0 and s[i]!=s[dp[i-1]-1]:
                    dp[i]=dp[i-1]-1
                elif s[i]!=s[i-1]:
                    dp[i]=i-1
            if dp[i]>-1 and self.valid(s[dp[i]:i+1]):
                retval=max(retval,i-dp[i]+1)
        print dp
        return retval

    def valid(self, s):
        left=s.count('(')
        right=s.count(')')
        if s[0]=='(' and left==right: return True
        return False

print Solution().longestValidParentheses("()(())") # 6
print Solution().longestValidParentheses("()()") # 4
print Solution().longestValidParentheses(")(") # 0
print Solution().longestValidParentheses("(()(()))") # 4