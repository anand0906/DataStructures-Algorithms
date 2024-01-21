
#TC : O(N*N)
#SC : O(N)
def algorithmic(arr,n):
    dp=[0]*n
    for i in range(n):
        dp[i]=1
    track={}
    for index in range(n):
        track[index]=index
        for last_index in range(index):
             if(arr[index] > arr[last_index] and (1+dp[last_index])>dp[index]):
                 dp[index]=1+dp[last_index]
                 track[index]=last_index
    final=-1
    maxIndex=-1
    for i in range(n):
        if(dp[i]>final):
            final=dp[i]
            maxIndex=i
    temp=[]
    temp.append(arr[maxIndex])
    last_index=maxIndex
    while track[last_index]!=last_index:
        last_index=track[last_index]
        temp.append(arr[last_index])
    return final,temp[::-1]

arr=list(map(int,input().split()))
n=len(arr)
print(algorithmic(arr,n))

                 
                 
