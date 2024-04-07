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

def bruteForce(head):
    cnt=0
    temp=head
    while temp:
        cnt+=1
        temp=temp.next
    temp1=head
    for i in range(cnt//2):
        temp1=temp1.next
    return temp1

def optimized(head):
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

arr=[1,2,3,4,5,6]
head=convert(arr)
printLL(head)
print(bruteForce(head))
print(optimized(head))
