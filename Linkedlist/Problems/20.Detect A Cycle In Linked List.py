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
    visited={}
    temp=head
    while temp:
        if(visited.get(temp)):
            return True
        visited[temp]=1
        temp=temp.next
    return False

def optimized(head):
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            return True
    return False

    



arr=[1,2,3]
head=convert(arr)
head.next.next=head.next
#printLL(head)
print(bruteForce(head))
print(optimized(head))
