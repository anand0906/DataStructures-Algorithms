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

def findKthNode(head,k):
    temp=head
    cnt=0
    while temp:
        cnt+=1
        if(cnt==k):
            return temp
        temp=temp.next
    return temp

def solve(head: Node, k: int) -> Node:
    if(head==None or head.next==None or k==0):
        return head
    length=0
    temp=head
    tail=head
    while temp:
        length+=1
        tail=temp
        temp=temp.next
    k=k%length
    if(k==0):
        return head
    kthNode=findKthNode(head,(length-k))
    tail.next=head
    head=kthNode.next
    kthNode.next=None
    return head
arr=[1,2,3,4,5,6,7]
head=convert(arr)
printLL(head)
head=solve(head,2)
printLL(head)
