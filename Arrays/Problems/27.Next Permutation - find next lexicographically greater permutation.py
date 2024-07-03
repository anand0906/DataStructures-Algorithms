def permute(arr,left,right):
    global temp
    if(left==right):
        temp.append(tuple(arr.copy()))
        return
    for i in range(left,right):
        arr[left],arr[i]=arr[i],arr[left]
        permute(arr,left+1,right)
        arr[left],arr[i]=arr[i],arr[left]

def optimized(arr,n):
    ind=-1
    for i in range(n-2,-1,-1):
        if(arr[i]<arr[i+1]):
            ind=i
            break
    if(ind==-1):
        return arr[::-1]
    temp=arr[ind]
    for i in range(n-1,ind,-1):
        if(arr[i]>arr[ind]):
            arr[i],arr[ind]=arr[ind],arr[i]
            break
    arr[ind+1:]=reversed(arr[ind+1:])
    return arr
    
            
arr=list(map(int,input().split()))
n=len(arr)
temp=[]
permute(sorted(arr),0,n)
ind=temp.index(tuple(arr))
print(temp[(ind+1)%n])
print(optimized(arr,n))
