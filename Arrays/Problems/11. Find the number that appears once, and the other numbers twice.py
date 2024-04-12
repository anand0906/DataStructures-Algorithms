def bruteForce(arr,n):
    count={}
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i,j in count.items():
        if(j==1):
            return i
    return -1

def optimized(arr,n):
    xor=0
    for i in arr:
        xor=xor^i
    return xor

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
