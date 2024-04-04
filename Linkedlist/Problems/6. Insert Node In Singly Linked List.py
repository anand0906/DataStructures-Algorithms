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

def insertAtHead(head,data):
    temp=Node(data)
    temp.next=head
    return temp

def insertAtTail(head,data):
    if(head==None):
        return Node(data)
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=Node(data)
    return head

def insertAtPosition(head,data,pos):
    if(head==None):
        if(pos==1):
            return Node(data)
        return head
    if(pos==1):
        temp=Node(data)
        temp.next=head
        return temp
    count=0
    temp=head
    while temp:
        count+=1
        if(count==pos-1):
            new=Node(data,temp.next)
            temp.next=new
            break
        temp=temp.next
    return head

def insertAtValue(head,data,value):
    if(head==None):
        return None
    if(head.data==value):
        temp=Node(data)
        temp.next=head
        return temp
    temp=head
    while temp:
        if(temp.next!=None and temp.next.data==value):
            new=Node(data,temp.next)
            temp.next=new
            break
        temp=temp.next
    return head


        
        
        

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
printLinkedList(head)
#head=insertAtHead(head,5)
#head=insertAtTail(head,50)
#head=insertAtPosition(head,50,5)
#head=insertAtValue(head,50,100)
printLinkedList(head)
