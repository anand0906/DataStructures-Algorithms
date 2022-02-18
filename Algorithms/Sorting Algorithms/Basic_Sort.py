#Normal Program For Sorting

class Solution:

    def ascending_sort(self,arr):
        n=len(arr)
        if(n==1):
            return arr
        else:
            for i in range(n):
                for j in range(i+1,n):
                    if(arr[i]>arr[j]):
                        #swap two elemets arr[i] and arr[j]
                        temp=arr[i]
                        arr[i]=arr[j]
                        arr[j]=temp
            return arr

    def descending_sort(self,arr):
        n=len(arr)
        if(n==1):
            return arr
        else:
            for i in range(n):
                for j in range(i+1,n):
                    if(arr[i]<arr[j]):
                        #swap two elemets arr[i] and arr[j]
                        temp=arr[i]
                        arr[i]=arr[j]
                        arr[j]=temp
            return arr


class Solution2:

    def sort(self,arr):
        n=len(arr)
        if(n==1):
            return arr
        else:
            final_sorted_array=[]
            for i in range(n):
                small=float('inf')
                for j in range(len(arr)):
                    if(arr[j]<small):
                        small=j
                final_sorted_array.append(arr[small])
                del arr[small]
            return final_sorted_array


        


arr=list(map(int,input().split()))
solution=Solution()
print(*solution.ascending_sort(arr),sep=" ")
print(*solution.descending_sort(arr),sep=" ")
solution=Solution2()
print(*solution.sort(arr))

