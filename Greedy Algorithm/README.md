<h1>Greedy Algorithm</h1>
<p><strong>What is a Greedy Algorithm?</strong></p>
<p>A <strong>Greedy Algorithm</strong> is a method used to solve problems by making the best choice available at each step without reconsidering previous choices. The aim is to find an overall solution that is good enough, or sometimes even optimal, by building it piece by piece based on immediate benefits.</p>

<p><strong>Key Characteristics in Simple Words:</strong></p>
<ul>
    <li><strong>Locally Best Choice</strong>: At each step, pick the option that looks the best at that moment.</li>
    <li><strong>No Going Back</strong>: Once a choice is made, it’s final.</li>
    <li><strong>Step-by-Step Solution</strong>: The solution is built gradually, step by step.</li>
</ul>

<p><strong>Real-Time Examples:</strong></p>

<p><strong>1. Coin Change Problem:</strong></p>
<p><strong>Scenario:</strong> Suppose you're at a vending machine and need to make 87 cents in change using the fewest coins possible. The available coins are 50 cents, 25 cents, 10 cents, 5 cents, and 1 cent.</p>
<p><strong>Greedy Approach:</strong></p>
<ol>
    <li>Start with the highest coin value that is less than or equal to 87 cents, which is 50 cents.</li>
    <li>Subtract 50 from 87, leaving 37 cents.</li>
    <li>Next, use a 25-cent coin, leaving 12 cents.</li>
    <li>Use a 10-cent coin, leaving 2 cents.</li>
    <li>Finally, use two 1-cent coins to make the total.</li>
</ol>
<p><strong>Result:</strong> You used 5 coins: one 50-cent, one 25-cent, one 10-cent, and two 1-cent coins.</p>

<p><strong>2. Activity Selection Problem:</strong></p>
<p><strong>Scenario:</strong> Imagine you're organizing a conference and have multiple talks to schedule. Each talk has a specific start and end time, and you want to fit as many non-overlapping talks as possible into a single room.</p>
<p><strong>Greedy Approach:</strong></p>
<ol>
    <li>Sort the talks by their end times.</li>
    <li>Start with the talk that ends the earliest.</li>
    <li>Add the next talk that starts after the current one ends.</li>
    <li>Repeat until you can't add more talks.</li>
</ol>
<p><strong>Result:</strong> You’ll have the maximum number of talks scheduled without any overlap.</p>

<p><strong>3. Huffman Coding for Data Compression:</strong></p>
<p><strong>Scenario:</strong> Consider you’re compressing text data where some characters appear more frequently than others.</p>
<p><strong>Greedy Approach:</strong></p>
<ol>
    <li>Count the frequency of each character in the text.</li>
    <li>Create a binary tree by repeatedly merging the two least frequent characters until only one tree remains.</li>
    <li>Assign shorter codes to more frequent characters and longer codes to less frequent characters.</li>
</ol>
<p><strong>Result:</strong> The text is compressed efficiently, reducing the amount of data storage required.</p>

<p><strong>Advantages:</strong></p>
<ul>
    <li><strong>Simplicity</strong>: Easy to implement and understand.</li>
    <li><strong>Speed</strong>: Often faster than other approaches since it doesn’t require exploring all possibilities.</li>
    <li><strong>Efficiency</strong>: Works well when the problem allows for a greedy approach to lead to an optimal solution.</li>
</ul>

<p><strong>Disadvantages:</strong></p>
<ul>
    <li><strong>Not Always Optimal</strong>: Sometimes, the greedy choice doesn’t lead to the best overall solution. For example, in the <strong>Knapsack Problem</strong>, where you must choose items with maximum total value without exceeding a weight limit, a greedy algorithm may not always pick the best combination of items.</li>
    <li><strong>Short-Sighted</strong>: Focuses on immediate benefits, potentially missing a better long-term solution.</li>
</ul>

<p><strong>Applications:</strong></p>
<ul>
    <li><strong>Network Routing</strong>: Used in algorithms like Dijkstra’s to find the shortest path between nodes in a graph.</li>
    <li><strong>Scheduling</strong>: Selecting jobs or activities that maximize profit or minimize time, such as in job scheduling.</li>
    <li><strong>Data Compression</strong>: Huffman coding is a classic example where greedy algorithms are used for efficient data compression.</li>
    <li><strong>Resource Allocation</strong>: Allocating limited resources, such as bandwidth or storage, to maximize efficiency or profit.</li>
