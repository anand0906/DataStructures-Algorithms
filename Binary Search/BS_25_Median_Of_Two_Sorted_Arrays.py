def mergeSort(arr1,arr2):
    final=[]
    n1=len(arr1)
    n2=len(arr2)
    p1=0
    p2=0
    while (p1 < n1 and p2 < n2):
        if(arr1[p1] <= arr2[p2]):
            final.append(arr1[p1])
            p1+=1
        else:
            final.append(arr2[p2])
            p2+=1
    while (p1 < n1):
        final.append(arr1[p1])
        p1+=1
    while (p2 < n2):
        final.append(arr2[p2])
        p2+=1
    return final


def bruteForce(arr1, arr2):
    n1=len(arr1)
    n2=len(arr2)
    total=n1+n2
    if(total&1):
        temp=mergeSort(arr1,arr2)
        print(temp[total//2])
    else:
        temp=mergeSort(arr1,arr2)
        print((temp[(total//2)-1]+temp[(total//2)])/2)


def betterApproach(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    target1=(n1+n2)//2
    target2=target1-1
    t1=0
    t2=0
    current=-1
    a,b=-1,-1
    while (t1<n1 and t2<n2):
        if(arr1[t1]<=arr2[t2]):
            t1+=1
            current+=1
            if(current==target1):
                a=arr1[t1-1]
            if(current==target2):
                b=arr1[t1-1]
        else:
            t2+=1
            current+=1
            if(current==target1):
                a=arr2[t2-1]
            if(current==target2):
                b=arr2[t2-1]
    while (t1< n1):
        t1+=1
        current+=1
        if(current==target1):
            a=arr1[t1-1]
        if(current==target2):
            b=arr1[t1-1]
    while(t2<n2):
        t2+=1
        current+=1
        if(current==target1):
            a=arr2[t2-1]
        if(current==target2):
            b=arr2[t2-1]
    total=n1+n2
    if(not(total&1)):
        print((a+b)/2)
    else:
        print(a)
        

def binarySearch(arr1,arr2):
    n1,n2=len(arr1),len(arr2)
    if(n1>n2):
        return binarySearch(arr2,arr1)
    left,right=0,n1
    n=n1+n2
    leftHalf=(n+1)//2
    while(left<=right):
        x=(left+right)//2
        y=leftHalf-x
        l1Index=x-1
        l2Index=y-1
        r1Index=x
        r2Index=y
        l1,l2,r1,r2=float("-inf"),float("-inf"),float("inf"),float("inf")
        if(l1Index<n1):
            l1=arr1[l1Index]
        if(l2Index<n2):
            l2=arr2[l2Index]
        if(r1Index<n1):
            r1=arr1[r1Index]
        if(r2Index<n2):
            r2=arr2[r2Index]
        t1=max(l1,l2)
        t2=min(r1,r2)
        if(l1 <= r2 and l2 <= r1):
            if(n%2==0):
                return sum([t1,t2])/2
            else:
                return t1
        elif(l1>r2):
            right=x-1
        else:
            left=x+1
    return 0
        
    
            
        




arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
bruteForce(arr1,arr2)
betterApproach(arr1,arr2)
print(binarySearch(arr1,arr2))

    
            
