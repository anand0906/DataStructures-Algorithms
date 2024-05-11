def solve(matrix,n,m):
    left,right=0,m-1
    top,bottom=0,n-1
    final=[]
    while(left<=right and top<=bottom):
        for i in range(left,right+1):
            final.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            final.append(matrix[i][right])
        right-=1
        if(top<=bottom):
            for i in range(right,left-1,-1):
                final.append(matrix[bottom][i])
            bottom-=1
        if(left<=right):
            for i in range(bottom,top-1,-1):
                final.append(matrix[i][left])
            left+=1
    return final

n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(solve(matrix,n,m))
            
