from itertools import accumulate as ac
from operator  import add
#print(dir(operator))
a=list(map(int,input().split()))
k=list(ac(a,add))
print(k)
for i in k:
    print(i)
