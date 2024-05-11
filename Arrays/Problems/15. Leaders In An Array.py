def bruteForce(arr,n):
    final=[]
    for i in range(n):
        flag=True
        for j in range(i+1,n):
            if(arr[j]>=arr[i]):
                flag=False
                break
        if(flag):
            final.append(arr[i])
    final.sort()
    return final

def optimized(arr,n):
    maxi=arr[n-1]
    final=[maxi]
    for i in range(n-1,-1,-1):
        if(arr[i]>maxi):
            maxi=arr[i]
            final.append(arr[i])
    final.sort()
    return final

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
            
        
        
