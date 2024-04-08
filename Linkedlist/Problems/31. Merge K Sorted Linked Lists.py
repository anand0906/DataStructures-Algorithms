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


def bruteForce(lists):
    arr=[]
    for head in lists:
        temp=head
        while temp:
            arr.append(temp.data)
            temp=temp.next
    arr.sort()
    dummy=Node(-1)
    temp=dummy
    for i in arr:
        new=Node(i)
        temp.next=new
        temp=new
    return dummy.next

def merge(first, second):
    t1,t2=first,second
    dummy=Node(-1)
    temp=dummy
    while t1 and t2:
        if(t1.data <= t2.data):
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

def optimized(lists):
    n=len(lists)
    head=lists[0]
    for i in range(1,n):
        mergeHead=merge(head,lists[i])
        head=mergeHead
    return head

import heapq
def moreOptimized(lists):
    pq=[]
    n=len(lists)
    for i in range(n):
        heapq.heappush(pq,(lists[i].data,id(lists[i]),lists[i]))
    dummy=Node(-1)
    temp=dummy
    while pq:
        data,_,node=heapq.heappop(pq)
        temp.next=node
        node=node.next
        if(node):
            heapq.heappush(pq,(node.data,id(node),node))
        temp=temp.next
    return dummy.next
    


arr1=[1,2,3,4,5,6,7]
arr2=[1,1,2,3,4,5,6]
arr3=[2,5,6,7,8,9]
first=convert(arr1)
second=convert(arr2)
third=convert(arr3)
printLL(first)
printLL(second)
printLL(third)
#head=bruteForce([first,second,third])
#head=optimized([first,second,third])
head=moreOptimized([first,second,third])
printLL(head)   
