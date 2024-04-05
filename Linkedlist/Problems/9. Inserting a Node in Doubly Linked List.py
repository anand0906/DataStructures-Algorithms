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


def insertBeforeHead(head,data):
    if(head==None):
        return Node(data)
    new=Node(data)
    new.next=head
    head.prev=new
    return new

def insertBeforeTail(head,data):
    if(head==None):
        return Node(data)
    if(head.next==None):
        head=insertBeforeHead(head,data)
        return head
    temp=head
    while temp.next:
        temp=temp.next
    tail=temp
    previous=tail.prev
    new=Node(data)
    new.next=tail
    new.prev=previous
    tail.prev=new
    previous.next=new
    return head

def insertBeforeKthElement(head,data,k):
    if(head==None):
        return None
    cnt=0
    temp=head
    while temp:
        cnt+=1
        if(cnt==k):
            break
        temp=temp.next
    else:
        return None
    previous=temp.prev
    new=Node(data)
    new.next=temp
    new.prev=previous
    previous.next=new
    temp.prev=new
    return head

array=[10,20,30,40,50]
head=convert(array)
printLinkedList(head)
#head=insertBeforeHead(head,5)
#head=insertBeforeTail(head,45)
head=insertBeforeKthElement(head,45,4)
printLinkedList(head)
