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
<img src="./images/graph1.JPG">

<p>he blue line represents the running time of the iterative approach (2n+2).</p>
<p>The red horizontal line represents the running time of the mathematical formula approach (5)</p>

<p>This graph may represent like, for smaller value of n, itertive approach take less time due to its machine configuration</p>
<p>But for as n increase, itertive approach times is linearly increases, but formula approach takes constant time always</p>
<p>At some point of n, itertive will take more time than formula appraoch as seen in graph</p>
<p>Mathematically also we can prove</p>
<p>We know that, fun1,fun2>=0</p>
<p>To prove fun2>fun1 at some point n, let c1=5, c2=2,c3=2</p>
<p>2n+2>=5</p>
<p>2n>=5-2</p>
<p>2n>=3</p>
<p>n>=3/2</p>
<p>n>=1.5</p>
<p>n>=2</p>
<p>When n reaches greater than 2, itertive will take more time than formula based approch</p>
<p>This can be proved for any kind of machines or programming languages, because asymptotic growth expresssions will be common for all implementations</p>

<h3>Asymptotic Analysis Comparison</h3>

<div class="section">
    <h4>Comparing Two Approaches Theoretically Using Order of Growth Expressions</h4>
    <p>To compare the efficiency of two algorithms theoretically, we use their order of growth expressions. Given two functions \( f(n) \) and \( g(n) \) representing the time complexities of two algorithms, we can determine which one is more efficient by analyzing the limit:</p>
    <div class="formula">lim<sub>n → ∞</sub> g(n)/f(n)</div>
</div>

<div class="section">
    <h4>Rules for Determining Efficiency</h4>
    <ul>
        <li><b>If</b> lim<sub>n → ∞</sub> g(n)/f(n) = 0:
            <ul>
                <li>f(n) grows faster than g(n).</li>
                <li>Algorithm represented by g(n) is more efficient for large n.</li>
            </ul>
        </li>
        <li><b>If</b> lim<sub>n → ∞</sub> g(n)/f(n) = ∞:
            <ul>
                <li>g(n) grows faster than f(n).</li>
                <li>Algorithm represented by f(n) is more efficient for large n.</li>
            </ul>
        </li>
        <li><b>If</b> lim<sub>n → ∞</sub> g(n)/f(n) = c where 0 &lt; c &lt; ∞:
            <ul>
                <li>Both f(n) and g(n) grow at the same rate.</li>
                <li>Both algorithms have similar efficiency for large n.</li>
            </ul>
        </li>
    </ul>
</div>

<div class="section">
    <h4>Examples with Order of Growth Expressions</h4>
    <h5>Example 1: Iterative vs. Mathematical Formula Approaches</h5>
    <p>1. <b>Iterative Approach</b>:</p>
    <div class="formula">T<sub>iterative</sub>(n) = 2n + 2</div>
    <p>2. <b>Mathematical Formula</b>:</p>
    <div class="formula">T<sub>formula</sub>(n) = 5</div>
    <p>To compare these:</p>
    <div class="formula">lim<sub>n → ∞</sub> (2n + 2) / 5 = ∞</div>
    <p>Since the limit is infinity, T<sub>iterative</sub>(n) grows faster than T<sub>formula</sub>(n). Thus, the mathematical formula approach is more efficient.</p>
</div>

<div class="section">
    <h4>Example 2: Linear vs. Quadratic Approach</h4>
    <p>1. <b>Linear Approach</b>:</p>
    <div class="formula">T<sub>linear</sub>(n) = 3n + 4</div>
    <p>2. <b>Quadratic Approach</b>:</p>
    <div class="formula">T<sub>quadratic</sub>(n) = 5n<sup>2</sup> + 3n + 2</div>
    <p>To compare these:</p>
    <div class="formula">lim<sub>n → ∞</sub> (5n<sup>2</sup> + 3n + 2) / (3n + 4) ≈ lim<sub>n → ∞</sub> (5n<sup>2</sup> / 3n) = ∞</div>
    <p>Since the limit is infinity, T<sub>quadratic</sub>(n) grows faster than T<sub>linear</sub>(n). Thus, the linear approach is more efficient.</p>
</div>

