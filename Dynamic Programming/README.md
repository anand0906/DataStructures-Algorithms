<h1>Dynamic Programming</h1>
<p>It is a technique to solve a complex problem by breaking it into smaller sub-problems and the result of each sub-problem is saved so the same sub-problem will not have to be computed again. Then the sub-problems are optimized together to find the original solution.</p>
<p>It can only be applied to the problem if it has overlapping sub-problems or optimum substructures.</p>
<h3>Overlapping Sub-problems</h3>
<p>While the problem is divided into multiple subproblems, if any subproblem is repeated more than once then those are called overlapping sub-problems</p>
<h3>Optimum substructure.</h3>
<p>After the problem is broken down into sub-problems, the solution for the main problem will come from the optimum solutions of its sub-problems answers. This behavior is called as an Optimum substructure.</p>
<h3>There are two approaches to dynamic programming</h3>
<ul>
  <li>Top-Down</li>
  <li>Bottom-Up</li>
</ul>
<h3>Top-Down</h3>
<p>In this approach, problem computation starts from the main problem and then breaks into sub-problems.</p>
<p>It can be achieved using recursion</p>
<h3>Bottom-Up</h3>
<p>In this approach, problem computation starts from subproblems and it leads to the main problem</p>
<p>It can be achieved using iteration</p>
<h3>Steps Involved in Solving Dynamic Programming</h3>
<h4>Define The Problem</h4>
<p>Understand the problem clearly and Observe what to do in each step to find the final answer</p>
<h4>Represent the Problem Programmatically</h4>
<p>Choose the right data structure to solve the problem (Represent the problem in terms of indexes)</p>
<h4>Finding Base Cases</h4>
<p>Find smaller values/inputs for the problem that don't need any decomposition into subproblems for the final answer. These values act as base cases for the main problem </p>
<h4>Finding The Recurrence Relation</h4>
<p>Observe steps to solve the problem by taking several inputs from smaller to bigger, express the solution to the problem in terms of solution to smaller subproblems</p>
<p>Find out the mathematical formula for the solution or current problem with a solution to the smaller subproblems. This is called a recurrence relation</p>
<h4>Recursive Solution (Top-Down Approach)</h4>
<p>Implement the recursive solution using recurrence relation and base cases</p>
<h4>Apply Memorization (Top-Down Approach)</h4>
<p>Memorize the solutions of the recursive approach, so that time complexity will be reduced.</p>
<h4>Iterative Solution (Bottom-Up Approach)</h4>
<p>Implement the iterative solution to solve the problem from smaller problems that lead to the solution to the original problem.</p>
<p>Here we will use arrays to store the solution for each subproblem that will be used for further cases to solve the original problem</p>
<h4>Space Optimization (Bottom-Up Approach)</h4>
<p>Modify the previous iterative solution such that to store only required values instead of entire subproblems solutions</p>
<p>This will improve the space complexity</p>
<h4>Observe Time And Space Complexity</h4>
<p>Find Time and Space Complexity for each approach, optimize the problem according to requirement</p>


<h3>Problems</h3>


<h4>1.Fibonacci Number</h4>
<h5>The Fibonacci numbers are the numbers in the following integer sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..</h5>
<h5>The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is, Given n, calculate F(n).</h5>
<h5>Step-1 : Define The Problem</h5>
<p>It is an integer sequence starting with 0,1, upcoming numbers can be obtained by adding its previous two numbers.</p>
<p>such that, next number will be 0+1=1</p>
<p>Series, is like, 0,1,1,2,3,5,8,13,21,34,56..etc</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
<p>Here the problem is a 0-based index and we have to find the nth Fibonacci number</p>
<p>Problem will n as input and we have to find nth fibonacci number</p>
<p> Since it is a 0-based index, including zero we have to find n+1 numbers and have to return (n+1)th Fibonacci number</p>
<h5>Step-3 : Finding Base Cases</h5>
<p>we know, for n=0 -> 0</p>
<p>we know, for n=1 -> 1</p>
<p>we know, for n=2 -> 1</p>
<h5>Step-4 : Finding The Recurrence Relation</h5>
<p>let's represent the problem in terms of mathematical function f(n), where n is the input represents nth Fibonacci number</p>
<p>we know base cases</p>
<p>f(0)=0</p>
<p>f(1)=1</p>
<p>f(2)=1</p>
<p>As per problem description, f(3)=f(2)+f(1)=1+1=2</p>
<p>As per problem description, f(4)=f(3)+f(2)=2+1=3</p>
<p>we can observe that, f(n)=f(n-1)+f(n-2)</p>
<p>Recurrence relation => <b>f(n)=f(n-1)+f(n-2)</b></p>
<h5>Step-5 : Recursive Solution</h5>

```python
  def recursive(n):
    if(n<=1):
        return n
    if(n==2):
        return 1 
    prev=recursive(n-1)
    prev2=recusive(n-2)
    answer=prev+prev2
    return answer

  n=int(input())
  print(recursive(n))
```
<p>TC : O(2^n)</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is n, since every n is unique for its answer</p>

