def bruteForce(mat,n,m,target):
    for i in range(n):
        for j in range(m):
            if(mat[i][j]==target):
                return True
    return False

def binarySearch(arr):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if(arr[mid]==target):
            return True
        elif(target < arr[mid]):
            high=mid-1
        else:
            low=mid+1
    return False

def better(mat,n,m,target):
    for i in range(n):
        if(binarySearch(mat[i])):
            return True
    return False

def optimized(mat,n,m,target):
    low=0
    high=(n*m)-1
    while low<=high:
        mid=(low+high)//2
        row,col=mid//m , mid%m
        if(mat[row][col]==target):
            return True
        elif(mat[row][col]<target):
            low=mid+1
        else:
            high=mid-1
    return False


n,m=list(map(int,input().split()))
mat=[list(map(int,input().split())) for i in range(n)]
target=int(input())
print(bruteForce(mat,n,m,target))
print(better(mat,n,m,target))
print(optimized(mat,n,m,target))
    
    