<div class="section">
    <p>By using the limit:</p>
    <div class="formula">lim<sub>n → ∞</sub> g(n)/f(n)</div>
    <p>we can determine which algorithm is more efficient for large input sizes:</p>
    <ul>
        <li>If the limit is <b>0</b>, g(n) is more efficient.</li>
        <li>If the limit is <b>∞</b>, f(n) is more efficient.</li>
        <li>If the limit is a positive constant, both have similar efficiency.</li>
    </ul>
    <p>This method allows us to compare algorithms theoretically, focusing on their asymptotic behavior and ensuring efficient and scalable solutions for large input sizes.</p>
</div>

<h3>Simplified Asymptotic Analysis</h3>

<div class="section">
    <h4>Simplified Approach Using Order of Growth</h4>
    <p>Instead of performing detailed calculations every time, we can directly determine the efficiency of algorithms by focusing on their highest-order terms and ignoring constant factors and lower-order terms. This approach simplifies the comparison using the concept of <b>asymptotic dominance</b>.</p>
</div>

<div class="section">
    <h4>Steps to Simplify Analysis</h4>
    <ul>
        <li><b>Eliminate Constants</b>: Remove constant coefficients from the expressions.</li>
        <li><b>Ignore Lower-Order Terms</b>: Focus only on the highest-order term, as it dominates the growth rate for large <i>n</i>.</li>
        <li><b>Use Universal Order of Growth</b>: Compare the simplified expressions based on their highest-order terms.</li>
    </ul>
</div>

<div class="section">
    <h4>Universal Order of Growth</h4>
    <p>Here is the commonly used hierarchy of growth rates, from smallest to largest:</p>
    <ul>
        <li><b>Constant Time</b>: \( O(1) \)</li>
        <li><b>Logarithmic Time</b>: \( O(\log n) \)</li>
        <li><b>Logarithmic Time</b>: \( O(\log (log n)) \)</li>
        <li><b>Linear Time</b>: \( O(n) \)</li>
        <li><b>Linearithmic Time</b>: \( O(n \log n) \)</li>
        <li><b>Quadratic Time</b>: \( O(n^2) \)</li>
        <li><b>Cubic Time</b>: \( O(n^3) \)</li>
        <li><b>Exponential Time</b>: \( O(2^n) \)</li>
        <li><b>Exponential Time</b>: \( O(n^n) \)</li>
        <li><b>Factorial Time</b>: \( O(n!) \)</li>
    </ul>
</div>

<div class="section">
    <h3>Examples with Simplified Analysis</h3>
    <h4>Example 1: Iterative vs. Mathematical Formula Approaches</h4>
    <p>1. <b>Iterative Approach</b>:</p>
    <div class="formula">T<sub>iterative</sub>(n) = 2n + 2</div>
    <p>Simplified: <b>O(n)</b></p>
    <p>2. <b>Mathematical Formula</b>:</p>
    <div class="formula">T<sub>formula</sub>(n) = 5</div>
    <p>Simplified: <b>O(1)</b></p>
    <p><b>Comparison</b>: O(1) (constant time) is more efficient than O(n) (linear time). Therefore, the mathematical formula approach is more efficient.</p>
</div>

<div class="section">
    <h4>Example 2: Linear vs. Quadratic Approach</h4>
    <p>1. <b>Linear Approach</b>:</p>
    <div class="formula">T<sub>linear</sub>(n) = 3n + 4</div>
    <p>Simplified: <b>O(n)</b></p>
    <p>2. <b>Quadratic Approach</b>:</p>
    <div class="formula">T<sub>quadratic</sub>(n) = 5n<sup>2</sup> + 3n + 2</div>
    <p>Simplified: <b>O(n<sup>2</sup>)</b></p>
    <p><b>Comparison</b>: O(n) (linear time) is more efficient than O(n<sup>2</sup>) (quadratic time). Therefore, the linear approach is more efficient.</p>
</div>

<div class="section">
    <p>By simplifying the analysis:</p>
    <ul>
        <li>Eliminate constant factors and ignore lower-order terms.</li>
        <li>Focus on the highest-order term to determine the growth rate.</li>
        <li>Use the <b>universal order of growth</b> to compare algorithms.</li>
    </ul>
    <p>This method provides a quick and effective way to evaluate the efficiency of algorithms, ensuring that we can make informed decisions without performing complex calculations every time.</p>
</div>

