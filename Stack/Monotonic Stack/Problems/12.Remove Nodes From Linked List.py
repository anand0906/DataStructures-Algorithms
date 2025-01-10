def solve(head):
    temp=head
    stack=[]
    while head:
        while stack and head.val>stack[-1].val:
            node=stack.pop()
            node.val=None
        stack.append(head)
        head=head.next
    dummyNode=ListNode()
    current=dummyNode
    while temp:
        if(temp.val):
            current.next=temp
            current=temp
        temp=temp.next
    return dummyNode.next
