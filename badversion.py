import pdb

def isBadVersion(n):
    if n==1:
        return True
    return False

def binsearch(t, low, high):
    while low < high:
        mid = (low + high)//2
        if not isBadVersion(t[mid]):
            low = mid + 1
        else:
            high = mid
    return low if isBadVersion(t[low]) else -1

pdb.set_trace()
print binsearch([1],0,1)