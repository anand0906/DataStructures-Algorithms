'''
track minimum value before each element which is pointing to buy stock
calculate by selling stock at each index
calculate profit at each index
return maximum profit
'''

def solve(arr,n):
    profit=0
    minimum=arr[0]
    buy=minimum
    for i in range(1,n):
        sell=arr[i]
        currentProfit=sell-buy
        profit=max(profit,currentProfit)
        minimum=min(minimum,i)
        buy=minimum
    return profit

n=int(input())
arr=list(map(int,input().split()))
print(solve(arr,n))
