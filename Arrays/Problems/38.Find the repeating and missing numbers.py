def bruteForce(n,arr):
    missing,repeating=None,None
    for i in range(1,n+1):
        cnt=0
        for j in range(n):
            if(arr[j]==i):
                cnt+=1
        if(cnt==0):
            missing=i
        if(cnt==2):
            repeating=i
        if(missing and repeating):
            break
    return [repeating,missing]

def better(n,arr):
    count={}
    missing,repeating=None,None
    for i in range(n):
        if arr[i] in count:
            count[arr[i]]+=1
        else:
            count[arr[i]]=1
        if(count[arr[i]]==2):
            repeating=arr[i]
    for i in range(1,n+1):
        if i not in count:
            missing=i
            break
    return [repeating,missing]

def optimized(n,arr):
    s1n=(n*(n+1))//2
    s2n=((n*(n+1))*(2*n+1))//6
    s1,s2=0,0
    for i in range(n):
        s1+=arr[i]
        s2+=(arr[i]*arr[i])
    val1=s1-s1n # (x-y)
    val2=s2-s2n # (x^2-y^2) 
    val2=val2//val1 # (x+y)
    x=(val1+val2)//2
    y=x-val1
    return [x,y]
    


arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
