#Recursion
#print the given string n times
n=int(input())
#for i in range(n):
#    print("mystring")
def myfunc(i,n):
    if(i==n):
        return
    print("mystring")
    myfunc(i+1,n)
#myfunc(0,n)
def myfunc(i,n):
    """Prints the numbers from 1 to n"""
    if(i>n):
        return
    print(i)
    myfunc(i+1,n)
#myfunc(1,n)
def myfunc(i,n):
    """Prints the numbers from 1 to n using backtracking"""
    if(i<1):
        return
    myfunc(i-1,n)
    print(i)
myfunc(n,n)
