arr=input().split()
start=input()
target=input()
visited={i:False for i in arr}
if start in visited:
    visited[start]=True
queue=[]
queue.append((start,1))
while queue:
    word,steps=queue.pop(0)
    if(word==target):
        print(steps)
        break
    for i in range(len(word)):
        for j in range(25):
            temp=list(word)
            charcter=chr(ord('a')+j)
            temp[i]=charcter
            temp="".join(temp)
            if(temp in visited and (not visited[temp])):
                queue.append((temp,steps+1))
                visited[temp]=True
else:
    print(-1)
            
