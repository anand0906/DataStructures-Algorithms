class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)

def convert(arr):
    n=len(arr)
    head=Node(arr[0])
    temp=head
    for i in range(1,n):
        new=Node(arr[i])
        temp.next=new
        temp=new
    return head

def printLL(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print()

def bruteForce(head):
    visited={}
    temp=head
    cnt=0
    while temp:
        cnt+=1
        if temp in visited:
            return cnt-visited[temp]
        visited[temp]=cnt
        temp=temp.next
    return 0

def optimized(head):
    slow,fast=head,head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if(fast==slow):
            temp1,temp2=fast.next,slow
            cnt=1
            while temp1!=temp2:
                cnt+=1
                temp1=temp1.next
            return cnt
    return 0
    
    

arr=[1,2,3]
head=convert(arr)
head.next.next=head.next
print(bruteForce(head))
print(optimized(head))
