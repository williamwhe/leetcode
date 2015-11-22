class Solution(object):
    def findRepeatedDnaSequences(self, s):
        cnt,retval=set(),set()
        if len(s)<=10: return []
        for i in xrange(len(s)-9):
            if s[i:i+10] in cnt:
                retval.add(s[i:i+10])
            cnt.add(s[i:i+10])
        return list(retval)

print Solution().findRepeatedDnaSequences("AAAAAAAAAAA")