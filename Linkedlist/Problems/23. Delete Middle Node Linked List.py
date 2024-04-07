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
    if(head==None or head.next==None):
        return None
    length=0
    temp=head
    while temp:
        length+=1
        temp=temp.next
    mid=(length//2)
    cnt=0
    temp=head
    while temp:
        cnt+=1
        if(cnt==mid):
            break
        temp=temp.next
    temp.next=temp.next.next
    return head


def optimized(head):
    if(head==None or head.next==None):
        return None
    slow,fast=head,head
    prev=None
    while fast and fast.next:
        prev=slow
        slow=slow.next
        fast=fast.next.next
    prev.next=prev.next.next
    return head


arr=[1,2,3]
head=convert(arr)
printLL(head)
#head=bruteForce(head)
head=optimized(head)
printLL(head)


