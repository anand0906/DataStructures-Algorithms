def bruteForce(n,arr):
    largest=0
    for i in range(n):
        for j in range(i+1,n):
            width=j-i
            height=min(arr[i],arr[j])
            area=width*height
            largest=max(largest,area)
    return largest

def optimized(n,arr):
    left,right=0,n-1
    largest=0
    while left<right:
        width=right-left
        height=min(arr[left],arr[right])
        area=width*height
        largest=max(largest,area)
        if(arr[left]<arr[right]):
            left+=1
        else:
            right-=1
    return largest
    
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
