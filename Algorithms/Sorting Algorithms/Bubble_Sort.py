#Bubble Sort
class BubbleSort:
    def ascending_sort(self,arr):
        n=len(arr)
        #iterating for n-1 times(passes)
        for i in range(0,n):
            #peform comparison operation for each pass
            for j in range(0,n-1):
                if(arr[j]>arr[j+1]):
                    #perform Swapping
                    arr[j],arr[j+1]=arr[j+1],arr[j]
            print("working on pass {} - {}".format(i+1,arr))
        return arr

    def descending_sort(self,arr):
        n=len(arr)
        #iterating for n-1 times(passes)
        for i in range(0,n):
            #peform comparison operation for each pass
            for j in range(0,n-1):
                if(arr[j]<arr[j+1]):
                    #perform Swapping
                    arr[j],arr[j+1]=arr[j+1],arr[j]
            print("working on pass {} - {}".format(i+1,arr))
        return arr

    def optimized_sort(self,arr):
        n=len(arr)
        for i in range(0,n):
            #let us take swapped as False
            swapped=False
            #doing traversal for n-i-1 means
            #at each pass we area sorting one element
            #so we don't need any more comparision for already sorted elements
            for j in range(0,n-i-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    #it means swapping occurs, arr is unsorted
                    swapped=True
            #if any swapping not occurs at any pass, that means array is already sorted
            #so no need any further passes
            print("working on pass {} - {}".format(i+1,arr))
            if(swapped==False):
                break
        return arr
        
            
from time import process_time
#Taking Input And passing it to function
arr=list(map(int,input().split()))
temp=BubbleSort()
start=process_time()
print(*temp.ascending_sort(arr.copy()))
print("Time Token :",process_time()-start)
start=process_time()
print(*temp.descending_sort(arr.copy()))
print("Time Token :",process_time()-start)
start=process_time()
print(*temp.optimized_sort(arr.copy()))
print("Time Token :",process_time()-start)


