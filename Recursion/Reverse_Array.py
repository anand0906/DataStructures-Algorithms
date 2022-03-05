"""arr=input().split()
l=0
r=len(arr)-1
while l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1
print(*arr)"""

def reverse(arr,l,r):
    if(l>r):
        print(arr)
        return
    else:
        arr[l],arr[r]=arr[r],arr[l]
        reverse(arr,l+1,r-1)
arr=input().split()
#reverse(arr,0,len(arr)-1)
"""n=len(arr)
for i in range(n//2):
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
print(arr)"""
def reverse(arr,i):
    if(i>=len(arr)//2):
        print(arr)
        return
    else:
        arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
        reverse(arr,i+1)
#reverse(arr,0)
def reverse(arr,i):
    if(i<0):
        return []
    else:
        return [arr[i]]+reverse(arr,i-1)
print(reverse(arr,len(arr)-1))
    
