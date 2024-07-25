def bruteforce(n,matrix):
    personKnows=[0]*n
    personKnownBy=[0]*n
    for i in range(n):
        for j in range(n):
            if(matrix[i][j]==1):
                personKnows[i]+=1
                personKnownBy[j]+=1
    for i in range(n):
        if(personKnows[i]==0 and personKnownBy[i]==n-1):
            return i
    return -1
def knows(a,b,matrix):
    return matrix[a][b]

def optimized(n,matrix):
    stack=[]
    for i in range(n):
        stack.append(i)
    while len(stack)>1:
        a,b=stack.pop(),stack.pop()
        if(knows(a,b,matrix)):
            stack.append(b)
        else:
            stack.append(a)
    celeb=stack.pop()
    for i in range(n):
        if(celeb!=i and (knows(celeb,i,matrix) or  not knows(i,celeb,matrix))):
           return -1
    return celeb

def optimized2(n,matrix):
    left,right=0,n-1
    while left<right:
        if(knows(left,right,matrix)):
            left+=1
        else:
            right-=1
    celeb=left
    for i in range(n):
        if(celeb!=i and (knows(celeb,i,matrix) or  not knows(i,celeb,matrix))):
           return -1
    return celeb   

n=int(input())
matrix=[list(map(int,input().split())) for i in range(n)]
print(bruteforce(n,matrix))
print(optimized(n,matrix))
print(optimized2(n,matrix))
