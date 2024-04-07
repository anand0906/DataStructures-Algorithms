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

def checkIntersection(head1,head2):
    check={}
    temp1=head1
    while temp1:
        check[temp1]=1
        temp1=temp1.next
    temp2=head2
    while temp2:
        if(check.get(temp2)):
            return temp2
        temp2=temp2.next
    return None


def checkIntersectionByLength(head1,head2):
    temp1,temp2=head1,head2
    length1,length2=0,0
    while temp1:
        length1+=1
        temp1=temp1.next
    while temp2:
        length2+=1
        temp2=temp2.next
    temp1,temp2=head1,head2
    if(length1>length2):
        diff=length1-length2
        temp1=head1
        for i in range(diff):
            temp1=temp1.next
    else:
        diff=length2-length1
        for i in range(diff):
            temp2=temp2.next    
    while temp1 and temp2:
        if(temp1==temp2):
            return temp1
        temp1=temp1.next
        temp2=temp2.next
    return None

def Optimized(head1,head2):
    temp1,temp2=head1,head2
    while temp1 or temp2:
        if(temp1==temp2):
            return temp1
        if(not temp1):
            temp1=head2
            temp2=temp2.next
        elif(not temp2):
            temp2=head1
            temp1=temp1.next
        else:
            temp1=temp1.next
            temp2=temp2.next
    return None
            
        
            
arr1=[1,2,3,4,5]
arr2=[4,8]
head1=convert(arr1)
head2=convert(arr2)
head2.next.next=head1.next
printLL(head1)
printLL(head2)
print(checkIntersection(head1,head2))
print(checkIntersectionByLength(head1,head2))
print(Optimized(head1,head2))

