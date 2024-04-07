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


def bruteForce(head,k):
    final=[]
    temp=head
    while temp:
        temp1=temp.next
        while temp1:
            if(temp1.data+temp.data==k):
                final.append([temp.data,temp1.data])
            temp1=temp1.next
        temp=temp.next
    return final

def optimized(head,k):
    final=[]
    start=head
    last=head
    while last.next:
        last=last.next
    while start and last and start.data <= last.data:
        s=start.data+last.data
        if(s==k):
            final.append([start.data,last.data])
            start=start.next
            last=last.prev
        if(s>k):
            last=last.prev
        if(s<k):
            start=start.next
    return final



arr=[1,2,3,4]
head=convert(arr)
printDLL(head)
print(bruteForce(head,5))
print(optimized(head,5))

