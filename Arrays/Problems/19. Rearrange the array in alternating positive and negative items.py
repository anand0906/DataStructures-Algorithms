
def bruteForce(arr,n):
    pos,neg=[],[]
    for i in range(n):
        if(arr[i]<0):
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    for i in range(len(pos)):
        arr[i*2]=pos[i]
    for i in range(len(neg)):
        arr[i*2+1]=neg[i]
    return arr

def optimized(arr,n):
    posIndex,negIndex=0,1
    final=[0]*n
    for i in range(n):
        if(arr[i]<0):
            final[negIndex]=arr[i]
            negIndex+=2
        else:
            final[posIndex]=arr[i]
            posIndex+=2
    return final
        
        


arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
