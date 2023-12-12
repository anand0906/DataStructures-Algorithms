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
<ol>
  <li> Understand the problem and check whether it can be divided into subproblems</li>
  <li> Check whether it supports overlapping sub-problems or optimum substructure</li>
  <li> Find recurrence relation</li>
  <li> Find Base Cases </li>
  <li> Try recursive solution</li>
  <li> Apply memorization</li>
  <li> Try tabulation</li>
  <li> Apply Optimization</li>
</ol>
