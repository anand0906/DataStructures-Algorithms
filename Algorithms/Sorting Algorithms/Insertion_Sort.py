#Insertion Sort

class InsertionSort:
    @staticmethod
    def insert(arr,j,current):
        t=j
        for t in range(j,-1,-1):
            if(arr[t-1]>current):
                arr[t]=arr[t-1]
            else:
                break
        arr[t]=current
        
    @staticmethod 
    def insert_2(arr,j,current):
        while(j>0 and arr[j-1]>current):
            arr[j]=arr[j-1]
            j-=1
        arr[j]=current

    def ascending_sort(self,arr):
        n=len(arr)
        for i in range(n):
            current=arr[i]
            j=i
            #self.insert(arr,j,current)
            self.insert_2(arr,j,current)
            print("Pass {}".format(i+1),arr)
        return arr


arr=list(map(int,input().split()))
temp=InsertionSort()
print(temp.ascending_sort(arr.copy()))

        
                