<p>We know that, how to measure efficiency of an algorithm using order of growth expression,but they don't specify whether they're referring to the best, worst, or average case.</p>
<p>To solve this problem,asymptotic notations are created to represent the efficieny of an algorithm</p>
<h3>Asymptotic Notations</h3>
<p>Asymptotic notations are mathematical tools to represent the time complexity of algorithms for asymptotic analysis.</p>
<p>There are mainly three asymptotic notations:</p>
<ol>
    <li>Big-O Notation (O-notation)</li>
    <li>Omega Notation (Ω-notation)</li>
    <li>Theta Notation (Θ-notation)</li>
</ol>
<p>We know that the efficiency of algorithm can be representd in terms of order pf growth expression, that can be any of these</p>
<img src="/images/bounds.JPG">
<p>As shown in image, the efficiency expression can have upper bound , lower bound and tightly bound expressions</p>
<p>Upper bound can be represented using Big O Notation</p>
<p>Lower bound can be represented using Big Omega Notation</p>
<p>Tightly bound can be represented using Big Theta Notation</p>

<p>Mathematically also we can prove these equations as follows.</p>

<h4>1. Big O Notation (O)</h4>
<p>Big O notation describes an upper bound on the time complexity of an algorithm. It provides the worst-case scenario of how an algorithm performs as the input size <em>n</em> grows. It gives us an asymptotic upper limit.</p>
<p><strong>Mathematical Definition:</strong><br>
<code>f(n) = O(g(n))</code><br>
if and only if there exist positive constants <em>c</em> and <em>n<sub>0</sub></em> such that for all <em>n</em> ≥ <em>n<sub>0</sub></em>:<br>
<code>0 ≤ f(n) ≤ c ⋅ g(n)</code></p>
<p>This notation says that, at some point <em>n<sub>0</sub></em> , if we multiply c with g(n), it will always greater than given function f(n), that will be the upper bound and worst case for our problem.There, the worst case complexity of f(n) will be O(g(n))</p>
<p><strong>Example:</strong><br>
Consider <code>f(n) = 3n<sup>2</sup> + 2n + 1</code>. To find the Big O notation:<br>
<code>f(n) = 3n<sup>2</sup> + 2n + 1</code><br>
<code>g(n) = n<sup>2</sup></code><br>
Let's choose <code>c = 6</code> and <code>n<sub>0</sub> = 1</code>:<br>
For <em>n</em> ≥ 1:<br>
<code>3n<sup>2</sup> + 2n + 1 ≤ 3n<sup>2</sup> + 2n<sup>2</sup> + n<sup>2</sup> = 6n<sup>2</sup></code><br>
Thus, <code>f(n) = O(n<sup>2</sup>)</code>.</p>

<h4>2. Big Omega Notation (Ω)</h4>
<p>Big Omega notation provides a lower bound on the time complexity of an algorithm. It describes the best-case scenario for the growth rate of an algorithm's running time.</p>
<p><strong>Mathematical Definition:</strong><br>
<code>f(n) = Ω(g(n))</code><br>
if and only if there exist positive constants <em>c</em> and <em>n<sub>0</sub></em> such that for all <em>n</em> ≥ <em>n<sub>0</sub></em>:<br>
<code>0 ≤ c ⋅ g(n) ≤ f(n)</code></p>
<p>This notation says that, at some point <em>n<sub>0</sub></em> , if we multiply c with g(n), it will always less than or equal to than given function f(n), that will be the lower bound and best case for our problem.There, the best case complexity of f(n) will be Ω(g(n))</p>

<p><strong>Example:</strong><br>
For <code>f(n) = 3n<sup>2</sup> + 2n + 1</code>, to find the Big Omega notation:<br>
<code>f(n) = 3n<sup>2</sup> + 2n + 1</code><br>
<code>g(n) = n<sup>2</sup></code><br>
Let's choose <code>c = 1</code> and <code>n<sub>0</sub> = 1</code>:<br>
For <em>n</em> ≥ 1:<br>
<code>3n<sup>2</sup> + 2n + 1 ≥ n<sup>2</sup></code><br>
Thus, <code>f(n) = Ω(n<sup>2</sup>)</code>.</p>

