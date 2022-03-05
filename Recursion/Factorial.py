def fact(n,ans):
    if(n==0):
        print(ans)
        return
    else:
        fact(n-1,ans*n)
#fact(int(input()),1)
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
print(fact(int(input())))
