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

def deleteHead(head):
    if(head==None or head.next==None):
        return None
    temp=head
    head=head.next
    head.prev=None
    temp.next=None

    return head

def deleteTail(head):
    if(head==None or head.next==None):
        return None
    tail=head
    while tail.next!=None:
        tail=tail.next
    previous=tail.prev
    previous.next=None
    tail.prev=None
    return head

def deleteByPosition(head,k):
    if(head==None):
        return head
    cnt=0
    temp=head
    while temp:
        cnt+=1
        if(cnt==k):
            break
        temp=temp.next
    prevNode=temp.prev
    nextNode=temp.next
    if(prevNode==None and nextNode==None):
        return None
    if(prevNode==None):
        head=deleteHead(head)
        return head
    if(nextNode==None):
        head=deleteTail(head)
        return head
    prevNode.next=temp.next
    nextNode.prev=prevNode
    temp.next=None
    temp.prev=None
    return head

def deleteByValue(head,data):
    if(head==None):
        return head
    temp=head
    while temp:
        if(temp.data==data):
            break
        temp=temp.next
    prevNode=temp.prev
    nextNode=temp.next
    if(prevNode==None and nextNode==None):
        return None
    if(prevNode==None):
        head=deleteHead(head)
        return head
    if(nextNode==None):
        head=deleteTail(head)
        return head
    prevNode.next=temp.next
    nextNode.prev=prevNode
    temp.next=None
    temp.prev=None
    return head
    
    

array=[10,20,30,40,50]
head=convert(array)
printLinkedList(head)
#head=deleteHead(head)
#head=deleteTail(head)
#head=deleteByPosition(head,5)
#head=deleteByValue(head,50)
printLinkedList(head)
