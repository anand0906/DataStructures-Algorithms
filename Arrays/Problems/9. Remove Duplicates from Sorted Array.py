def bruteForce(arr,n):
    temp=set()
    for i in arr:
        temp.add(i)
    k=len(temp)
    j=0
    for i in temp:
        arr[j]=i
        j+=1
    return arr
        

def optimized(arr,n):
    i=0
    for j in range(1,n):
        if(arr[j]!=arr[i]):
            i+=1
            arr[i]=arr[j]
    return arr
            

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
