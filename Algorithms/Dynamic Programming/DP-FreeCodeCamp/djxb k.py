d={1:',@',
2:'ABCabc2',
3:'DEFdef3',
4:'GHIghi4',
5:'JKLjkl5',
6:'MNOmno6',
7:'PQRSpqrs7',
8:'TUVtuv8',
9:'WXYZwxyz9',
 12:'_' ,
0:' 0'
}
t=int(input())
res=[]
for _ in range (t):
    a=input()
    n=len(a)
    final=''
    ind=0
    while ind<n:
        count=1
        ind+=1
        while ind<n and a[ind]==a[ind-1]:
            ind+=1
            count+=1
        if(a[ind-1]=='_'):
            continue
        temp=d[int(a[ind-1])]
        final+=temp[count%len(temp)-1]
    print(final)
        
