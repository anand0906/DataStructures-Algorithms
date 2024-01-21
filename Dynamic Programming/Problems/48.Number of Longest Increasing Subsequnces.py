
def solve(arr,n):
    dp=[1]*n
    count=[1]*n
    for index in range(n):
        for last_index in range(index):
            if(arr[index]>arr[last_index]):
                if(1+dp[last_index] > dp[index]):
                    dp[index]=max(dp[index],1+dp[last_index])
                    count[index]=count[last_index]
                elif(1+dp[last_index]==dp[index]):
                    count[index]+=count[last_index]
    maxi=-1
    for i in dp:
        maxi=max(maxi,i)
    
    final=0
    for i in range(n):
        if(dp[i]==maxi):
            final+=count[i]
    return final

arr=list(map(int,input().split()))
n=len(arr)
print(solve(arr,n))
            
                    
