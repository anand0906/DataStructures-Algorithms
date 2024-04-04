class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def printLinkedList(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
printLinkedList(head)

