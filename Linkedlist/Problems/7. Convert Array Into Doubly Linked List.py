class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

def convert(array):
    n=len(array)
    head=Node(array[0])
    previous=head
    for i in range(1,n):
        temp=Node(array[i])
        temp.prev=previous
        previous.next=temp
        previous=temp
    return head

def printLinkedList(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next


array=list(map(int,input().split()))
head=convert(array)
printLinkedList(head)

