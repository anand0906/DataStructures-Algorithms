def bruteForce(arr,r,c):
    final=float("-inf")
    max_cnt=0
    for i in range(r):
        cnt=0
        for j in range(c):
            if(arr[i][j]==1):
                cnt+=1
        if(cnt>max_cnt):
            final=i
            max_cnt=cnt
    return final

def binarySearch(arr,r,c):
    final=float("-inf")
    max_cnt=0
    for i in range(r):
        cnt=0
        temp=float('inf')
        left,right=0,c-1
        while(left<=right):
            mid=(left+right)//2
            if(arr[i][mid]==1):
                temp=min(temp,mid)
                right=mid-1
            elif(arr[i][mid]==0):
                left=mid+1
            else:
                left=mid+1
        if(temp!=float('inf')):
            cnt=c-temp
        if(cnt>max_cnt):
            max_cnt=cnt
            final=i
    return final
            

r=int(input())
c=int(input())
arr=[list(map(int,input().split())) for i in range(r)]
print(bruteForce(arr,r,c))
print(binarySearch(arr,r,c))
     
