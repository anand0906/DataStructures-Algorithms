#https://www.youtube.com/watch?v=3YFUQDRL1s4&list=PLTZbNwgO5ebqdDy16sKYjmfCzkzoS0fxN&index=1
def checkForTwoPoints(p1,p2):
    x1,y1=p1
    x2,y2=p2
    cross_product=x1*y2-x2*y1
    if(cross_product > 0):
        return "Anti ClockWise"
    elif(cross_product < 0):
        return "clockwise"
    else:
        return "collinear"

def checkForThreePoints(p0,p1,p2):
    v1=(p1[0]-p0[0],p1[1]-p0[1])
    v2=(p2[0]-p0[0],p2[1]-p0[1])
    x1,y1=v1
    x2,y2=v2
    cross_product=x1*y2-x2*y1
    if(cross_product > 0):
        return "Anti ClockWise"
    elif(cross_product < 0):
        return "clockwise"
    else:
        return "collinear"

p1=tuple(map(int,input().split()))
p2=tuple(map(int,input().split()))
print(checkForTwoPoints(p1,p2))

p0=tuple(map(int,input().split()))
p1=tuple(map(int,input().split()))
p2=tuple(map(int,input().split()))
print(checkForThreePoints(p0,p1,p2))
    
