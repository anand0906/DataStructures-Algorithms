def bruteForce(n,arr):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            s=set()
            for k in range(i,j+1):
                s.add(arr[k])
                if(len(s)>2):
                    break
            else:
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def better(n,arr):
    maxi=0
    for i in range(n):
        s=set()
        for j in range(i,n):
            s.add(arr[j])
            if(len(s)>2):
                break
            length=j-i+1
            maxi=max(maxi,length)
    return maxi

def optimized(n,arr):
    maxi=0
    left,right=0,0
    count={}
    while right<n:
        if arr[right] in count:
            count[arr[right]]+=1
        else:
            count[arr[right]]=1
        if(len(count)>2):
            while (len(count)>2):
                count[arr[left]]-=1
                if(count[arr[left]]==0):
                    del count[arr[left]]
                left+=1
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
