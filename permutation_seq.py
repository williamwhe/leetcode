import math

class Solution(object):
    def getPermutation(self, n, k):
        retval=[]
        perm=range(1,n+1)
        self.gao(perm,k,retval)
        return "".join(map(str,retval))

    def gao(self, perm, k, retval):
        if len(perm)==1:
            retval.append(perm[0])
            return
        jie=math.factorial(len(perm)-1)
        if k>jie:
            pos=(k-1)/jie
            retval.append(perm[pos])
            del perm[pos]
            k-=pos*math.factorial(len(perm))
        else:
            retval.append(perm[0])
            del perm[0]
        self.gao(perm,k,retval)

print Solution().getPermutation(3,4) #231
print Solution().getPermutation(4,2) #1243
print Solution().getPermutation(4,7) #2134
print Solution().getPermutation(4,6) #1432
print Solution().getPermutation(4,24) #4321