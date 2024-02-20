#https://www.youtube.com/watch?v=SBdWdT_5isI

import math

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return math.sqrt((y2-y1)**2 + (x2-x1)**2)


def polar_angle(p1, p2):
    if p1[1] == p2[1]:
        return -math.pi
    dy = p1[1]-p2[1]
    dx = p1[0]-p2[0]
    return math.atan2(dy, dx)

def orientation(p1, p2, p3):
     cross_product = (p2[1] - p1[1]) * (p3[0] - p1[0]) - (p2[0] - p1[0]) * (p3[1] - p1[1])
     if(cross_product==0):
         return 0
     elif(cross_product>0):
         return 1
     else:
         return 2
        
def findConvexHull(n,points):
    p0=min(points,key=lambda x:(x[1],x[0]))
    points=sorted(points,key=lambda p:(polar_angle(p0, p),dist(p0, p)))
    hull=[]
    for i in range(n):
        while len(hull)>=2 and orientation(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()
        hull.append(points[i])
    return hull;
            
    


n=int(input())
points=[tuple(map(int,input().split())) for i in range(n)]
print(findConvexHull(n,points))
