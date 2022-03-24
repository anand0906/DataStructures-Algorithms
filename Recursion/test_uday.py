def myfunc(n,c=0):
    if(n==0):
        return c
    k=myfunc(n-1,c+1)
    print(n,c)
    return k
myfunc(int(input()))