<h4>3. Big Theta Notation (Θ)</h4>
<p>Big Theta notation provides a tight bound on the time complexity of an algorithm. It describes the exact asymptotic behavior of the algorithm, meaning it is both an upper and lower bound.</p>
<p><strong>Mathematical Definition:</strong><br>
<code>f(n) = Θ(g(n))</code><br>
if and only if there exist positive constants <em>c<sub>1</sub></em>, <em>c<sub>2</sub></em>, and <em>n<sub>0</sub></em> such that for all <em>n</em> ≥ <em>n<sub>0</sub></em>:<br>
<code>0 ≤ c<sub>1</sub> ⋅ g(n) ≤ f(n) ≤ c<sub>2</sub> ⋅ g(n)</code></p>
<p>This notation says that, at some point <em>n<sub>0</sub></em> , if we multiply c1 and c2 with g(n), f(n) will be always between c1g(n) and c2g(n), that will be the lower bound and best case for our problem.There, the average case complexity of f(n) will be Θ(g(n))</p>
<p><strong>Example:</strong><br>
For <code>f(n) = 3n<sup>2</sup> + 2n + 1</code>, to find the Big Theta notation:<br>
<code>f(n) = 3n<sup>2</sup> + 2n + 1</code><br>
<code>g(n) = n<sup>2</sup></code><br>
Let's choose <code>c<sub>1</sub> = 1</code>, <code>c<sub>2</sub> = 6</code>, and <code>n<sub>0</sub> = 1</code>:<br>
For <em>n</em> ≥ 1:<br>
<code>n<sup>2</sup> ≤ 3n<sup>2</sup> + 2n + 1 ≤ 6n<sup>2</sup></code><br>
Thus, <code>f(n) = Θ(n<sup>2</sup>)</code>.</p>

<h4>Summary</h4>
<ul>
    <li><strong>Big O (O):</strong> Provides an upper bound. <code>f(n) = O(g(n))</code> means <code>f(n)</code> grows no faster than <code>g(n)</code>.</li>
    <li><strong>Big Omega (Ω):</strong> Provides a lower bound. <code>f(n) = Ω(g(n))</code> means <code>f(n)</code> grows at least as fast as <code>g(n)</code>.</li>
    <li><strong>Big Theta (Θ):</strong> Provides a tight bound. <code>f(n) = Θ(g(n))</code> means <code>f(n)</code> grows exactly as fast as <code>g(n)</code>.</li>
</ul>
<p>These notations help in understanding and comparing the efficiency of different algorithms, especially for large input sizes.</p>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ14rgfDct8iJa9IAfkPNHU5WENAr7AEvWizQ&s">

<p>Eventhough , we have best case , worst case and average case, we used to mesure performance of an algorithm using worst case only.</p>

<h3>Analysis of Common Programs</h3>
<h4>1. Linear Search</h4>
    <p>A linear search algorithm that finds an element in a list by checking each element one by one has a time complexity of O(n).</p>
    <code>
        def linear_search(arr, target):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;for i in range(len(arr)):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if arr[i] == target:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return i<br>
        &nbsp;&nbsp;&nbsp;&nbsp;return -1<br><br>
        # Example usage<br>
        arr = [2, 4, 6, 8, 10]<br>
        target = 8<br>
        print(linear_search(arr, target))  # Output: 3
    </code>

<h4>Time Complexity Calculation</h4>
<p>The <code>for</code> loop iterates through each element of the list <code>arr</code>. In the worst case, it will go through all <code>n</code> elements where <code>n</code> is the length of <code>arr</code> if the target is not found. Hence, the time complexity is O(n).</p>

<h4>2. Finding the Maximum Element in a List</h4>
<p>Finding the maximum element in a list by iterating through each element has a time complexity of O(n).</p>
<code>
    def find_max(arr):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;max_value = arr[0]<br>
    &nbsp;&nbsp;&nbsp;&nbsp;for num in arr:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if num > max_value:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_value = num<br>
    &nbsp;&nbsp;&nbsp;&nbsp;return max_value<br><br>
    # Example usage<br>
    arr = [3, 5, 7, 2, 8, 10]<br>
    print(find_max(arr))  # Output: 10
</code>

