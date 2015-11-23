class Solution(object):
    def candy(self, ratings):
        tmp=[1]*len(ratings)
        for i in xrange(0,len(ratings)-1):
            if ratings[i]>ratings[i+1] and tmp[i]<=tmp[i+1]:
                tmp[i]=tmp[i+1]+1
            elif ratings[i]<ratings[i+1] and tmp[i]>=tmp[i+1]:
                tmp[i+1]=tmp[i]+1
        print ratings
        print tmp
        for i in xrange(len(ratings)-1,0,-1):
            if ratings[i]>ratings[i-1] and tmp[i]<=tmp[i-1]:
                tmp[i]=tmp[i-1]+1
            elif ratings[i]<ratings[i-1] and tmp[i]>=tmp[i-1]:
                tmp[i-1]=tmp[i]+1
        print tmp
        return sum(tmp)

print Solution().candy([1,3,4,3,2,1])
print Solution().candy([1,3,5])
print Solution().candy([1,0,2])
print Solution().candy([2,2])
print Solution().candy([1,2,2])
print Solution().candy([7,0,6,2,4,9,4,6])