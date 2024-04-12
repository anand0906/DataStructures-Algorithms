def solve(arr,n,num):
    for i in range(n):
        if(arr[i]==num):
            return i+1
    return -1

arr=list(map(int,input().split()))
n=len(arr)
num=int(input())
print(solve(arr,n,num))
