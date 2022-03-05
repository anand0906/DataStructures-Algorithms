from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    if(n==0):
        return 0
    right=1000000000000
    left=frogJump(n-1,heights)+abs(heights[n]-heights[n-1])
    if(n>1):
        right=frogJump(n-2,heights)+abs(heights[n]-heights[n-2])
    return min(left,right)
        
print(frogJump(int(input())-1,list(map(int,input().split()))))
