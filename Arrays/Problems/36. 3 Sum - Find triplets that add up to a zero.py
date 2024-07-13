def bruteForce(n,arr):
    ans=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if((arr[i]+arr[j]+arr[k])==0):
                    temp=sorted([arr[i],arr[j],arr[k]])
                    ans.add(tuple(temp))
    return list(ans)

def better(n,arr):
    ans=set()
    for i in range(n):
        s=set()
        for j in range(i+1,n):
            third=-(arr[i]+arr[j])
            if third in s:
                temp=sorted([arr[i],arr[j],third])
                ans.add(tuple(temp))
            s.add(arr[j])
    return list(ans)

def optimized(n,arr):
    ans=[]
    arr.sort()
    for i in range(n):
        if(i!=0 and arr[i]==arr[i-1]):
            continue
        j,k=i+1,n-1
        while(j<k):
            sum=arr[i]+arr[j]+arr[k]
            if(sum<0):
                j+=1
            elif(sum>0):
                k-=1
            else:
                temp=[arr[i],arr[j],arr[k]]
                ans.append(temp)
                j+=1
                k-=1
                while(j<k and arr[j]==arr[j-1]):
                    j+=1
                while(k>j and arr[k]==arr[k+1]):
                    k-=1
    return ans
                
    
    

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
