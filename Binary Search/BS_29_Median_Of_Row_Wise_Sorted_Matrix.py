def bruteForce(arr,r,c):
    left=float('inf')
    right=float('-inf')
    for i in arr:
        left=min(left,min(i))
    for j in arr:
        right=max(right,max(i))
    final=(r*c)//2
    while(left<=right):
        mid=(left+right)//2
        cntG=0
        cntS=0
        for i in range(r):
            l,r=0,c-1
            for j in arr[i]:
                if(j<mid):
                    cntS+=1
        print(mid,cntS)
        if(cntS<final):
            right=mid-1
        else:
            left=mid+1
    print(left,right)

r=int(input())
c=int(input())
arr=[list(map(int,input().split())) for i in range(r)]
bruteForce(arr,r,c)

#Incompleted

            
                    
                    
                    
            
        
