def fib(n):
    if(n<=1):
        return n
    else:
        last=fib(n-1)
        slast=fib(n-2)
        return last+slast

print(fib(int(input())))
