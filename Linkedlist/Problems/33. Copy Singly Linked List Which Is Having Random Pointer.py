class Node:
    def __init__(self,data,next=None,random=None):
        self.data=data
        self.next=next
        self.random=random

    def __str__(self):
        return str(self.random.data) if self.random else "None"


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
        print(temp.data,temp.random,sep=":",end="->")
        temp=temp.next
    print()

def bruteForce(head):
    temp=head
    copy={}
    while temp:
        copy[temp]=Node(temp.data)
        temp=temp.next
    temp=head
    while temp:
        copy[temp].next=copy.get(temp.next)
        copy[temp].random=copy.get(temp.random)
        temp=temp.next
    return copy[head]

def insertCopyNodes(head):
    temp=head
    while temp:
        new=Node(temp.data)
        new.next=temp.next
        temp.next=new
        temp=temp.next.next
    return head

def updateRandom(head):
    temp=head
    while temp:
        copyNode=temp.next
        if(temp.random):
            copyNode.random=temp.random.next
        else:
            copyNode.random=None
        temp=temp.next.next
    return head
        

def optimized(head):
    head=insertCopyNodes(head)
    head=updateRandom(head)
    dummy=Node(-1)
    new=dummy
    temp=head
    while temp:
        new.next=temp.next
        new=new.next
        temp.next=temp.next.next
        temp=temp.next
    return head
arr=[1,2,3]
head=convert(arr)
head.random=None
head.next.random=head
head.next.next.random=head.next
printLL(head)
#head=bruteForce(head)
head=optimized(head)
printLL(head)
