class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def printLinkedList(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print()

def deleteHead(head):
    if(head==None):
        return None
    temp=head
    head=head.next
    return head

def deleteTail(head):
    if(head==None or head.next==None):
        return None
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
    return head

def deleteByPosition(head,pos):
    if(head==None):
        return None
    if(pos==1):
        temp=head
        head=head.next
        return head
    previous=None
    temp=head
    count=0
    while temp:
        count+=1
        if(count==pos):
            previous.next=temp.next
            return head
        previous=temp
        temp=temp.next
    return head

def deleteByValue(head,value):
    if(head==None):
        return None
    if(head.data==value):
        temp=head
        head=head.next
        return head
    previous=None
    temp=head
    while temp:
        if(temp.data==value):
            previous.next=temp.next
            return head
        previous=temp
        temp=temp.next
    return head
        
        

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
printLinkedList(head)
#head=deleteHead(head)
#head=deleteTail(head)
#head=deleteByPosition(head,4)
#head=deleteByValue(head,30)
printLinkedList(head)
