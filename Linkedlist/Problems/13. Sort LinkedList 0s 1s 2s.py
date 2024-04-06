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

def bruteForce(head):
    if(head==None or head.next==None):
        return head5
    cnt0,cnt1,cnt2=0,0,0
    temp=head
    while temp:
        if(temp.data==0):
            cnt0+=1
        elif(temp.data==1):
            cnt1+=1
        else:
            cnt2+=1
        temp=temp.next

    temp=head
    while temp:
        if(cnt0!=0):
            temp.data=0
            cnt0-=1
        elif(cnt1!=0):
            temp.data=1
            cnt1-=1
        else:
            temp.data=2
            cnt2-=1
        temp=temp.next
    return head

def optimized(head):
    zeroHead,oneHead,secHead=Node(-1),Node(-1),Node(-1)
    zero,one,sec=zeroHead,oneHead,secHead
    temp=head
    while temp:
        if(temp.data==0):
            zero.next=temp
            zero=temp
        elif(temp.data==1):
            one.next=temp
            one=temp
        elif(temp.data==2):
            sec.next=temp
            sec=temp
        temp=temp.next

    temp=[]
    current=zero
    if(one.data!=-1):
        current.next=oneHead.next
        current=one
    if(sec.data!=-1):
        current.next=secHead.next
        sec.next=None
    else:
        one.next=None

    return zeroHead.next;
            


    
    
        
    


arr=[0,0,2,1,0,2]
head=convert(arr)
printLL(head)
#head=bruteForce(head)
head=optimized(head)
printLL(head)
