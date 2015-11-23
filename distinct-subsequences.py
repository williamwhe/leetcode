class Solution(object):
    def numDistinct(self, s, t):
        dp=[]
        for i in xrange(len(t)):
            dp.append([0]*len(s))
        for i in xrange(len(t)):
            tmp=0
            for j in xrange(len(s)):
                if i==0:
                    dp[i][j]=1 if t[i]==s[j] else 0
                    continue
                if t[i]==s[j]:
                    dp[i][j]=tmp
                if dp[i-1][j]>0:
                    tmp+=dp[i-1][j]
            if tmp==0 and i>0:
                return 0
        return sum(dp[-1])

print Solution().numDistinct("rabbbit","rabbit")
print Solution().numDistinct("abcabbc","abc")