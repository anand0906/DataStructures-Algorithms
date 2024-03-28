import heapq
n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
sourceRow,sourceCol=list(map(int,input().split()))
destRow,destCol=list(map(int,input().split()))
difference=[[float('inf')]*m for i in range(n)]
difference[sourceRow][sourceCol]=0
queue=[]
heapq.heappush(queue,(0,(sourceRow,sourceCol)))
while queue:
    currentDiff,(row,col)=heapq.heappop(queue)
    for i,j in zip([0,0,-1,1],[1,-1,0,0]):
        r=row+i
        c=col+j
        if(r>=0 and c>=0 and r<n and c<m):
            newDiff=max(abs(matrix[r][c]-matrix[row][col]),currentDiff)
            if(newDiff < difference[r][c]):
                heapq.heappush(queue,(newDiff,(r,c)))
                difference[r][c]=newDiff
print(difference[destRow][destCol])
    
