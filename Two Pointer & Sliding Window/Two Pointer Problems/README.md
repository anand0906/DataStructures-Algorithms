<h1>Container With Most Water</h1>
<p><strong>Problem Statement</strong></p>
<p>Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i are at (i, ai) and (i, 0). Find two lines, which together with the x-axis form a container, such that the container contains the most water.</p>
<p><strong>Examples : </strong></p>
<p><strong>Input</strong> : [1, 8, 6, 2, 5, 4, 8, 3, 7]  </p>
<p><strong>Output</strong> : 49 </p>
<p><strong>Explanation</strong> The vertical lines at positions 1 and 8 form the container with the maximum area (7 units wide and height of min(8, 7) = 7 units). </p>
<br>
<p><strong>Input</strong> : [6, 5, 4, 3, 2, 1]  </p>
<p><strong>Output</strong> : 6 </p>
<p><strong>Explanation</strong>  The first and last lines form the container with the maximum area. </p>
<br>
<p><strong>Input</strong> : [10000, 1, 1, 1, 10000]  </p>
<p><strong>Output</strong> : 40000 </p>
<p><strong>Explanation</strong>  The first and last lines form the container with the maximum area. </p>
<br>
<p><strong>Input</strong> : [3, 3, 3, 3, 3]  </p>
<p><strong>Output</strong> : 12 </p>
<p><strong>Explanation</strong>  The first and last lines form the container with the maximum area. </p>
<br>
<p><strong>Solution</strong></p>
<p>This problem can be solved several approaches</p>
<p><strong>BruteForce Approach : </strong></p>
<p>In this approach, we will find out all possible unique pairs in given array. Then we will calculate the area for each combination.Out of all we will get the maximum array as our answer</p>
<p>Steps To Follow</p>
<ul>
	<li>largest: This variable keeps track of the largest area found so far. It is initialized to 0.</li>
	<li>The outer loop runs from 0 to n-1, where n is the number of elements in the array arr</li>
	<ul>
		<li>The inner loop runs from i+1 to n, ensuring that we only consider pairs (i, j) where i < j.</li>
		<ul>
			<li>For each combination of i and j, we will find width and height</li>
			<li>width: The distance between the two lines at positions i and j, which is j - i.</li>
			<li>height: The height of the container, determined by the shorter of the two lines, which is min(arr[i], arr[j]).</li>
			<li>calculate area , The area of the container formed by the lines at i and j, calculated as width * height.</li>
			<li>largest: Update this variable if the current area is greater than the largest area found so far.</li>
		</ul>
	</ul>
	<li>After all pairs have been checked, the function returns the largest area found.</li>
</ul>

```python
def bruteForce(n, arr):
    largest = 0
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            height = min(arr[i], arr[j])
            area = width * height
            largest = max(largest, area)
    return largest

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```

<p><strong>Time Complexity</strong>: O(n**2)</p>
<p>This is because it checks all possible pairs of lines.</p>
<p><strong>Space Complexity</strong>: O(1)</p>
<p>This approach is not taking any extra space</p>
<br>
<p><strong>Optimized Approach</strong></p>
<p>Here we can observer that the area is determined by the shorter of two lines and the width between them.</p>
<p>By considering width atmost from begginning, we can find out max area for each line by using two pointer approach</p>
<ul>
	<li>Initialize two pointers, one at the beginning (left) and one at the end (right) of the list.</li>
	<li>Calculate the area formed by the lines at these two pointers.</li>
	<li>Move the pointer pointing to the shorter line inward, as this might lead to a larger area by potentially increasing the height.Since we have found max area formed for shorter line as width is maximum.</li>
</ul>
<p>Steps To Follow</p>
<ol>
	<li><strong>Initialization:</strong></li>
	<ul>
		<li>left: Pointer starting at the beginning of the list.</li>
		<li>right: Pointer starting at the end of the list.</li>
		<li>largest: Variable to keep track of the largest area found, initialized to 0.</li>
	</ul>
	<li><strong>While Loop</strong></li>
	<ul>
		<li>The loop runs as long as left is less than right</li>
		<ul>
			<li><strong>Calculate Area Between Left and right</strong></li>
			<ul>
				<li>width: The distance between the two pointers, calculated as right - left.</li>
				<li>height: The height of the container, determined by the shorter of the two lines, which is min(arr[left], arr[right]).</li>
				<li>area: The area of the container formed by the lines at left and right, calculated as width * height</li>
				<li>largest: Update this variable if the current area is greater than the largest area found so far.</li>
			</ul>
			<li><strong>Move Pointers</strong></li>
			<ul>
				<li>If the height at left is less than the height at right, increment the left pointer to potentially find a taller line.That means, we have found max area possible with left pointer</li>
				<li>Otherwise, decrement the right pointer.</li>
			</ul>
		</ul>
	</ul>
	<li>After the loop terminates, the function returns the largest area found.</li>
</ol>

```python
def optimized(n, arr):
    left, right = 0, n - 1
    largest = 0
    
    while left < right:
        width = right - left
        height = min(arr[left], arr[right])
        area = width * height
        largest = max(largest, area)
        
        # Move the pointer pointing to the shorter line inward
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return largest

arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```

<p><strong>Time Complexity</strong> : O(n)</p>
<p>Each element is visited at most once, making it much more efficient than the brute force approach.</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p>We are not using any extra space</p>

