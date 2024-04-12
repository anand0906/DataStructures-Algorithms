def bruteForce(arr1,arr2):
    s=set()
    for i in arr1:
        s.add(i)
    for j in arr2:
        s.add(j)
    return list(s)

def optimized(arr1,arr2):
    n1,n2=len(arr1),len(arr2)
    i,j=0,0
    union=[]
    while i<n1 and j<n2:
        if(arr1[i]==arr2[j]):
            if(len(union)==0 or arr1[i]!=union[-1]):
                union.append(arr1[i])
            i+=1
        elif(arr1[i] < arr2[j]):
            if(len(union)==0 or arr1[i]!=union[-1]):
                union.append(arr1[i])
            i+=1
        elif(arr1[i] > arr2[j]):
            if(len(union)==0 or arr2[j]!=union[-1]):
                union.append(arr2[j])
            j+=1
    while i<n1:
        if(len(union)==0 or arr1[i]!=union[-1]):
            union.append(arr1[i])
        i+=1
    while j<n2:
        if(len(union)==0 or arr2[j]!=union[-1]):
            union.append(arr2[j])
        j+=1
    return union
    

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(bruteForce(arr1,arr2))
print(optimized(arr1,arr2))
