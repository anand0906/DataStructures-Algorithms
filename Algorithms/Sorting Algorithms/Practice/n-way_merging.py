#Merge Sort
def combine(a,b):
    final=[]
    n=len(a)
    m=len(b)
    i,j=0,0
    while(i<n and j<m):
        if(a[i]<=b[j]):
            final.append(a[i])
            i+=1
        else:
            final.append(b[j])
            j+=1
    while i<n:
        final.append(a[i])
        i+=1
    while j<m:
        final.append(b[j])
        j+=1
    return final

a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
t=combine(a,b)
k=combine(t,c)
print(k)


        
    
    
