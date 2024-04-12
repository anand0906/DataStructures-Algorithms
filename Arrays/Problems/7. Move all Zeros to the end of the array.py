def bruteForce(arr,n):
    temp=[]
    for i in range(n):
        if(arr[i]!=0):
            temp.append(arr[i])
    nz=len(temp)
    
    for i in range(nz):
        arr[i]=temp[i]
        
    for i in range(nz,n):
        arr[i]=0
    return arr
    

def optimized(arr,n):
    j=-1
    for i in range(n):
        if(arr[i]==0):
            j=i
            break
    if(j==-1):
        return arr
    for i in range(j+1,n):
        if(arr[i]!=0):
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
    

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
