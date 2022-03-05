#we need to find the number of ways to reach nth stair
#we can climb either 1 stair or 2 stairs at a time
#n=1
#0 1 -->1 way (0->1)
#n=2
#0 1 2 -->2 ways(0->1&1->2)+(0->2)
#n=3



def count(n):
    if(n<=0):
        return 0
    if(n==1):
        return 1
    else:
        return count(n-1)+count(n-2)

def count(n):
    global dp
    if n in dp:
        return dp[n]
    if(n<=0):
        return 0
    if(n==1):
        return 1
    else:
        dp[n]=count(n-1)+count(n-2)
        return dp[n] 
n=int(input())
dp={}
print(count(n+1))
