def optimizedHistogram(n,arr):
    stack=[]
    maxi=0
    for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
            index=stack.pop()
            height=arr[index]
            leftMin=stack[-1] if stack else -1
            rightMin=i
            width=rightMin-leftMin-1
            maxi=max(maxi,width*height)
        stack.append(i)
    while stack:
        index=stack.pop()
        height=arr[index]
        leftMin=stack[-1] if stack else -1
        rightMin=n
        width=rightMin-leftMin-1
        maxi=max(maxi,width*height)
    return maxi

def solve(n,m,matrix):
    mat=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]=='1'):
                if(i==0):
                    mat[i][j]=1
                else:
                    mat[i][j]=1+mat[i-1][j]
    maxi=0
    for i in range(n):
        ans=optimizedHistogram(m,mat[i])
        maxi=max(maxi,ans)
    return maxi 
n,m=list(map(int,input().split()))
matrix=[input().split() for i in range(n)]
print(solve(n,m,matrix))
