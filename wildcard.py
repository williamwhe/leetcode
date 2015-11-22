class Solution(object):
    def isMatch(self, s, p):
        i,j,star=0,0,False
        while i<len(s):
            if j<len(p) and (p[j]=='?' or s[i]==p[j]):
                i,j=i+1,j+1
                continue
            if j<len(p) and p[j]=='*':
                star=True
                tmpi,tmpj,j=i,j,j+1
                continue
            if star:
                tmpi+=1
                i,j=tmpi,tmpj+1
                continue
            return False
        while j<len(p) and p[j]=="*": j+=1
        if j==len(p): return True
        return False

print Solution().isMatch("aa","a")
print Solution().isMatch("aa","a*")
print Solution().isMatch("aaa","aa")
print Solution().isMatch("aa","*")
print Solution().isMatch("ab","a?")
print Solution().isMatch("aab","c*a*b")