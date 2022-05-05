def myfunc(a,b,c=0):
    global final
    if(a==b):
        final=min(final,c)
        return c
    if(a<=0):
        return float('inf')
    if c>final:
        return float('inf')
    first=float('inf')
    second=float('inf')
    if a<b:
        second=myfunc(a*2,b,c+1)
    first=myfunc(a-1,b,c+1)
    return min(first,second)
final=float('inf')
print(myfunc(int(input()),int(input())))
