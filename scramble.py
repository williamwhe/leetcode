class Solution(object):
    def isScramble(self, s1, s2):
        if s1==s2: return True
        if len(s1)!=len(s2): return False
        alphabet=[0]*26
        for i in xrange(len(s1)):
            alphabet[ord(s1[i])-97]+=1
        for i in xrange(len(s2)):
            alphabet[ord(s2[i])-97]-=1
        if alphabet.count(0)!=26: return False
        for i in xrange(1,len(s1)):
            if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]) or self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i])): return True
        return False

print Solution().isScramble("great","raget")
# print Solution().isScramble("great","rgeat")
# print Solution().isScramble("great","rgtae")