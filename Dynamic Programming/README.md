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
<p>TC : O(n)</p>
<p>SC : O(n)</p>
<h5>Step-6 : Iterative Implementation / Tabulation</h5>
<p>Since we have to reach n-1 step, we have to declare array of size n</p>
<p>Fill base cases</p>
<p>loop from 2 and fill all values based on recurrance relation</p>


```python
def tabulation(n,height):
    dp=[0]*(n)
    dp[0]=0
    dp[1]=abs(height[0]-height[1])
    for i in range(2,n):
        prev=dp[i-1]+abs(height[i-1]-height[i])
        prev2=dp[i-2]+abs(height[i-2]-height[i])
        dp[i]=min(prev,prev2)
    return dp[n-1]

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

<h4>4.Frog Jump : Minimum Energy : Up to k Steps</h4>
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


