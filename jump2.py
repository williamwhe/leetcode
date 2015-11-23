import pdb
#pdb.set_trace()

def jump(A):
    if len(A)==1:
        return 0
    B=[min(A[0],len(A)-1)]
    for i in range(1,len(A)):
        B.append(min(max(A[i]+i,B[i-1]),len(A)-1))
    prev=B[0]
    cnt=1
    for i in range(1,len(B)):
        if B[i]>prev:
            cnt+=1
        prev=B[i]
        if B[i]>=len(B)-1:
            break
    return cnt

a=[3,1,1,1,1]
print jump(a)