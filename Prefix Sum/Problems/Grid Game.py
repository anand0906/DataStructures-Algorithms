def optimized(n,m,matrix):
    prefix1,prefix2=matrix[0].copy(),matrix[1].copy()
    for i in range(1,m):
        prefix1[i]+=prefix1[i-1]
        prefix2[i]+=prefix2[i-1]

    ans=float('inf')
    for i in range(m):
        top=prefix1[-1]-prefix1[i]
        bottom=prefix2[i-1] if(i>0) else 0
        points=max(top,bottom)
        ans=min(ans,points)
    return ans
n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(optimized(n,m,matrix))
