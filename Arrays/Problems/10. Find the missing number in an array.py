def bruteForce(arr,n):
    for i in range(1,n+1):
        flag=False
        for j in arr:
            if(j==i):
                flag=True
                break
        if(flag==False):
            return i
    return -1

def better(arr,n):
    visited={}
    for i in arr:
        visited[i]=True
    for i in range(1,n+1):
        if(not visited.get(i)):
            return i
    return -1

def optimal(arr,n):
    givenSum=0
    for i in arr:
        givenSum+=i
    expSum=((n*(n+1))//2)
    return expSum-givenSum

def optimal2(arr,n):
    xor1=0
    xor2=0
    for i in range(n-1):
        xor1=xor1^arr[i]
        xor2=xor2^(i+1)
    xor2=xor2^(n)
    return xor1^xor2
        

arr=list(map(int,input().split()))
n=int(input())
print(bruteForce(arr,n))
print(better(arr,n))
print(optimal(arr,n))
print(optimal2(arr,n))
