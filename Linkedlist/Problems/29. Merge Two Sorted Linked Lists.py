class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)

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


def solve(first, second):
    t1,t2=first,second
    dummy=Node(-1)
    temp=dummy
    while t1 and t2:
        if(t1.data < t2.data):
            temp.next=t1
            temp=temp.next
            t1=t1.next
        else:
            temp.next=t2
            temp=temp.next
            t2=t2.next
    if(t1):
        temp.next=t1
    if(t2):
        temp.next=t2
    return dummy.next


arr1=[1,2,3,4,5,6,7]
arr2=[1,1,2,3,4,5,6]
first=convert(arr1)
second=convert(arr2)
printLL(first)
printLL(second)
head=solve(first,second)
printLL(head)
