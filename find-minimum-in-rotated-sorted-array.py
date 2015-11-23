def findMin(num):
    minlist = sorted(num)
    print minlist
    strlist = map(str, minlist)
    print strlist
    return int("".join(strlist))

n = [4,3,2,0]
print findMin(n)