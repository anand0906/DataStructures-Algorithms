def bruteForce(n,m,arr1,arr2):
    arr=[0]*(n+m)
    index=0
    i,j=0,0
    while (i<n and j<m) :
        if(arr1[i]<=arr2[j]):
            arr[index]=arr1[i]
            i+=1
            index+=1
        else:
            arr[index]=arr2[j]
            j+=1
            index+=1

    while i<n:
        arr[index]=arr1[i]
        i+=1
        index+=1

    while j<m:
        arr[index]=arr2[j]
        j+=1
        index+=1
    return arr

def optimized(n,m,arr1,arr2):
    i,j=n-1,0
    while i>=0 and j<m:
        if(arr1[i]>arr2[j]):
            arr1[i],arr2[j]=arr2[j],arr1[i]
            i-=1
            j+=1
        else:
            break
    arr1.sort()
    arr2.sort()
    return arr1+arr2

import math

def swap(arr1,arr2,left,right):
    if(arr1[left]>arr2[right]):
        arr1[left],arr2[right]=arr2[right],arr1[left]

def optimized2(n,m,arr1,arr2):
    length=n+m
    gap=math.ceil(length/2)
    while(gap>0):
        left=0
        right=left+gap
        while right<length:
            if(left<n and right>=n):
                swap(arr1,arr2,left,right-n)
            elif(left>=n and right>=n):
                swap(arr2,arr2,left-n,right-n)
            else:
                swap(arr1,arr1,left,right)
            left+=1
            right+=1
        if(gap==1):
            break
        gap=math.ceil(gap/2)
    return arr1+arr2


                
        
        
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n,m=len(arr1),len(arr2)
print(bruteForce(n,m,arr1,arr2))
print(optimized(n,m,arr1,arr2))
print(optimized2(n,m,arr1,arr2))
