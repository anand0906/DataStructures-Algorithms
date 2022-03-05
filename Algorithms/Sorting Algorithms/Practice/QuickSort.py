#code for finding right place of a pivot element
#all elememts to left of pvot should be smaller than this
#all elements to right of pivot should be greater than this
def partion(a,low,high):
    pvot=low
    i=low
    j=high
    #loop untill you reach i crossed j
    while(i<j):
        #sort elements to position the all left elements are small
        while (i<len(a) and a[i]<=a[pvot]):
            i+=1
        while (a[j]>a[pvot]):
            j-=1
        if(i<j):
            a[j],a[i]=a[i],a[j]
    a[pvot],a[j]=a[j],a[pvot]
    return j

def quicksort(arr,low,high):
    if(low<high):
        temp=partion(arr,low,high)
        quicksort(arr,low,temp-1)
        quicksort(arr,temp+1,high)
    return arr


arr=list(map(int,input().split()))
n=len(arr)
print(quicksort(arr,0,n-1))





def quicksort(arr,low,high):
    if(low<high):
        temp=partion(arr,low,high)
        quicksort(arr,temp-1,high)
        quicksort(arr,low,temp-1)

def partion(arr,low,high):
    pivot=low
    i=low
    j=high
    while (i<j):
        while(i<len(arr) and arr[i]<arr[pivot]):
            i+=1
        while(j>=0 and arr[j]>arr[pivot]):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[pivot],arr[j]=arr[j],arr[pivot]
    return j
arr=list(map(int,input().split()))
n=len(arr)
print(quicksort(arr,0,n-1))
        
