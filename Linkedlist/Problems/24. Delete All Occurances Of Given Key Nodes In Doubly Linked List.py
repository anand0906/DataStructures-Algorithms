class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev


def convert(arr):
    n=len(arr)
    head=Node(arr[0])
    temp=head
    for i in range(1,n):
        new=Node(arr[i])
        new.prev=temp
        temp.next=new
        temp=new
    return head

def printDLL(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print()

def solve(head,key):
    temp=head
    while temp:
        if(temp.data==key):
            if(temp==head):
                head=temp.next
            next=temp.next
            prev=temp.prev
            if(next):
                next.prev=prev
            if(prev):
                prev.next=next
            temp=next
        else:
            temp=temp.next
    return head

arr=[2,1,2,3,4,2,2,2]
head=convert(arr)
printDLL(head)
head=solve(head,2)
printDLL(head)
