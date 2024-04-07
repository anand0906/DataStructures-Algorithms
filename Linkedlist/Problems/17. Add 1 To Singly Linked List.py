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

def reverse(head):
    temp=head
    current=head
    previous=None
    while temp:
        current=temp
        temp.next,previous=previous,temp.next
        temp=previous
        previous=current
    return current


def helper(node):
    if(node==None):
        return 1
    carry=helper(node.next)
    s=node.data+carry
    if(s>=10):
        node.data=s%10
        return s//10
    else:
        node.data=s
        return 0

def recursive(head):
    carry=helper(head)
    if(carry!=0):
        new=Node(carry)
        new.next=head
        return new
    return head
        

def iterative(head):
    temp=head
    carry=1
    head1=reverse(temp)
    temp1=head1
    while temp1:
        s=temp1.data+carry
        if(s<10):
            temp1.data=s
            temp1=temp1.next
            carry=0
            break
        else:
            temp1.data=s%10
            temp1=temp1.next
            carry=s//10
    head2=reverse(head1)
    if(carry!=0):
        new=Node(carry)
        new.next=head2
        return new
    return head2
        
        
    
arr=[9,9,9]
head=convert(arr)
printLL(head)
#head=iterative(head)
head=recursive(head)
printLL(head)
