def solve():
    array=list(map(int,input().split()))
    start=int(input())
    end=int(input())
    distance=[float('inf') for i in range(100000)]
    distance[start]=0
    queue=[(start,0)]
    mod=100000
    while queue:
        current,steps=queue.pop(0)
        for i in array:
            new=(current*i)%mod
            if(steps+1 < distance[new]):
                distance[new]=steps+1
                if(new==end):
                    return distance[new]
                queue.append((new,distance[new]))
    return -1
print(solve())