<h4>Time Complexity Calculation</h4>
<p>The <code>for</code> loop iterates through each element of the list <code>arr</code>. It compares each element to the current <code>max_value</code>. Since it processes each element once, the time complexity is O(n).</p>

 <h4>1. Finding Duplicate Elements</h4>
    <p>This example finds duplicate elements in a list by comparing each element with every other element. The time complexity is O(n^2).</p>
    <code>
        def find_duplicates(arr):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;duplicates = []<br>
        &nbsp;&nbsp;&nbsp;&nbsp;n = len(arr)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;for i in range(n):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for j in range(i + 1, n):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if arr[i] == arr[j]:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duplicates.append(arr[i])<br>
        &nbsp;&nbsp;&nbsp;&nbsp;return duplicates<br><br>
        # Example usage<br>
        arr = [1, 2, 3, 1, 4, 2]<br>
        print(find_duplicates(arr))  # Output: [1, 2]
    </code>

<h4>Time Complexity Calculation</h4>
<p>The outer <code>for</code> loop runs <code>n</code> times. The inner <code>for</code> loop runs <code>n-i-1</code> times for each iteration of the outer loop. In the worst case, the total number of comparisons is proportional to the sum of the first <code>n</code> natural numbers, which is \( \frac{n(n-1)}{2} \). Therefore, the time complexity is O(n^2).</p>

<h4>2. Generating Pairs of Elements</h4>
<p>This example generates pairs of elements from a list. The time complexity is O(n^2).</p>
<code>
    def generate_pairs(arr):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;pairs = []<br>
    &nbsp;&nbsp;&nbsp;&nbsp;n = len(arr)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;for i in range(n):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for j in range(n):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pairs.append((arr[i], arr[j]))<br>
    &nbsp;&nbsp;&nbsp;&nbsp;return pairs<br><br>
    # Example usage<br>
    arr = [1, 2, 3]<br>
    print(generate_pairs(arr))  # Output: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
</code>

<h4>Time Complexity Calculation</h4>
<p>The outer <code>for</code> loop runs <code>n</code> times. The inner <code>for</code> loop also runs <code>n</code> times for each iteration of the outer loop. In the worst case, the total number of operations is \( n \times n = n^2 \). Therefore, the time complexity is O(n^2).</p>

<h4>1. Counting the Number of Divisions by 2</h4>
    <p>This example repeatedly divides a number by 2 until it becomes 1, and counts the number of divisions. The time complexity is O(log n).</p>
    <code>
        def count_divisions_by_2(n):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;count = 0<br>
        &nbsp;&nbsp;&nbsp;&nbsp;while n > 1:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n //= 2<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count += 1<br>
        &nbsp;&nbsp;&nbsp;&nbsp;return count<br><br>
        # Example usage<br>
        n = 16<br>
        print(count_divisions_by_2(n))  # Output: 4
    </code>

<h4>Time Complexity Calculation</h4>
<p>Each iteration of the <code>while</code> loop divides <code>n</code> by 2, reducing the size of <code>n</code> by a factor of 2. Therefore, the time complexity is O(log n).</p>

<h4>2. Binary Search for a Specific Value</h4>
<p>Binary search is an efficient algorithm for finding an item from a sorted list of items by repeatedly dividing the search interval in half. The time complexity is O(log n).</p>
<code>
    def binary_search(arr, target):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;left, right = 0, len(arr) - 1<br>
    &nbsp;&nbsp;&nbsp;&nbsp;while left <= right:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mid = (left + right) // 2<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if arr[mid] == target:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return mid<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif arr[mid] < target:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;left = mid + 1<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;right = mid - 1<br>
    &nbsp;&nbsp;&nbsp;&nbsp;return -1<br><br>
    # Example usage<br>
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br>
    target = 7<br>
    print(binary_search(arr, target))  # Output: 6
</code>

<h4>Time Complexity Calculation</h4>
<p>Each iteration of the <code>while</code> loop reduces the search interval by half. Therefore, the time complexity is O(log n).</p>

<h4>Exponential Growth Function</h4>
    <p>This example repeatedly raises a number to a given power until it exceeds a certain value and prints the intermediate results. The time complexity is O(log log n).</p>
    <code>
        def exponentfun(n, c):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;result = 2<br>
        &nbsp;&nbsp;&nbsp;&nbsp;while result &lt; n:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(result)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result = result ** c<br><br>
        # Example usage<br>
        base = 2<br>
        exponent = 32<br>
        exponentfun(exponent, base)  # Output: 2, 4, 16
    </code>