</ul>

<br>
<br>

<h1>Assign Cookies</h1>
<p><strong>Problem Statement:</strong></p>
<p>You are given two arrays: 
<ul>
    <li><strong>g[i]</strong> represents the greed factor of the ith child.</li>
    <li><strong>s[j]</strong> represents the size of the jth cookie.</li>
</ul>
You want to assign each child at most one cookie such that the maximum number of children are content. A child will be content if the size of the cookie is greater than or equal to the child's greed factor. Your goal is to maximize the number of content children and return that number.</p>

<p><strong>Sample Test Cases:</strong></p>

<p><strong>Test Case 1:</strong></p>
<p><strong>Input:</strong> g = [1, 2, 3], s = [1, 1]</p>
<p><strong>Output:</strong> 1</p>
<p><strong>Explanation:</strong> You have 3 children with greed factors 1, 2, and 3, and 2 cookies of size 1. Only the child with greed factor 1 can be content with a cookie, so the output is 1.</p>

<p><strong>Test Case 2:</strong></p>
<p><strong>Input:</strong> g = [1, 2], s = [1, 2, 3]</p>
<p><strong>Output:</strong> 2</p>
<p><strong>Explanation:</strong> You have 2 children with greed factors 1 and 2, and 3 cookies of sizes 1, 2, and 3. Both children can be content with the cookies, so the output is 2.</p>

<p><strong>Test Case 3:</strong></p>
<p><strong>Input:</strong> g = [1, 2, 3], s = [3]</p>
<p><strong>Output:</strong> 1</p>
<p><strong>Explanation:</strong> Only one child can be content with the only available cookie.</p>

<p><strong>Test Case 4:</strong></p>
<p><strong>Input:</strong> g = [4, 5, 6], s = [1, 2, 3]</p>
<p><strong>Output:</strong> 0</p>
<p><strong>Explanation:</strong> None of the children can be content since all available cookies are smaller than the greed factors.</p>

<p><strong>Test Case 5:</strong></p>
<p><strong>Input:</strong> g = [2, 2, 3], s = [1, 2, 3]</p>
<p><strong>Output:</strong> 2</p>
<p><strong>Explanation:</strong> Two of the three children can be content with the available cookies.</p>

<p><strong>Approach:</strong></p>
<p>The problem can be solved using a Greedy Algorithm. The idea is to sort both arrays and try to satisfy the children starting from the one with the smallest greed factor.</p>

<p><strong>Intuition in Detail:</strong></p>
<ul>
    <li><strong>Greedy Approach:</strong> The greedy choice in this problem is to assign the smallest available cookie that can satisfy the child's greed. This way, larger cookies are saved for children with higher greed factors.</li>
    <li><strong>Sorting:</strong> 
        <ul>
            <li>Sort the <strong>g</strong> array in non-decreasing order, so we can start with the child with the smallest greed factor.</li>
            <li>Sort the <strong>s</strong> array in non-decreasing order, so we can try to match the smallest available cookie first.</li>
        </ul>
    </li>
    <li><strong>Two-Pointer Technique:</strong> 
        <ul>
            <li>Use two pointers, one for the <strong>g</strong> array (children) and one for the <strong>s</strong> array (cookies).</li>
            <li>If the current cookie can satisfy the current child (i.e., <strong>s[right] >= g[left]</strong>), then move both pointers forward (child is satisfied).</li>
            <li>If the current cookie cannot satisfy the child, move only the cookie pointer forward to try the next larger cookie.</li>
        </ul>
    </li>
    <li><strong>End Condition:</strong> The process continues until we have either satisfied all children we can or run out of cookies.</li>
</ul>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Sort both <strong>g</strong> and <strong>s</strong> arrays.</li>
    <li>Initialize two pointers: <strong>left</strong> (starting from 0 for the children) and <strong>right</strong> (starting from 0 for the cookies).</li>
    <li>Traverse through both arrays using the two pointers.</li>
    <li>For each child, check if the current cookie can satisfy them. If yes, move both pointers. If not, move only the cookie pointer.</li>
    <li>Count how many children are satisfied and return that count.</li>
</ol>

