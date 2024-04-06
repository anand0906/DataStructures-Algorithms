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
    if(head==None or head.next==None):
        return head
    newOrder=[]
    temp=head
    while temp and temp.next:
        newOrder.append(temp.data)
        temp=temp.next.next
    if(temp):
        newOrder.append(temp.data)

    temp=head.next
    while temp and temp.next:
        newOrder.append(temp.data)
        temp=temp.next.next
    if(temp):
        newOrder.append(temp.data)

    temp=head
    i=0
    while temp and temp.next:
        temp.data=newOrder[i]
        i+=1
        temp=temp.next
    if(temp):
        temp.data=newOrder[i]

    return head

def optimized(head):
    if(head==None or head.next==None):
        return head
    oddHead=head
    evenHead=head.next

    odd=head
    even=head.next
    while even and even.next:
        odd.next=odd.next.next
        even.next=even.next.next

        odd=odd.next
        even=even.next

    odd.next=evenHead

    return head
        

    
    
        
        
    


arr=[1,2,3,4,5,6]
head=convert(arr)
printLL(head)
#head=bruteForce(head)
head=optimized(head)
printLL(head)