<h4>Time Complexity Calculation</h4>
<p>Each iteration of the <code>while</code> loop raises <code>result</code> to the power of <code>c</code>, exponentially increasing the value of <code>result</code>. Therefore, the number of iterations is proportional to log(log(n)). Thus, the time complexity is O(log log n).</p>


<h2>Space Complexity in Python</h2>

<p>Space complexity refers to the amount of memory space required by an algorithm during its execution. It includes both auxiliary space used by the algorithm itself and space used by the input.</p>

<h3>How Space Complexity is Calculated</h3>

<p>Space complexity is typically categorized into:</p>
<ul>
    <li><strong>Auxiliary Space Complexity:</strong> Extra space used by the algorithm, apart from input space.</li>
    <li><strong>Input Space Complexity:</strong> Space required to store input data that the algorithm processes.</li>
</ul>

<h3>Examples of Space Complexity in Python</h3>

<h4>Example 1: Constant Space Complexity (O(1))</h4>
<code>
    def constant_space(n):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;a = 1<br>
    &nbsp;&nbsp;&nbsp;&nbsp;b = 2<br>
    &nbsp;&nbsp;&nbsp;&nbsp;c = 3<br>
    &nbsp;&nbsp;&nbsp;&nbsp;return a + b + c<br><br>
    # Example usage<br>
    result = constant_space(5)<br>
    print(result)  # Output: 6
</code>

<p><strong>Explanation:</strong> The <code>constant_space</code> function allocates a fixed amount of memory for three integer variables (<code>a</code>, <code>b</code>, <code>c</code>), regardless of the input <code>n</code>. Thus, its space complexity is O(1) or constant space.</p>

<h4>Example 2: Linear Space Complexity (O(n))</h4>
<code>
    def linear_space(n):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;arr = [0] * n<br>
    &nbsp;&nbsp;&nbsp;&nbsp;for i in range(n):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arr[i] = i<br>
    &nbsp;&nbsp;&nbsp;&nbsp;return arr<br><br>
    # Example usage<br>
    result = linear_space(5)<br>
    print(result)  # Output: [0, 1, 2, 3, 4]
</code>

<p><strong>Explanation:</strong> The <code>linear_space</code> function creates a list <code>arr</code> of size <code>n</code>. As <code>n</code> increases, the space required by the list linearly increases. Therefore, its space complexity is O(n).</p>

<h2>More Examples On Finding Time Complexity</h2>

```python
n=int(input())
for i in range(1,n+1):
    print(i)
```

<p>In the Above example, loop will run for maximum of n times, i,e 1 to n</p>
<p>Time Complexity : O(n)</p>

```python
n=int(input())
for i in range(n,0,-1):
    print(i)
```

<p>In the Above example, loop will run for maximum of n times, i,e n to 1</p>
<p>Time Complexity : O(n)</p>

```python
n=int(input())
for i in range(1,n+1,2):
    print(i)
```

<p>Here, i is incremented by 2, if n=6, then i=1,3,5 so it will loop for 3 times, that is n/2</p>
<p>In the Above example, loop will run for maximum of n/2 times since step value is 2, i,e 1,3,5,..n</p>
<p>Time Complexity : O(n/2) -> O(n)</p>

```python
n=int(input())
for i in range(1,n+1,5):
    print(i)
```

<p>Here, i is incremented by 5, if n=20, then i=1,6,11,16 so it will loop for 4 times, that is n/5</p>
<p>In the Above example, loop will run for maximum of n/2 times since step value is 2, i,e 0,2,4,6,..n</p>
<p>Time Complexity : O(n/5) -> O(n)</p>

<p>So, for any value of step, Time Complexity Will Be : o(n)</p>

```python
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,j)
```

<p>In this case, loop-1 will loops for n times</p>
<p>Then, For each iteration of loop 1 , loop 2 will run for n times</p>
<p>So, total iterations for loop-2 will be, n*n</p>
<p>So, Time Complexity Will Be O(n+n*n) -> O(n*n)</p>

