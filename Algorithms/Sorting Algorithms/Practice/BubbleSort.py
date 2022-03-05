a=list(map(int,input().split()))
n=len(a)
for i in range(n):
    f=0
    for j in range(n-i-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
            f=1
    if(f==0):
        break
print(a)
