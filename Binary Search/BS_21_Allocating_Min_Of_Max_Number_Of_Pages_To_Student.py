def countOfStudents(arr,pages):
    count=1
    currentPages=0
    for i in arr:
        if((currentPages+i)<=pages):
            currentPages+=i
        else:
            count+=1
            currentPages=i
    return count

def bruteForce(arr,students):
    if(students> len(arr)):
        return -1
    minPossible=max(arr)
    maxPossible=sum(arr)
    for i in range(minPossible,maxPossible+1):
        temp=countOfStudents(arr,i)
        if(temp==students):
            return i
    return minPossible

def BinarySearch(arr,students):
    if(students> len(arr)):
        return -1
    left,right=max(arr),sum(arr)
    final=float("inf")
    while(left<=right):
        mid=(left+right)//2
        temp=countOfStudents(arr,mid)
        if(temp==students):
            final=min(final,mid)
            right=mid-1
        elif(temp<students):
            right=mid-1
        elif(temp>students):
            left=mid+1
    return final

arr=list(map(int,input().split()))
students=int(input())
print(bruteForce(arr,students))
print(BinarySearch(arr,students))
        
            
