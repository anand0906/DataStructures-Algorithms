
def solve(n,child,m,cookies):
    if(n==0):
        return 0
    child.sort()
    cookies.sort()
    print(child,cookies)
    left,right=0,0
    while left<n and right<m:
        if(child[left]<=cookies[right]):
            left+=1
        right+=1
    return left


child=list(map(int,input().split()))
cookies=list(map(int,input().split()))
n=len(child)
m=len(cookies)
print(solve(n,child,m,cookies))
