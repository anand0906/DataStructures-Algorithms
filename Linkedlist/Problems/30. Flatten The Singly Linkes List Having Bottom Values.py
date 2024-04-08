class Node:
    def __init__(self,data,next=None,bottom=None):
        self.data=data
        self.next=next
        self.bottom=bottom

def convertLL(arr):
    if(arr==None):
        return None
    n=len(arr)
    head=Node(arr[0])
    temp=head
    for i in range(1,n):
        new=Node(arr[i])
        temp.bottom=new
        temp=new
    return head

def convert(dictionary):
    dummy=Node(-1)
    temp=dummy
    for key,values in dictionary.items():
        new=Node(key)
        temp.next=new
        child=convertLL(values)
        new.bottom=child
        temp=new
    return dummy.next


def printLL(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        child=temp.bottom
        while child:
            print(child.data,end=",")
            child=child.bottom
        print()
        temp=temp.next


def bruteForce(head):
    temp=head
    arr=[]
    while temp:
        arr.append(temp.data)
        child=temp.bottom
        while child:
            arr.append(child.data)
            child=child.bottom
        temp=temp.next
    arr.sort()
    new=Node(arr[0])
    n=len(arr)
    temp=new
    for i in range(1,n):
        n=Node(arr[i])
        temp.next=n
        temp=n
    return new
        
    
    


def merge(first,second):
    t1,t2=first,second
    dummy=Node(-1)
    temp=dummy
    while t1 and t2:
        if(t1.data < t2.data):
            temp.bottom=t1
            temp=t1
            t1=t1.bottom
        else:
            temp.bottom=t2
            temp=t2
            t2=t2.bottom
        temp.next=None
            
    if(t1):
        temp.bottom=t1
    else:
        temp.bottom=t2
    if(dummy.bottom):
        dummy.bottom.next=None
    return dummy.bottom

def solve(head):
    if(head==None or head.next==None):
        return head
    mergedHead=solve(head.next)
    head=merge(head,mergedHead)
    return head


dictionary={1:[3,4],2:[1,2],4:[3,4,5]}
head=convert(dictionary)
printLL(head)
head=solve(head)
#head=bruteForce(head)
printLL(head)
