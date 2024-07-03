<h1>Analysis of algorithm</h1>
<p>When solving a problem like finding the sum of the first n natural numbers, we can approach it in multiple ways. To determine which approach is more efficient, we can't depend solely on measurements (like running the code on a machine and calculating time taken for execution for each approach) because these measurements depend on several factors, such as:</p>
<ul>
	<li><strong>Machine Type:</strong> Different machines have different processing capabilities. A more powerful (and expensive) machine will generally perform tasks faster than a less powerful (and cheaper) one.</li>
	<li><strong>Programming Language:</strong> Some programming languages (like C) are faster due to their lower-level operations and optimizations, while others (like Python) may be slower due to their higher-level nature and additional abstractions.</li>
	<li><strong>Load:</strong> depends on load that current machine is handling while executing programs</li>
</ul>
<p>Because of these variables, it's essential to use theoretical or mathematical analysis, known as asymptotic analysis, to evaluate the efficiency of algorithms in a machine-independent manner.</p>

<h2>Asymptotic Analysis</h2>
<p>Asymptotic analysis involves evaluating the performance of an algorithm in terms of its time and space complexity as the input size n grows. This approach uses mathematical functions to describe the behavior of an algorithm, allowing for a comparison that is independent of machine and language specifics.</p>
<p>In asymptotic analysis, we focus on the order of growth of an algorithm's running time or space requirements as a function of the input size</p>
<p>The order of growth describes how the running time or space requirements of an algorithm increase as the input size n increases.</p>
<p>Let's take an example and represent each approach in terms of order growth expressions</p>
<p><strong>Example : </strong></p>
<ul>
	<li>Mathematical Formula:</li>

```python
def fun1(n):
    return n * (n + 1) // 2
print(fun1(1000000))

```

<p>In this approach, finding answer involves only single calculation which takes constant amount of for any input n</p>
<p>let'a assume c1 time</p>

<p>Hence, order of growth expression can be represented as</p>
<p><strong>fun1(n)=c1</strong></p>
<p>c1 be the constant time for the computation.</p>


<li>Iterative Approach:</li>

```python
def fun2(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(fun2(1000000))
```

<p>In this approach, The loop runs n times and Each iteration performs a constant amount of work.let it be c2</p>
<p>let c3 be the constant time for initializing total to 0.</p>
<p>let c4 be the constant time for the final return statement.</p>
<p>Hence, order of growth expression can be represented as</p>
<p><strong>fun2(n)=c2n+c3+c4</strong></p>

<li>Quadratic Approach</li>

```python
def fun3(n):
    total = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            total += 1
    return total

print(fun3(1000))
```

<p>In this approach, The outer loop runs n times.</p>
<p>The inner loop runs i times for each i from 1 to n</p>
<p>let c5 be the he constant time for initializing total to 0.</p>
<p>let c6 be the constant time for each iteration of the inner loop.</p>
<p>let c7 be the constant time for the final return statement.</p>
<p>Hence, order of growth expression can be represented as</p>
<p>fun3(n)=c5+c6(n(n+1)//2)+c7</p>
<p>fun3(n)=c5+c6(n**2/2)+c6(n/2)+c7</p>
</ul>

<p>By representing the running times in terms of order of growth expressions, we can better understand the efficiency of each algorithm.</p>

<p>In asymptotic analysis, we focus on positive input sizes (n>0) and positive running time (T(n)>0).</p>
<p>This means we graph these functions in the first quadrant of a Cartesian coordinate system. By comparing the order of growth of different algorithms, we can predict their performance for large input sizes, regardless of the machine or language used.</p>
<p>In the above example, if we compare mathematical formula expression vs itertive expression in graph</p>
<p>Mathematical approach , <strong>fun1(n)=c1</strong></p>
<p>Itertive aproach , <strong>fun2(n)=c2n+c3+c4</strong></p>
<img src="./images/grpah1.jpg">