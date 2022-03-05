def myfunc(n,m):
    if(n<0):
        return 0
    if(n==0):
        return 1
    count=0
    for i in range(1,m+1):
        count+=myfunc(n-i,m)
    return count

print(myfunc(int(input()),int(input())))
        
