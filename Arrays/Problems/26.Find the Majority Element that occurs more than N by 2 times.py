def bruteForce(n,arr):
    count={}
    for i in range(n):
        if(arr[i] in count):
            count[arr[i]]+=1
        else:
            count[arr[i]]=1

    for i,v in count.items():
        if(v>(n//2)):
            return i
    return -1


def optimized(n,arr):
    count=0
    current=0
    for i in range(n):
        if(count==0):
            current=arr[i]
            count=1
        elif(current==arr[i]):
            count+=1
        else:
            count-=1
    final=0
    for i in range(n):
        if(arr[i]==current):
            final+=1
    if(final>(n//2)):
        return current
    return -1

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
