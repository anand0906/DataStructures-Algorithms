class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

def convert(array):
    if(not array):
        return None
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
    print()

def reverseBruteForce(head):
    stack=[]
    temp=head
    while temp:
        stack.append(temp.data)
        temp=temp.next
    temp=head
    while temp:
        temp.data=stack.pop()
        temp=temp.next
    return head

def reverseOptimized(head):
    temp=head
    current=head
    while temp:
        current=temp
        temp.next,temp.prev=temp.prev,temp.next
        temp=temp.prev
    head=current
    return head
    
array=[10,20,30,40,50]
head=convert(array)
printLinkedList(head)
#head=reverseBruteForce(head)
head=reverseOptimized(head)
printLinkedList(head)

