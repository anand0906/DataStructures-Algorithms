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
    while temp:
        if temp in visited:
            return temp
        visited[temp]=1
        temp=temp.next
    return None

def optimized(head):
    slow,fast=head,head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if(fast==slow):
            temp1,temp2=head,slow
            while temp1!=temp2:
                temp1=temp1.next
                temp2=temp2.next
            return temp1
    return None
    
    

arr=[1,2,3]
head=convert(arr)
head.next.next=head.next
print(bruteForce(head))
print(optimized(head))