```python
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,j)
```
<p>loop1 : loop2</p>
<p> 1    : 1</p>
<p> 2    : 1,2</p>
<p> 3    : 1,2,3</p>
<p> 4    : 1,2,3,4</p>
<p> 5    : 1,2,3,4,5</p>
<p>------------------</p>
<p> 5    : 15</p>
<p> n    : n(n+1)//2</p>
<p>In this case, loop-1 will loops for n times</p>
<p>Then, For each iteration of loop 1 , loop 2 will run for i times</p>
<p>So, total iterations for loop-2 will be, n(n+1)/2</p>
<p>So, Time Complexity Will Be O(n/2+n*n/2) -> O(n*n/2) -> o(n*n)</p>


```python
n=int(input())
p=0
i=1
while p<=n:
    p=p+i
    i++
print(p)
```
<p>i : p</p>
<p>1 : 0+1=1</p>
<p>2 : 1+2=3</p>
<p>3 : 1+2+3</p>
<p>4 : 1+2+3+4</p>
<p>5 : 1+2+3+4+5</p>
<p>k : 1+2+3+4+5+..+k</p>

<p>Loop will end when p>n</p>

```python
p>n
k(k+1)/2 > n
k*2/2+k/2 > n
k*2 > n
k >  √n
```
<p> So, loop will end when i value greater than  √n</p>
<p>Time Complexity = O(√n)</p>

```python
n=int(input())
i=1
while i<n:
    i=i*2
```

```python
i
--
1
1*2=2
2*2=2**2
(2**2)*2 = 2**3
(2**3)*2 = 2**4
..
..
2**k
```
<p>This loop will end when only when i>=n</p>

```python
i>=n
2**k >= n
2**k=n
k=log2n
```

<p>So, loop will end when, i reaches log<sub>2</sub>n</p>
<p>Time Complexity : O(log<sub>2</sub>n)</p>

```python
n=int(input())
i=1
while i<n:
    i=i*3
```

```python
i
--
1
1*3=3
3*3=3**3
(3**3)*3 = 3**3
(3**3)*3 = 3**4
..
..
3**k
```
<p>This loop will end when only when i>=n</p>

```python
i>=n
3**k >= n
3**k=n
k=log3n
```

<p>So, loop will end when, i reaches log<sub>3</sub>n</p>
<p>Time Complexity : O(log<sub>3</sub>n)</p>


```python
n=int(input())
i=n
while i>=1:
    i=i//2
```

```python
i
--
n
n/2=n/2
n/2/2=n/2**2
n/2**2/2 = n/2**3
(n/2**3)/2 = n/2**4
..
..
n/2**k
```
<p>This loop will end when only when i>=n</p>

```python
i>=1
n/2**k >= 1
n/2**k=1
n=2**k
k=log2n
```

<p>So, loop will end when, i reaches log<sub>2</sub>n</p>
<p>Time Complexity : O(log<sub>2</sub>n)</p>

```python
n=int(input())
i=0
while (i*i)<n:
    i+=1
```

```python
i
--
0
1*1
2*2
3*3
...
...
k*k
```
<p>This loop will end when only when (i*i)>=n</p>

```python
k*k>=n
K*2=n
k= √n
```

<p>So, loop will end when, i reaches √n</p>
<p>Time Complexity : O(√n)</p>


```python
n=int(input())
p=0
i=1
while i<n:
    i=i*2
    p+=1

j=1
while j<p:
    j=j*2
```

<p>We know that first loop will take log<sub>2</sub>n times</p>
<p>So, p will be incremented by log<sub>2</sub>n, p=log<sub>2</sub>n</p>
<p>second loop will run for, log<sub>2</sub>p</p>
<p>so, second loop will run for log<sub>2</sub>(log<sub>2</sub>n)</p>

<p>Final Complexity Will be : o(log(logn))</p>

```python
n=int(input())
for i in range(1,n+1):
    j=0
    while j<n:
        j=j*2
```

<p>We know that inner loop for run for every iteration of outer loop that is n times</p>
<p>Inner loop will take time log<sub>2</sub>n</p>
<p>So , Total Complexity Will Be : o(n*log<sub>2</sub>n)</p>


```python
for(i=0;i<n;i++) -> O(n)
for(i=0;i<n;i=i+2) -> O(n/2) -> O(n)
for(i=0;i<n;i=i+3) -> O(n/3) -> O(n)
for(i=n;i>0;i--) ->O(n)
for(i=0;i<n;i=i*2) -> O(logn)
for(i=0;i<n;i=i*3) -> O(logn)
for(i=n;i>1;i=i/2) -> O(logn)
```