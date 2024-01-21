
#TC : O(N*N)
#SC : O(N)
def algorithmic(arr,n):
    dp=[0]*n
    for i in range(n):
        dp[i]=1
    for index in range(n):
        for last_index in range(index):
            if(arr[index]%arr[last_index]==0):
                temp=1+dp[last_index]
                dp[index]=max(dp[index],temp)
    final=-1
    for i in dp:
        final=max(final,i)
    return final

#TC : O(N*N)
#SC : O(N)
def printLDS(arr,n):
    dp=[0]*n
    for i in range(n):
        dp[i]=1
    track={}
    for index in range(n):
        track[index]=index
        for last_index in range(index):
            if(arr[index]%arr[last_index]==0 and 1+dp[last_index] > dp[index]):
                temp=1+dp[last_index]
                dp[index]=max(dp[index],temp)
                track[index]=last_index
    final=-1
    maxIndex=-1
    for i in range(n):
        if(dp[i]>final):
            final=dp[i]
            maxIndex=i
    last_index=maxIndex
    temp=[arr[last_index]]
    while track[last_index]!=last_index:
        last_index=track[last_index]
        temp.append(arr[last_index])
    return temp[::-1]

arr=list(map(int,input().split()))
n=len(arr)
arr=sorted(arr)
print(algorithmic(arr,n))
print(printLDS(arr,n))
