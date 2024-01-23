arr=input().split()
start=input()
target=input()
visited={i:False for i in arr}
if start in visited:
    visited[start]=True
queue=[]
queue.append([start])
while queue:
    seq=queue.pop(0)
    word=seq[-1]
    if(word==target):
        print(seq)
        break
    for i in range(len(word)):
        for j in range(25):
            temp=list(word)
            charcter=chr(ord('a')+j)
            temp[i]=charcter
            temp="".join(temp)
            if(temp in visited and (not visited[temp])):
                queue.append(seq+[temp])
                visited[temp]=True
else:
    print(-1)
            