<p><strong>Code:</strong></p>
<pre><code>
def solve(n, child, m, cookies):
    if n == 0:
        return 0
    child.sort()
    cookies.sort()
    print(child, cookies)
    left, right = 0, 0
    while left < n and right < m:
        if child[left] <= cookies[right]:
            left += 1
        right += 1
    return left

# Example Usage:
g = [1, 2, 3]
s = [1, 1]
print(solve(len(g), g, len(s), s))  # Output: 1

g = [1, 2]
s = [1, 2, 3]
print(solve(len(g), g, len(s), s))  # Output: 2
</code></pre>

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> The time complexity is <strong>O(n log n + m log m)</strong>, where <strong>n</strong> is the number of children and <strong>m</strong> is the number of cookies. This comes from the need to sort both arrays.</li>
    <li><strong>Space Complexity:</strong> The space complexity is <strong>O(1)</strong> because no additional space is used beyond a few variables, and the sorting is done in-place.</li>
</ul>

<p><strong>How We Found the Problem Can Be Solved Using a Greedy Approach:</strong></p>

<p><strong>The Problem:</strong></p>
<p>You have some children and some cookies. Each child has a minimum size of cookie they need to be happy. Your goal is to make as many children happy as possible by giving them one cookie each.</p>

<p><strong>Why Greedy Works:</strong></p>

<ul>
    <li><strong>Simple Choice:</strong> The greedy approach means you make the best choice at each step. Here, you always give the smallest cookie that can still make a child happy. This way, you use up cookies efficiently and keep larger cookies available for children with bigger needs.</li>
    <li><strong>Step-by-Step:</strong> If you start by giving the smallest cookie to the least demanding child, you ensure that the larger cookies are left for children who need more. This step-by-step approach fits well because it directly helps in maximizing the number of happy children.</li>
    <li><strong>Proven Success:</strong>
        <ul>
            <li><strong>Matching Strategy:</strong> If you give a large cookie to a child who would be satisfied with a smaller one, you might waste the large cookie that could have satisfied a greedier child. By always choosing the smallest suitable cookie, you ensure better use of resources.</li>
            <li><strong>Testing and Examples:</strong> Testing shows that this greedy method consistently gives the best results, making the maximum number of children happy.</li>
        </ul>
    </li>
</ul>

<p><strong>Summary:</strong></p>
<p>The greedy approach works for this problem because it ensures that you are using your cookies in the most efficient way possible. By always choosing the smallest cookie that meets a child's needs, you reserve larger cookies for children with bigger needs and make the most children happy.</p>



<br>
<br>


<h1>Fractional Knapsack</h1>
<p><strong>Fractional Knapsack Problem</strong></p>

<p><strong>Problem Statement:</strong></p>
<p>You are given <code>n</code> items, each with a <code>cost</code> and <code>weight</code>, and a knapsack with a maximum weight capacity. The goal is to maximize the total value of the knapsack by selecting items and potentially taking fractions of items. Unlike the 0/1 knapsack problem, you can take any fraction of an item.</p>

<p><strong>Sample Test Cases:</strong></p>

<ul>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> <code>cost = [60, 100, 120]</code>, <code>weight = [10, 20, 30]</code>, <code>capacity = 50</code></li>
            <li><strong>Output:</strong> <code>240.0</code></li>
            <li><strong>Explanation:</strong> Take all of the second item and two-thirds of the third item to maximize the value.</li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> <code>cost = [500, 300, 200]</code>, <code>weight = [30, 20, 10]</code>, <code>capacity = 50</code></li>
            <li><strong>Output:</strong> <code>800.0</code></li>
            <li><strong>Explanation:</strong> Take all of the first item and all of the second item to maximize the value.</li>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> <code>cost = [60, 100, 120]</code>, <code>weight = [10, 20, 30]</code>, <code>capacity = 10</code></li>
            <li><strong>Output:</strong> <code>60.0</code></li>
            <li><strong>Explanation:</strong> Only the first item can be taken completely.</li>
        </ul>
    </li>
    <li><strong>Test Case 4:</strong>
        <ul>
            <li><strong>Input:</strong> <code>cost = [10, 20, 30]</code>, <code>weight = [10, 20, 30]</code>, <code>capacity = 15</code></li>
            <li><strong>Output:</strong> <code>35.0</code></li>
            <li><strong>Explanation:</strong> Take half of the second item and the whole first item.</li>
        </ul>
    </li>
    <li><strong>Test Case 5:</strong>
        <ul>
            <li><strong>Input:</strong> <code>cost = [10, 20, 30]</code>, <code>weight = [10, 20, 30]</code>, <code>capacity = 0</code></li>
            <li><strong>Output:</strong> <code>0.0</code></li>
            <li><strong>Explanation:</strong> No capacity in the knapsack, so no value can be obtained.</li>
        </ul>
    </li>
