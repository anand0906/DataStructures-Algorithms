k=input()
l=0
r=len(k)-1
while l<r:
    if(k[l]!=k[r]):
        print("Not Palindrome")
        break
    else:
        l+=1
        r-=1
else:
    print("Palindrome")
n=len(k)
for i in range(len(k)//2):
    if(k[i]!=k[n-i-1]):
        print("Not Palindrome")
        break
else:
    print("Palindrome")


def check(k,i):
    if(i>=len(k)//2):
        return True
    elif(k[i]!=k[len(k)-i-1]):
        return False
    else:
        return check(k,i+1)
print(check(k,0))
    
        
    
