class Solution(object):
    def isAdditiveNumber(self, num):
        if len(num)<3: return False
        for i in xrange(1,len(num)-1):
            for j in xrange(i+1,len(num)):
                left,mid=num[:i],num[i:j]
                if left[0]=='0' and len(left)>1 or mid[0]=='0' and len(mid)>1: continue
                if self.recursion(long(left),long(mid),num[j:]): return True
        return False

    def recursion(self, l, m, rstr):
        if rstr[0]=='0' and len(rstr)>1: return False
        sstr=str(l+m)
        if l+m==long(rstr): return True
        elif l+m>long(rstr): return False
        elif not rstr.startswith(sstr): return False
        else: return self.recursion(m,l+m,rstr[len(sstr):])

print Solution().isAdditiveNumber("121224036")
print Solution().isAdditiveNumber("101")
print Solution().isAdditiveNumber("123")