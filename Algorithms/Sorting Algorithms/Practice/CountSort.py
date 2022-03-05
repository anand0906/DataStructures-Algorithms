arr=list(map(int,input().split()))
n=len(arr)
maximum=-float("inf")
for i in arr:
    maximum=max(i,maximum)
final=[0]*(maximum+1)
f=[]
for i in arr:
    final[i]+=1
i=0
while i<=maximum:
    if(final[i]>0):
        f.append(i)
        final[i]-=1
    else:
        i+=1
print(f)
        
