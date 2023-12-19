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
<h4>Fibonacci Number</h4>
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
