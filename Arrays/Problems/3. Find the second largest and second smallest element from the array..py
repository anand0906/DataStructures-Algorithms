def bruteForce(arr,n):
    smallest=arr[0]
    largest=arr[0]
    for i in range(1,n):
        if(arr[i]<smallest):
            smallest=arr[i]
        if(arr[i]>largest):
            largest=arr[i]
    second_smallest=float('inf')
    second_largest=float('-inf')
    for i in range(n):
        if(arr[i]<second_smallest and arr[i]!=smallest):
            second_smallest=arr[i]
        if(arr[i]>second_largest and arr[i]!=largest):
            second_largest=arr[i]
    if(second_smallest==float('inf')): # for array having same elements
        second_smallest=smallest
    if(second_largest==float('-inf')): # for array having same elements
        second_largest=largest
    return [second_smallest,second_largest]

def optimized(arr,n):
    smallest,second_smallest=float('inf'),float('inf')
    largest,second_largest=float('-inf'),float('-inf')
    for i in range(n):
        if(arr[i]<smallest):
            second_smallest=smallest
            smallest=arr[i]
        elif(arr[i]<second_smallest and arr[i]!=smallest):
            second_smallest=arr[i]

        if(arr[i]>largest):
            second_largest=largest
            largest=arr[i]
        elif(arr[i]>second_largest and arr[i]!=largest):
            second_largest=arr[i]
            
    return [second_smallest,second_largest]

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
