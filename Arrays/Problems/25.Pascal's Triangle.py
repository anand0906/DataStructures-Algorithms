def nCr(N,R):
    final=1
    for i in range(R):
        final=final*(N-i)
        final=final//(i+1)
    return final

def printPascal(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(nCr(row-1,col-1),end=" ")
        print()

def optimized(n):
    for row in range(1,n+1):
        temp=[1]
        final=1
        for col in range(1,row):
            final*=(row-col)
            final//=col
            temp.append(final)
        print(*temp,sep=" ")
        
n=int(input())
printPascal(n)
optimized(n)
