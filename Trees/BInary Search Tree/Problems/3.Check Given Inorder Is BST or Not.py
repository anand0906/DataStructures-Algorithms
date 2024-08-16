
def check(inorder):
    n=len(inorder)
    for i in range(n-1):
        if(inorder[i]>=inorder[i+1]):
            return False
    return True


inorder=list(map(int,input().split()))
print(check(inorder))
