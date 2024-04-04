class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

def length(head):
    count=0
    temp=head
    while temp:
        count+=1
        temp=temp.next
    return count

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
print(length(head))

