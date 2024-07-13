def bruteForce(n,arr,target):
    ans=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    sum=arr[i]+arr[j]+arr[k]+arr[l]
                    if(sum==target):
                        temp=[arr[i],arr[j],arr[k],arr[l]]
                        temp.sort()
                        ans.add(tuple(temp))
    return ans

def better(n,arr,target):
    ans=set()
    for i in range(n):
        for j in range(i+1,n):
            s=set()
            for k in range(j+1,n):
                fourth=target-(arr[i]+arr[j]+arr[k])
                if(fourth in s):
                    temp=[arr[i],arr[j],arr[k],fourth]
                    temp.sort()
                    ans.add(tuple(temp))
                s.add(arr[k])
    return ans

def optimized(n,arr,target):
    ans=[]
    arr.sort()
    for i in range(n):
        if(i!=0 and arr[i]==arr[i-1]):
            continue
        for j in range(i+1,n):
            if(j!=i+1 and arr[j]==arr[j-1]):
                continue
            k,l=j+1,n-1
            while(k<l):
                sum=arr[i]+arr[j]+arr[k]+arr[l]
                if(sum<target):
                    k+=1
                elif(sum>target):
                    l-=1
                else:
                    temp=[arr[i],arr[j],arr[k],arr[l]]
                    ans.append(tuple(temp))
                    k+=1
                    l-=1
                    while(k<l and arr[k]==arr[k-1]):
                        k+=1
                    while(l>k and arr[l]==arr[l+1]):
                        l-=1
    return ans
                        

arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(bruteForce(n,arr,target))
print(better(n,arr,target))
print(optimized(n,arr,target))
