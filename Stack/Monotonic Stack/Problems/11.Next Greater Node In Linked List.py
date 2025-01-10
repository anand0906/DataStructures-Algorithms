def solve(head):
    temp=head
    n=0
    ans=[]
    stack=[]
    while head:
        while stack and head.val >stack[-1][1]:
            index,val=stack.pop()
            ans[index]=head.val
        stack.append((n,head.val))
        n+=1
        ans.append(0)
        head=head.next
    return ans
