def optimizedHistogram(n,arr):
    stack=[]
    maxArea=0
    for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
            current=arr[stack.pop()]
            rightMin=i
            if(stack):
                leftMin=stack[-1]
            else:
                leftMin=-1
            area=(rightMin-leftMin-1)*current
            maxArea=max(maxArea,area)
        stack.append(i)
    while stack:
        rightMin=n
        current=arr[stack.pop()]
        if(stack):
            leftMin=stack[-1]
        else:
            leftMin=-1
        area=(rightMin-leftMin-1)*current
        maxArea=max(maxArea,area)
    return maxArea


def optimized(n,m,matrix):

    for i in range(m):
        sum=0
        for j in range(n):
            sum+=matrix[j][i]
            if(matrix[j][i]==0):
                sum=0
            matrix[j][i]=sum
    maxArea=0
    for i in range(n):
        area=optimizedHistogram(m,matrix[i])
        maxArea=max(maxArea,area)
    return maxArea
    

n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(optimized(n,m,matrix))
