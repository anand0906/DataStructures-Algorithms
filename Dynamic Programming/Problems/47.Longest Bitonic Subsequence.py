

def solve(arr,n):
    dp_increasing=[1]*n
    dp_decreasing=[1]*n

    for index in range(1,n):
        for last_index in range(index):
            if(arr[index] > arr[last_index]):
                temp=1+dp_increasing[last_index]
                dp_increasing[index]=max(dp_increasing[index],temp)

    for index in range(n-1,-1,-1):
        for last_index in range(index+1,n):
            if(arr[index] > arr[last_index]):
                temp=1+dp_decreasing[last_index]
                dp_decreasing[index]=max(dp_decreasing[index],temp)

    final=0
    for i in range(n):
        temp=dp_increasing[i]+dp_decreasing[i]-1
        final=max(final,temp)
    return final

arr=list(map(int,input().split()))
n=len(arr)
print(solve(arr,n))
