

#TC : O(log n)
def lowerbound(arr,left,right,target):
    while left<=right:
        mid=(left+right)//2
        if(target>=arr[mid]):
            left=mid+1
        else:
            right=mid-1
    return left

#TC : O(n*log n)
#SC : O(n)
def solve(arr,n):
    temp=[arr[0]]
    currentLength=1
    for index in range(1,n):
        if(arr[index]>temp[currentLength-1]):
            temp.append(arr[index])
            currentLength+=1
        else:
            i=lowerbound(temp,0,currentLength-1,arr[index])
            temp[i]=arr[index]
    return currentLength
            
        

arr=list(map(int,input().split()))
n=len(arr)
print(solve(arr,n))
