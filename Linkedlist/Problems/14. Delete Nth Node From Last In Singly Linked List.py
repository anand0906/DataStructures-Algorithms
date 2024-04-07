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

def delete(head,n):
    if(head==None):
        return head
    length=0
    temp=head
    while temp:
        length+=1
        temp=temp.next
    if(length==n):
        head=head.next
        return head
    target=length-n
    cnt=0
    temp=head
    while temp:
        cnt+=1
        if(cnt==target):
            break
        temp=temp.next
    temp.next=temp.next.next
    return head

def optimized(head,n):
    slow,fast=head,head
    for i in range(n):
        fast=fast.next
    if(fast==None):
        head=head.next
        return head
    while fast.next:
        fast=fast.next
        slow=slow.next
    slow.next=slow.next.next
    return head
    

arr=[1,2,3,4,5]
n=2
head=convert(arr)
printLL(head)
#head=delete(head,1)
head=optimized(head,2)
printLL(head)
