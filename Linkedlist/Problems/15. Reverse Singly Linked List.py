class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


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

def bruteforce(head):
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

def optimized(head):
    temp=head
    prev=None
    current=head
    while temp:
        current=temp
        temp.next,prev=prev,temp.next
        temp=prev
        prev=current
    return current
    

arr=[1,2,3,4]
head=convert(arr)
printLL(head)
#head=bruteforce(head)
head=optimized(head)
printLL(head)
