n,q=list(map(int,input().split()))
queries=[list(map(int,input().split())) for i in range(q)]
arr=[0]*n
for i,j,k in queries:
    i=i-1
    arr[i]+=k
    arr[j]-=k
for i in range(1,n):
    arr[i]=arr[i-1]+arr[i]
print(max(arr))
