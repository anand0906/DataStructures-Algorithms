
def bruteForce(arr,n):
    profit=0
    for i in range(n):
        for j in range(i+1,n):
            buy=arr[i]
            sell=arr[j]
            if(sell > buy):
                profit=max(profit,(sell-buy))
    return profit

def optimized(arr,n):
    mini=arr[0]
    profit=0
    for i in range(1,n):
        if(arr[i] > mini):
            profit=max(profit,arr[i]-mini)
        mini=min(mini,arr[i])
    return profit
        


arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
