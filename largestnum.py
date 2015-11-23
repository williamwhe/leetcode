def cmp2(str,l,step):
    for i in range(l):
        if str[i]>str[i+step]:
            return -1
        elif str[i]<str[i+step]:
            return 1
    return 0

def cmp(x,y):
    if len(x)==len(y):
        return int(y)-int(x)
    if len(x)<len(y):
        if int(y[0:len(x)])==int(x):
            print "===x<y==="
            return cmp2(y+x,len(y),len(x))
        else:
            return int(y[0:len(x)])-int(x)
    else:
        if int(x[0:len(y)])==int(y):
            print "===x>y==="
            return -1*(cmp2(x+y,len(x),len(y)))
        else:
            return int(y)-int(x[0:len(y)])

class Solution(object):
    def largestNumber(self, nums):
        strs=map(str,nums)
        strs.sort(cmp)
        retval="".join(strs)
        last=retval[-1]
        retval=retval[:-1].lstrip('0')+last
        return retval
    
s=Solution()
print s.largestNumber([883,8,9576])
print s.largestNumber([12,128])
print s.largestNumber([0,0])
print s.largestNumber([2,10])
print s.largestNumber([121,12])
print s.largestNumber([12,121])
print s.largestNumber([1211,12])