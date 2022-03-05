def merge(a,b):
    final=[]
    m=len(a)
    n=len(b)
    i,j=0,0
    while(i<m and j<n):
        if(a[i]<=b[j]):
            final.append(a[i])
            i+=1
        else:
            final.append(b[j])
            j+=1
    while i<m:
        final.append(a[i])
        i+=1
    while(j<n):
        final.append(b[j])
        j+=1
    return final  

def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    a=mergesort(left)
    b=mergesort(right)
    return merge(a,b)
        
arr=list(map(int,input().split()))
print(mergesort(arr))
