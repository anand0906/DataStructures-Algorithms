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

def reverse(head):
    temp=head
    previous=None
    current=None
    while temp:
        current=temp
        temp.next,previous=previous,temp.next
        temp=previous
        previous=current
    return current

def getKthNode(temp,k):
    cnt=0
    while temp:
        cnt+=1
        if(cnt==k):
            return temp
        temp=temp.next
    return None
        

def solve(head,k):
    temp=head
    nextNode=None
    prevLast=None
    while temp:
        kthNode=getKthNode(temp,k)
        if(kthNode==None):
            if(prevLast):
                prevLast.next=temp
            break
        nextNode=kthNode.next
        kthNode.next=None
        reverse(temp)
        if(temp==head):
            head=kthNode
        else:
            prevLast.next=kthNode
        prevLast=temp
        temp=nextNode
    return head

arr=[1,2,3,4,5,6,7]
head=convert(arr)
printLL(head)
head=solve(head,2)
printLL(head)
