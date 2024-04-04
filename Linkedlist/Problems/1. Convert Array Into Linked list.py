class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def convert(arr):
    n=len(arr)
    head=Node(arr[0])
    current=head
    for i in range(1,n):
        temp=Node(arr[i])
        current.next=temp
        current=temp
    return head

def printLinkedList(head):
    while head:
        print(head.data,end="->")
        head=head.next

arr=list(map(int,input().split()))
head=convert(arr)
printLinkedList(head)


