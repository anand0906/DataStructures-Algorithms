def myfun(n,sum):
    if(n==0):
        print(sum)
        return
    else:
        myfun(n-1,sum+n)
def myfun(n):
    if(n==0):
        return 0
    else:
        return n+myfun(n-1)
#myfun(int(input()),0)
print(myfun(int(input())))
