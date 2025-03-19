def bruteForce(n):
    final=-float("inf")
    for i in range(1,n+1):
        if(i*i <= n):
            final=i
        else:
            break
    return final

def binarySearch(n):
    left,right=1,n+1
    final=-float("inf")
    while(left<=right):
        mid=(left+right)//2
        if(mid*mid<=n):
            final=mid
            left=mid+1
        else:
            right=mid-1
    return final

n=int(input())
print(bruteForce(n))
print(binarySearch(n))
