#https://www.youtube.com/watch?v=ldHA8UcQI9Q

import math
def findDistance(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def findClosestPairBf(n,points):
    min_dist=float('inf')
    p1,p2=None,None
    for i in range(n):
        for j in range(i+1,n):
            dist=findDistance(points[i],points[j])
            temp=min_dist
            min_dist=min(min_dist,dist)
            if(temp!=min_dist):
                p1,p2=points[i],points[j]
    return p1,p2,min_dist

def recursion(n,x_sorted,y_sorted):
    if(n<=3):
        return findClosestPairBf(n,x_sorted)
    mid=len(x_sorted)//2
    xsorted_left=x_sorted[mid:]
    xsorted_right=x_sorted[:mid]
    midpoint=x_sorted[mid]
    ysorted_left,ysorted_right=[],[]
    for point in y_sorted:
        if(point[0]<=midpoint[0]):
            ysorted_left.append(point)
        else:
            ysorted_right.append(point)
    left=recursion(n//2,xsorted_left,ysorted_left)
    right=recursion(n//2,xsorted_right,ysorted_right)
    (p1,p2,delta)=min(left,right,key=lambda x:x[2])
    in_band=[point for point in y_sorted if (midpoint[0]-delta < point[0] < midpoint[0]+delta)]
    len_in_band=len(in_band)
    for i in range(len_in_band):
        for j in range(i+1,min(i+7,len_in_band)):
            dist=findDistance(in_band[i],in_band[j])
            if(dist < delta):
                (p1,p2,delta)=(in_band[i],in_band[j],dist)
    return (p1,p2,delta)
    

def closest(n,points):
    x_sorted=sorted(points,key=lambda x:x[0])
    y_sorted=sorted(points,key=lambda x:x[1])
    return recursion(n,x_sorted,y_sorted)
n=int(input())
points=[tuple(map(int,input().split())) for i in range(n)]
print(findClosestPairBf(n,points))
print(closest(n,points))
