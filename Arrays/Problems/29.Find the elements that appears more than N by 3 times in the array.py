def bruteForce(n,arr):
    count={}
    final=[]
    for i in range(n):
        if arr[i] in count:
            count[arr[i]]+=1
        else:
            count[arr[i]]=1

        if(count[arr[i]] > n//3 and arr[i] not in final):
            final.append(arr[i])

    return sorted(final)

def optimized(n,arr):
    cnt1,cnt2=0,0
    ele1,ele2=None,None
    for i in range(n):
        current=arr[i]
        if(cnt1==0 and current!=ele2):
            cnt1+=1
            ele1=current
        elif(cnt2==0 and current!=ele1):
            cnt2+=1
            ele2=current
        elif(ele1==current):
            cnt1+=1
        elif(ele2==current):
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    c1,c2=0,0
    for i in range(n):
        if(ele1==arr[i]):
            c1+=1
        if(ele2==arr[i]):
            c2+=1
    final=[]
    if(c1>(n//3)):
        final.append(ele1)
    if(c2>(n//3)):
        final.append(ele2)
    return sorted(final)


arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
