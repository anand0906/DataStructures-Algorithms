def bruteForce(arr,r,c,target):
    for i in range(r):
        if(arr[i][0]<=target<=arr[i][c-1]):
            for j in range(c):
                if(arr[i][j]==target):
                    return True
    return False

def betterApproach(arr,r,c,target):
    for i in range(r):
        if(arr[i][0]<=target<=arr[i][c-1]):
            left,right=0,c-1
            while(left<=right):
                mid=(left+right)//2
                if(arr[i][mid]==target):
                    return True
                elif(target>arr[i][mid]):
                    left=mid+1
                else:
                    right=mid-1
    return False

def binarySearch(arr,r,c,target):
    left,right=0,r*c-1
    while(left<=right):
        mid=(left+right)//2
        col=mid%c
        row=mid//r
        temp=arr[row][col]
        if(temp==target):
            return True
        elif(target>temp):
            left=mid+1
        else:
            right=mid-1
    return False

r=int(input())
c=int(input())
arr=[list(map(int,input().split())) for i in range(r)]
target=int(input())
print(bruteForce(arr,r,c,target))
print(betterApproach(arr,r,c,target))
print(binarySearch(arr,r,c,target))
