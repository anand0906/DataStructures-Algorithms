

def solve(n,cost,weight,capacity):
    if(n==0):
        return 0
    items=list(zip(cost,weight))
    items.sort(key=lambda x:x[1]/x[0])
    total=0
    for itemCost,itemWeight in items:
        if(itemWeight<=capacity):
            total+=itemCost
            capacity-=itemWeight
        else:
            unitCost=itemCost/itemWeight
            total+=(capacity*unitCost)
            capacity-=capacity
        if(capacity==0):
            break
    return total
        
    
cost=list(map(int,input().split()))
weight=list(map(int,input().split()))
capacity=int(input())
n=len(cost)
print(solve(n,cost,weight,capacity))
