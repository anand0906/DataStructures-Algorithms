#https://www.youtube.com/watch?v=R08OY6yDNy0&list=PLTZbNwgO5ebqdDy16sKYjmfCzkzoS0fxN&index=2

def onSegment(p, q, r):
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))


def checkClockOrAntiClock(p0,p1,p2):
    v1=(p1[0]-p0[0],p1[1]-p0[1])
    v2=(p2[0]-p0[0],p2[1]-p0[1])
    x1,y1=v1
    x2,y2=v2
    cross_product=x1*y2-x2*y1
    if(cross_product > 0):
        return 1
    elif(cross_product < 0):
        return -1
    else:
        return 0

def checkIntersection(p1,p2,p3,p4):
    d1=checkClockOrAntiClock(p3,p4,p1)
    d2=checkClockOrAntiClock(p3,p4,p2)
    d3=checkClockOrAntiClock(p1,p2,p3)
    d4=checkClockOrAntiClock(p1,p3,p4)
    if(((d1>0 and d2<0) or (d1<0 and d2> 0)) and
       (d3>0 and d4<0) or (d3<0 and d4> 0)):
        return True;
    elif(d1==0 and onSegment(p3, p4, p1)):
        return True
    elif(d2==0 and onSegment(p3, p4, p2)):
        return True
    elif(d3==0 and onSegment(p1, p2, p3)):
        return True
    elif(d4==0 and onSegment(p1, p2, p3)):
        return True
    return False
    
    
    

p1=tuple(map(int,input().split()))
p2=tuple(map(int,input().split()))
p3=tuple(map(int,input().split()))
p4=tuple(map(int,input().split()))
print(checkIntersection(p1,p2,p3,p4))
