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

def bruteForce(head):
    arr=[]
    temp=head
    length=0
    while temp:
        length+=1
        arr.append(temp.data)
        temp=temp.next
    arr.sort()
    newHead=Node(arr[0])
    temp=newHead
    for i in range(1,length):
        new=Node(arr[i])
        temp.next=new
        temp=temp.next
    return newHead

def findMiddle(head):
    slow,fast=head,head.next # Slight Change To Original Alogorithm
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

def merge(first,second):
    t1,t2=first,second
    dummy=Node(-1)
    temp=dummy
    while t1 and t2:
        if(t1.data<t2.data):
            temp.next=t1
            temp=t1
            t1=t1.next
        else:
            temp.next=t2
            temp=t2
            t2=t2.next
    if(t1):
        temp.next=t1
    if(t2):
        temp.next=t2
    return dummy.next
          

    
def mergeSort(head):
    if(head==None or head.next==None):
        return head
    middle=findMiddle(head)
    leftHead=head
    rightHead=middle.next
    middle.next=None
    leftHead=mergeSort(leftHead)
    rightHead=mergeSort(rightHead)
    return merge(leftHead,rightHead)
    
    
arr=[5,3,4,1,8,6]
head=convert(arr)
printLL(head)
#head=bruteForce(head)
head=mergeSort(head)
printLL(head)
