class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev


def convert(arr):
    n=len(arr)
    head=Node(arr[0])
    temp=head
    for i in range(1,n):
        new=Node(arr[i])
        new.prev=temp
        temp.next=new
        temp=new
    return head

def printDLL(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print()

def solve(head):
    temp=head
    while temp and temp.next:
        current=temp.next
        while current and current.data==temp.data:
            current=current.next
        temp.next=current
        if(current):
            current.prev=temp
        temp=temp.next
    return head

arr=[1,1,2,2,3,4,4]
head=convert(arr)
printDLL(head)
head=solve(head)
printDLL(head)
