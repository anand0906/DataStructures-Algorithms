
def compare(s1,s2):
    if(len(s1)!=len(s2)+1):
        return False
    n1,n2=0,0
    while n1<len(s1):
        if(n2<len(s2) and s1[n1]==s2[n2]):
            n1+=1
            n2+=1
        else:
            n1+=1
    if(n1==len(s1) and n2==len(s2)):
        return True
    return False


def solve(arr,n):
    dp=[0]*n
    for i in range(n):
        dp[i]=1
    for index in range(n):
        for last_index in range(index):
            if(compare(arr[index],arr[last_index])):
                temp=1+dp[last_index]
                dp[index]=max(dp[index],temp)
    final=-1
    for i in dp:
        final=max(final,i)
    return final
arr=input().split()
n=len(arr)
print(solve(arr,n))
