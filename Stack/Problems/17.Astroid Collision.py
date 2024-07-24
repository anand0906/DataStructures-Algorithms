def solve(n,arr):
    stack=[]
    for i in range(n):
        if(arr[i]>0):
            stack.append(arr[i])
        else:
            while(stack and stack[-1]>0 and abs(arr[i])>stack[-1]):
                stack.pop()
            if(stack and stack[-1]==abs(arr[i])):
                stack.pop()
            elif((not stack) or stack[-1]<0):
                stack.append(arr[i])
    return stack

arr=list(map(int,input().split()))
n=len(arr)
print(solve(n,arr))
