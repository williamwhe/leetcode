import math

def andall(m,n):
    retval=m
    i=m+1
    while i<=n:
        retval&=i
        i+=1
    return retval

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        if m==0:
            return 0
        if m==n:
            return m
        maxmi=int(math.log(2147483647)/math.log(2))
        two_times=[]
        for i in range(maxmi+1):
            two_times.append(2**i)
        for i in range(len(two_times)-1):
            if m>=two_times[i] and n<two_times[i+1]:
                return andall(m,n)
        if m>=two_times[-1]:
            return andall(m,n)
        return 0
            
s=Solution()
print s.rangeBitwiseAnd(2147483646,2147483647)