</ul>

<p><strong>Approach:</strong></p>

<ul>
    <li><strong>Calculate Value-to-Weight Ratio:</strong> For each item, calculate the ratio of its value to weight. This helps determine how valuable each item is per unit of weight.</li>
    <li><strong>Sort Items:</strong> Sort the items based on their value-to-weight ratio in descending order. This ensures that the most valuable items are considered first.</li>
    <li><strong>Greedy Selection:</strong> Iterate through the sorted list and add as much of each item as possible to the knapsack. If an item cannot be fully added due to capacity constraints, take the fraction of it that fits.</li>
    <li><strong>Stop When Capacity is Zero:</strong> Once the knapsack is full, stop the process.</li>
</ul>

<p><strong>Intuition in Detail:</strong></p>

<ul>
    <li><strong>Best Immediate Choice:</strong> By always selecting the item with the highest value-to-weight ratio, you maximize the value added to the knapsack with each step. This approach works because taking fractions of items allows you to utilize the capacity of the knapsack optimally.</li>
    <li><strong>Efficiency:</strong> Sorting the items based on their value-to-weight ratio and then processing them ensures that you are making the best possible use of the knapsack’s capacity. This method provides an efficient way to solve the problem without needing to check all possible combinations.</li>
</ul>

<p><strong>Steps to Solve:</strong></p>

<ul>
    <li><strong>Combine Cost and Weight:</strong> Create a list of items where each item is represented by its cost and weight.</li>
    <li><strong>Sort Items:</strong> Sort the items in descending order based on their value-to-weight ratio.</li>
    <li><strong>Iterate and Add:</strong> Traverse through the sorted items and add as much of each item to the knapsack as possible. If an item’s weight exceeds the remaining capacity, add only a fraction of it.</li>
    <li><strong>Calculate Total Value:</strong> Keep track of the total value added to the knapsack and return it once the capacity is reached.</li>
</ul>

<p><strong>Code:</strong></p>

```python
def solve(n, cost, weight, capacity):
    if n == 0:
        return 0
    
    # Combine cost and weight into a list of tuples
    items = list(zip(cost, weight))
    
    # Sort items based on the value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0  # To keep track of the total value
    
    for item_cost, item_weight in items:
        if item_weight &lt;= capacity:
            # If the entire item can fit into the knapsack
            total_value += item_cost
            capacity -= item_weight
        else:
            # If only a fraction of the item can fit into the knapsack
            unit_value = item_cost / item_weight
            total_value += (capacity * unit_value)
            capacity = 0  # Knapsack is full
        
        if capacity == 0:
            break
    
    return total_value

# Example Usage:
print(solve(3, [60, 100, 120], [10, 20, 30], 50))  # Output: 240.0</code></pre>

```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> 
        Sorting the items takes <code>O(n \log n)</code>. The iteration through the items is <code>O(n)</code>. Thus, the total time complexity is <code>O(n \log n)</code>.
    </li>
    <li><strong>Space Complexity:</strong> 
        The space complexity is <code>O(n)</code> due to the storage of the items and additional variables used.
    </li>
</ul>

<p><strong>How We Found the Problem Can Be Solved Using a Greedy Approach:</strong></p>
<ul>
    <li><strong>Optimal Substructure:</strong> 
        The problem can be broken down into smaller subproblems where each subproblem involves making the best choice of how to fill the knapsack. Greedy choices at each step lead to an overall optimal solution.
    </li>
    <li><strong>Proof of Greedy Choice:</strong> 
        By sorting items based on their value-to-weight ratio, we ensure that the most valuable items are considered first, which maximizes the value of the knapsack. Any deviation from this approach would lead to suboptimal results.
    </li>
    <li><strong>Efficiency:</strong> 
        The greedy algorithm provides an efficient solution by sorting and then iterating, ensuring that the problem is solved in a time-effective manner.
    </li>
</ul>


<br>
<br>

<h1></h1>