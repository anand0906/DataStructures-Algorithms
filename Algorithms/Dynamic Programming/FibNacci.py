def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)
#print(fib(int(input())))
def fib(n,memo):
    if n in memo:
        return memo[n]
    if(n<=1):
        return n
    else:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
        return memo[n]

memo={}
#print(fib(int(input()),memo))
n=int(input())
memo=[None]*(n+1)
memo[0]=0
memo[1]=1
for i in range(2,n+1):
    memo[i]=memo[i-1]+memo[i-2]
print(memo[n])
    
