s=0
for i in range(1,256):
    for j in range(1,12):
        a=(i*i)-(4*i*j)
        i*=4
        j+=2
        s+=a
        s-=1
print(s)
