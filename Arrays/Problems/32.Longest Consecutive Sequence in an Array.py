def bruteForce(n,arr):
    longest=1

    for i in range(n):
        current=arr[i]
        cnt=1
        while True:
            if((current+1) in arr):
                cnt+=1
                current=current+1
            else:
                break
        longest=max(longest,cnt)
    return longest

def better(n,arr):
    arr.sort()
    last=float('-inf')
    longest=1
    cnt=0
    for i in range(n):
        if(arr[i]==last):
            continue
        if(arr[i]-1 ==last):
            cnt+=1
            last=arr[i]
            longest=max(longest,cnt)
        else:
            cnt=1
            last=arr[i]
    return longest

def optimized(n,arr):
    temp=set(arr)
    longest=1
    for i in range(n):
        current=arr[i]
        if(current-1 not in temp):
            cnt=1
            while current+1 in temp:
                current+=1
                cnt+=1
            longest=max(longest,cnt)
    return longest
        


arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
