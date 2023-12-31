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
<img src="https://lh3.googleusercontent.com/PDblNXbL7kmOxKoI7_0Yevnr7JF2FbXVr-9OaH9nn5uNeq6_P6fItMrWdEhs7fPUDBSoEKorJ9_lConrOtDUetBpq2s1bw4A9nIasR3dSJ">
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


