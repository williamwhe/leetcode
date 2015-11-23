def threeSum(num):
    num.sort()
    s=set()
    for i in range(len(num)-2):
        j=i+1
        k=len(num)-1
        while j<k:
            if num[i]+num[j]+num[k]==0:
                s.add((num[i],num[j],num[k]))
                j+=1
                k-=1
                continue
            if num[i]+num[j]+num[k]<0:
                j+=1
                continue
            if num[i]+num[j]+num[k]>0:
                k-=1
                continue
    return list(map(list, s))
print threeSum([0,0,0])