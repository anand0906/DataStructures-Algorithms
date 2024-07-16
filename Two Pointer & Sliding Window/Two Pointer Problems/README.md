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


<h1>Trapping Rain Water</h1>
<p>Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.</p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png">
<p><strong>Examples</strong></p>
<p><strong>Input</strong> : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  </p>
<p><strong>Output</strong> : 6 </p>
<p><strong>Explanation</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. </p>
<br>
<p><strong>Input</strong> : [4, 2, 0, 3, 2, 5]  </p>
<p><strong>Output</strong> : 9 </p>
<p><strong>Explanation</strong> The elevation map can trap 9 units of water. </p>
<br>
<p><strong>Input</strong> : [1, 0, 2]  </p>
<p><strong>Output</strong> : 1 </p>
<p><strong>Explanation</strong> The elevation map can trap 1 unit of water. </p>
<br>
<p><strong>Input</strong> : [3, 0, 0, 2, 0, 4]  </p>
<p><strong>Output</strong> : 10 </p>
<p><strong>Explanation</strong> The elevation map can trap 10 units of water. </p>
<br>
<p><strong>Input</strong> : [0,0,0]  </p>
<p><strong>Output</strong> : 0 </p>
<p><strong>Explanation</strong> The elevation map cannot trap any water. </p>
<br>
<p><strong>Input</strong> : [1,2,3]  </p>
<p><strong>Output</strong> : 0 </p>
<p><strong>Explanation</strong> The elevation map cannot trap any water. </p>
<br>
<p><strong>Input</strong> : [3,2,1]  </p>
<p><strong>Output</strong> : 0 </p>
<p><strong>Explanation</strong> The elevation map cannot trap any water. </p>
<br>
<br>
<p><strong>Solution :</strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>Bruteforce approach</strong></p>
<p>In this approach, we will try to find maximum water can be trapped at each step and we will sum all those to get our final answer</p>
<p>The Amount of water that can be trapped at a step, will be minimum of (maximum height of step which is left to it and maximum height of step which is right to it) - current step size.</p>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240613172631/Trapping-Rain-Water-Problem.png">
<p>By observing above example, we can say water at step-3, can be calculated as</p>
<p>maximum step height to its left is 3, i.e is step-1</p>
<p>maximum step height to its right is 4, i.e is step-5</p>
<p>So, maximum step-3, we can have water up to 3 units</p>
<p>since we have a step of size-1 already, then water at step-3. will be 3-1=2</p>
<p>Steps To Follow</p>
<ol>	
	<li>Loop through given array</li>
	<ul>
		<li>For each element, find the left maximum height and right maximum height</li>
		<li>Find water content at current element, currentWater=min(leftHeight,rightHeight)-current element height</li>
		<li><strong>Edge Case : </strong>If there is negative value fot current water, that means, current element can't trap any water, so continue with next element</li>
		<li>add current water to total, to calculate total water</li>
	</ul>
	<li>return total as final answer</li>
</ol>

```python
def bruteForce(n,arr):
    total=0
    for i in range(n):
        leftMax,rightMax=0,0
        for j in range(0,i):
            leftMax=max(leftMax,arr[j])
        for j in range(i+1,n):
            rightMax=max(rightMax,arr[j])
        currentWater=min(leftMax,rightMax)-arr[i]
        if(currentWater<0):
            continue
        total+=currentWater
    return total
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```

<p><strong>Time Complexity</strong> : O(n**2)</p>
<p>This is because for each element, we are computing the maximum height to the left and right, leading to a nested loop structure.</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p> No additional space is used apart from a few variables.</p>

<p><strong>Better Approach</strong></p>
<p>In previous approach, we try to loop for every element to find its maximum left height and minimum left height</p>
<p>We can loop from last element to first element once and store maximum right height at each element and store it in an array</p>
<p>Then, we will loop from first to last element, we will track current maximum height that can used as left height at each element</p>
<p>now, at each element, we will find out water content using current maximum height and maximum right height stored in a array previously</p>
<p>this resolves inner looping for each element</p>

```python
def better(n,arr):
    total=0
    rightMax=[0]*n
    maxi=0
    for i in range(n-1,-1,-1):
        rightMax[i]=maxi
        maxi=max(maxi,arr[i])
    leftMax=0
    for i in range(n):
        currentWater=min(leftMax,rightMax[i])-arr[i]
        leftMax=max(leftMax,arr[i])
        if(currentWater<0):
            continue
        total+=currentWater
    return total
arr=list(map(int,input().split()))
n=len(arr)
print(better(n,arr))
```
<p><strong>Time Complexity</strong> : O(n+n) = O(2n)</p>
<p>This is because, we looping through entire array two times</p>
<p><strong>Space Complexity</strong> : O(n)</p>
<p>We are using an extra array of size n, to store maximum right height at each element</p>

<p><strong>Optimized Appraoch</strong></p>
<p>In this approach, we will use two pointer algorithm to solve the problem</p>
<p>We will place a pointer on first element called left pointer and a pointer on last element called right pointer</p>
<p>We will loop through array element untill left < right </p>
<ul>
	<li>If left value is less than right pointer value then we know 100% current building (left) will trap the water = currentHeight - leftMax.We can update the total water trapped and increase the left pointer.</li>
	<li>Similarly if the right value is less than left then we can calculate the water that will be trapped on the current building (right).We can update the total water trapped and reduce the right pointer.</li>
</ul>
<p>To calculate water content , we need left maximum and right maximum, we will track it along with pointer movements</p>
<p>steps to solve</p>
<ol>
	<li>Initialise left,right,leftMax,rightMax</li>
	<li>Loop untill left< right </li>
	<ul>
		<li>check if left height is greater than right height</li>
		<ul>
			<li>if true, that means, left bar can trap elements</li>
			<li>check if left element greater than left maximum height</li>
			<ul>
				<li>if true, that means it can't hold water, since left maximum is small, water may split out, so update left max with current left element</li>
				<li>if false, that means it can hold water, calculate water=leftMaximum-leftelement and update total</li>
			</ul>
			<li>increase left pointer</li>
		</ul>
		<ul>
			<li>if false,that means, right bar can trap elements</li>
			<li>check if right element greater than right maximum height</li>
			<ul>
				<li>if true, that means it can't hold water, since right maximum is small, water may split out, so update right max with current right element</li>
				<li>if false, that means it can hold water, calculate water=rightmaximum-rightelement and update total</li>
			</ul>
			<li>reduce right pointer</li>
		</ul>
	</ul>
</ol>

```python
def optimized(n,arr):
    left,right=0,n-1
    leftMax,rightMax=0,0
    total=0
    while left<right:
        if(arr[left]<=arr[right]):
            if(arr[left] > leftMax):
                leftMax=arr[left]
            else:
                currentWater=(leftMax-arr[left])
                total+=currentWater
            left+=1
        else:
            if(arr[right]>rightMax):
                rightMax=arr[right]
            else:
                currentWater=(rightMax-arr[right])
                total+=currentWater
            right-=1
    return total

arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```

<p><strong>Time Complexity</strong> : O(n)</p>
<p>This because we are looping through entire array only once</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p>This because we are not using any extra space</p>

<br>
<br>