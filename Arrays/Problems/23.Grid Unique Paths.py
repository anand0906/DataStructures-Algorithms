def solve(n,m):
    N=n+m-2
    R=m-1
    final=1
    for i in range(R):
        final=final*(N-i)
        final=final//(i+1)
    return final

n,m=list(map(int,input().split()))
print(solve(n,m))
