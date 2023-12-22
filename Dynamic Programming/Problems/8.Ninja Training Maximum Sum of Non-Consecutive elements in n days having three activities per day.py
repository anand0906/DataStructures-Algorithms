

#TC : O(3*n)
#Sc : O(n)+O(n*3)
def recursive(day,last_picked_activity,points):
    if(day==0):
        maxi=float('-inf')
        for activity in range(3):
            if(activity!=last_picked_activity):
                maxi=max(maxi,points[day][activity])
        return maxi

    final=float('-inf')
    for activity in range(3):
        if(activity!=last_picked_activity):
            temp=points[day][activity]+recursive(day-1,activity,points)
            final=max(final,temp)
    return final

#TC : O(n*3)
#Sc : O(n)+O(n*3)
def memorization(day,last,points,memo):
    key=(day,last)
    if key in memo:
        return memo[key]
    if(day==0):
        maxi=float('-inf')
        for i in range(3):
            if(i!=last):
                maxi=max(maxi,points[day][i])
        return maxi
    final=float('-inf')
    for i in range(3):
        if(i!=last):
            temp=points[day][i]+memorization(day-1,i,points,memo)
            final=max(final,temp)
    memo[key]=final
    return final

#TC : O(n*3*3)
#Sc : O(n)+O(n*3)+O(n*3)
def tabulation(n,points):
    dp=[[0]*3 for i in range(n)]
    for last in range(3):
        maxi=float('-inf')
        for i in range(3):
            if(i!=last):
                maxi=max(maxi,points[0][i])
        dp[0][last]=maxi
    for day in range(1,n):
        for last in range(3):
            final=float('-inf')
            for activity in range(3):
                if(last!=activity):
                    temp=points[day][activity]+dp[day-1][activity]
                    final=max(final,temp)
            dp[day][last]=final
    return max(dp[n-1])

#TC : O(n*3*3)
#Sc : O(n)+O(n*3)
def optimization(n,points):
    dp_prev=[0,0,0]
    
    dp_curr=[0,0,0]
    for last in range(3):
        maxi=float('-inf')
        for i in range(3):
            if(i!=last):
                maxi=max(maxi,points[0][i])
        dp_prev[last]=maxi
    for day in range(1,n):
        for last in range(3):
            final=float('-inf')
            for activity in range(3):
                if(last!=activity):
                    temp=points[day][activity]+dp_prev[activity]
                    final=max(final,temp)
            dp_curr[last]=final
        dp_prev=dp_curr.copy()
    return max(dp_prev)
                

n=int(input())
points=[list(map(int,input().split())) for i in range(n)]
print(recursive(n-1,-1,points))
memo={}
print(memorization(n-1,-1,points,memo))
print(tabulation(n,points))
print(optimization(n,points))

    

















































