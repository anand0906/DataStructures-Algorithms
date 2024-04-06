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

def sum(head1,head2):
    sumHead=Node(-1)
    temp=sumHead
    temp1=head1
    temp2=head2
    carry=0
    while temp1 or temp2:
        s=carry
        if(temp1):
            s+=temp1.data
            temp1=temp1.next
        if(temp2):
            s+=temp2.data
            temp2=temp2.next
        carry=s//10
        new=Node(s%10)
        temp.next=new
        temp=new
    if(carry!=0):
        new=Node(carry)
        temp.next=new
    return sumHead.next
        
        
arr1=[9,9,9,9,9,9,9]
arr2=[9,9,9,9]
head1=convert(arr1)
head2=convert(arr2)
printLL(head1)
printLL(head2)
head=sum(head1,head2)
printLL(head)
