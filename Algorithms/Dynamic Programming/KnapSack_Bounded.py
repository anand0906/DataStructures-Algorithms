def myfunc(products,profits,space,n,temp=[],memo={}):
    key=(space,n)
    if key in memo:
        memo[key]
    if(n<0 or space<=0):
        return 0
    include=-float('inf')
    if not (temp.count(profits[n])>=products[n]):
        include=profits[n]+myfunc(products,profits,space-1,n,temp+[profits[n]])
    exclude=myfunc(products,profits,space,n-1,temp)
    memo[key]=max(include,exclude)
    return memo[key]
n=int(input())
products=[int(input()) for i in range(n)]
profits=[int(input()) for i in range(n)]
space=int(input())
print(myfunc(products,profits,space,n-1))