```python
  def memorization(n,memo):
    if n in memo:
        return memo[n]
    if(n<=1):
        return n
    a=memorization(n-1,memo)
    b=memorization(n-2,memo)
    answer=a+b
    memo[n]=answer
    return memo[n]
  n=int(input())
  memo={}
  print(memorization(n,memo))
```
<p>TC : O(n)</p>
<p>SC : O(n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we have to find the nth Fibonacci number, we have to store (n+1) subproblem answers including zero </p>
<p>Create a 1-d array of size (n+1), fill 0 as defualt</p>
<p>we know base cases, 0->0, 1->1, 2->1</p>
<p> Fill base cases, index represent nth Fibonacci number</p>
<p>loop from 3rd index up to n, find each answer based on recurrence relation</p>
<p>f(n)=f(n-1)+f(n-2)</p>
<p>dp[n]=dp[n-1]+dp[n-2]</p>

```python
  def tabulation(n):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    dp[2]=1
    for i in range(3,n+1):
        prev=dp[i-1]
        prev2=dp[i-2]
        answer=prev+prev2
        dp[i]=answer
    return dp[n]
  n=int(input())
  print(tabulation(n))
```
<p>TC : O(n)</p>
<p>SC : O(n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step in tabulation, we're using the last two answers only</p>
<p> We don't need all previous subproblem solutions</p>

```python
  def optimization(n):
    prev=1
    prev2=1
    for i in range(3,n+1):
        answer=prev+prev2
        prev=prev2
        prev2=answer
    return prev2
  n=int(input())
  print(optimization(n))
```
<p>TC : O(n)</p>
<p>SC : O(1)</p>

<br>
<br>

<h4>2.Climbing Stairs : Count of ways : One or Two Steps</h4>
<h5>Given a number of stairs. Starting from the 0th stair we need to climb to the “Nth” stair. At a time we can climb either one or two steps. We need to return the total number of distinct ways to reach from 0th to Nth stair.</h5>
<pre>
  Input: n = 2
  Output: 2
  Explanation: There are two ways to climb to the top.
  1. 1 step + 1 step
  2. 2 steps
</pre>
<pre>
  Input: n = 3
  Output: 3
  Explanation: There are three ways to climb to the top.
  1. 1 step + 1 step + 1 step
  2. 1 step + 2 steps
  3. 2 steps + 1 step
</pre>
<h5>Step-1 : Define The Problem</h5>
<p>We have n steps, we are starting from 0th step, we have to reach the nth step</p>
<p>At a time, we can jump to one step or two steps</p>
<p>We have to fine total number of different ways to reach nth step</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
<p>Here we have to start from 0th step and reach to the nth step</p>
<p>We might need 1-d array of size (n+1) to include 0th step also</p>
<p>here , 0 to n represents step number we are at currently</p>
<p>f(n) => represents function which return number of ways at nth step </p>
<h5>Step-3 : Finding Base Cases</h5>
<p>Suppose we are at starting 0th step and have to reach 0th step only, so there is only one way to stay there itself</p>
<p>f(0)=1</p>
<p>Suppose , we have to reach 1th step. Then there is only one way that is jumping to one step</p>
<p>f(1)=1</p>
<p>Suppose, we have to reach 2nd step, then there will be two ways, those are jump 1+1 or jump 2</p>
<p>f(2)=2</p>
<pre>
  0->1
  1->1
  2->2
</pre>
<h5>Step-4 : Finding The Recurrence Relation</h5>
<p>Suppose, we have to reach 3rd step (n), basically we can jump 1 or 2 steps at a time.</p>
<p>To Reach 3rd step, The previous step should either 2 (n-1 if takes one jump) or 1 (n-2 if take two jumps)</p>
<p>if we know how many ways for to reach 2 (n-1) and 1 (n-2)</p>
<p>By Combining the both ways, we can get total number of ways to reach nth step</p>
<p>We know, f(1)=1 and f(2)=2 , hence f(3)=f(2)+f(1)=1+2=3</p>
<p>Number of ways at n = number of ways at n-1 + number of ways at n-2</p>
<p>Recurrance relation : <b>f(n)=f(n-1)+f(n-2)</b></p>
<h5>Step-5 : Recursive Solution</h5>

```python
  def recursive(n):
    if(n<=1):
        return 1
    if(n==2):
        return 2 
    prev=recursive(n-1)
    prev2=recusive(n-2)
    answer=prev+prev2
    return answer
  n=int(input())
  print(recursive(n))
```
<p>TC : O(2^n)</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is n, since every n is unique for its answer</p>

```python
  def memorization(n,memo):
    if n in memo:
        return memo[n]
    if(n<=1):
        return 1
    if(n==2):
      return 2
    a=memorization(n-1,memo)
    b=memorization(n-2,memo)
    answer=a+b
    memo[n]=answer
    return memo[n]
  n=int(input())
  memo={}
  print(memorization(n,memo))
```
<p>TC : O(n)</p>
<p>SC : O(n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we have to find the Number of ways at nth step, we have to store (n+1) subproblem answers including zero </p>
<p>Create a 1-d array of size (n+1), fill 0 as defualt</p>
<p>we know base cases, 0->0, 1->1, 2->1</p>
<p> Fill base cases, index represent nth step</p>
<p>loop from 3rd index up to n, find each answer based on recurrence relation</p>
<p>f(n)=f(n-1)+f(n-2)</p>
<p>dp[n]=dp[n-1]+dp[n-2]</p>

```python
  def tabulation(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        prev=dp[i-1]
        prev2=dp[i-2]
        answer=prev+prev2
        dp[i]=answer
    return dp[n]
  n=int(input())
  print(tabulation(n))
```
<p>TC : O(n)</p>
<p>SC : O(n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step in tabulation, we're using the last two answers only</p>
<p> We don't need all previous subproblem solutions</p>

```python
  def optimization(n):
    prev=2
    prev2=1
    for i in range(3,n+1):
        answer=prev+prev2
        prev=prev2
        prev2=answer
    return prev2
  n=int(input())
  print(optimization(n))
```
<p>TC : O(n)</p>
<p>SC : O(1)</p>

<br>
<br>

<h4>3.Climbing Stairs : Count of ways : Up to K Steps</h4>
<h5>Given a number of stairs. Starting from the 0th stair we need to climb to the “Nth” stair. At a time we can climb either k steps ( 1 or 2 or 3 ...k). We need to return the total number of distinct ways to reach from 0th to Nth stair.</h5>
<pre>
  Input: n = 2 , k = 2
  Output: 2
  Explanation: There are two ways to climb to the top.
  1. 1 step + 1 step
  2. 2 steps
</pre>
<pre>
  Input: n = 3 , k=3
  Output: 4
  Explanation: There are four ways to climb to the top.
  1. 1 step + 1 step + 1 step
  2. 1 step + 2 steps
  3. 2 steps + 1 step
  4. 3 steps
</pre>
<h5>Step-1 : Define The Problem</h5>
<p>We have n steps, we are starting from 0th step, we have to reach the nth step</p>
<p>At a time, we can jump to up to k steps</p>
<p>We have to fine total number of different ways to reach nth step</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
<p>Here we have to start from 0th step and reach to the nth step</p>
<p>We might need 1-d array of size (n+1) to include 0th step also</p>
<p>here , 0 to n represents step number we are at currently</p>
<p>f(n) => represents function which return number of ways at nth step </p>
<h5>Step-3 : Finding Base Cases</h5>
<p>Suppose we are at starting 0th step and have to reach 0th step only, so there is only one way to stay there itself</p>
<p>f(0)=1</p>
<p>Suppose , we have to reach 1th step. Then there is only one way that is jumping to one step (Since minimum k value is 1)</p>
<p>f(1)=1</p>
<pre>
  0->1
  1->1
</pre>
<h5>Step-4 : Finding The Recurrence Relation</h5>
<h6>k=2</h6>
<p>Suppose, we have to reach 3rd step (n), basically we can jump 1 or 2 steps at a time since k=2.</p>
<p>To Reach 3rd step, The previous step should either 2 (n-1 if takes one jump) or 1 (n-2 if take two jumps)</p>
<p>if we know how many ways for to reach 2 (n-1) and 1 (n-2)</p>
<p>By Combining the both ways, we can get total number of ways to reach nth step</p>
<p>We know, f(1)=1 and f(2)=2 , hence f(3)=f(2)+f(1)=1+2=3</p>
<p>Number of ways at n = number of ways at n-1 + number of ways at n-2</p>
<p>Recurrance relation : <b>f(n)=f(n-1)+f(n-2)</b></p>
<h6>k=3</h6>
<p>Suppose, we have to reach 3rd step (n), basically we can jump 1 or 2 or 3 steps at a time since k=3.</p>
<p>To Reach 3rd step, The previous step should either 2 (n-1 if takes one jump) or 1 (n-2 if take two jumps) or 0 (n-3 if take three jumps)</p>
<p>if we know how many ways for to reach 2 (n-1) and 1 (n-2) and 0 (n-3)</p>
<p>By Combining the both ways, we can get total number of ways to reach nth step</p>
<p>We know,f(0)=0, f(1)=1 and f(2)=2 , hence f(3)=f(2)+f(1)+f(0)=2+1+1=4</p>
<p>Number of ways at n = number of ways at n-1 + number of ways at n-2 + number of ways at n-3</p>
<p>Recurrance relation : <b>f(n)=f(n-1)+f(n-2)+f(n-2)</b></p>
<h6>For K Steps</h6>
<p>Suppose we have k choices, from nth stair, we have to found all ways for previous k steps</p>
<p>Recurrance Relation : <b>f(n)=f(n-1)+f(n-2)+...+f(n-k)</b></p>

<p>We have to remind that, (n-k) should not be less than 0. i.e f(-1) is meaning less</p>

```python
  total=0
  for i in range(1,k+1):
    if(n-i > 0):
        total+=f(n-i)

```
<h5>Step-5 : Recursive Solution</h5>

```python
  def recursive(n,k):
    if(n==0):
        return 1
    if(n==1):
        return 1
    total=0
    for i in range(1,k+1):
        if(n-i >= 0):
            total+=recursive(n-i,k)
    return total
  n=int(input())
  k=int(input())
  print(recursive(n,k))
```
<p>TC : O((n^k)*k)</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is n, since every n is unique for its answer</p>

```python
  def memorization(n,k,memo):
    if(n in memo):
        return memo[n]
    if(n<=1):
        return 1
    totalWays=0
    for i in range(1,k+1):
        if(n-i>=0):
            totalWays+=memorization(n-i,k,memo)
    memo[n]=totalWays
    return memo[n]
  n=int(input())
  k=int(input())
  memo={}
  print(memorization(n,k,memo))
```
<p>TC : O(n*k)</p>
<p>SC : O(n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we have to find number of ways at nth step, we have to store (n+1) subproblem answers including zero </p>
<p>Create a 1-d array of size (n+1), fill 0 as defualt</p>
<p>we know base cases, 0->0, 1->1</p>
<p> Fill base cases, index represent nth Step</p>
<p>loop from 2rd index up to n, find each answer based on recurrence relation</p>
<p>f(n)=f(n-1)+f(n-2)+...+f(n-k)</p>
<p>dp[n]=dp[n-1]+dp[n-2]+..+dp[n-k]</p>

```python
 def tabulation(n,k):
    dp=[0]*(n+1)
    dp[0],dp[1]=1,1
    for i in range(2,n+1):
        totalWays=0
        for j in range(1,k+1):
            if(i-j>=0):
                totalWays+=dp[i-j]
        dp[i]=totalWays
    return dp[n]
  n=int(input())
  k=int(input())
  print(tabulation(n,k))

```
<p>TC : O(n*k)</p>
<p>SC : O(n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step in tabulation, we're have to store last k answers</p>
<p> We don't need all previous subproblem solutions</p>
<p>Managing last k answers will consume less memory but increases time complexity</p>
<p>hence it is not preferred</p>

<br>
<br>

<h4>4.Frog Jump : Minimum Energy : One or Two Steps</h4>
<h5>Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.</h5>
<pre>
  If the given ‘HEIGHT’ array is [10,20,30,10], the answer 20 as the frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost) and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost). So, the total energy lost is 20.
</pre>
<h5>Step-1 : Define The Problem</h5>
<p>It is similar to climbing stairs problem. But here we have to find minimum energy requrired to reach nth step</p>
<p>Frog is at 0th step, it has to reach nth step. It can jump one or two steps at a time</p>
<p>Every step is asscocited with some height / energy. Energy consumed for a single jump from i to j is abs(height[i]- height[j])</p>
<p>We have to find the minimum energy required to reach nth step</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
<p>Here we have to start from 0th step and reach to the n-1th step</p>
<p>We might need 1-d array of size (n) to include 0th step also</p>
<p>here , 0 to n represents step number we are at currently</p>
<h5>Step-3 : Finding Base Cases</h5>
<p>Suppose we are at starting 0th step and have to reach 0th step only, so we don't need to move, energy required is zero</p>
<p>f(0)=0</p>
<p>Suppose , we have to reach 1th step. Then there is only one way that is jumping to one step. Energy required is abs(height[0]-height[1])</p>
<p>f(1)=abs(height[0]-height[1])</p>
<pre>
  0->1
  1->abs(height[0]-height[1])
</pre>
<h5>Step-4 : Finding The Recurrence Relation</h5>
<p>We know energy required for 0 and 1 steps.</p>
<p>suppose let's take step-2,To reach step-2, we have to come from either from 1st step or 0th step. Since we have two options only</p>
<p>If we are coming from 1st step, energy=energy required reach 1st + enrgy required to jump 1st to 2nd (abs(height[1]-height[2]))</p>
<p>If we are coming from 0th step, energy=energy required reach 0th step (0)+ enrgy required to jump 0th to 2nd (abs(height[0]-height[2]))</p>
<p>Since we need minimum energy, just minimum of above two energies</p>
<p>f(2)=min(f(2-1)+abs(height[1]-height[2]), f(2-2)+abs(height[0]-height[2]))</p>
<p>Similary, To Reach nth step, we have to come from either (n-1)th step or (n-2)th step</p>
<p>Minimum Energy Required At nth Step = Min(Energy Required at (n-1)th step + energy required to jump n-1 to nth step, Energy Required at (n-2)th step + energy required to jump n-2 to nth step)</p>
<p>Recurrance Relation : <b>f(n)=min(f(n-1)+abs(height[n-1]-height[n]), f(n-2)+abs(height[n-2]-height[n]]))</b></p>
<h5>Step-5 : Recursive Solution</h5>

```python
  def recursive(n,height):
    if(n==0):
        return 0
    if(n==1):
        return abs(height[1]-height[0])
    prev=recursive(n-1,height)+abs(height[n-1]-height[n])
    prev2=recursive(n-2,height)+abs(height[n-2]-height[n])
    answer=min(prev,prev2)
    return answer
  n=int(input())
  height=list(map(int,input().split()))
  print(recursive(n,height))
```
<p>TC : O(2^n)</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is n, since every n is unique for its answer</p>

```python
  def memorization(n,height,memo):
    if n in memo:
        return memo
    if(n==0):
        return 0
    if(n==1):
        return abs(height[1]-height[0])
    prev=memorization(n-1,height,memo)+abs(height[n-1]-height[n])
    prev2=memorization(n-2,height,memo)+abs(height[n-2]-height[n])
    answer=min(prev,prev2)
    memo[n]=answer
    return answer
  n=int(input())
  height=list(map(int,input().split()))
  memo={}
  print(memorization(n,height,memo))
```
<p>TC : O(n^2)</p>
<p>SC : O(n^2)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we have to reach from n-1 to 0 step, we have to declare array of size n</p>
<p>Fill base cases</p>
<p>loop from n-2 to 0th row and fill all values based on recurrance relation</p>


```python
def tabulation(n,matrix):
    dp=[[0]*i for i in range(1,n+1)]
    for i in range(n):
        dp[n-1][i]=matrix[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            bottom,bottomRight=float('inf'),float('inf')
            if(i+1>0 and j<=(i+1)):
                bottom=matrix[i][j]+dp[i+1][j]
            if(i+1>0 and (j+1)<=(i+1)):
                bottomRight=matrix[i][j]+dp[i+1][j+1]
            dp[i][j]=min(bottom,bottomRight)
    return dp[0][0]

  n=int(input())
  height=list(map(int,input().split()))
  print(tabulation(n,height))

```
<p>TC : O(n)</p>
<p>SC : O(n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step, we are using only previous two step values</p>
<p>we don't need to store all subproblem answers</p>

```python
def optimization(n,height):
    prev2=0
    prev=abs(height[0]-height[1])
    for i in range(2,n):
        a=prev+abs(height[i-1]-height[i])
        b=prev2+abs(height[i-2]-height[i])
        answer=min(a,b)
        prev2=prev
        prev=answer
    return prev

  n=int(input())
  height=list(map(int,input().split()))
  print(optimization(n,height))

```
<p>TC : O(n)</p>
<p>SC : O(1)</p>

<br>
<br>

<h4>5.Frog Jump : Minimum Energy : Up to k Steps</h4>
<h5>This is a follow-up question to “Frog Jump” discussed in the previous problem. In the previous question, the frog was allowed to jump either one or two steps at a time. In this question, the frog is allowed to jump up to ‘K’ steps at a time. If K=4, the frog can jump 1,2,3, or 4 steps at every index.</h5>

<h5>Step-1 : Define The Problem</h5>
<p>Similar to previous problem, but here we can jump up to k steps at a time</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
<p>Here we have to start from 0th step and reach to the n-1th step</p>
<p>We might need 1-d array of size (n) to include 0th step also</p>
<h5>Step-3 : Finding Base Cases</h5>
<p>At step 0, energy equal to zero, since we don't need to jump</p>
<p>f(0)=0</p>
<h5>Step-4 : Finding The Recurrence Relation</h5>
<p>To reach nth step, we can come from either n-1,n-2,n-3 ....n-k</p>
<p>Calculte enregy required for all cases and take min out of it</p>

```python
f(n)=min(f(n-1)+abs(height[n-1]-height[n]),
         f(n-2)+abs(height[n-2]-height[n])
         f(n-3)+abs(height[n-3]-height[n])
         ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
         ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
         f(n-k)+abs(height[n-k]-height[n])
         )
```
<p> </p>
<h5>Step-5 : Recursive Solution</h5>

```python
  def recursive(n,k,height):
    if(n==0):
        return 0
    minEnergy=float('inf')
    for i in range(1,k+1):
        if((n-i)>=0):
            temp=recursive(n-i,k,height)+abs(height[n-i]-height[n])
            minEnergy=min(minEnergy,temp)
    return minEnergy
  n=int(input())
  k=int(input())
  height=list(map(int,input().split()))
  print(recursive(n,k,height))
```
<p>TC : O((k^n))</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is n, since every n is unique for its answer</p>

```python
  def memorization(n,k,height,memo):
    if n in memo:
        return memo[n]
    if(n==0):
        return 0
    minEnergy=float('inf')
    for i in range(1,k+1):
        if((n-i)>=0):
            temp=memorization(n-i,k,height,memo)+abs(height[n-i]-height[n])
            minEnergy=min(minEnergy,temp)
    memo[n]=minEnergy
    return minEnergy
  n=int(input())
  k=int(input())
  height=list(map(int,input().split()))
  memo={}
  print(memorization(n,k,height,memo))
```
<p>TC : O(n*k)</p>
<p>SC : O(n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we have to reach n-1 step, we have to declare array of size n</p>
<p>Fill base cases</p>
<p>loop from 2 and fill all values based on recurrance relation</p>


```python
def tabulation(n,k,height):
    dp=[0]*n
    dp[0]=0
    for i in range(1,n):
        minEnergy=float('inf')
        for j in range(1,k+1):
            if(i-j >=0):
                temp=dp[i-j]+abs(height[i-j]-height[i])
                minEnergy=min(temp,minEnergy)
            dp[i]=minEnergy
    return dp[n-1]

  n=int(input())
  k=int(input())
  height=list(map(int,input().split()))
  print(tabulation(n,k,height))

```
<p>TC : O(n*k)</p>
<p>SC : O(n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step, we are using only previous k step values</p>
<p>we don't need to store all subproblem answers</p>
<p> but managing previous k step values will effect Time complexity</p>
<p>So, space optimization is not preffered</p>

<br>
<br>

<h4>6.Maximum Sum Of Non-Adjacent Elements</h4>
<h5>Given an array of ‘N’  positive integers, we need to return the maximum sum of the subsequence such that no two elements of
the subsequence are adjacent elements in the array.</h5>
<h5>Note: A subsequence of an array is a list with elements of the array where some elements are deleted ( or not deleted at all) and the elements should be in the same order in the subsequence as in the array.</h5>
<img src="https://lh6.googleusercontent.com/gQPoRaBGkwCKbJNy8cvXG2LBzD3khfxca938a6Zrph4HWQGLOxtVbDW3xO6WkDalQCBopYfBp5DX3oo_Drug3kRNBwhqDkYapMUu4LjwL_6_8dPot0h8ESZeMrbp1_3M_SW0zICR">
<h5>Step-1 : Define The Problem</h5>
<p>Given an array, we have to find maximum sum of element which are not adjacent together, No two elements should be together</p>
<p>For Example, arr=[1,2,3,4]</p>
<p>Non-Adjacenent Subsequences are</p>
<p>[1,3],[2,4],[1,4],[1],[2],[3],[4]</p>
<p>We have to return maximum sum of combination that is [2,4]=6</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
<p>Given an array, so each element has index</p>
<p>Let us assume f(index), it represents maximum sum of non-adjacent elements from 0 to index</p>
<p>we have to find, maximum sum at n-1 index , f(n-1), where n = size of array</p>
<h5>Step-3 : Finding Base Cases</h5>
<p>Array will contain atleast one element</p>
<p>if array size=1, n=1, then there is no adjacency since it contains only one element</p>
<p>f(0)=arr[0], where 0->index of first element</p>
<p>if array contains two elements, since both are adjacent together, max sum will be max of two elements</p>
<p>f(1)=max(arr[0],arr[1])</p>
<p>Base Cases :</p>
<p>f(0)->arr[0]</p>
<p>f(1)->max(arr[0],arr[1])</p>
<h5>Step-4 : Finding The Recurrence Relation</h5>
<p>To find recurrence relation, lets solve smaller inputs</p>
<p>we know base cases</p>
<h4>arr=[1,2,3]</h4>
<p>we know, f(0)=arr[0]=1 -> Maximum non-adjacent sum at index 0</p>
<p>f(1)=max(arr[0],arr[1])=max(1,2)=2 -> Maximum non-adjacent sum from index 0 to index 1</p>
<p>for f(2), i.e maximum non-adjacent sum from index 0 to index 2</p>
<p>we have to choices</p>
<p>1.Include element at index 2</p>
<p>2.not include element at index 2</p>
<p>Max of both choices will be answer</p>
<p>If we are including element at index 2, we can't add element which is adjacent to it. so, we have to add maximum sum which just before its adjacent position. i.e f(n-2)</p>
<p>f(2)=arr[2]+f(2-2)=2+f(0)=2+1=3</p>
<p>If we are not including current element, we have to take adjacent sum, i.e f(n)=f(n-1)</p>
<p>f(2)=f(n-1)=f(2-1)=f(1)=2</p>
<p>we have to take max of two cases</p>
<p>max(3,2)=3=f(2)-> this is the maximum obtained from index 0 to index 2</p>
<p>Hence Recurrance realation at index n, will be</p>
<p>f(n)=max(include current element, not include current element)</p>
<p>Include Element= element at current index + previous no-adjecent index maximum sum=arr[n]+f(n-2)</p>
<p>Exclude Element= Get the Maximum Sum Untill previous index = f(n-1)</p>
<p>Recurrance relation : <b>f(n)=max(arr[n]+f(n-2),f(n-1))</b></p>
<h5>Step-5 : Recursive Solution</h5>

```python
 def recursive(n,arr):
    if(n==0):
        return arr[0]
    if(n==1):
        return max(arr[0],arr[1])
    include=arr[n]+recursive(n-2,arr)
    exclude=recursive(n-1,arr)
    answer=max(include,exclude)
    return answer

  n=int(input())
  arr=list(map(int,input().split()))
  print(recursive(n,arr))
```
<p>TC : O(2^n)</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is n, since every n is unique for its answer</p>

```python
  def memorization(n,arr,memo):
    if n in memo:
        return memo[n]
    if(n==0):
        return arr[0]
    if(n==1):
        return max(arr[0],arr[1])
    include=arr[n]+memorization(n-2,arr,memo)
    exclude=memorization(n-1,arr,memo)
    answer=max(include,exclude)
    memo[n]=answer
    return memo[n]
  n=int(input())
  arr=list(map(int,input().split()))
  memo={}
  print(memorization(n,arr,memo))
```
<p>TC : O(n)</p>
<p>SC : O(n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we need to find maximum sum from 0 to n-1, declare array of size n</p>
<p>Intialize base cases</p>
<p>loop from 2, since 2 values are aleady filled</p>
<p>Based on recurrance relation</p>

```python
  def tabulation(n,arr):
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2,n):
        include=arr[i]+dp[i-2]
        exclude=dp[i-1]
        dp[i]=max(include,exclude)
    return dp[n-1]
  n=int(input())
  arr=list(map(int,input().split()))
  print(tabulation(n,arr))
```
<p>TC : O(n)</p>
<p>SC : O(n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step in tabulation, we're using the last two answers only</p>
<p> We don't need all previous subproblem solutions</p>

```python
  def optimization(n,arr):
    prev2=arr[0]
    prev=max(arr[0],arr[1])
    for i in range(2,n):
        include=arr[i]+prev2
        exclude=prev
        answer=max(include,exclude)
        prev2=prev
        prev=answer
    return prev
  n=int(input())
  arr=list(map(int,input().split()))
  print(optimization(n,arr))
```
<p>TC : O(n)</p>
<p>SC : O(1)</p>


<br>
<br>

<h4>7.House Robber : Maximum Non Adjacent Sum : Circular manner</h4>
<h5>A thief needs to rob money in a street. The houses in the street are arranged in a circular manner. Therefore the first and the last house are adjacent to each other. The security system in the street is such that if adjacent houses are robbed, the police will get notified.</h5>
<h5>Given an array of integers “Arr” which represents money at each house, we need to return the maximum amount of money that the thief can rob without alerting the police.</h5>
<h5>Step-1 : Define Problem</h5>
<p>We were finding the maximum sum of non-adjacent elements in the previous questions. For a circular street, the first and last house are adjacent, therefore one thing we know for sure is that the answer will not consider the first and last element simultaneously (as they are adjacent).</p>
<p>ow building on the article DP5, we can say that maybe the last element is not considered in the answer. In that case, we can consider the first element. Let’s call this answer ans1. Hence we have reduced our array(arr- last element), say arr1, and found ans1 on it by using the article DP5 approach.</p>
<img src="https://lh3.googleusercontent.com/0mkwqypWCCVBzCR3p4y0kpIcfaOtXVj554Oppzazg3vz8R7BSgWstj6oIwKJtgmDVVZ7Ixn5I3q-KTAWMP3xWzQX88XoyrZBEZ7KcCH6T2IMGSserlmIDas4ZlI8OhMAe84kgL72">
<p>Now, it can also happen that the final answer does consider the last element. If we consider the last element, we can’t consider the first element( again adjacent elements). We again use the same approach on our reduced array( arr – first element), say arr2. Let’s call the answer we get as ans2.</p>
<img src="https://lh6.googleusercontent.com/0x1VzdE2zZniwJr84vvkNsZWQSeNsKu385q_o-ySKc7rdFGdj-Qhc7I6XSif0vldfl9NIfqEd92e7mlYkDc6Z05dgtO0pZX7Qg30W09hU7qOHFuzvvv0Sh8KgphfR5IZ2mVdFJqf">
<p>Now, the final answer can be either ans1 or ans2. As we have to return the maximum money robbed by the robber, we will return max(ans1, ans2) as our final answer.</p>


```python
  def maxNonAdjSum(n,arr):
    prev2=arr[0]
    prev=max(arr[0],arr[1])
    for i in range(2,n):
        include=arr[i]+prev2
        exclude=prev
        answer=max(include,exclude)
        prev2=prev
        prev=answer
    return prev
n=int(input())
arr=list(map(int,input().split()))
excludeFirst=maxNonAdjSum(n-2,arr[1:])
excludeLast=maxNonAdjSum(n-2,arr[:-1])
print(max(excludeFirst,excludeLast))
```
<p>TC : O(n)</p>
<p>SC : O(1)</p>

<br>
<br>

<h4>8.Ninja's Training : Maximum Points earned in n days by taking no consecutive activities</h4>
<h5>A Ninja has an ‘N’ Day training schedule. He has to perform one of these three activities (Running, Fighting Practice, or Learning New Moves) each day. There are merit points associated with performing an activity each day. The same activity can’t be performed on two consecutive days. We need to find the maximum merit points the ninja can attain in N Days.</h5>
<h5>We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of specific activity on that particular day. Our task is to calculate the maximum number of merit points that the ninja can earn.</h5>
<img src="https://lh3.googleusercontent.com/fGhKc0zD0hrkqCd-4jAGVuIiJgqFvyk1dSLmTiwWwTXmRmG_LoqpiaOwk1puC3jgVB_HZx3p0v0Ovq66QWwKhaYanSBF8yI09GLZwm-aumvQT8LPuSSvlDerGoN0uz2MyNhX8I67">
<h5>Step-1 : Define The Problem</h5>
<p>Given n days, and each day has 3 activities associated with three activities each has points</p>
<p>we have to start from day one,has to pick one activity and can pickup different activity in next day</p>
<p>We have to earn maxpoints by doing n activities in n days.</p>
<p>Maximum points earned in nth day is the answer</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
<p>We have n days, each day has three activities. So we can store input in the form of matrix n*3, where n=days(rows) and 3=Activity Points(columns)</p>
<p>Since matrix is zero based indexing,Problem has 0 to n-1 days(rows), 0 to 2 activities(columns)</p>
<p>Has to start from 0th row, find answer at (n-1)th day</p>
<h5>Step-3 : Finding Base Cases</h5>
<p>if we have only one day, maximum of 3 activity points at day 1, f(0)=max(activity1,activity2,activity3)=max(points[0][0],points[0][1],points[0][2])</p>
<p>If we have more than one day, on first day we may pick any one activity based on next day activity</p>
<p>if next day activity=0, first day = max(activity2,activity3)=max(points[0][1],points[0][2])</p>
<p>if next day activity=1, first day = max(activity1,activity3)=max(points[0][0],points[0][2])</p>
<p>if next day activity=2, first day = max(activity1,activity2)=max(points[0][0],points[0][1])</p>
<p>Based on next/last day previous/next day activity will be choosen</p>
<p>Above all conditions will be written as follows</p>

```python
    maxi=float('inf')
    for i in range(3):
      if(i!=last):
        maxi=max(maxi,points[0][i])
    return maxi
```
<p>So the base condition will be as follows</p>
<p>If last = -1, then there is only one day, other wise there are more than one day</p>
<p>For Last = -1 , f(0)=max(activity1,activity2,activity3)=max(points[0][0],points[0][1]</p>
<p>For Last = 0 , f(0)=max(activity2,activity3)=max(points[0][1],points[0][2])</p>
<p>For Last = 1 , f(0)=max(activity1,activity3)=max(points[0][0],points[0][2])</p>
<p>For Last = 2 , f(0)=max(activity1,activity2)=max(points[0][0],points[0][1])</p>
<p>This applies for only 3 activities, if there are k activities, we can't follow this,so</p>
<p>f(0)=</p>

```python
    maxi=float('-inf')
    for i in range(3):
      if(i!=last):
        maxi=max(maxi,points[0][i])
    return maxi
```

<h5>Step-4 : Finding The Recurrence Relation</h5>
<p>for first day, we have already discussed</p>
<p>For day two, we have to pick a activity and find the maximum no consecutive activity in previous day</p>
<p>By adding these two values, we can get maximum value we can get at day-2 for that particular activity at day-2</p>
<p>By finding total points for each activity</p>
<p>We can get the obtained points for each activity at day-2</p>
<p>Maximum of those points will be answer for day-2</p>
<p>So the recurrance relation will be as follows</p>

```python 
    for current_activity in range(3) : #looping throw each activity
        maxi=float('-inf')
        for last_activity in range(3):
          if(current_activity!=last_activity):
            maxi=max(maxi,current_activity_points+previous_activity_points)
        current_activity_points=maxi

```

<h5>Step-5 : Recursive Solution</h5>

```python
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

  n=int(input())
  points=[list(map(int,input().split())) for i in range(n)]
  print(recursive(n-1,-1,points))
```
<p>TC : O(3^n)</p>
<p>SC : O(n)+O(n*3)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is day + last_day, since it is unique for its answer</p>

```python
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
  n=int(input())
  points=[list(map(int,input().split())) for i in range(n)]
  memo={}
  print(memorization(n-1,-1,points,memo))
```
<p>TC : O(n*3*3)</p>
<p>SC : O(n)+o(n*3)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
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
    n=int(input())
    points=[list(map(int,input().split())) for i in range(n)]
    print(tabulation(n,points))
```
<p>TC : O(n*3*3)</p>
<p>SC : O(n*3)+o(n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step in tabulation, we're using the last two answers only</p>
<p> We don't need all previous subproblem solutions</p>

```python
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
    print(optimization(n,points))
```
<p>TC : O(n*3*3)</p>
<p>SC : O(n*3)+o(n)</p>

<br>
<br>

<h4>9.Grid Unique Paths : Number of Unique ways from top left to bottom-right</h4>
<h5>Given two values M and N, which represent a matrix[M][N]. We need to find the total unique paths from the top-left cell (matrix[0][0]) to the rightmost cell (matrix[M-1][N-1]).</h5>
<h5>At any cell we are allowed to move in only two directions:- bottom and right.</h5>
<img src="https://lh3.googleusercontent.com/PDblNXbL7kmOxKoI7_0Yevnr7JF2FbXVr_0mKBpY8lza4066Gqz7yvw-4bn6NATQ9OaH9nn5uNeq6_P6fItMrWdEhs7fPUDBSoEKorJ9_lConrOtDUetBpq2s1bw4A9nIasR3dSJ">
<h5>Step-1 : Define The Problem</h5>
<p>Given two value m and n which represents row size and column size</p>
<p>It represents a matrix of size m*n</p>
<p>We have to start from top-left(matrix[0][0]) and has to reach bottom-right(matrix[m-1][n-1])</p>
<p>We have to find number of unique ways</p>
<p>We can move right or bottom only</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
<p>we have to use 2-d matrix to represent matrix of size m*n</p>
<p>Find Number ways from matrix[0][0] to matrix[m-1][n-1]</p>
<p>we have to f(m-1,n-1)-> number ways to reach matrix[m-1][n-1]</p>
<p>f(x,y)->number of ways to reach matrix[x][y]</p>
<h5>Step-3 : Finding Base Cases</h5>
<p>if m==1 and n==1 there will be one block only, so number of ways=1</p>
<p>if m==1 and n!=1 , then there will be single column only, for that we can move down only, then number ways to reach all block will be only one way</p>
<p>if m!=1 and n==1 , then there will be single row only, for that also, we can move right only. then number of ways will be one only</p>
<p>base cases : </p>
<p>row==0 & colum==0 -> f(0,0)=1</p>
<p>for row<0 or column<0, there is no more blocks</p>
<p>row <0 or column<0 -> f(row,column)=0</p>
<h5>Step-4 : Finding The Recurrence Relation</h5>
<p>m=1,n=1</p>
<p>It will contain only one block, hence number of ways are 1</p>
<p>m=1,n=2</p>
<p>Here we are having two blocks, (0,0) and (0,1)</p>
<p>f(0,0)=1</p>
<p>for (0,1), to reach this block we have to come from either (0,0)(left) or (-1,0)(top)</p>
<p>From top there is no way, so f(-1,0)=0</p>
<p>for (0,0), the number ways will be f(0,0)=1</p>
<p>So, total number ways to reach (0,1)=f(0,1)=f(0,0)+f(-1,0)=1+0=0</p>
<p>Hence Recurrance Relation will be</p>
<p>Number ways to reach (row,column)=f(row,column)=number ways which comes from left + number ways which comes from top</p>
<p>Recurrance relation : <b>f(row,column)=f(row-1,column)+f(row,column-1)</b></p>
<h5>Step-5 : Recursive Solution</h5>

```python
 def recursive(row,column):
    if(row==0 and column==0):
        return 1
    if(row<0 or column<0):
        return 0
    left=recursive(row,column-1)
    top=recursive(row-1,column)
    return top+left

  m,n=list(map(int,input().split()))
  print(recursive(m-1,n-1))
```
<p>TC : O(2^n)</p>
<p>SC : O(m*n)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is day + last_day, since it is unique for its answer</p>

```python
  def memorization(row,column,memo):
    key=(row,column)
    if key in memo:
        return memo[key]
    if(row==0 and column==0):
        return 1
    if(row<0 or column<0):
        return 0
    left=memorization(row,column-1,memo)
    top=memorization(row-1,column,memo)
    memo[key]=top+left
    return memo[key]
  m,n=list(map(int,input().split()))
  print(memorization(m-1,n-1,memo))
```
<p>TC : O(m*n)</p>
<p>SC : O(m+n)+o(m*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
  def tabulation(m,n):
    dp=[[0]*n for i in range(m)]
    dp[0][0]=1
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=0,0
            if(i-1>=0):
                top=dp[i-1][j]
            if(j-1>=0):
                left=dp[i][j-1]
            dp[i][j]=left+top
    return dp[m-1][n-1]
  m,n=list(map(int,input().split()))
  print(tabulation(m,n))

```
<p>TC : O(m*n)</p>
<p>SC : O(m*n)+o(n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step in tabulation, we're using the last two answers only</p>
<p> We don't need all previous subproblem solutions</p>

```python
  def optimization(m,n):
    dp_prev=[0]*n
    dp_curr=[0]*n
    dp_curr[0]=1
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=0,0
            if(j-1>=0):
                left=dp_curr[j-1]
            if(i-1>=0):
                top=dp_prev[j]
            dp_curr[j]=left+top
        dp_prev=dp_curr.copy()
    return dp_prev[n-1]

  print(optimization(m,n))

```
<p>TC : O(m*n)</p>
<p>SC : o(n)</p>

<br>
<br>

<h4>10.Grid Unique Paths : Number of Unique ways from top left to bottom-right With Obstacle</h4>
<h5>We are given an “N*M” Maze. The maze contains some obstacles. A cell is ‘blockage’ in the maze if its value is -1. 0 represents non-blockage. There is no path possible through a blocked cell.</h5>
<h5>We need to count the total number of unique paths from the top-left corner of the maze to the bottom-right corner. At every cell, we can move either down or towards the right.</h5>
<img src="https://lh6.googleusercontent.com/0DE0Aw9ic6x1B_dMqiuJah-CAgwLL4AKdE9r-1Ot1hyqBXC9YuAWf835zNh8vAbEvYu08hLQXrjIae0psqQqAYu6WVhPk6fsOzfgVaEHDRo6MweRI1Po4Q6I8a-y2qrpww4y02MA">
<h5>Step-1 : Define The Problem</h5>
  <p>It is same as previous problem, but here we are given matrix with value, 0->can have path -1->Blocked no path possible</p>
  <p>We have to find number of unique ways from matrix[0][0] to matrix[m-1][n-1]</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
  <p>we have to use 2-d matrix to represent matrix of size m*n</p>
  <p>Find Number ways from matrix[0][0] to matrix[m-1][n-1]</p>
  <p>we have to f(m-1,n-1)-> number ways to reach matrix[m-1][n-1]</p>
  <p>f(x,y)->number of ways to reach matrix[x][y]</p>
<h5>Step-3 : Finding Base Cases</h5>
  <p>if we have only one element in matrix</p>
  <p>row=0,column=0, f(0,0)=1</p>
  <p>if row<0 or column <0 , f(<0,<0)=0</p>
  <p>if there is an obtacle, f(row,column)=0 if matrix[row][column]=-1</p>
<h5>Step-4 : Finding The Recurrence Relation</h5>
  <p>Same as previous problem</p>
  <p>f(row,column)=f(row-1,column)+f(column,row-1)</p>
<h5>Step-5 : Recursive Solution</h5>

```python
 def recursive(row,column,matrix):
    if(row==0 and column==0 and matrix[row][column]==0):
        return 1
    if(row<0 or column<0):
        return 0
    if(matrix[row][column]==-1):
        return 0
    left=recursive(row,column-1,matrix)
    top=recursive(row-1,column,matrix)
    return left+top

  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(recursive(m-1,n-1,matrix))
```
<p>TC : O(2^n)</p>
<p>SC : O(m*n)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is day + last_day, since it is unique for its answer</p>

```python
  def memorization(row,column,matrix,memo):
    key=(row,column)
    if key in memo:
        return memo[key]
    if(row==0 and column==0 and matrix[row][column]==0):
        return 1
    if(row<0 or column<0):
        return 0
    if(matrix[row][column]==-1):
        return 0
    left=memorization(row,column-1,matrix,memo)
    top=memorization(row-1,column,matrix,memo)
    memo[key]=left+top
    return memo[key]
  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(memorization(m-1,n-1,matrix,memo))
```
<p>TC : O(m*n)</p>
<p>SC : O(m+n)+o(m*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
  def tabulation(m,n,matrix):
    dp=[[0]*n for i in range(m)]
    dp[0][0]=1
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=0,0
            if(j-1>=0 and matrix[i][j-1]==0):
                left=dp[i][j-1]
            if(i-1>=0 and matrix[i-1][j]==0):
                top=dp[i-1][j]
            dp[i][j]=left+top
    return dp[m-1][n-1]
  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(tabulation(m,n,matrix))

```
<p>TC : O(m*n)</p>
<p>SC : O(m*n)+o(n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step in tabulation, we're using the last two row answers only</p>
<p> We don't need all previous subproblem solutions</p>

```python
  def optimization(m,n,matrix):
    dp_prev=[0]*n
    dp_curr=[0]*n
    dp_curr[0]=1
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=0,0
            if(j-1>=0 and matrix[i][j-1]==0):
                left=dp_curr[j-1]
            if(i-1>=0 and matrix[i-1][j]==0):
                top=dp_prev[j]
            dp_curr[j]=left+top
        dp_prev=dp_curr.copy()
    return dp_prev[n-1]

  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(optimization(m,n,matrix))

```
<p>TC : O(m*n)</p>
<p>SC : o(n)</p>

<br>
<br>

<h4>11.Minimum Path Sum In a Grid : Minimum Path Sum from top left to bottom-right</h4>

  <h5>We are given an “M*N” matrix of integers. We need to find a path from the top-left corner to the bottom-right corner of the matrix, such that there is a minimum cost past that we select.</h5>
  <h5>At every cell, we can move in only two directions: right and bottom. The cost of a path is given as the sum of values of cells of the given matrix.</h5>
  <img src="https://lh3.googleusercontent.com/0NwVLxnlw_pj_A8zXJMtCtfxaVBdN9TckPiv3yLtHeROub8tvHjqeSBqqy29jBx4Cb8dqhkcsub6-zzC4K8Zwv5yDb4yKW4Irg2RmK1kvnK0IFaSjL82S1fUSApESPjwjcRayR4U">

<h5>Step-1 : Define The Problem</h5>

  <p>Given a matrix of size m*n, where m=row Size, n=column size</p>
  <p>We have to start from top-left, i.e matrix[0][0] and has to reach bottom-right , i.e matrix[m-1][n-1]</p>
  <p>we can move either right or bottom, there will be different ways.</p>
  <p>we have to find a way which has minimum sum by finding sum of elements in that path</p>

<h5>Step-2 : Represent the Problem Programmatically</h5>

  <p>We can use 2-d arrays to represent matrix of size m*n</p>
  <p>we have to find maximum path from matrix[0][0] to matrix[m-1][n-1]</p>
  <p>f(row,column) -> minimum sum obtained to reach matrix[row][column] from matrix[0][0]</p>
  <p>We have to find, f(m-1,n-1)</p>

<h5>Step-3 : Finding Base Cases</h5>
  
  <p>f(0,0)=matrix[0][0], we are at starting position only</p>
  <p>f(row<0,column<0)=float('inf'), there is no path with row<0 or column<0, so consider maximum value as we are finding minimum value</p>

<h5>Step-4 : Finding The Recurrence Relation</h5>

  <p>f(row,column) -> minimum sum obtained to reach matrix[row][column] from matrix[0][0]</p>
  <p>To Reach (row,column), we have to come from either left (row,column-1) or top (row-1,column)</p>
  <p>Recurrance Relation : <b> f(row,column)=min(matrix[row][column]+f(row,column-1),matrix[row][column]+f(row-1,column))</b></p>
  
<h5>Step-5 : Recursive Solution</h5>

```python
 def recursive(row,column,matrix):
    if(row==0 and column==0):
        return matrix[0][0]
    if(row<0 or column<0):
        return float('inf')
    left=matrix[row][column]+recursive(row,column-1,matrix)
    top=matrix[row][column]+recursive(row-1,column,matrix)
    return min(left,top)

  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(recursive(m-1,n-1,matrix))
```
<p>TC : O(2^n)</p>
<p>SC : O(m*n)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is day + last_day, since it is unique for its answer</p>

```python
  def memorization(row,column,matrix,memo):
    key=(row,column)
    if key in memo:
        return memo[key]
    if(row==0 and column==0):
        return matrix[0][0]
    if(row<0 or column<0):
        return float('inf')
    left=matrix[row][column]+memorization(row,column-1,matrix,memo)
    top=matrix[row][column]+memorization(row-1,column,matrix,memo)
    memo[key]=min(left,top)
    return memo[key]
  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(memorization(m-1,n-1,matrix,memo))
```
<p>TC : O(m*n)</p>
<p>SC : O(m+n)+o(m*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
  def tabulation(m,n,matrix):
    dp=[[0]*n for i in range(m)]
    dp[0][0]=matrix[0][0]
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=float('inf'),float('inf')
            if(j-1>=0):
                left=matrix[i][j]+dp[i][j-1]
            if(i-1>=0):
                top=matrix[i][j]+dp[i-1][j]
            dp[i][j]=min(left,top)
    return dp[m-1][n-1]
  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(tabulation(m,n,matrix))

```
<p>TC : O(m*n)</p>
<p>SC : O(m*n)+o(n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step in tabulation, we're using the last two row answers only</p>
<p> We don't need all previous subproblem solutions</p>

```python
  def optimization(m,n,matrix):
    dp_prev=[0]*n
    dp_curr=[0]*n
    dp_curr[0]=matrix[0][0]
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=float('inf'),float('inf')
            if(j-1>=0):
                left=matrix[i][j]+dp_curr[j-1]
            if(i-1>=0):
                top=matrix[i][j]+dp_prev[j]
            dp_curr[j]=min(left,top)
        dp_prev=dp_curr.copy()
    return dp_prev[n-1]

  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(optimization(m,n,matrix))

```
<p>TC : O(m*n)</p>
<p>SC : o(n)</p>

<br>
<br>

<h4>12.Minimum Path Sum in Traingular Grid : Minimum Path Sum from First Row to Last Row</h4>

  <h5>We are given a Triangular matrix. We need to find the minimum path sum from the first row to the last row.</h5>
  <h5>At every cell we can move in only two directions: either to the bottom cell (↓) or to the bottom-right cell(↘)</h5>
  <img src="https://lh3.googleusercontent.com/EIm_osUvLQDqDWEZ0AkumtyDzfn8TEefpZ-ZpIVIh1ITEKl2rnu_yLdXqZolvrqYkKNsGjicgLtS2gr9py0uCp89tu15PoROUcDj3wT9RQi3dIe4Cwb9ricoxjFEFOsu4rDVY1Yn">

<h5>Step-1 : Define The Problem</h5>

  <p>We have given a triangluar grid, we have to start from first row and has to reach last row</p>
  <p>From first row, we can move either bottom or bottom-right to reach second row</p>
  <p>each grid element has some value, find minimum path sum to reach last row from first row</p>

<h5>Step-2 : Represent the Problem Programmatically</h5>

  <P>We will be given n , which represent the number of rows</P>
  <p>Each row contains, row number of elements</p>
  <p>We can use 2-d array to represent the trianglar grid</p>
  <p>Since we have multiple ending points in last row, We have to find minimum path sum if we start from matrix[0][0]</p>
  <p>We have to find f(0,0), f(i,j)-> minimum path sum from matrix[i][j] to last row</p>

<h5>Step-3 : Finding Base Cases</h5>

  <p>if we are at last row, minimum path sum = value at that particular grid</p>
  <p>f(i,j)=matrix[i][j]</p>

<h5>Step-4 : Finding The Recurrence Relation</h5> 
  
  <p>If we are at current row, to move second row. either we can move bottom or bottom-right</p>
  <p>Path sum for moving to bottom -> f(i,j)=matrix[i][j]+f(i+1,j)=value at current grid+path sum for bottom grid</p>
  <p>Path sum for moving to bottom-right -> f(i,j)=matrix[i][j]+f(i+1,j+1)==value at current grid+path sum for bottom-right grid</p>
  <p>We have to find minimum path sum</p>
  <p>f(i,j)=min(matrix[i][j]+f(i+1,j),matrix[i][j]+f(i+1,j+1))</p>

<h5>Step-5 : Recursive Solution</h5>

```python
 def recursive(n,i,j,matrix):
    if(i==n-1):
        return matrix[i][j]
    if(i<0 or j<0 or j>(i+1)):
        return float('inf')
    bottom=matrix[i][j]+recursive(n,i+1,j,matrix)
    bottomRight=matrix[i][j]+recursive(n,i+1,j+1,matrix)
    return min(bottom,bottomRight)

  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(recursive(m-1,n-1,matrix))
```
<p>TC : O(2^(n^2))</p>
<p>SC : O(n^2)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is row + column, since it is unique for its answer</p>

```python
  def memorization(n,i,j,matrix,memo):
    key=(i,j)
    if key in memo:
        return memo[key]
    if(i==n-1):
        return matrix[i][j]
    if(i<0 or j<0 or j>(i+1)):
        return float('inf')
    bottom=matrix[i][j]+memorization(n,i+1,j,matrix,memo)
    bottomRight=matrix[i][j]+memorization(n,i+1,j+1,matrix,memo)
    memo[key]=min(bottom,bottomRight)
    return memo[key]

  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  memo={}
  print(memorization(m-1,n-1,matrix,memo))
```
<p>TC : O(m*n)</p>
<p>SC : O(m+n)+o(m*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
  def tabulation(m,n,matrix):
    dp=[[0]*n for i in range(m)]
    dp[0][0]=matrix[0][0]
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=float('inf'),float('inf')
            if(j-1>=0):
                left=matrix[i][j]+dp[i][j-1]
            if(i-1>=0):
                top=matrix[i][j]+dp[i-1][j]
            dp[i][j]=min(left,top)
    return dp[m-1][n-1]
  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(tabulation(m,n,matrix))

```
<p>TC : O(n^2)</p>
<p>SC : O(n^2)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step in tabulation, we're using the next two row answers only</p>
<p> We don't need all previous subproblem solutions</p>

```python
def optimization(n,matrix):
    dp_next=[0]*n
    dp_current=[0]*(n-1)
    for i in range(n):
        dp_next[i]=matrix[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            bottom,bottomRight=float('inf'),float('inf')
            if((i+1)>0 and j<=(i+1)):
                bottom=matrix[i][j]+dp_next[j]
            if((i+1)>0 and (j+1)<=(i+1)):
                bottomRight=matrix[i][j]+dp_next[j+1]
            dp_current[j]=min(bottom,bottomRight)
        dp_next=dp_current.copy()
    return dp_next[0]

  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(optimization(m,n,matrix))

```
<p>TC : O(n^2)</p>
<p>SC : o(n)</p>



<h4>13.Minimum Path Sum in Grid : Minimum Path Sum from First Row to Last Row</h4>

  <h5>We are given a m*n matrix. We need to find the minimum path sum from the first row to the last row.</h5>
  <h5>At every cell we can move in only two directions: either to the bottom cell (↓) or to the bottom-right cell(↘)</h5>
  <img src="https://lh6.googleusercontent.com/xpFMcLpnK7M66ZKw8tK6zXQDNtd45bCEmY6BkkbOtb3jJzQiv1NreJTv63xCkkTOuMG-C0KjmN1cmP2m2hVxx7IDUS38Ut78Com243xZDJHO6dMsinsc5R_EhT7htyCp0s-TxLDw">

<h5>Step-1 : Define The Problem</h5>

  <p>We have given a m*n grid, we have to start from first row and has to reach last row</p>
  <p>From first row, we can move either bottom or bottom-right to reach second row</p>
  <p>each grid element has some value, find minimum path sum to reach last row from first row</p>

<h5>Step-2 : Represent the Problem Programmatically</h5>

  <P>We will be given m , which represent the number of rows</P>
  <P>We will be given n , which represent the number of columns</P>
  <p>We can use 2-d array to represent the trianglar grid</p>
  <p>Since we have multiple ending points in last row, We have to find minimum path sum if we start from matrix[0][0]</p>
  <p>We have to find f(0,0), f(i,j)-> minimum path sum from matrix[i][j] to last row</p>

<h5>Step-3 : Finding Base Cases</h5>

  <p>if we are at last row, minimum path sum = value at that particular grid</p>
  <p>f(i,j)=matrix[i][j]</p>

<h5>Step-4 : Finding The Recurrence Relation</h5> 
  
  <p>If we are at current row, to move second row. either we can move bottom or bottom-right</p>
  <p>Path sum for moving to bottom -> f(i,j)=matrix[i][j]+f(i+1,j)=value at current grid+path sum for bottom grid</p>
  <p>Path sum for moving to bottom-right -> f(i,j)=matrix[i][j]+f(i+1,j+1)==value at current grid+path sum for bottom-right grid</p>
  <p>We have to find minimum path sum</p>
  <p>f(i,j)=min(matrix[i][j]+f(i+1,j),matrix[i][j]+f(i+1,j+1))</p>

<h5>Step-5 : Recursive Solution</h5>

  <p>Since we have multiple starting points in first row</p>
  <p>Consider all starting points, find minimum value for each starting and minimum out of it</p>

```python
 def recursive(n,i,j,matrix):
    if(i==n-1):
        return matrix[i][j]
    if(i<0 or j<0 or j>(i+1)):
        return float('inf')
    bottom=matrix[i][j]+recursive(n,i+1,j,matrix)
    bottomRight=matrix[i][j]+recursive(n,i+1,j+1,matrix)
    return min(bottom,bottomRight)

m,n=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(m)]
final=float('-inf')
for i in range(n):
    temp=recursive(n,0,i,matrix)
    final=max(final,temp)
print(final)
```
<p>TC : O(2^(m*n))</p>
<p>SC : O(m*n)</p>
<h5>Step-5 : Memorization</h5>
<p>Create a map, and store every answer</p>
<p>Here Key for storing the answer is row + column, since it is unique for its answer</p>

```python
  def memorization(n,i,j,matrix,memo):
    key=(i,j)
    if key in memo:
        return memo[key]
    if(i==n-1):
        return matrix[i][j]
    if(i<0 or j<0 or j>(i+1)):
        return float('inf')
    bottom=matrix[i][j]+memorization(n,i+1,j,matrix,memo)
    bottomRight=matrix[i][j]+memorization(n,i+1,j+1,matrix,memo)
    memo[key]=min(bottom,bottomRight)
    return memo[key]

m,n=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(m)]
final=float('-inf')
for i in range(n):
    memo={}
    temp=memorization(n,0,i,matrix,memo)
    final=max(final,temp)
print(final)
```
<p>TC : O(m*n)</p>
<p>SC : O(m*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
  def tabulation(n,matrix):
    n=len(matrix)
    dp=[[0]*n for i in range(n)]
    for i in range(n):
        dp[n-1][i]=matrix[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(n):
            bottom,bottomRight,bottomLeft=float('-inf'),float('-inf'),float('-inf')
            bottom=matrix[i][j]+dp[i+1][j]
            if(j+1<n):
                bottomRight=matrix[i][j]+dp[i+1][j+1]
            if(j-1>=0):
                bottomLeft=matrix[i][j]+dp[i+1][j-1]
            dp[i][j]=max(bottom,bottomLeft,bottomRight)
    return max(dp[0])
  m,n=list(map(int,input().split()))
  matrix=[list(map(int,input().split())) for i in range(m)]
  print(tabulation(m,n,matrix))

```
<p>TC : O(m*n)</p>
<p>SC : O(m*n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>At each step in tabulation, we're using the next two row answers only</p>
<p> We don't need all previous subproblem solutions</p>

```python
def optimization(n,matrix):
    n=len(matrix)
    dp_next=[0]*n
    dp_current=[0]*n
    for i in range(n):
        dp_next[i]=matrix[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(n):
            bottom,bottomRight,bottomLeft=float('-inf'),float('-inf'),float('-inf')
            bottom=matrix[i][j]+dp_next[j]
            if(j+1<n):
                bottomRight=matrix[i][j]+dp_next[j+1]
            if(j-1>=0):
                bottomLeft=matrix[i][j]+dp_next[j-1]
            dp_current[j]=max(bottom,bottomLeft,bottomRight)
        dp_next=dp_current.copy()
    return max(dp_next)

m,n=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(m)]
print(optimization(m,n,matrix))

```
<p>TC : O(m*n)</p>
<p>SC : o(n)</p>

<br>  
<br>  

<h4>14.Ninja Training Maximum Sum By Alice and Bob</h4>

  

<h5>Step-1 : Define The Problem</h5>

  

<h5>Step-2 : Represent the Problem Programmatically</h5>

  

<h5>Step-3 : Finding Base Cases</h5>

  

<h5>Step-4 : Finding The Recurrence Relation</h5> 
  


<h5>Step-5 : Recursive Solution</h5>



```python

```
<p>TC : O(2^(m*n))</p>
<p>SC : O(m*n)</p>
<h5>Step-5 : Memorization</h5>

```python
  
```
<p>TC : O(m*n)</p>
<p>SC : O(m*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python


```
<p>TC : O(m*n)</p>
<p>SC : O(m*n)</p>
<h5>Step-7 : Space Optimization </h5>

```python


```
<p>TC : O(m*n)</p>
<p>SC : o(n)</p>


<br>  
<br>

<h4>Problems On Subsequences</h4>

<h4>15.Subset sum equal to target</h4>
    <h5>We are given an array ‘ARR’ with N positive integers. We need to find if there is a subset in “ARR” with a sum equal to K. If there is, return true else return false.</h5>
    <h5>A subset/subsequence is a contiguous or non-contiguous part of an array, where elements appear in the same order as the original array.</h5>
    <p>For example, for the array: [2,3,1] , the subsequences will be [{2},{3},{1},{2,3},{2,1},{3,1},{2,3,1}} but {3,2} is not a subsequence because its elements are not in the same order as the original array.</p>
    <img src="https://lh3.googleusercontent.com/rysBOW8CTed-bDzIHGURWVZDU-Ckn7F6Xhjl3QxKdbMY2f5cPZe0fk0FTpUxUqMDHamE3bTSK0PvMDZmwXWB3yta0JchhCVajBy0ieq4uOJ_lszEK7oJK9fBdEhy23WFZI1wR0jA">
<h5>Step-1 : Define The Problem</h5>
    <p>We are given an array and value k, we have to check whether there is subsequence of array with sum equal to k</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
    <p>We are given an array which is 0-based indexing and given a target value(k)</p>
    <p>We have to return either True or False as a final answer</p>
    <p>f(index,target) -> checks whether target sum subsequnce present from 0 to index</p>
    <p>We have to find f(n-1,target), where n=len(arr) and target=k</p>
<h5>Step-3 : Finding Base Cases</h5>
    <p>if target=0, then answer is always True, because empty subsequnce sum equals to zero</p>
    <p>f(index,0)=True</p>
    <p>if index=0, array contains only one element, then we can check like target==arr[index]</p>
    <p>if arr[0]==target, then target sum equals to element, that means answer is true</p>
    <p>f(0,target)=(arr[0]==target)</p>
    <p>f(0,target)=(target-arr[0]==0)</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
    <p>We know that, f(index,0)=True</p>
    <p>f(0,target)=(target-arr[0]==0)</p>
    <p>For Subsequnce Generation, we have to include current element and have to find all combintions</p>
    <p>we have to exclude current element and have to find all combinations</p>
    <p>Same principle we have to apply here</p>
    <p>f(index,target) = f(index-1,target-arr[index]) or f(index-1,target)</p>
    <p>f(index-1,target-arr[index]) -> Include current element (Reduce target) and move to next position</p>
    <p>f(index-1,target) -> Exclude current element and move to next position</p>
    <p>While including check, current element is less than or equal to target</p>
<h5>Step-5 : Recursive Solution</h5>



```python
  def recursive(arr,ind,target):
    if(target==0):
        return True
    if(ind==0):
        return target-arr[0]==0
    exclude=recursive(arr,ind-1,target)
    include=False
    if(target>=arr[ind]):
        include=recursive(arr,ind-1,target-arr[ind])
    return exclude or include
  n=int(input())
  arr=list(map(int,input().split()))
  target=int(input())
  print(recursive(arr,n-1,target))
```
<p>TC : O(2^(n))</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>
<p>Here key to store each subproblem answer is index and target sum</p>

```python
  def memorization(arr,ind,target,memo):
    key=(ind,target)
    if key in memo:
        return memo[key]
    if(target==0):
        return True
    if(ind==0):
        return target-arr[0]==0
    exclude=memorization(arr,ind-1,target,memo)
    include=False
    if(target>=arr[ind]):
        include=memorization(arr,ind-1,target-arr[ind],memo)
    memo[key]=exclude or include
    return memo[key]
  n=int(input())
  arr=list(map(int,input().split()))
  target=int(input())
  memo={}
  print(memorization(arr,n-1,target,memo))
```
<p>TC : O(target*n)</p>
<p>SC : O(target*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<img src="https://lh4.googleusercontent.com/78km0lvY5WD_q5H3fJPcdXpwFoAjQueE1brTZN-IGImd_YyS9DFPgLyyNaZGxHJ3fwBznyuU1VDEy8CrgNkKCZtK7rKZA1KtJp04UhE6kHMI56eJA0fH9V0uZEvEu4nbxXyqjuAH">

```python
  def tabulation(n,arr,target):
    dp=[[False for i in range(target+1)] for i in range(n)]
    for i in range(n):
        dp[i][0]=True
    if(arr[0]<=target):
        dp[0][arr[0]]=True
    for i in range(1,n):
        for j in range(1,target+1):
            exclude=dp[i-1][j]
            include=False
            if(arr[i]<=j):
                include=dp[i-1][j-arr[i]]
            dp[i][j]=include or exclude
    return dp[n-1][target]
  n=int(input())
  arr=list(map(int,input().split()))
  target=int(input())
  print(tabulation(n,arr,target))
```
<p>TC : O(target*n)</p>
<p>SC : O(target*n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>We are using current and previous row values only</p>
<p>we don't need to store all answers</p>

```python
  def optimization(n,arr,target):
    dp_prev=[False for i in range(target+1)]
    dp_current=[False for i in range(target+1)]
    dp_prev[0]=True
    dp_current[0]=True
    if(arr[0]<=target):
        dp_prev[arr[0]]=True
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=False,False
            exclude=dp_prev[j]
            if(arr[i]<=target):
                include=dp_prev[j-arr[i]]
            dp_current[j]=include or exclude
        dp_prev=dp_current.copy()
    return dp_prev[target]

```
<p>TC : O(target*n)</p>
<p>SC : o(target)</p>

<br>
<br>

<h4>16.Unbounded Knapsack</h4>
    <h5>A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items of infinite supply. Its weight is given by the ‘wt’ array and its value by the ‘val’ array. He can either include an item in its knapsack or exclude it but can’t partially have it as a fraction. We need to find the maximum value of items that the thief can steal. He can take a single item any number of times he wants and put it in his knapsack.</h5>
    <img src="https://lh4.googleusercontent.com/NXDXKmwueWiUKdOgXhDuQlxTTRXjStKg8sQ8ddyaLI6IU0s1vhWnBHuifDDDDEvWJXD9SnaI8gNsahmRMl_g3p0GTy6O01jZ_TygtaobjxC38UwWTmeD7zOlyJTPJz5lIP8dC3fd">
<h5>Step-1 : Define The Problem</h5>
    <p>we have given some set of items , each of it associated with some weight and cost</p>
    <p>We have given a bag, we have to include those items in such that it should carry those items perfectly</p>
    <p>we have to store like, we can carry most amount items in bag</p>
    <p>We can include same item many times</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
    <p>given cost and weight as arrays</p>
    <p>let us assume, index -> represents the item</p>
    <p>cost[index]-> cost of item</p>
    <p>weight[index]-> weight of item</p>
    <p>we have bag and its capacity(weight)</p>
    <p>f(ind,currentWeight)-> represents maximum costly items (from 0 to index) in bag up to currentWeight</p>
    <p>We have to find f(n-1,totalWeight)-> n-> number of items, totalWeight->Bag Capacity</p>
<h5>Step-3 : Finding Base Cases</h5>
    <p>if index=0, then there is only one item, then max cost we can gain is</p>
    <p>f(0,currentWeight)-> cost[0]*(currentWeight//weight[0])</p>
    <p>if currentWeight==0, max cost is 0</p>
    <p>f(index,0)=0</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
    <p>we know that, f(0,currentWeight)=cost[0]*(currentWeight//weight[0])</p>
    <p>f(index,currentWeight)=max(include,exclude)</p>
    <p>Include-> cost[index]+f(index,currentWeight-weight[index])</p>
    <p>Exclude-> f(index-1,currentWeight)</p>
    <p>f(index,currentWeight)=max(cost[index]+f(index,currentWeight-weight[index]),f(index-1,currentWeight))</p>
    <p>While include, we are not moving to next position because we can include current element many times</p>
    <p>While exclud, we are moving next position</p>
    <p>While including , we have to check, current element weight is less than or equal top currentWeight</p>
<h5>Step-5 : Recursive Solution</h5>



```python
  def recursive(ind,cost,weight,currentWeight):
    if(ind==0):
        return (cost[0])*(currentWeight//weight[ind])
    exclude=recursive(ind-1,cost,weight,currentWeight)
    include=float('-inf')
    if(weight[ind]<=currentWeight):
        include=cost[ind]+recursive(ind,cost,weight,currentWeight-weight[ind])
    return max(exclude,include)
  n=int(input())
  weight=list(map(int,input().split()))
  cost=list(map(int,input().split()))
  currentWeight=int(input())
  print(recursive(n-1,cost,weight,currentWeight))
```
<p>TC : O(2^(n))</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>
<p>Here key to store each subproblem answer is index and currentWeight</p>

```python
  def memorization(ind,cost,weight,currentWeight,memo):
    key=(ind,currentWeight)
    if key in memo:
        return memo[key]
    if(ind==0):
        return (cost[0])*(currentWeight//weight[ind])
    exclude=memorization(ind-1,cost,weight,currentWeight,memo)
    include=float('-inf')
    if(weight[ind]<=currentWeight):
        include=cost[ind]+memorization(ind,cost,weight,currentWeight-weight[ind],memo)
    memo[key]=max(exclude,include)
    return memo[key]
  n=int(input())
  weight=list(map(int,input().split()))
  cost=list(map(int,input().split()))
  currentWeight=int(input())
  memo={}
  print(memorization(n-1,cost,weight,currentWeight))
```
<p>TC : O(w*n)</p>
<p>SC : O(w*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<img src=" https://astikanand.github.io/techblogs/dynamic-programming-patterns/assets/unbounded_knapsack_tabulation.gif">
<img src="https://astikanand.github.io/techblogs/dynamic-programming-patterns/assets/unbounded_knapsack_tabulation_final.png">

```python
  def tabulation(n,weight,cost,currentWeight):
    dp=[[0 for i in range(currentWeight+1)] for i in range(n)]
    for i in range(1,currentWeight+1):
        dp[0][i]=(i//weight[0])*cost[0]
    for i in range(1,n):
        for j in range(1,currentWeight+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp[i-1][j]
            if(weight[i]<=j):
                include=cost[i]+dp[i][j-weight[i]]
            dp[i][j]=max(include,exclude)
    return dp[n-1][currentWeight]
  n=int(input())
  weight=list(map(int,input().split()))
  cost=list(map(int,input().split()))
  currentWeight=int(input())
  print(tabulation(n,weight,cost,currentWeight)) 
```
<p>TC : O(w*n)</p>
<p>SC : O(w*n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>We are using current and previous row values only</p>
<p>we don't need to store all answers</p>

```python
  def optimization(n,weight,cost,currentWeight):
    dp_prev=[0 for i in range(currentWeight+1)]
    dp_curr=[0 for i in range(currentWeight+1)]
    for i in range(1,currentWeight+1):
        dp_prev[i]=(i//weight[0])*cost[0]
    for i in range(1,n):
        for j in range(1,currentWeight+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp_prev[j]
            if(weight[i]<=j):
                include=cost[i]+dp_curr[j-weight[i]]
            dp_curr[j]=max(include,exclude)
        dp_prev=dp_curr.copy()
    return dp_prev[currentWeight]
  n=int(input())
  weight=list(map(int,input().split()))
  cost=list(map(int,input().split()))
  currentWeight=int(input())
  print(optimization(n,weight,cost,currentWeight))

```
<p>TC : O(w*n)</p>
<p>SC : o(w)</p>

<br>
<br>


<h4>16.Rod Cutting Problem</h4>
    <h5>We are given a rod of size ‘N’. It can be cut into pieces. Each length of a piece has a particular price given by the price array. Our task is to find the maximum revenue that can be generated by selling the rod after cutting( if required) into pieces.</h5>
    <img src="https://lh3.googleusercontent.com/xjrJJkoDBbO16Zh_F7AWOg4KWtaZp9DGiFWvGJcgpySH6WDfDU4k--N5hS2S6767_bdW5pfjxgFRK5koD9X7yUPERE5qcWig8xMIZsRYoJ11M3kvso0Sv3d30gJN_EPWlqoUg_jQ">
<h5>Step-1 : Define The Problem</h5>
    <p>We have given a rod of some size N</p>
    <p>We can break that rod into some pieces of length 1...N</p>
    <p>Eacch length has given some cost</p>
    <p>We have to cut like to get maximum cost</p>
    <p>Same as unbounded knapsack</p>
    <p>rodSize=N</p>
    <p>cost=cost of item</p>
    <p>length 1..N=weight</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
    <p>given cost arrays</p>
    <p>let us assume, index -> represents the length of piece</p>
    <p>cost[index]-> cost of particular length piece</p>
    <p>f(ind,currentRodSize)-> represents maximum costly pieces (from length 0 to index) up to currentRodSize</p>
    <p>We have to find f(n-1,rodSize)-> n-> length of pieces, rodSize->rod Size</p>
<h5>Step-3 : Finding Base Cases</h5>
    <p>if index=0, then there is only single length piece, then max cost we can gain is</p>
    <p>f(0,currentRodSize)-> cost[0]*(currentRodSize//length[0])</p>
    <p>if currentRodSize==0, max cost is 0</p>
    <p>f(index,0)=0</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
    <p>we know that, f(0,currentRodSize)=cost[0]*(currentRodSize//length[0])</p>
    <p>f(index,currentRodSize)=max(include,exclude)</p>
    <p>Include-> cost[index]+f(index,currentRodSize-length[index])</p>
    <p>Exclude-> f(index-1,currentRodSize)</p>
    <p>f(index,currentRodSize)=max(cost[index]+f(index,currentRodSize-length[index]),f(index-1,currentRodSize))</p>
    <p>While include, we are not moving to next position because we can include current element many times</p>
    <p>While exclud, we are moving next position</p>
    <p>While including , we have to check, current element weight is less than or equal top currentRodSize</p>
<h5>Step-5 : Recursive Solution</h5>



```python
  def recursive(ind,cost,length,rodSize):
    if(ind==0):
        return cost[0]*(rodSize//length[0])
    exclude=recursive(ind-1,cost,length,rodSize)
    include=float('-inf')
    if(length[ind]<=rodSize):
        include=cost[ind]+recursive(ind,cost,length,rodSize-length[ind])
    return max(include,exclude)
  n=int(input())
  length=list(map(int,input().split()))
  cost=list(map(int,input().split()))
  rodSize=int(input())
  print(recursive(n-1,cost,length,rodSize))
```
<p>TC : O(2^(n))</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>
<p>Here key to store each subproblem answer is index and currentRodSizes</p>

```python
  def memorization(ind,cost,length,rodSize,memo):
    key=(ind,rodSize)
    if key in memo:
        return memo[key]
    if(ind==0):
        return cost[0]*(rodSize//length[0])
    exclude=memorization(ind-1,cost,length,rodSize,memo)
    include=float('-inf')
    if(length[ind]<=rodSize):
        include=cost[ind]+memorization(ind,cost,length,rodSize-length[ind],memo)
    memo[key]=max(include,exclude)
    return memo[key]
  n=int(input())
  length=list(map(int,input().split()))
  cost=list(map(int,input().split()))
  rodSize=int(input())
  memo={}
  print(memorization(n-1,cost,length,rodSize,memo))
```
<p>TC : O(rodSize*n)</p>
<p>SC : O(rosSize*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
  def tabulation(n,cost,length,rodSize):
    dp=[[0 for i in range(rodSize+1)] for i in range(n)]
    for i in range(rodSize+1):
        dp[0][i]=cost[0]*(i//length[0])
    for i in range(1,n):
        for j in range(1,rodSize+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp[i-1][j]
            if(length[i]<=j):
                include=cost[i]+dp[i][j-length[i]]
            dp[i][j]=max(include,exclude)
    return dp[n-1][rodSize]
  n=int(input())
  length=list(map(int,input().split()))
  cost=list(map(int,input().split()))
  rodSize=int(input())
  print(tabulation(n,cost,length,rodSize))
   
```
<p>TC : O(rodSize*n)</p>
<p>SC : O(rodSize*n)</p>
<h5>Step-7 : Space Optimization </h5>
<p>We are using current and previous row values only</p>
<p>we don't need to store all answers</p>

```python
  def optimization(n,cost,length,rodSize):
    dp_prev=[0 for i in range(rodSize+1)]
    dp_curr=[0 for i in range(rodSize+1)]
    for i in range(rodSize+1):
        dp_prev[i]=cost[0]*(i//length[0])
    for i in range(1,n):
        for j in range(1,rodSize+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp_prev[j]
            if(length[i]<=j):
                include=cost[i]+dp_curr[j-length[i]]
            dp_curr[j]=max(include,exclude)
        dp_prev=dp_curr.copy()
    return dp_prev[rodSize]
  n=int(input())
  length=list(map(int,input().split()))
  cost=list(map(int,input().split()))
  rodSize=int(input())
  print(optimization(n,cost,length,rodSize))

```
<p>TC : O(rodSize*n)</p>
<p>SC : o(rodSize)</p>

<br>
<br>

<h4>18.Partition Equal Subset Sum</h4>
  <h5>We are given an array ‘ARR’ with N positive integers. We need to find if we can partition the array into two subsets such that the sum of elements of each subset is equal to the other.</h5>
  <h5>If we can partition, return true else return false.</h5>
  <img src="https://lh5.googleusercontent.com/4cpcGpegSp1TGUp1ItTKaOzmZt93QD6-ebefylt6HjWE8ta6haxobbjIkwprij5Pal9LHqqNu_JUeqo8F0Xr_cirKMXxv8uUlh5n6Y1lGe6Min8j8tyV7KPdUJ4qe_us8Gcf6a_x">
<h4>Step-1 : Define The Problem</h4>
  <p>We have given an array, we have to check like, whether we can divide the array into two subsequnces such that their sumr are equal</p>
  <p>We have already solved subset sum equal to k</p>
  <p>Lets say temp=sum(array)</p>
  <p>if we divide total sum into two parts, half=temp//2</p>
  <p>so, we have to check like whether there are two subsequnces with sum==half</p>
  <p>Here we don't need to check for two subsequnces, because if we can check for one sequence, remaining will always equal to half</p>
  <p>So, we have to check whethere there is subsequnce with sum equals to half of total sum</p>
  <p>if totalSum is odd, its no possible for partion</p>

```python
def isSubsetSumEqualToK(n,arr,target):
    dp=[[False]*(target+1) for i in range(n)]
    for i in range(n):
        dp[i][0]=True
    if(target<=arr[0]):
        dp[0][arr[0]]=True
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=False,False
            exclude=dp[i-1][j]
            if(arr[i]<=j):
                include=dp[i-1][j-arr[i]]
            dp[i][j]=include or exclude
    return dp[n-1][target]

n=int(input())
arr=list(map(int,input().split()))
totalSum=sum(arr)
if(totalSum & 1):
    print(False)
else:
    half=totalSum//2
    print(isSubsetSumEqualToK(n,arr,half))
```

<h4>19.Partition Set Into 2 Subsets With Min Absolute Sum Diff</h4>
  <h5>Partition A Set Into Two Subsets With Minimum Absolute Sum Difference</h5>
  <h5>We are given an array ‘ARR’ with N positive integers. We need to partition the array into two subsets such that the absolute difference of the sum of elements of the subsets is minimum.</h5>
  <h5>We need to return only the minimum absolute difference of the sum of elements of the two partitions.</h5>
  <img src="https://lh5.googleusercontent.com/oICvHTjrORRPm9JUDytnyHqWrUlINxqjDiubEr6QuxIoOo9jSyour1Vj2_qHB_db7odN6GSMfwrjq9Xo-cW6bVucybEuGI8e5otDrZYJfJ9lOinss2svNF2l7WSFDOS4RjfB0e33">
<h4>Step-1 : Define Problem</h4>
  <p>We have given array, we have to split array into two subsequnces such that their difference in sum is minimum</p>
  <p>In Subset Sum Equal to k tabulation approach</p>
  <p>We have checked for each index, whether there is susequnce sum is there or not for 1 to target sum</p>
  <p>The last row shows, subsequnce sum is there or not for given array from 1 to target sum</p>
  <p>From This row, we can get all possible subsequnce sums</p>
  <p>If we know one subseqnce sum, other will total-sum</p>
  <p>easily we can get the difference</p>

```python 
def isSubsetSumEqualToK(n,arr,target):
    dp=[[False]*(target+1) for i in range(n)]
    for i in range(n):
        dp[i][0]=True
    if(target<=arr[0]):
        dp[0][arr[0]]=True
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=False,False
            exclude=dp[i-1][j]
            if(arr[i]<=j):
                include=dp[i-1][j-arr[i]]
            dp[i][j]=include or exclude
    return dp

n=int(input())
arr=list(map(int,input().split()))
totalSum=sum(arr)
dp=isSubsetSumEqualToK(n,arr,totalSum)
final=float('inf')
for i in range(1,totalSum+1):
    if(dp[n-1][i]):
        currentSum=i
        otherSum=totalSum-i
        diff=abs(currentSum-otherSum)
        final=min(final,diff)
print(final)
```

<br>
<br>

<h4>20.Count Subsets with Sum K</h4>
  <h5>We are given an array ‘ARR’ with N positive integers and an integer K. We need to find the number of subsets whose sum is equal to K.</h5>
  <img src="https://lh4.googleusercontent.com/pKgBxODRwO9eGi2OEQPcgpZwmOz-BaOcCpy29NqzoOau4IN_ioOJvjsnHkl5cB2bCJx67byJbceLB1sX7enyoTa1kwa1BE6NBdPX0szXrnzY7HADEQuo0BeRIkD28yq2WcVR8JzV">
<h5>Step-1 : Define The Problem</h5>
  <p>We have given an array, we need find different subsequnces whose sum equal to k</p>
  <p>we need to find the count of subsequences</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
  <p>We know aleady about finding subsequnces, i.e pick and not-pick technique</p>
  <p>f(index,target)-> number of subsequences from 0 to index whose sum equal to k</p>
<h5>Step-3 : Finding Base Cases</h5>
  <p>Suppose we have only one element in array, then number os subsequnces that can be generated is only one</p>
  <p>As per problem, Sum of subsequnce should equal to given target k</p>
  <p>Then, if array contains only one element</p>
  <p>f(0,target)=1 if(target==arr[0]) else 0</p>
  <p>if target==0, then we found a way</p>
  <p>f(index,0)=1</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
  <p>We know technique of generation of subsequnces</p>
  <p>since we need count of subsequences, we will add</p>
  <p>1.If we include current index in subsequnce -> f(index,target)=f(index-1,target-arr[index])</p>
  <p>1.If we exclude current index in subsequnce -> f(index,target)=f(index-1,target)</p>
  <p>f(index,target)->number of subsequences from 0 to index whose sum equal to k</p>
  <p>f(index,target)->f(index-1,target-arr[i])+f(index-1,target)</p>
  <p>When we are including, we have to check whether element is less than or equal to target</p>
<h5>Step-5 : Recursive Solution</h5>

```python
def recursive(arr,n,target):
    if(target==0):
        return 1
    if(n==0):
        if(target-arr[n]==0):
            return 1
        else:
            return 0
    exclude=recursive(arr,n-1,target)
    include=0
    if(arr[n]<=target):
        include=recursive(arr,n-1,target-arr[n])
    return include+exclude
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(recursive(arr,n-1,target))
```
<p>TC : O(2^n)</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>

```python
def memorization(arr,n,target,memo):
  key=(n,target)
  if key in memo:
      return memo[key]
  if(target==0):
      return 1
  if(n==0):
      if(target-arr[n]==0):
          return 1
      else:
          return 0
  exclude=memorization(arr,n-1,target,memo)
  include=0
  if(arr[n]<=target):
      include=memorization(arr,n-1,target-arr[n],memo)
  memo[key]=include+exclude
  return memo[key]
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
memo={}
print(memorization(arr,n-1,target,memo))
```
<p>TC : O(N*target)</p>
<p>SC : O(N)+O(N*Target)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
def tabulation(n,arr,target):
    dp=[[0]*(target+1) for i in range(n)]
    for i in range(n):
        dp[i][0]=1
    if(arr[0]<=target):
        dp[0][arr[0]]=1
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp[i-1][j]
            if(arr[i]<=j):
                include=dp[i-1][j-arr[i]]
            dp[i][j]=include+exclude
    return dp[n-1][target]
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(tabulation(n,arr,target))
```
<p>TC : O(n*target)</p>
<p>SC : O(n*target)</p>
<h5>Step-7 : Space Optimization </h5>

```python
def optimization(n,arr,target):
    dp_prev=[0]*(target+1)
    dp_current=[0]*(target+1)
    dp_prev[0]=1
    dp_current[0]=1
    if(arr[0]<=target):
        dp_prev[arr[0]]=1
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp_prev[j]
            if(arr[i]<=j):
                include=dp_prev[j-arr[i]]
            dp_current[j]=include+exclude
        dp_prev=dp_current.copy()
    return dp_prev[target]
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(optimization(n,arr,target))
```
<p>TC : O(n*target)</p>
<p>SC : o(target)</p>


<br>  
<br>


<h4>21.Count Partitions with Given Difference</h4>
  <h5>We are given an array ‘ARR’ with N positive integers and an integer D. We need to count the number of ways we can partition the given array into two subsets, S1 and S2 such that S1 – S2 = D and S1 is always greater than or equal to S2.</h5>
  <img src="https://lh4.googleusercontent.com/e9O5M_ol5HElVA5aHG794M4VGdBiuHllaqMCokrYVkRVvvcK2oqd4SL37yFYhJ6GlT7Cp11TWH_LeDMqXaF-CwkWUULx_-BfCpaASzZhtOUOssxXX2VX8PwvntCP9ZHZLzL6_RNE">
<h4>Step-1 : Define Problem</h4>
  <p>We have given Difference D=S1-S2</p>
  <p>We know, Total Sum S=S1+S2</p>
  <p>If we know S1, S2=S-S1</p>
  <p>Based on Above Equations, D-S=S1-S2-S1-S2=-S2</p>
  <p>S2=(S-D)//2</p>
  <p>so, if we are able to find number of subsequnce whose sum == S2, that will be our answer</p>
  <p>if S-D is Odd, we can't divide into two parts</p>
  <p>if S-D is zero, we can't find any ways</p>

```python 
def optimization(n,arr,target):
    dp_prev=[0]*(target+1)
    dp_current=[0]*(target+1)
    dp_prev[0]=1
    dp_current[0]=1
    if(arr[0]<=target):
        dp_prev[arr[0]]=1
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp_prev[j]
            if(arr[i]<=j):
                include=dp_prev[j-arr[i]]
            dp_current[j]=include+exclude
        dp_prev=dp_current.copy()
    return dp_prev[target]

n=int(input())
arr=list(map(int,input().split()))
target=int(input())
totalSum=sum(arr)
if((totalSum-target)<0 or (totalSum-target)&1):
    print(0)
else:
    temp=(totalSum-target)//2
    print(optimization(n,arr,temp))
```

<p>TC : O(n*target)</p>
<p>SC : o(target)</p>

<br>  
<br>  

<h4>22.0/1 Knapsack</h4>
  <h5>A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items. Its weight is given by the ‘wt’ array and its value by the ‘val’ array. He can either include an item in its knapsack or exclude it but can’t partially have it as a fraction. We need to find the maximum value of items that the thief can steal.</h5>
  <img src="https://lh3.googleusercontent.com/bgxCoEMMmxwuN3HgXNgYZ_o_Gxb8QSyBXXTxwSpsP7757ECoAplkpCtBdoS5LFM-3C-YhAbIhIbB9XGKxTZBGm6GB7HstnwmKf3hix_8V3zfuHLrK70bOjr01PezXrYOymoEiCaZ">
<h5>Step-1 : Define The Problem</h5>
  <p>We have given a knapsack of weight and given some n items , each has some weight and value</p>
  <p>We can include items in bag such that, we should not exceed the bag weight and can earn max value</p>
  <p>Find out all possible ways to include items in bag, find max value items list</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
  <p>Since we are check all possible ways and has to find max value</p>
  <p>We need to use pick or not-pick technique</p>
  <p>All items are reporesented in terms of indexes</p>
  <p>f(index,weight)->Maximum valuable items collected in bag with atmost weight of bag</p>
<h5>Step-3 : Finding Base Cases</h5>
  <p>if weight of bag is zero, we can't include any items, so max value=0</p>
  <p>f(index,0)->0</p>
  <p>if we have only one item left, we have some weight in bag, then we can include only when itemWeight <= weight</p>
  <p>f(0,weight) -> val[0] if(W[0]<=weight) else float('inf')</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
  <P>We need to find all possible combinations, it can be found by </P>
  <p>Include current index item -> find all ways further</p>
  <p>Exclude current index item -> find all ways further</p>
  <p>find max of both cases, that will be our answer</p>
  <p>f(index,weight)=max(include,exclude)</p>
  <p>include=val[index]+f(index-1,weight-w[index])</p>
  <p>we can include current item only when w[index]<=weight</p>
  <p>exclude=f(index-1,weight)</p>
<h5>Step-5 : Recursive Solution</h5>

```python
def recursive(index,weight,w,v):
  if(index==0):
      if(w[index]<=weight):
          return v[index]
  exclude=recursive(index-1,weight,w,v)
  include=float('-inf')
  if(w[index]<=weight):
      include=v[index]+recursive(index-1,weight-w[index],w,v)
  return max(include,exclude)
n=int(input())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
weight=int(input())
print(recursive(n-1,weight,w,v))
```
<p>TC : O(2^(n))</p>
<p>SC : O(n)</p>
<h5>Step-5 : Memorization</h5>

```python
def memorization(index,weight,w,v,memo):
    key=(index,weight)
    if key in memo:
        return memo[key]
    if(index==0):
        if(w[index]<=weight):
            return v[index]
    exclude=memorization(index-1,weight,w,v,memo)
    include=float('-inf')
    if(w[index]<=weight):
        include=v[index]+memorization(index-1,weight-w[index],w,v,memo)
    memo[key]=max(include,exclude)
    return memo[key]
n=int(input())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
weight=int(input())
memo={}
print(memorization(n-1,weight,w,v,memo))
```
<p>TC : O(weight*n)</p>
<p>SC : O(weight*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
def tabulation(n,weight,w,v):
    dp=[[0]*(weight+1) for i in range(n)]
    for j in range(1,weight+1):
        if(w[0]<=j):
            dp[0][j]=v[0]
    for i in range(1,n):
        for j in range(1,weight+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp[i-1][j]
            if(w[i]<=j):
                include=v[i]+dp[i-1][j-w[i]]
            dp[i][j]=max(include,exclude)
    return dp[n-1][weight]
n=int(input())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
weight=int(input())
```
<p>TC : O(weight*n)</p>
<p>SC : O(weight*n)</p>
<h5>Step-7 : Space Optimization </h5>

```python
def optimization(n,weight,w,v):
    dp_prev=[0]*(weight+1)
    dp_curr=[0]*(weight+1)
    for j in range(1,weight+1):
        if(w[0]<=j):
            dp_prev[j]=v[0]
    for i in range(1,n):
        for j in range(1,weight+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp_prev[j]
            if(w[i]<=j):
                include=v[i]+dp_prev[j-w[i]]
            dp_curr[j]=max(include,exclude)
        dp_prev=dp_curr.copy()
    return dp_prev[weight]
n=int(input())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
weight=int(input())
```
<p>TC : O(weight*n)</p>
<p>SC : o(n)</p>


<br>  
<br>

<h4>23.Minimum Coins</h4>
  <h5>We are given a target sum of ‘X’ and ‘N’ distinct numbers denoting the coin denominations. We need to tell the minimum number of coins required to reach the target sum. We can pick a coin denomination for any number of times we want.</h5>
  <img src="https://lh3.googleusercontent.com/vjYc2Da63eMYCY65kP0Q_mrE1Uf7F-CReNgdvGiidaz2nAdR6-jPxSspcMrvzM9UONzBYjcCMdaIwF2z_t7idvIwNQQy4cCbDQN0YRgI3A6NPI6GoA6KrjEUavSlUfOGYnFI1cKy">
<h5>Step-1 : Define The Problem</h5>
  <p>we have given some target sum and array of numbers</p>
  <p>we need to make the sum with miniumum number of coins and we can use a number many times</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
  <p>Since we are check all possible ways and has to find min count of numbes</p>
  <p>We need to use pick or not-pick technique</p>
  <p>When we pick a number, istead of moving further lets give a chance to include same number again</p>
  <p>All items are reporesented in terms of indexes</p>
  <p>f(index,target)->Minimum number of coins used to make target sum using 0 to index coins </p>
<h5>Step-3 : Finding Base Cases</h5>
  <p>if target sum is zero, we can't include any coins, so coins required=0</p>
  <p>f(index,0)->0</p>
  <p>if we have only one coin left, we have some target sum, then we can include coins as many possible which nakes targetSum</p>
  <p>if we can't make that sum with given coin, we can't make sum</p>
  <p>f(0,weight) -> target//arr[0] if(target%arr[0]==0) else float('inf')</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
  <P>We need to find all possible combinations, it can be found by </P>
  <p>Include current index item -> find all ways With same coin again</p>
  <p>Exclude current index item -> find all ways further</p>
  <p>find max of both cases, that will be our answer</p>
  <p>f(index,target)=min(include,exclude)</p>
  <p>include=1+f(index-1,target-arr[index])</p>
  <p>we can include current item only when w[index]<=target</p>
  <p>exclude=f(index-1,target)</p>
<h5>Step-5 : Recursive Solution</h5>

```python
def recursive(index,arr,target):
    if(target==0):
        return 0
    if(index==0):
        if(target%arr[0]==0):
            return target//arr[0]
        else:
            return float('inf')
    exclude=recursive(index-1,arr,target)
    include=float('inf')
    if(arr[index]<=target):
        include=1+recursive(index,arr,target-arr[index])
    return min(include,exclude)
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(recursive(n-1,arr,target))
```
<p>TC : O(2^(n*target))</p>
<p>SC : O(n*target)</p>
<h5>Step-5 : Memorization</h5>

```python
def memorization(index,arr,target,memo):
    key=(index,target)
    if key in memo:
        return memo[key]
    if(target==0):
        return 0
    if(index==0):
        if(target%arr[0]==0):
            return target//arr[0]
        else:
            return float('inf')
    exclude=recursive(index-1,arr,target)
    include=float('inf')
    if(arr[index]<=target):
        include=1+recursive(index,arr,target-arr[index])
    memo[key]=min(include,exclude)
    return memo[key]
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
memo={}
print(memorization(n-1,arr,target,memo))
```
<p>TC : O(target*n)</p>
<p>SC : O(target*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
def tabulation(n,arr,target):
    dp=[[0]*(target+1) for i in range(n)]
    for i in range(1,target+1):
        if(i%arr[0]==0):
            dp[0][i]=(i//arr[0])
        else:
            dp[0][i]=float('inf')
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=float('inf'),float('inf')
            exclude=dp[i-1][j]
            if(arr[i]<=j):
                include=1+dp[i][j-arr[i]]
            dp[i][j]=min(include,exclude)
    return dp[n-1][target]
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(tabulation(n,arr,target))
```
<p>TC : O(target*n)</p>
<p>SC : O(target*n)</p>
<h5>Step-7 : Space Optimization </h5>

```python
def optimization(n,arr,target):
    dp_prev=[0]*(target+1)
    dp_curr=[0]*(target+1)
    for i in range(1,target+1):
        if(i%arr[0]==0):
            dp_prev[i]=(i//arr[0])
        else:
            dp_prev[i]=float('inf')
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=float('inf'),float('inf')
            exclude=dp_prev[j]
            if(arr[i]<=j):
                include=1+dp_curr[j-arr[i]]
            dp_curr[j]=min(include,exclude)
        dp_prev=dp_curr.copy()
    return dp_prev[target]
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(optimization(n,arr,target))
```
<p>TC : O(target*n)</p>
<p>SC : o(n)</p>


<br>  
<br>

<h4>24.Target Sum </h4>
  <h5>We are given an array ‘ARR’ of size ‘N’ and a number ‘Target’. Our task is to build an expression from the given array where we can place a ‘+’ or ‘-’ sign in front of an integer. We want to place a sign in front of every integer of the array and get our required target. We need to count the number of ways in which we can achieve our required target.</h5>
  <img src="https://lh5.googleusercontent.com/vMo25kPQM_P2t1Uav9EXflTOGwHNajBPXO_GULWMbNbgnuPP7CcxksX_B0szm13u7OKd2JiouZYNoWFEomMibbxBAlt_hi66_-Zd2NtLeL9-9WgjxBFyaCNmh3HUT1orTLr6l_r1">
<h4>Step-1 : Define Problem</h4>
  <p>We have given array and target</p>
  <p>We have to apply whether + or - to each element in array and has to make that expression value equal to target</p>
  <p>We have to find the number of different ways</p>
  <p>suppose, if array has [a,b,c,d,e]</p>
  <p>if we apply + and -, a+b+c-d-e</p>
  <p>it can be shown as (a+b+c)-(d+e)=target</p>
  <p>it is similar to difference=S1-S2</p>
  <p>This problem we have already discussed in Count of Subsets With given difference problem</p>

```python 
def optimization(n,arr,target):
    dp_prev=[0]*(target+1)
    dp_current=[0]*(target+1)
    dp_prev[0]=1
    dp_current[0]=1
    if(arr[0]<=target):
        dp_prev[arr[0]]=1
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp_prev[j]
            if(arr[i]<=j):
                include=dp_prev[j-arr[i]]
            dp_current[j]=include+exclude
        dp_prev=dp_current.copy()
    return dp_prev[target]

n=int(input())
arr=list(map(int,input().split()))
target=int(input())
totalSum=sum(arr)
if((totalSum-target)<0 or (totalSum-target)&1):
    print(0)
else:
    temp=(totalSum-target)//2
    print(optimization(n,arr,temp))
```

<br>
<br>

<h4>25.Coin Change 2 : Count Of Ways to Make Target Coins Can Used Many Times</h4>
  <h5>We are given an array Arr with N distinct coins and a target. We have an infinite supply of each coin denomination. We need to find the number of ways we sum up the coin values to give us the target.</h5>
  <h5>Each coin can be used any number of times.</h5>
  <img src="https://lh5.googleusercontent.com/iyZgys0bQ2_EjJUUXEjjtYn3y4ZKThe_MYqLQ0E9YKL93xHDV0KzsK1zaq1mrB7CzmTSuUtZA75JsaRBnDq-K4RigX31GOd6B3Tr9-Ts_yuf_OyELBFM3ZdR3ulCEXMSbHFC9nr9">
<h5>Step-1 : Define The Problem</h5>
  <p>we have given some target sum and array of numbers</p>
  <p>we need to make the sum with numbers of array and we can use a number many times</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
  <p>Since we are check all possible ways and has to find min count of numbes</p>
  <p>We need to use pick or not-pick technique</p>
  <p>When we pick a number, istead of moving further lets give a chance to include same number again</p>
  <p>All items are reporesented in terms of indexes</p>
  <p>f(index,target)->Number of Ways to make target sum using 0 to index coins </p>
<h5>Step-3 : Finding Base Cases</h5>
  <p>if target sum is zero, we can't include any coins, so coins required=0</p>
  <p>f(index,0)->0</p>
  <p>if we have only one coin left, we have some target sum, then we can include coins as many possible which nakes targetSum, Then there is one way</p>
  <p>if we can't make that sum with given coin, we can't make sum</p>
  <p>f(0,weight) -> 1 if(target%arr[0]==0) else 0</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
  <P>We need to find all possible combinations, it can be found by </P>
  <p>Include current index item -> find all ways With same coin again</p>
  <p>Exclude current index item -> find all ways further</p>
  <p>find max of both cases, that will be our answer</p>
  <p>f(index,target)=include+exclude</p>
  <p>include=f(index-1,target-arr[index])</p>
  <p>we can include current item only when arr[index]<=target</p>
  <p>exclude=f(index-1,target)</p>
<h5>Step-5 : Recursive Solution</h5>

```python
def recursive(index,arr,target):
    if(target==0):
        return 1
    if(index==0):
        if(target%arr[0]==0):
            return 1
        else:
            return 0
    exclude=recursive(index-1,arr,target)
    include=0
    if(arr[index]<=target):
        include=recursive(index,arr,target-arr[index])
    return include+exclude
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(recursive(n-1,arr,target))
```
<p>TC : O(2^(n*target))</p>
<p>SC : O(n*target)</p>
<h5>Step-5 : Memorization</h5>

```python
def memorization(index,arr,target,memo):
    key=(index,target)
    if key in memo:
        return memo[key]
    if(target==0):
        return 1
    if(index==0):
        if(target%arr[0]==0):
            return 1
        else:
            return 0
    exclude=recursive(index-1,arr,target)
    include=0
    if(arr[index]<=target):
        include=recursive(index,arr,target-arr[index])
    memo[key]=include+exclude
    return memo[key]
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
memo={}
print(memorization(n-1,arr,target,memo))
```
<p>TC : O(target*n)</p>
<p>SC : O(target*n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>

```python
def tabulation(n,arr,target):
    dp=[[0]*(target+1) for i in range(n)]
    for i in range(n):
        dp[i][0]=1
    for i in range(1,target+1):
        if(i%arr[0]==0):
            dp[0][i]=1
        else:
            dp[0][i]=0
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp[i-1][j]
            if(arr[i]<=j):
                include=dp[i][j-arr[i]]
            dp[i][j]=include+exclude
    return dp[n-1][target]

n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(tabulation(n,arr,target))
```
<p>TC : O(target*n)</p>
<p>SC : O(target*n)</p>
<h5>Step-7 : Space Optimization </h5>

```python
def optimization(n,arr,target):
    dp_prev=[0]*(target+1)
    dp_curr=[0]*(target+1)
    dp_prev[0]=1
    dp_curr[0]=1
    for i in range(1,target+1):
        if(i%arr[0]==0):
            dp_prev[i]=1
        else:
            dp_prev[i]=0
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp_prev[j]
            if(arr[i]<=j):
                include=dp_curr[j-arr[i]]
            dp_curr[j]=include+exclude
        dp_prev=dp_curr.copy()
    return dp_prev[target]
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(optimization(n,arr,target))
```
<p>TC : O(target*n)</p>
<p>SC : o(n)</p>


<br>  
<br>

<h3>DP On Strings</h3>

<h4>26.Longest Common Subsequence</h4>
  <h5>A subsequence of a string is a list of characters of the string where some characters are deleted ( or not deleted at all) and they should be in the same order in the subsequence as in the original string.</h5>
  <h5>The longest Common Subsequence is defined for two strings. It is the common subsequence that has the greatest length.</h5>
  <img src="https://lh4.googleusercontent.com/kqP_myXD1uP-WyUCAeuvaC9242HVbXUetsiMG-FF5DlYpDubYitw_SvLcfvVuviS0c_V32NBJp1Yok4Pn6mevktHwAVjGgoYc23p80nfVCkT7JZ_X6Ic--DRRxzU_TxP1cnbpTls">
<h5>Step-1 : Define The Problem</h5>
  <p>We have given two strings s1 and s2, each of it have length n1 and n2</p>
  <p>s1 will have some set of subsequnces abd s2 will have some set of subsequences</p>
  <p>We have to find common subsequnce which is present in both string</p>
  <p>We may have more than one common subsequences</p>
  <p>We have find what is the length of longest subsequence present in both strings</p>
  <p>Eg: s1=abc s=ac</p>
  <p>abc -> [a,b,c,ab,bc,abc]</p>
  <p>ac -> [a,c,ac]</p>
  <p>Common -> [a,c,ac]</p>
  <p>Longest -> ac</p>
  <p>length of longest ->2</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
  <p>both strings can be represented interms index 0...n1-1, 0...n2-1</p>
  <p>let us assume, f(index1,index2) -> it represents the length of longest common subsequence in s1 of 0 ... index1 and s2 of 0 ...index2</p>
<h5>Step-3 : Finding Base Cases</h5>
  <p>if any one of the string have no characters, then there is no subsequnces for it</p>
  <p>hence,there will be no common subsequnce, so answer will be 0</p>
  <p>f(index1<0 (or) index2<0)->0</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
  <p>Since we need length of common subsequnce in two string, we will just compare charcters of two string charcters</p>
  <p>Since subsequnce should be in order, we will move in same direction while iteration</p>
  <p>we have to compare the characters of both sequences, one by one</p>
  <p>When comparing the characters: </p>
  <p>If both characters in strings matches, then we found a common character for a sequence we will increase length by one, and move to next position for remaining common charcters</p>
  <p>if(s1[index1]==s2p[index2]) 1+f(index1-1,index2-1)</p>
  <p>If the characters don't match, you explore two possibilities:</p>
  <p>Either the last characters of both sequences don't contribute to the common subsequence.</p>
  <p>So, you try excluding the last character of Sequence 1 and compare again.</p>
  <p>f(index1-1,index2)</p>
  <p>Or you exclude the last character of Sequence 2 and compare again.</p>
  <p>f(index1,index2-1)</p>
  <p>You pick the longer subsequence of the two possibilities.</p>
  <p>if(s1[index1]!=s2p[index2]) max(f(index1-1,index2),f(index1,index2-1))</p>
  <p>recurrance relation</p>

```python
if seq1[i] == seq2[j]:
    LCS[i][j] = 1 + LCS[i - 1][j - 1]  # if the characters match, add 1 to the LCS length
else:
    LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])  # characters don't match, take the maximum of the two possibilities

```
<h5>Step-5 : Recursive Solution</h5>



```python
def recursive(S1,S2,index1,index2):
    if(index1<0 or index2<0):
        return 0
    if(S1[index1]==S2[index2]):
        return 1+recursive(S1,S2,index1-1,index2-1)
    else:
        excludeS1=recursive(S1,S2,index1-1,index2)
        excludeS2=recursive(S1,S2,index1,index2-1)
        return max(excludeS1,excludeS2)
S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
print(recursive(S1,S2,n1-1,n2-1))
```
<p>TC : O(2^(n1*n2))</p>
<p>SC : O(n1*n2)</p>
<h5>Step-5 : Memorization</h5>

```python
def memorization(S1,S2,index1,index2,memo):
  key=(index1,index2)
  if key in memo:
      return memo[key]
  if(index1<0 or index2<0):
      return 0
  if(S1[index1]==S2[index2]):
      memo[key]=1+ memorization(S1,S2,index1-1,index2-1,memo)
      return memo[key]
  else:
      excludeS1= memorization(S1,S2,index1-1,index2,memo)
      excludeS2= memorization(S1,S2,index1,index2-1,memo)
      memo[key]=max(excludeS1,excludeS2)
      return memo[key]
S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
memo={}
print(memorization(S1,S2,n1-1,n2-1,memo))
```
<p>TC : O(n1*n2)</p>
<p>SC : O(n1*n2)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we are dealing with string, to implement tabulation we have to represent strings in 1-based indexing</p>
<p>So that, for empty strings, index will be 0</p>

```python
def tabulation(S1,S2):
    n1,n2=len(S1),len(S2)
    dp=[[0]*(n2+1) for i in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                excludeS1=dp[i-1][j]
                excludeS2=dp[i][j-1]
                dp[i][j]=max(excludeS1,excludeS2)
    return dp[n1][n2]
S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
print(tabulation(S1,S2))
```
<p>TC : O(n1*n2)</p>
<p>SC : O(n1*n2)</p>
<h5>Step-7 : Space Optimization </h5>

```python
def optimization(S1,S2):
    n1,n2=len(S1),len(S2)
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp_curr[j]=1+dp_prev[j-1]
            else:
                excludeS1=dp_prev[j]
                excludeS2=dp_curr[j-1]
                dp_curr[j]=max(excludeS1,excludeS2)
        dp_prev=dp_curr.copy()
    return dp_curr[n2]
S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
print(optimization(S1,S2))
```
<p>TC : O(n1*n2)</p>
<p>SC : o(n2)</p>


<br>  
<br>

<h4>27.WildCard Matching : '*' / '?' Check String1 matches String2 or not </h4>
  <h5>We are given two strings ‘S1’ and ‘S2’. String S1 can have the following two special characters:</h5>
  <h5>1.‘?’ can be matched to a single character of S2.</h5>
  <h5>2.‘*’ can be matched to any sequence of characters of S2. (sequence can be of length zero or more).</h5>
  <h5>We need to check whether strings S1 and S2 match or not.</h5>
  <img src="https://lh6.googleusercontent.com/zR799fMPurVRIqbURhPX34iIwt7qov7AcczQnqMUfFIywmegsFWSSUg4hbhiVhBa1P6nJ_bM_ssJnm3rmomKuuiUfwhaOe2AqCKvpvoMFTUZ_Vl7sC73-zgrergtC8neAQ4_zfdp">
<h5>Step-1 : Define The Problem</h5>
  <p>we have given two strings s1 and s2</p>
  <p>We have to check whether two strings are equal or not</p>
  <p>but, s1 may contain wildcards like '?' or '*'</p>
  <p>? -> it is match any single charcter</p>
  <p>* -> it can match any number of charcters</p>
  <p>We have to find two strings can be equal or not.</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
  <p>both strings can be represented interms index 0...n1-1, 0...n2-1</p>
  <p>let us assume, f(index1,index2) -> it represents both string are matched or not  in s1 from 0 ... index1 and s2 from 0 ...index2</p>
  <p>We have to check total strings</p>
  <p>so, we have to find f(n1-1,n2-1)</p>
  <p>We have to return either True or False</p>
<h5>Step-3 : Finding Base Cases</h5>
  <p>we have to match the two string character by character</p>
  <p>if both string charcters are compard and if there is nothing to compare, that means both are equal</p>
  <p>index1<0 and index2<0 -> True</p>
  <p>if first string charcters are completed, and second string characters left te compare, it means both strings are not matched</p>
  <p>index1<0 and index2>=0 -> False</p>
  <p>if second string charcters were compared, and first string characters left te compare, it has two cases</p>
  <p>if first string contains only *'s , it means it may match empty also, that means both are matched</p>
  <p>if first string contains other than *, both strings are not matched</p>
  <p>index2<0 and index1>=0 -> True if(AllStar(S1,index1)) else False</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
  <p>we have to compare each character at same position in two strings</p>
  <p>While comparing characters</p>
  <p>if both characters are same, then move to next position in string</p>
  <p>if string one character equals to ?, then it is always to equal any character at string two, then we will move to next position</p>
  <p>if s1 character equals to * , then it has two cases</p>
  <p>1.it may match nothing or single charcter in s2</p>
  <p>we have to consider both cases</p>
  <p>if matches nothing -> f(index1-1,index2) -> since it matches nothing, s1 will move and s2 will be at same position</p>
  <p>if matches single character-> f(index1,index2-1)-> we will be at same position in s1, because, we may match multiple chacrters</p>
  <p>if s1 character not equals to s2 character, then return False</p>

```python
if(S1[index1]==S2[index2] or s1[index1]=='?'):
    return f(index1-1,index2-1) # both characters are equal
else:
    if(S1[index1]=='*'):
        a=f(index1-1,index2) # matches nothing
        b=f(index1,index2-1) # matches a character
        return a or b 
    else:
         return False # both characters are not equal
```
<h5>Step-5 : Recursive Solution</h5>



```python
def recursive(S1,S2,index1,index2):
    if(index1<0 and index2<0):
        return True
    if(index1<0 and index2>=0):
        return False
    if(index2<0 and index1>=0):
        if(S1[index1]=='*' and len(set(S1[index1:]))==1):
            return True
        else:
            return False

    if(S1[index1]==S2[index2] or S1[index1]=='?'):
        return recursive(S1,S2,index1-1,index2-1)
    else:
        if(S1[index1]=='*'):
            excludeS1=recursive(S1,S2,index1-1,index2)
            excludeS2=recursive(S1,S2,index1,index2-1)
            return excludeS1 or excludeS2
        else:
            return False
S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
print(recursive(S1,S2,n1-1,n2-1))
```
<p>TC : O(2^(n1*n2))</p>
<p>SC : O(n1*n2)</p>
<h5>Step-5 : Memorization</h5>

```python
def memorization(S1,S2,index1,index2,memo):
    key=(index1,index2)
    if key in memo:
        return memo[key]
    if(index1<0 and index2<0):
        return True
    if(index1<0 and index2>=0):
        return False
    if(index2<0 and index1>=0):
        if(S1[index1]=='*' and len(set(S1[index1:]))==1):
            return True
        else:
            return False

    if(S1[index1]==S2[index2] or S1[index1]=='?'):
        memo[key]=memorization(S1,S2,index1-1,index2-1,memo)
        return memo[key]
    else:
        if(S1[index1]=='*'):
            excludeS1=memorization(S1,S2,index1-1,index2,memo)
            excludeS2=memorization(S1,S2,index1,index2-1,memo)
            memo[key]=excludeS1 or excludeS2
            return memo[key]
        else:
            memo[key]=False
            return memo[key]
S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
memo={}
print(memorization(S1,S2,n1-1,n2-1,memo))
```
<p>TC : O(n1*n2)</p>
<p>SC : O(n1*n2)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we are dealing with string, to implement tabulation we have to represent strings in 1-based indexing</p>
<p>So that, for empty strings, index will be 0</p>

```python
def tabulation(S1,S2,n1,n2):
    dp=[[False]*(n2+1) for i in range(n1+1)]
    dp[0][0]=True
    for i in range(1,n2+1):
        dp[0][i]=False
    for i in range(1,n1+1):
        index1=i-1
        if(S1[index1]=='*' and len(set(S1[index1:]))==1):
            dp[i][0]=True
        else:
            dp[i][0]=False
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2] or S1[index1]=='?'):
                dp[i][j]=dp[i-1][j-1]
            else:
                if(S1[index1]=='*'):
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
    return dp[n1][n2]
S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
print(tabulation(S1,S2,n1,n2))
```
<p>TC : O(n1*n2)</p>
<p>SC : O(n1*n2)</p>
<h5>Step-7 : Space Optimization </h5>
<p>Since we are dealing with string, to implement tabulation we have to represent strings in 1-based indexing</p>
<p>So that, for empty strings, index will be 0</p>

```python
def optimization(S1,S2,n1,n2):
    dp_prev=[False]*(n2+1)
    dp_curr=[False]*(n2+1)
    dp_prev[0]=True
    for i in range(1,n2+1):
        dp_prev[i]=False
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]=='*' and len(set(S1[index1:]))==1):
                dp_curr[0]=True
            else:
                dp_curr[0]=False
            if(S1[index1]==S2[index2] or S1[index1]=='?'):
                dp_curr[j]=dp_prev[j-1]
            else:
                if(S1[index1]=='*'):
                    dp_curr[j]=dp_prev[j] or dp_curr[j-1]
                else:
                    dp_curr[j]=False
        dp_prev=dp_curr.copy()
    return dp_curr[n2]
S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
print(optimization(S1,S2,n1,n2))
```
<p>TC : O(n1*n2)</p>
<p>SC : o(n2)</p>


<br>  
<br>

<h4>28.Print Longest Common Subsequence</h4>
  <h5>In the previous article Longest Common Subsequence, we learned to print the length of the longest common subsequence of two strings. In this article, we will learn to print the actual string of the longest common subsequence. </h5>
  <img src="https://lh3.googleusercontent.com/rzY1hPZD4poztbgaEVhEqVUcaNmdMm6UQL0opF87uE9ALhBJIrHMsdZZ61J_e0cEiyKFrzeaf-eMdo8er2W2opBEh1SPNd5GJJac3GrS6h4yDQoEW5OPBTQ5Wsu68FCnN_zRv-Gz">
<h5>Step-1 : Define The Problem</h5>
  <p>We have given two strings s1 and s2</p>
  <p>We have to print the longest common subsequnces</p>
<h5>Step=2 : Solution</h5>
  <p>previously we have solved lcs problem</p>
  <p>In that problem, we have found length of common subsequence in lcs tabulation</p>
  <p>based on those lengths and how those are evaluated, we can print the lcs</p>
  <p>we know that</p>
  <p>if(S1[i-1] == S2[j-1]), then return 1 + dp[i-1][j-1] -> it means when two charcters are equal we are coming from diagnolly</p>
  <p>if(S1[i-1] != S2[j-1]) , then return 0 + max(dp[i-1][j],dp[i][j-1]) -> it means when two charcters are not equal, then we two choise either vertically or horizontally, we have to take maximum</p>
  <p>same formula applied from dp[n1][n2] to dp[0][0], in reverse way and if we found match will add it in an array</p>
  <a href="https://takeuforward.org/data-structure/print-longest-common-subsequence-dp-26/">Refer Here</a>

```python
def tabulation(S1,S2,n1,n2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    lcs=dp[n1][n2]
    i,j=n1,n2
    final=[]
    while(i>0 and j>0):
        index1,index2=i-1,j-1
        if(S1[index1]==S2[index2]):
            i-=1
            j-=1
            final.append(S1[index1])
        else:
            if(dp[i-1][j] > dp[i][j-1]):
                i-=1
            else:
                j-=1
    return "".join(final[::-1])
S1=input()
S2=input()
n1,n2=len(S1),len(S2)
print(tabulation(S1,S2,n1,n2))
```  
<p>TC : O(n1*n2)</p>
<p>SC : O(n1*n2)</p>


<br>
<br>

<h4>29.Longest Common Substring</h4>
  <p>A substring of a string is a subsequence in which all the characters are consecutive. Given two strings, we need to find the longest common substring.</p>
  <p>We need to print the length of the longest common substring.</p>
  <img src="https://lh5.googleusercontent.com/Ik0eDD_Ms5v1ag5jkvA9zLxXZjHivGNPY0VWtge8iQftgzebSpwFN8FqocTZGBIEmL2iHe64K08HibQbNfDZt27oMWW7CuQwqwdXTZtNldv1mg5w6ssV7zY66bHQEV82ejPKx_W8">
<h4>Step-1 : Define The Problem</h4>
  <p>we have given two strings s1 and s2</p>
  <p>s1 will have some set of substrings and s2 will have some set of substrings</p>
  <p>we need to find common substrings in both sets</p>
  <p>We need to return length of longest common substring</p>
  <p>It is similar to longest common subsequence, but here we need to find for substring</p>
  <p>Substring should be occur in adjust charcters only</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
  <p>both strings can be represented interms index 0...n1-1, 0...n2-1</p>
  <p>let us assume, f(index1,index2) -> it represents the length of longest common subsequence in s1 of 0 ... index1 and s2 of 0 ...index2</p>
<h5>Step-3 : Finding Base Cases</h5>
  <p>if any one of the string have no characters, then there is no subsequnces for it</p>
  <p>hence,there will be no common subsequnce, so answer will be 0</p>
  <p>f(index1<0 (or) index2<0)->0</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
  <p>Since we need length of common substring in two strings, we will just compare charcters of two string charcters</p>
  <p>Since subsequnce should be in order, we will move in same direction while iteration</p>
  <p>we have to compare the characters of both sequences, one by one</p>
  <p>When comparing the characters: </p>
  <p>If both characters in strings matches, then we found a common character for a sequence we will increase length by one, and move to next position for remaining common charcters</p>
  <p>if(s1[index1]==s2p[index2]) 1+f(index1-1,index2-1)</p>
  <p>If the characters don't match, substring ended there hence length will be come zero</p>
  <p>So, will move to next position and repeat same process</p>
  <p>We can take maximum value while increasing length</p>

```python
if seq1[i] == seq2[j]:
    LCS[i][j] = 1 + LCS[i - 1][j - 1]  # if the characters match, add 1 to the LCS length
else:
    LCS[i][j] = 0  # characters don't match, substring length will be zero

```
```python
def tabulation(S1,S2,n1,n2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    final=float('-inf')
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                temp=1+dp[i-1][j-1]
                dp[i][j]=temp
                final=max(final,temp)
            else:
                dp[i][j]=0
    return final

def optimization(S1,S2,n1,n2):
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    final=float('-inf')
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                temp=1+dp_prev[j-1]
                dp_curr[j]=temp
                final=max(final,temp)
            else:
                dp_curr[j]=0
        dp_prev=dp_curr.copy()
    return final
S1=input()
S2=input()
n1,n2=len(S1),len(S2)
print(tabulation(S1,S2,n1,n2))
print(optimization(S1,S2,n1,n2))
```


<br>
<br>

<h4>30.Longest Palindromic Subsequence</h4>
  <h5>A palindromic string is a string that is equal to its reverse. For example: “Nitin” is a palindromic string. Now the question states to find the length of the longest palindromic subsequence of a string. It is that palindromic subsequence of the given string with the greatest length. We need to print the length of the longest palindromic subsequence.</h5>
  <img src="https://lh4.googleusercontent.com/fpGtOSDImpZYH646I4H-04UkBgm3ej5qD8inRrdWGLqSvQ5r-l6HZ9YVDnKR9NuPNrlS_Qi-hcnkItk97WYFGcekJqVB2jWsYpx_wLJAuElhXomvVBCjhAu1sCr3jAK4PbyFaCvv">
<h5>Step-1 : Define The Problem</h5>
  <p>We know that longest common subsequence is common subsequence in two strings</p>
  <p>here we have given a string, we need to find a subsequnce of it which should be palindrome</p>
  <p>Palindrome is same as it is when we reverse it</p>
  <p>Subsequnce which is common for both string and its reverse is called palindromic subsequence</p>
  <p>so answer will be, Longest Common Subsequence for given string and its reverse</p>

```python
def optimizationlcs(S1,S2):
    n1,n2=len(S1),len(S2)
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp_curr[j]=1+dp_prev[j-1]
            else:
                excludeS1=dp_prev[j]
                excludeS2=dp_curr[j-1]
                dp_curr[j]=max(excludeS1,excludeS2)
        dp_prev=dp_curr.copy()
    return dp_curr[n2]

S1=input()
S2=S1[::-1]
n1=len(S1)
n2=len(S2)
print(optimizationlcs(S1,S2))
```

<h4>31.Minimum insertions to make string palindrome</h4>
  <h5>A palindromic string is a string that is the same as its reverse. For example: “nitin” is a palindromic string. Now the question states that we are given a string, we need to find the minimum insertions that we can make in that string to make it a palindrome.</h5>
  <img src="https://lh4.googleusercontent.com/tGTO25pL7yBykieDKbmcMGcwUGGim4YX-x97z_DxbOCGh9Lb7AN61pSZTUKEDT_T9WZVc8oRvAOTwPCYc6qan-AZC9-4LKmL5xo_t8ox1KhpHuySlvIRccODTsc8CzmRyQPpxkqH">

<h5>Step-1 : Define The Problem</h5>
  <p>We have given a string, we have to find number of min insertions to make string palindrome</p>
  <p>Firstly, we have find already existing palindomic sequence present in given string</p>
  <p>For remaining characters, to make them palindromic we all same characters again to it</p>
  <p>answer=len(String)-length of longest palindromic subsequnce</p>

```python
def optimization(S1,S2):
    n1,n2=len(S1),len(S2)
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp_curr[j]=1+dp_prev[j-1]
            else:
                excludeS1=dp_prev[j]
                excludeS2=dp_curr[j-1]
                dp_curr[j]=max(excludeS1,excludeS2)
        dp_prev=dp_curr.copy()
    return dp_curr[n2]

S1=input()
S2=S1[::-1]
n1=len(S1)
n2=len(S2)
lcs=optimization(S1,S2)
print(n1-lcs)
```

<br>
<br>

<h4>32.Minimum Insertions/Deletions to Convert String</h4>
  <h5>Minimum Insertions/Deletions to Convert String A to String B</h5>
  <h5>We are given two strings, str1 and str2. We are allowed the following operations:</h5>
  <h5>Delete any number of characters from string str1.</h5>
  <h5>Delete any number of characters from string str1.</h5>
  <h5>We need to tell the minimum operations required to convert str1 to str2.</h5>
  <img src="https://lh5.googleusercontent.com/A8n8o72QL6MTlp6mHwRPPIkAbNfSryFpp2SxQt-abKGqFhfVcbcwfdydf8gBeW-z6E1Yxumm6f6SFZdWPfWLQ41Ik_hmhZnUZs74L6RRHUbtp02g0LlcD0dTUXSEje1hi41EVJdf">
<h5>Step-1 : Define The Problem</h5>
  <p>We have given two strings s1 and s2</p>
  <p>We have to convert s1 into s2</p>
  <p>We have to find minimum number of insertions and deletions required for it</p>
  <p>To find the answer</p>
  <p>first we have to find longest common characters</p>
  <p>Then delete extra characters in s2</p>
  <p>Then insert required characters in s2 to make s1</p>
  <p>Answer = Number of deletions + Number of Insertion</p>
  <p>Number of deletions = len(s2)-lcs</p>
  <p>Number of insertions = len(s1)-lcs</p>

```python
def optimization(S1,S2):
    n1,n2=len(S1),len(S2)
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp_curr[j]=1+dp_prev[j-1]
            else:
                excludeS1=dp_prev[j]
                excludeS2=dp_curr[j-1]
                dp_curr[j]=max(excludeS1,excludeS2)
        dp_prev=dp_curr.copy()
    return dp_curr[n2]

S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
lcs=optimization(S1,S2)
deletions=n1-lcs
insertions=n2-lcs
print(deletions+insertions)
```
<br>
<br>

<h4>33.Shortest Common Supersequence</h4>
  <h5>We are given two strings ‘S1’ and ‘S2’. We need to return their shortest common supersequence. A supersequence is defined as the string which contains both the strings S1 and S2 as subsequences.</h5>
  <img src="https://lh3.googleusercontent.com/yCJEIc5nB_P1SIqKzcBEcywKRgTAgQt3w1wHrYad81cPdwFQRcagmfJLtOtw7_NzhsmbX0VxPxsm64fyGSolB-j0jY0QeC_vDaA-iEdUIWJQAf9bzjKdeRyc7fcHlWkfVhEIsL4i">

<h5>Step-1 : Define The Problem</h5>
  <p>We have given two Strings s1 and s2</p>
  <p>we need to find a string which contains both s1 and s2, It should have minimum length as possible</p>
  <p>It similar to printing largest common subsequnces</p>
  <p>While moving from dp[n1][n2] to dp[0][0]</p>
  <p>If we got same characters, include it once only</p>
  <p>When we get different characters, we will add both characters in order</p>
  <p>So final string will contain both strings</p>
  <p>Will loop through each string for remianinfg characters</p>

```python
def tabulation(S1,S2,n1,n2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    temp=[]
    i,j=n1,n2
    while(i>0 and j>0):
        index1,index2=i-1,j-1
        if(S1[index1]==S2[index2]):
            temp.append(S1[index1])
            i-=1
            j-=1
        else:
            if(dp[i-1][j]>dp[i][j-1]):
                temp.append(S1[index1])
                i-=1
            else:
                temp.append(S2[index2])
                j-=1
    while i>0:
        temp.append(S1[i-1])
        i-=1
    while j>0:
        temp.append(S2[j-1])
        j-=1
    return "".join(temp[::-1])
S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
print(tabulation(S1,S2,n1,n2))
```

<br>
<br>

<h4>34.Distinct Subsequences : Count Of Different Subsequnces</h4>
  <h5>We are given two strings S1 and S2, we want to know how many distinct subsequences of S2 are present in S1.</h5>
  <img src="https://lh4.googleusercontent.com/xo9fySafqrICbnFuGmCaAooWdzSJFDUV0Vm_1-yyA_z23Qega-BRMN0NVWIYrmF9jnDKTKU1I07NhGhT5D5dmJc-5OTYXpzlwTXIseopikjJY-QM8VPJSrmhSaCDyXCZIwF-ABjr">
<h5>Step-1 : Define The Problem</h5>
  <p>We have given two strings s1 and s2</p>
  <p>We have to find number of times s2 present in s1</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
  <p>both strings can be represented interms index 0...n1-1, 0...n2-1</p>
  <p>let us assume, f(index1,index2) -> it represents the count of s2 from 0 ...index2 present in s1 of 0 ... index1</p>
<h5>Step-3 : Finding Base Cases</h5>
  <p>Since we are finding s2 in s1</p>
  <p>we are comparing s2 charcters with s1</p>
  <p>If s2 characters all are compared and came to end, then s2 present in s1</p>
  <p>index2<0 -> 1</p>
  <p>if s1 characters all are compared and came to end, still s2 is there means, s2 not found in s1 anymore</p>
  <p>index1<0 -> 0</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
  <p>To check the existance of s2 in s1, we will compare characters of s2 with characters if s1 in order</p>
  <p>when comparing, if Character of s2 matches with s1, then we will increase s1 position to find remaining characters</p>
  <p>But, s2 will have two posibilities</p>
  <p>1.S2 may exist another time also</p>
  <p>2.S2 needs to compare for reminaing characters</p>
  <p>We have to combine both cases, since we are finding total ways</p>
  <p>f(index1-1,index2)=>check for another existance</p>
  <p>f(index1-1,index2-1)=>checking for remianing characters of s2</p>
  <p>f(index1-1,index2)+f(index1-1,index2-1) if(s1[index1]==s2[index2])</p>
  <p>If characters of s1 and s2 at current position not mataches, then we will move to next position in s1</p>
  <p>f(index1-1,index2) if(s1[index1]!=s2[index2])</p>

```python
  if(s1[index1]==s2[index2]):
    return f(index1-1,index2)+f(index1-1,index2-1)
  else:
    return f(index1-1,index2)
```
<h5>Step-5 : Recursive Solution</h5>



```python
def recursive(s1,s2,index1,index2):
    if(index2<0):
        return 1
    if(index1<0):
        return 0
    if(s1[index1]==s2[index2]):
        return recursive(s1,s2,index1-1,index2-1)+recursive(s1,s2,index1-1,index2)
    else:
        return recursive(s1,s2,index1-1,index2)
s1,s2=input(),input()
n1,n2=len(s1),len(s2)
print(recursive(s1,s2,n1-1,n2-1))
```
<p>TC : O(2^(n1*n2))</p>
<p>SC : O(n1*n2)</p>
<h5>Step-5 : Memorization</h5>

```python
def memorization(s1,s2,index1,index2,memo):
    key=(index1,index2)
    if key in memo:
        return memo[key]
    if(index2<0):
        return 1
    if(index1<0):
        return 0
    if(s1[index1]==s2[index2]):
        memo[key]=memorization(s1,s2,index1-1,index2-1,memo)+memorization(s1,s2,index1-1,index2,memo)
        return memo[key]
    else:
        memo[key]=memorization(s1,s2,index1-1,index2,memo)
        return memo[key]
s1,s2=input(),input()
n1,n2=len(s1),len(s2)
memo={}
print(memorization(s1,s2,n1-1,n2-1,memo))
```
<p>TC : O(n1*n2)</p>
<p>SC : O(n1*n2)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we are dealing with string, to implement tabulation we have to represent strings in 1-based indexing</p>
<p>So that, for empty strings, index will be 0</p>

```python
def tabulation(s1,s2,n1,n2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    for i in range(n2+1):
        dp[i][0]=1
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(s1[index1]==s2[index2]):
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n1][n2]
s1,s2=input(),input()
n1,n2=len(s1),len(s2)
print(tabulation(s1,s2,n1,n2))
```
<p>TC : O(n1*n2)</p>
<p>SC : O(n1*n2)</p>
<h5>Step-7 : Space Optimization </h5>

```python
def optimization(s1,s2,n1,n2):
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    dp_prev[0]=1
    dp_curr[0]=1
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(s1[index1]==s2[index2]):
                dp_curr[j]=dp_prev[j-1]+dp_prev[j]
            else:
                dp_curr[j]=dp_prev[j]
        dp_prev=dp_curr.copy()
    return dp_curr[n2]
s1,s2=input(),input()
n1,n2=len(s1),len(s2)
print(optimization(s1,s2,n1,n2))
```
<p>TC : O(n1*n2)</p>
<p>SC : o(n2)</p>


<br>
<br>

<h4>35.Edit Distance : Min Number Of Operations(insert/replace/delete) to Convert S1 to S2</h4>
  <h5>We are given two strings ‘S1’ and ‘S2’. We need to convert S1 to S2. The following three operations are allowed:</h5>
  <h5>1.Deletion of a character.</h5>
  <h5>2.Replacement of a character with another one.</h5>
  <h5>3.Insertion of a character.</h5>
  <h5>We have to return the minimum number of operations required to convert S1 to S2 as our answer.</h5>
  <img src="https://lh6.googleusercontent.com/Dxn0cvswqpu9nszd6gMXThvxbSwlyz_lLBUwzYmyNhvV9LcGNYWUjC9D8T9iP0pUlaf1WRtpYz061ttrSe8cvo-DvUeknkKX8MuDrBy4_JhsSqj4TVKoEoePOauIEpvN-UaeSZ5N">
<h5>Step-1 : Define The Problem</h5>
  <p>We have two strings s1 and s2, each of them has length n1 and n2</p>
  <p>We have to convert s1 to s2, either we can insert,delete,replace operation</p>
  <p>We have to find minium operations to convert s1 to s2</p>
  <p>At a time we can do only one action on one character only</p>
<h5>Step-2 : Represent the Problem Programmatically</h5>
  <p>two strings can be represented in terms of index's, i.e 0..n1 and 0..n2</p>
  <p>f(index1,index2) -> represents minimum operation to convert s1 in 0...index1 to s2 in 0...index2</p>
<h5>Step-3 : Finding Base Cases</h5>
  <p>while comparing, if s2 becomes empty and s1 has still characters, then minimum operations = number of characters left in s1, that has to be added in s2 to make it equal</p>
  <p>index2<0 -> index1+1</p>
    <p>while comparing, if s1 becomes empty and s2 has still characters, then minimum operations = number of characters left in s2, that has to be deleted in s2 to make it equal</p>
  <p>index1<0 -> index2+1</p>
<h5>Step-4 : Finding The Recurrence Relation</h5> 
  <p>To make s1==s2, we will compare each character in s1 and s2</p>
  <p>if both are equal, we don't need any operation and move on to next position</p>
  <p>f(index1-1,index2-1) if(s1[index1]==s2[index2])</p>
  <p>if both are diiferent, we have three ways to make it equal</p>
  <p>1.replace s1[index] with s2[index], then both positions has to move next position -> f(index1-1,index2-1)</p>
  <p>2.we can delete s1[index] and try matching for next position -> f(index1-1,index2)</p>
  <p>3.we can insert s2[index2] at index2, so that they become equal, so index1 position willnot change because new character inserted -> f(index1,index2-1)</p>
  <p>we have to take minimum of all three posibilities</p>

```python
if(S1[index2]==S2[index2]):
    return f(index1-1,index2-1)
else:
    replace=1+f(index1-1,index2-1)
    insert=1+f(index1-1,index2)
    delete=1+f(index1,index2-1)
    return min(replace,insert,delete)
```
<h5>Step-5 : Recursive Solution</h5>

```python
def recursive(s1,s2,index1,index2):
    if(index1<0):
        return index2+1
    if(index2<0):
        return index1+1
    if(s1[index1]==s2[index2]):
        return recursive(s1,s2,index1-1,index2-1)
    else:
        replace=1+recursive(s1,s2,index1-1,index2-1)
        insert=1+recursive(s1,s2,index1-1,index2)
        delete=1+recursive(s1,s2,index1,index2-1)
        return min(replace,insert,delete)
s1,s2=input(),input()
n1,n2=len(s1),len(s2)
print(recursive(s1,s2,n1-1,n2-1))
```
<p>TC : O(2^(n1*n2))</p>
<p>SC : O(n1*n2)</p>
<h5>Step-5 : Memorization</h5>

```python
def memorization(s1,s2,index1,index2,memo):
    key=(index1,index2)
    if key in memo:
        return memo[key]
    if(index1<0):
        return index2+1
    if(index2<0):
        return index1+1
    if(s1[index1]==s2[index2]):
        memo[key]=memorization(s1,s2,index1-1,index2-1,memo)
        return memo[key]
    else:
        replace=1+memorization(s1,s2,index1-1,index2-1,memo)
        insert=1+memorization(s1,s2,index1-1,index2,memo)
        delete=1+memorization(s1,s2,index1,index2-1,memo)
        memo[key]=min(replace,insert,delete)
        return memo[key]
s1,s2=input(),input()
n1,n2=len(s1),len(s2)
memo={}
print(memorization(s1,s2,n1-1,n2-1,memo))
```
<p>TC : O(n1*n2)</p>
<p>SC : O(n1*n2)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we are dealing with string, to implement tabulation we have to represent strings in 1-based indexing</p>
<p>So that, for empty strings, index will be 0</p>

```python
def tabulation(s1,s2,n1,n2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    for i in range(1,n1+1):
        dp[i][0]=i
    for i in range(1,n2+1):
        dp[0][i]=i
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(s1[index1]==s2[index2]):
                dp[i][j]=dp[i-1][j-1]
            else:
                replace=1+dp[i-1][j-1]
                insert=1+dp[i-1][j]
                delete=1+dp[i][j-1]
                dp[i][j]=min(replace,insert,delete)
    return dp[n1][n2]
s1,s2=input(),input()
n1,n2=len(s1),len(s2)
print(tabulation(s1,s2,n1,n2))
```
<p>TC : O(n1*n2)</p>
<p>SC : O(n1*n2)</p>
<h5>Step-7 : Space Optimization </h5>

```python
def optimization(s1,s2,n1,n2):
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    dp_curr[0]=0
    for i in range(1,n2+1):
        dp_prev[i]=i
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            dp_curr[0]=i
            index1,index2=i-1,j-1
            if(s1[index1]==s2[index2]):
                dp_curr[j]=dp_prev[j-1]
            else:
                replace=1+dp_prev[j-1]
                insert=1+dp_prev[j]
                delete=1+dp_curr[j-1]
                dp_curr[j]=min(replace,insert,delete)
        dp_prev=dp_curr.copy()
    return dp_curr[n2]
s1,s2=input(),input()
n1,n2=len(s1),len(s2)
print(optimization(s1,s2,n1,n2))

```
<p>TC : O(n1*n2)</p>
<p>SC : o(n2)</p>