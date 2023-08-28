def check(i,k):
    s=1
    for i in range(i):
        s*=k
    return s

def bruteForce(num,n):
    for i in range(1,num+1):
        temp=check(i,n)
        if(temp==num):
            return i
    return -1

def BinarySearch(num,n):
    left,right=1,num
    while(left<=right):
        mid=(left+right)//2
        temp=check(mid,n)
        if(temp==num):
            return mid
        elif(temp > num):
            right=mid-1
        else:
            left=mid+1
    return -1

num=int(input())
n=int(input())
print(bruteForce(num,n))
print(BinarySearch(num,n))

    
        
    
