a=list(map(int,input().split()))
n=len(a)
for i in range(n):
    minimum=i
    for j in range(i+1,n):
        if(a[j]<a[minimum]):
            minimum=j
    a[minimum],a[i]=a[i],a[minimum]
print(a)
    
