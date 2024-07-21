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

<h1>Longest Substring Without Repeating Characters</h1>
<p>Given a string s, find the length of the longest substring without repeating characters.</p>
<p><strong>Examples</strong></p>
<p><strong>Input</strong> : s = "abcabcbb"</p>
<p><strong>Output</strong>: 3</p>
<p><strong>Explanation</strong> : The answer is "abc", with the length of 3.</p>
<p><strong>Input</strong> : s = "bbbbb"</p>
<p><strong>Output</strong>: 1</p>
<p><strong>Explanation</strong> : The answer is "b", with the length of 1.</p>
<p><strong>Input</strong> : s = "pwwkew"</p>
<p><strong>Output</strong>: 3</p>
<p><strong>Explanation</strong> : The answer is "wke", with the length of 3.</p>
<p>Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.</p>
<p><strong>Input</strong> : s = ""</p>
<p><strong>Output</strong>: 0</p>
<p><strong>Explanation</strong> : There is no substring in an empty string.</p>
<p><strong>Input</strong> : s = "abcdef"</p>
<p><strong>Output</strong>: 6</p>
<p><strong>Explanation</strong> : All characters are unique, so the entire string is the longest substring without repeating characters.</p>
<br>
<p><strong>Solution</strong></p>
<p>This problem can be solved in several appraoches</p>
<p>In this problem, we have to find length of longest substring having unique charcters</p>
<p><strong>Bruteforce Approach</strong></p>
<p>In this approach, we will find out all possible substrings for given string, for each substring we will check if has any duplicate charcters, if not we will track its length</p>
<p>Then, we will return longest length</p>

```python
def bruteForce(n,s):
    maxi=0
    for i in range(n):
        for j in range(i+1,n+1):
            substr=s[i:j]
            count={}
            for k in substr:
                if k in count:
                    count[k]+=1
                else:
                    count[k]=1
                if(count[k]>1):
                    break
            else:
                length=j-i
                maxi=max(maxi,length)
    return maxi
s=input()
n=len(s)
print(bruteForce(n,s))
```

<p><strong>Time Complexity</strong> : O(n**3), we are have three loops</p>
<p><strong>Space Complexity</strong> : O(n), we storing each charcter for duplicate check</p>

<p><strong>Better Approach</strong></p>
<p>In previous approach, we are using three loops, instead of that we can reduce to two loops</p>
<p>Outer loop is used to determine starting point for each substring</p>
<p>Inner loop is used to determine ending point for each substring</p>
<p>For current starting point, the substrings will be generated by adding character by character to next to it</p>
<p>For Each Charcter adding new substring will be created, we can track duplicates and track its length</p>
<p>The final answer will be longest length</p>

```python
def better(n,s):
    maxi=0
    for i in range(n):
        check={}
        substr=""
        for j in range(i,n):
            if s[j] in check:
                break
            substr+=s[j]
            check[s[j]]=1
            length=j-i+1
            maxi=max(maxi,length)
    return maxi
s=input()
n=len(s)
print(better(n,s))
```
<p><strong>Time Complexity</strong> : O(N**2), since we are using two loops</p>
<p><strong>Space Complexity</strong> : O(n), we are using dictionary for checking duplicates</p>

<p>We can also use array of size 256 instead of dictionary, that can store any charcter count, this will take constant amount of space</p>

```python
def better2(n,s):
    maxi=0
    for i in range(n):
        check=[0]*256
        for j in range(i,n):
            if check[ord(s[j])]:
                break
            check[ord(s[j])]=1
            length=j-i+1
            maxi=max(maxi,length)
    return maxi
s=input()
n=len(s)
print(better2(n,s))
```

<p><strong>Time Complexity</strong> : O(N**2), since we are using two loops</p>
<p><strong>Space Complexity</strong> : O(256), we are using array of size 256 for checking duplicates</p>


<p><strong>Optimized Approach</strong></p>
<p>In this approach, we can use sliding window approach</p>
<p>We will create two pointers left and right which points 0th position of string</p>
<p>We will move right pointer towards nth position</p>
<p>While moving, we will check if current window,i.e substring from left to right contains unique characters or not.if it has unique charcters we will track its length</p>
<p>Other wise we will shrink the window, by moving left pointer towards a position that will result the unique substring window</p>
<p>Steps To Follow</p>
<ol>
	<li><strong>Initialization:</strong></li>
	<ul>
		<li>maxi: Keeps track of the maximum length of substrings found.</li>
		<li>check: A dictionary to store the index of each character.</li>
		<li>left: Pointer to mark the start of the current window.</li>
		<li>right: Pointer to iterate through the string</li>
	</ul>
	<li><strong>While Loop:</strong></li>
	<ul>
		<li>The loop runs as long as right is less than n (length of the string).</li>
	</ul>
	<li><strong>Handling Duplicates:</strong></li>
	<ul>
		<li>If the character at right is already in 'check', update left to be the maximum of check[s[right]] + 1 (next position after the last occurrence of the current character) and left (to ensure it never moves backwards).</li>
		<li>Update 'check' with the current index of s[right].</li>
	</ul>
	<li><strong>Calculating Length and Updating Maximum:</strong></li>
	<ul>
		<li>Calculate the length of the current window as right - left + 1.</li>
		<li>Update maxi with the maximum of the current length and maxi.</li>
	</ul>
	<li><strong>Increment Right Pointer:</strong></li>
	<ul>
		<li>Move the right pointer to the next character.</li>
	</ul>
	<li><strong>Return Result:</strong></li>
	<ul>
		<li>After the loop completes, maxi will contain the length of the longest substring without repeating characters.</li>
	</ul>
</ol>

```python
def optimized(n,s):
    maxi=0
    check={}
    left,right=0,0
    while right<n:
        if s[right] in check:
            left=max(check[s[right]]+1,left)
        check[s[right]]=right
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi
s=input()
n=len(s)
print(optimized(n,s))
```

<p><strong>Time Complexity</strong> : O(n)  Each character is processed at most twice (once when added to the window and once when the left pointer moves past it).</p>
<p><strong>Space Complexity</strong> : O(n), we have used map to store dupliacte charcters tracking</p>

<p>We can also we array of size 256 to manage duplicate characters instead of dictionary</p>

```python
def optimized2(n,s):
    maxi=0
    check=[-1]*256
    left,right=0,0
    while right<n:
        if check[ord(s[right])]!=-1:
            left=max(check[ord(s[right])]+1,left)
        check[ord(s[right])]=right
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi
s=input()
n=len(s)
print(optimized(n,s)
```

<p><strong>Time Complexity</strong> : O(n)  Each character is processed at most twice (once when added to the window and once when the left pointer moves past it).</p>
<p><strong>Space Complexity</strong> : O(256), we have used array to store dupliacte charcters tracking</p>

<br>
<br>

<h2>Maximum Consecutive 1's wih atmost k flips binary array</h2>
<p>Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's</p>
<p><strong>Example</strong></p>
<p><strong>Input</strong> : nums = [1,1,0,0,1,1,1,0,1,1], k = 2</p>
<p><strong>Output</strong> : 8</p>
<p><strong>Explanation</strong> : By flipping the two 0's at indices 2 and 3, we get the array [1,1,1,1,1,1,1,0,1,1], which has 8 consecutive 1's.</p>
<p><strong>Input</strong> : nums = [1,0,1,1,0,1,0,1], k = 1</p>
<p><strong>Output</strong> : 4</p>
<p><strong>Explanation</strong> :  By flipping the 0 at index 1, we get [1,1,1,1,0,1,0,1], which has 4 consecutive 1's.</p>
<p><strong>Input</strong> : nums = [1,1,1,1], k = 0</p>
<p><strong>Output</strong> : 4</p>
<p><strong>Explanation</strong> :  The array already has 4 consecutive 1's without any flips.</p>
<p><strong>Input</strong> :  nums = [0,0,0,0], k = 2</p>
<p><strong>Output</strong> : 2</p>
<p><strong>Explanation</strong> :  We can flip any two 0's to get at most 2 consecutive 1's.</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>
<p>In this problem, simply we have to find longest subarray contains less than or equal to k zeros</p>
<p><strong>Bruteforce Approach</strong></p>
<p>In this approach, we will find all possible subarrays , and for each subarray we will count number of zeros in it, if count less than or equal to k, then we will find length of that subarray</p>
<p>Out of all subarrays, we will return longest length</p>

```python
def bruteforce(n,arr,k):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            zeros=0
            for t in range(i,j+1):
                if(arr[t]==0):
                    zeros+=1
            if(zeros<=k):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteforce(n,arr,k))
```

<p><strong>Time Complexity</strong> : O(n**3), we are using three loops here</p>
<p><strong>Space Complexity</strong> : O(1) , we are not using any extra space</p>

<p><strong>Better Approach</strong></p>
<p>In this approach, we will modify previous approach to eliminate third inner loop</p>
<p>We don't need to loop for every combination of i and j</p>
<p>current subarray will come from just adding current element to previous subarray</p>

```python
def better(n,arr,k):
    maxi=0
    for i in range(n):
        zeros=0
        for j in range(i,n):
            if(arr[j]==0):
                zeros+=1
            if(zeros<=k):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(better(n,arr,k))
```

<p><strong>Time Complexity</strong> : O(n**2)</p>
<p>We are using two nested loops</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p>We are not using any extra space</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, we will use two pointer sliding window approach</p>
<p>Here, we will use two pointer left and right, that points to 0th position initially</p>
<p>We will move right pointer towards nth position</p>
<p>We will check current window zeros count for each move, if it has less than or equal to k, then we will track its length</p>
<p>Otherwise, we will shrink window, by moving left pointer towards to right, so that window should contain atmost k zeros</p>
<p>finally, we will return maximum window length as answer</p>

<ol>
    <li>Initialize two pointers, <code>left</code> and <code>right</code>, both at the beginning of the array.</li>
    <li>Use a variable <code>zeros</code> to keep track of the number of zeros in the current window.</li>
    <li>Iterate with the <code>right</code> pointer through the array:
        <ul>
            <li>If the element at <code>right</code> is 0, increment <code>zeros</code>.</li>
            <li>If <code>zeros</code> exceeds <code>k</code>, increment the <code>left</code> pointer until <code>zeros</code> is less than or equal to <code>k</code>.</li>
            <li>Update the maximum length of the window as <code>right - left + 1</code>.</li>
        </ul>
    </li>
    <li>Return the maximum length found.</li>
</ol>

```python
def optimized(n,arr,k):
    maxi=0
    left,right=0,0
    zeros=0
    while right<n:
        if(arr[right]==0):
            zeros+=1
        if(zeros>k):
            while (zeros>k):
                if(arr[left]==0):
                    zeros-=1
                left+=1
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(optimized(n,arr,k))
```

<p><strong>Time Complexity</strong> : O(n)</p>
<p>Each element is processed at most twice (once when added to the window and once when the left pointer moves past it).</p>
<p><strong>Space Complexity</strong> : O(1) </p>
<p>Only a fixed amount of extra space is used.</p>

<br>
<br>

<h2>Fruits Into Basket : Longest Subarray Contains atmost 2 different element</h2>
<p>You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits of size N, where fruits[i]  is the type of fruit the ith tree produces.</p>
<p>You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow :</p>
<ul>
	<li>You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.</li>
	<li>Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of the baskets.</li>
	<li>Once you reach a tree with fruit that cannot fit in your baskets, you must stop.</li>
</ul>
<p>Given the integer array fruits, return the maximum number of fruits you can pick.</p>
<p><strong>Examples</strong></p>
<p><strong>Input</strong> : fruits [ ] = { 2, 1, 2 }</p>
<p><strong>Output</strong> : 3</p>
<p><strong>Explantion</strong> : We can pick from all three trees. </p>
<p><strong>Input</strong> : fruits [ ] = { 0, 1, 2, 2, 2, 2 }</p>
<p><strong>Output</strong> : 5</p>
<p><strong>Explantion</strong> : It's optimal to pick from trees(0-indexed) [1,2,3,4,5]. </p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>
<p>In this problem, length of maximum subarra which contains atmost 2 different integers</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we will find all possible subarrays, for each subarray we will check if it has 2 different integers or not</p>
<p>if it has, we will track its length</p>
<p>Out of all possibilities, longest length will be our answer</p>

```python
def bruteForce(n,arr):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            s=set()
            for k in range(i,j+1):
                s.add(arr[k])
                if(len(s)>2):
                    break
            else:
                length=j-i+1
                maxi=max(maxi,length)
    return maxi
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```

<p><strong>Time Complexity</strong> : O(n**3)</p>
<p><strong>Space Complexity</strong> : O(n)</p>

<p><strong>Better Approach</strong></p>
<p>In this appraoch, we will just modify previous approach, to eliminate third inner loop</p>

```python
def better(n,arr):
    maxi=0
    for i in range(n):
        s=set()
        for j in range(i,n):
            s.add(arr[j])
            if(len(s)>2):
                break
            length=j-i+1
            maxi=max(maxi,length)
    return maxi
arr=list(map(int,input().split()))
n=len(arr)
print(better(n,arr))
```

<p><strong>Time Complexity</strong> : O(n**2)</p>
<p><strong>Space Complexity</strong> : O(n)</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, we will use two pointer sliding window approach</p>
<p>We will create two pointers left and right which points 0th position of string</p>
<p>We will move right pointer towards nth position</p>
<p>While moving, we will check if current window,i.e subarray from left to right contains 2 unique integers or not.if it has 2 unique integers we will track its length</p>
<p>Other wise we will shrink the window, by moving left pointer towards a position that will result the 2 unique integer subarray window</p>
<p>steps to solve</p>
 <ol>
    <li>Initialize two pointers, <code>left</code> and <code>right</code>, both at the beginning of the array.</li>
    <li>Use a dictionary <code>count</code> to keep track of the frequency of characters in the current window.</li>
    <li>Iterate with the <code>right</code> pointer through the array:
        <ul>
            <li>If the character at <code>right</code> is in <code>count</code>, increment its count.</li>
            <li>If the character is not in <code>count</code>, add it with a count of 1.</li>
            <li>If the number of distinct characters exceeds 2, increment the <code>left</code> pointer until the number of distinct characters is less than or equal to 2.</li>
            <li>Update the maximum length of the window as <code>right - left + 1</code>.</li>
        </ul>
    </li>
    <li>Return the maximum length found.</li>
</ol>

```python
def optimized(n,arr):
    maxi=0
    left,right=0,0
    count={}
    while right<n:
        if arr[right] in count:
            count[arr[right]]+=1
        else:
            count[arr[right]]=1
        if(len(count)>2):
            while (len(count)>2):
                count[arr[left]]-=1
                if(count[arr[left]]==0):
                    del count[arr[left]]
                left+=1
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi
arr=list(map(int,input().split()))
n=len(arr)
print(better(n,arr))
```

<p><strong>Time Complexity</strong> : O(n)</p>
<p>Each element is processed at most twice (once when added to the window and once when the left pointer moves past it).</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p>Only a fixed amount of extra space is used.</p>

<h2>Longest Repeating Character Replacement With Atmost K Operations</h2>
<p>You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.</p>
<p>Return the length of the longest substring containing the same letter you can get after performing the above operations.</p>
<p><strong>Examples</strong></p>
<p><strong>Input</strong> :  s = "ABAB", k = 2</p>
<p><strong>Output</strong> :  4</p>
<p><strong>Explanation</strong> : Replace the two 'A's with two 'B's or vice versa.</p>
<p><strong>Input</strong> : s = "AABABBA", k = 1</p>
<p><strong>Output</strong> :  4</p>
<p><strong>Explanation</strong> : Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.</p>


<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>
<p>In this problem, length of maximum substring which contains all elements same , we can change up to k character</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we will find all possible subarrays, for each substring, we will minimum opearations to convert the substring contains all charcters same</p>
<p>minimum operations = length of substring - maxFrequency</p>
<p>maxFrequency=count of element occurs most number of times in substring</p>
<p>if minimum operations less than or equal to k, we will track its length</p>
<p>Out of all possibilities, longest length will be our answer</p>

```python
def bruteforce(n,s,k):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            maxFreq=0
            count={}
            for t in range(i,j+1):
                if s[t] in count:
                    count[s[t]]+=1
                else:
                    count[s[t]]=1
                maxFreq=max(maxFreq,count[s[t]])
            length=j-i+1
            if((length-maxFreq)<=k):
                maxi=max(maxi,length)
    return maxi
s=input()
n=len(s)
k=int(input())
print(bruteforce(n,s,k))
```

<p><strong>Time Complexity</strong> : O(n**3)</p>
<p><strong>Space Complexity</strong> : O(n)</p>

<p><strong>Better Approach</strong></p>
<p>In this appraoch, we will just modify previous approach, to eliminate third inner loop</p>

```python
def better(n,s,k):
    maxi=0
    for i in range(n):
        maxFreq=0
        count={}
        for j in range(i,n):
            if s[j] in count:
                count[s[j]]+=1
            else:
                count[s[j]]=1
            maxFreq=max(maxFreq,count[s[j]])
            length=j-i+1
            if((length-maxFreq)<=k):
                maxi=max(maxi,length)
    return maxi
s=input()
n=len(s)
k=int(input())
print(better(n,s,k))
```

<p><strong>Time Complexity</strong> : O(n**2)</p>
<p><strong>Space Complexity</strong> : O(n)</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, we will use two pointer sliding window approach</p>
<p>We will create two pointers left and right which points 0th position of string</p>
<p>We will move right pointer towards nth position</p>
<p>While moving, we will check if current window,i.e substring from left to right can be converted to have all same characters with atmost k operations</p>
<p>Other wise we will shrink the window, by moving left pointer towards a position that will result required substring</p>
<p>steps to solve</p>
<ol>
    <li>Initialize two pointers, <code>left</code> and <code>right</code>, both at the beginning of the string.</li>
    <li>Use a dictionary <code>count</code> to keep track of the frequency of characters in the current window.</li>
    <li>Use a variable <code>maxFreq</code> to keep track of the highest frequency of any character in the current window.</li>
    <li>Iterate with the <code>right</code> pointer through the string:
        <ul>
            <li>Increment the frequency of the character at <code>right</code> in the <code>count</code> dictionary.</li>
            <li>Update <code>maxFreq</code> to be the maximum frequency in the current window.</li>
            <li>If the number of characters to replace (i.e., <code>length - maxFreq</code>) exceeds <code>k</code>, increment the <code>left</code> pointer to reduce the window size until the number of replacements is less than or equal to <code>k</code>.</li>
            <li>Update the maximum length of the window as <code>right - left + 1</code>.</li>
        </ul>
    </li>
    <li>Return the maximum length found.</li>
</ol>

```python
def optimized(n,arr):
    maxi=0
    left,right=0,0
    count={}
    while right<n:
        if arr[right] in count:
            count[arr[right]]+=1
        else:
            count[arr[right]]=1
        if(len(count)>2):
            while (len(count)>2):
                count[arr[left]]-=1
                if(count[arr[left]]==0):
                    del count[arr[left]]
                left+=1
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi
arr=list(map(int,input().split()))
n=len(arr)
print(better(n,arr))
```

<p><strong>Time Complexity</strong> : O(n)</p>
<p>Each element is processed at most twice (once when added to the window and once when the left pointer moves past it).</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p>It may store atmost 256 charcters in count map</p>

<br>
<br>

<h2>Longest SubString With Atmost K Different Characters</h2>
<p>Given a string <code>s</code> and an integer <code>k</code>, return the length of the longest substring that contains at most <code>k</code> different characters.</p>
<p><strong>Example Test Cases:</strong></p>
<ul>
    <li><strong>Basic Case</strong><br>
        <strong>Input:</strong> <code>s = "eceba"</code>, <code>k = 2</code><br>
        <strong>Output:</strong> <code>3</code><br>
        <strong>Explanation:</strong> The substring <code>"ece"</code> contains at most two different characters.
    </li>
    <li><strong>Single Character</strong><br>
        <strong>Input:</strong> <code>s = "aaaa"</code>, <code>k = 1</code><br>
        <strong>Output:</strong> <code>4</code><br>
        <strong>Explanation:</strong> The entire string contains only one distinct character.
    </li>
    <li><strong>Two Characters</strong><br>
        <strong>Input:</strong> <code>s = "ab"</code>, <code>k = 2</code><br>
        <strong>Output:</strong> <code>2</code><br>
        <strong>Explanation:</strong> The entire string contains exactly two distinct characters.
    </li>
    <li><strong>Multiple Characters</strong><br>
        <strong>Input:</strong> <code>s = "abcabcabc"</code>, <code>k = 2</code><br>
        <strong>Output:</strong> <code>2</code><br>
        <strong>Explanation:</strong> The longest substring with at most two distinct characters is <code>"ab"</code>.
    </li>
</ul>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p>In this problem, we have to find longest substring contains atmost k- distinct characters</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we will find all possible subarrays, for each substring, we will find number of unique charcters present in it</p>
<p>if count less than or equal to k, we will track its length</p>
<p>Out of all possibilities, longest length will be our answer</p>

```python
def bruteForce(n,s,k):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            temp=set()
            for t in range(i,j+1):
                temp.add(s[t])
                if(len(temp)>k):
                    break
            else:
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

s=input()
n=len(s)
k=int(input())
print(bruteForce(n,s,k))
```

<p><strong>Time Complexity</strong> : o(n**3)</p>
<p><strong>Space Complexity</strong> : o(1)</p>
<p>It may store atmost 256 charcters in count map</p>

<p><strong>Better Approach</strong></p>
<p>In this appraoch, we will just modify previous approach, to eliminate third inner loop</p>

```python
def better(n,s,k):
    maxi=0
    for i in range(n):
        temp=set()
        for j in range(i,n):
            temp.add(s[j])
            if(len(temp)>k):
                break
            length=j-i+1
            maxi=max(maxi,length)
    return maxi
s=input()
n=len(s)
k=int(input())
print(better(n,s,k))
```

<p><strong>Time Complexity</strong> : O(n**2)</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p>It may store atmost 256 charcters in count map</p>

<p><strong>Optimized Approach</strong></p>

<ol>
    <li>Initialize two pointers, <code>left</code> and <code>right</code>, both at the beginning of the string.</li>
    <li>Use a dictionary <code>count</code> to keep track of the frequency of characters in the current window.</li>
    <li>Iterate with the <code>right</code> pointer through the string:
        <ul>
            <li>If the character at <code>right</code> is in <code>count</code>, increment its count.</li>
            <li>If the character is not in <code>count</code>, add it with a count of 1.</li>
            <li>If the number of distinct characters exceeds <code>k</code>, increment the <code>left</code> pointer to reduce the window size until the number of distinct characters is less than or equal to <code>k</code>.</li>
            <li>Update the maximum length of the window as <code>right - left + 1</code>.</li>
        </ul>
    </li>
    <li>Return the maximum length found.</li>
</ol>

```python
def optimized(n,s,k):
    maxi=0
    left,right=0,0
    count={}
    while right<n:
        if s[right] in count:
            count[s[right]]+=1
        else:
            count[s[right]]=1
        if(len(count)>2):
            while (len(count)>k):
                count[s[left]]-=1
                if(count[s[left]]==0):
                    del count[s[left]]
                left+=1
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi

s=input()
n=len(s)
k=int(input())
print(optimized(n,s,k))
```

<p><strong>Time Complexity</strong> : O(n)</p>
<p>Each element is processed at most twice (once when added to the window and once when the left pointer moves past it).</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p>It may store atmost 256 charcters in count map</p>

<h2>Minimum Window Substring</h2>
<p>Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".</p>
<p><strong>Examples</strong></p>
<p><strong>Input</strong> : s = "ADOBECODEBANC", t = "ABC"</p>
<p><strong>Output</strong> : "BANC"</p>
<p><strong>Explanation</strong> : The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.</p>
<p><strong>Input</strong> : s = "a", t = "a"</p>
<p><strong>Output</strong> : "BANC"</p>
<p><strong>Explanation</strong> : The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.</p>
<p><strong>Input</strong> : s = "a", t = "aa"</p>
<p><strong>Output</strong> : ""</p>
<p><strong>Explanation</strong> : Both 'a's from t must be included in the window.Since the largest window of s only has one 'a', return empty string.</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approches</p>
<p>In this problem, we have to fine minimum length of substring which contains all characters of another string</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we will find all possible substrings for given string, for each substring we will check if it contains all characters of another string or not</p>
<p>If it has, we have to check its length, out of all possible substrings, we have to find minimum length substring</p>
<p><strong>How to Check a string contains all characters of another string</strong></p>
<ul>
	<li>create a visited dictionary</li>
	<li>loop over the another string and store frequency of each character</li>
	<li>Then, loop through the given string, if any charcter is already there in dictionary then reduce the frequncey, that means that character is already there in another string and we have visited that in current string, we will reduce the frequency by one</li>
	<li>When, the frequency of one character becomes zero or positive, that means one charcter is visited, then we can track the count of visited charcters</li>
	<li>when, visited count equal to length of another string, then substring contains all charcters of another string</li>
</ul>

```python
def bruteForce(n,s,t):
    minLen=float('inf')
    minSubStr=""
    cnt=len(t)
    for i in range(n):
        for j in range(i,n):
            visited={}
            for temp in t:
                if temp in visited:
                    visited[temp]+=1
                else:
                    visited[temp]=1
            currentCnt=0
            for k in range(i,j+1):
                if s[k] in visited:
                    visited[s[k]]-=1
                else:
                    visited[s[k]]=-1
                if(visited[s[k]]>=0):
                    currentCnt+=1
            if(currentCnt>=cnt and (j-i+1)<minLen):
                minLen=j-i+1
                minSubStr=s[i:j+1]
    return minSubStr
s=input()
t=input()
n=len(s)
print(bruteForce(n,s,t))
```

<p><strong>Time Complexity</strong> : O(n**3)</p>
<p><strong>Space Complexity</strong>: O(1)</p>
<p>visited dictionary can store at max 256 characters</p>

<p><strong>Better Approach</strong></p>
<p>We can modify the previous approach from 3 inner loops to 2 inner loops, as previous problems</p>

```python
def better(n,s,t):
    minLen=float('inf')
    minSubStr=""
    cnt=len(t)
    for i in range(n):
        visited={}
        for temp in t:
            if temp in visited:
                visited[temp]+=1
            else:
                visited[temp]=1
        currentCnt=0
        for j in range(i,n):
            if s[j] in visited:
                visited[s[j]]-=1
            else:
                visited[s[j]]=-1
            if(visited[s[j]]>=0):
                currentCnt+=1
            if(currentCnt>=cnt and (j-i+1)<minLen):
                minLen=j-i+1
                minSubStr=s[i:j+1]
    return minSubStr
s=input()
t=input()
n=len(s)
print(optimized(n,s,t))
```

<p><strong>Time Complexity</strong> : O(n**2)</p>
<p><strong>Space Complexity</strong> : O(1)</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, we will use two pointer sliding window technique to  solve the problem</p>
<ol>
    <li>Create a dictionary <code>visited</code> to count the characters in <code>t</code>.</li>
    <li>Initialize <code>left</code> and <code>right</code> pointers to the start of the string <code>s</code>.</li>
    <li>Initialize <code>currentCnt</code> to track how many characters in <code>t</code> have been matched in the current window.</li>
    <li>Iterate with the <code>right</code> pointer through the string <code>s</code>:
        <ul>
            <li>If the character at <code>right</code> is in <code>visited</code>, decrement its count in the dictionary.</li>
            <li>If the count of the character at <code>right</code> is greater than or equal to zero, increment <code>currentCnt</code>.</li>
            <li>While <code>currentCnt</code> is equal to the length of <code>t</code>, indicating all characters of <code>t</code> are in the current window:
                <ul>
                    <li>Update the minimum length and substring if the current window is smaller.</li>
                    <li>Move the <code>left</code> pointer to the right, adjusting counts and <code>currentCnt</code> accordingly.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Return the minimum substring found, or <code>""</code> if no such substring exists.</li>
</ol>

```python
def optimized(n,s,t):
    left,right=0,0
    minLength=float('inf')
    minSubStr=""
    visited={}
    for temp in t:
        if temp in visited:
            visited[temp]+=1
        else:
            visited[temp]=1
    cnt=len(t)
    currentCnt=0
    while(right<n):
        if(s[right] in visited):
            visited[s[right]]-=1
        else:
            visited[s[right]]=-1
        if(visited[s[right]]>=0):
            currentCnt+=1
        while(currentCnt==cnt):
            length=right-left+1
            if(length<minLength):
                minLength=length
                minSubStr=s[left:right+1]
            visited[s[left]]+=1
            if(visited[s[left]]>0):
                currentCnt-=1
            left+=1
        right+=1
    return minSubStr
s=input()
t=input()
n=len(s)
print(optimized(n,s,t))
```

<p><strong>Time Complexity</strong> : O(n)</p>
<p><strong>Space Complexity</strong> : O(1)</p>

<br>
<br>

<h2>Count Of Subarrays Whose Sum Equals To Given Value : Binary Array</h2>
<p>Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.</p>
<p>A subarray is a contiguous part of the array.</p>
<p><strong>Examples</strong></p>
<p><strong>Input</strong> :nums = [1,0,1,0,1], goal = 2</p>
<p><strong>Output</strong>:4</p>
<p><strong>Explanation</strong>:The 4 subarrays are bolded and underlined below:</p>
<p><strong>Input</strong> :nums = [0,0,0,0,0], goal = 0</p>
<p><strong>Output</strong>:15</p>
<p><strong>Explanation</strong>:The 4 subarrays are bolded and underlined below:</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>
<p>In this problem, we have given an binary array which contains only 0 and 1, we have to find count of subarrays whose sum equal to given value</p>

<p><strong>Bruteforce approach</strong></p>
<p>In this approach, we can find all possible subarrays, and for each subarray we will find the possible sum, if sum equals to given target then we will count that subarray</p>
<p>Finally, we can return the count of all possible subarrays</p>

```python
def bruteForce(n,arr,target):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum+=arr[k]
            if(sum==target):
                cnt+=1
    return cnt
arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(bruteForce(n,arr,target))
```

<p><strong>Time Complexity</strong> : O(n**3)</p>
<p><strong>Space Complexity</strong> : O(1)</p>

<p><strong>Better Approach</strong></p>
<p>In this apporoach, we will just modify the previous apporach to eliminate 3rd inner loop as previous problems</p>

```python
def better(n,arr,target):
    cnt=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum==target):
                cnt+=1
            if(sum>target):
                break
    return cnt
arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(better(n,arr,target))
```

<p><strong>Time Complexity</strong> : O(n**2)</p>
<p><strong>Space Complexity</strong> : O(1)</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, we use two pointer approach</p>
<p>Instead of directly counting subarrays with a sum equal to the target, we can make use of two simpler problems:</p>
<ul>
    <li>Count the number of subarrays with a sum less than or equal to the target.</li>
    <li>Count the number of subarrays with a sum less than or equal to the target minus one.</li>
</ul>
<p>The difference between these two counts will give us the number of subarrays with a sum exactly equal to the target.</p>
<p><strong>Explanation</strong></p>
<ol>
    <li>Subarrays with Sum ≤ Target:</li>
    <ul>
        <li>We use a sliding window (two pointers, left and right) to find the number of subarrays whose sum is less than or equal to the target.</li>
        <li>Start with both pointers at the beginning of the array.</li>
        <li>Move the right pointer to expand the window and add the value at arr[right] to currentSum.</li>
        <li>If currentSum exceeds the target, move the left pointer to reduce the window size and subtract arr[left] from currentSum until currentSum is less than or equal to the target again.</li>
        <li>For each position of the right pointer, the number of valid subarrays ending at right is (right - left + 1) because any subarray starting from left to right is valid.</li>
        <li>Sum up these counts to get the total number of subarrays with a sum ≤ target.</li>
    </ul>
    <li>Difference of Counts</li>
    <ul>
        <li>To find the number of subarrays with a sum exactly equal to the target, calculate:</li>
        <ul>
            <li>Number of subarrays with sum ≤ target.</li>
            <li>Number of subarrays with sum ≤ target - 1.</li>
        </ul>
        <li>The difference between these two counts gives the number of subarrays with sum exactly equal to the target. This works because the first count includes all subarrays with sum ≤ target, while the second count excludes subarrays with sum exactly equal to target.</li>
    </ul>
</ol>

```python
def optimizedAtmostTarget(n,arr,target):
    if(target<0):
        return 0
    cnt=0
    left,right=0,0
    currentSum=0
    while (right<n):
        currentSum+=arr[right]
        while currentSum>target and left<=right:
            currentSum-=arr[left]
            left+=1
        cnt+=(right-left+1)
        right+=1
    return cnt
        
        
def optimized(n,arr,target):
    return optimizedAtmostTarget(n,arr,target)-optimizedAtmostTarget(n,arr,target-1)
```

<p><strong>Time Complexity</strong> : O(2n)</p>
<p><strong>Space Complexity</strong> : O(1)</p>

<br>
<br>

<h2>Count Number of Nice Subarrays : Number Of Subarray Which Contains K number of odd elements</h2>
<p>Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.</p>
<p>Return the number of nice sub-arrays.</p>
<p><strong>Examples</strong></p>
<p><strong>Input</strong> : nums = [1,1,2,1,1], k = 3</p>
<p><strong>Output</strong> : 2</p>
<p><strong>Explanation</strong> : The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].</p>
<p><strong>Input</strong> : nums = [2,4,6], k = 1/p>
<p><strong>Output</strong> : 0</p>
<p><strong>Explanation</strong> : There are no odd numbers in the array.</p>
<p><strong>Input</strong> : nums = [2,2,2,1,2,2,1,2,2,2], k = 2/p>
<p><strong>Output</strong> : 16</p>

<p><strong>Solution</strong></p>
<p>This problem is similar to previous problem</p>
<p>Here, we have to convert the integer array into binary subarray</p>
<p>We can have same approaches as previously</p>
<p>After Converting [2,3,4,5] to binary, it will be like [0,1,0,1], we are just modulo divison each number with 2</p>
<p>Now we have to find subarray with sum equal to k, that means, 1 always represents odd number. number of odd numbers equal to sum</p>

```python
def bruteForce(n,arr,target):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum+=arr[k]
            if(sum==target):
                cnt+=1
    return cnt

def better(n,arr,target):
    cnt=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum==target):
                cnt+=1
            if(sum>target):
                break
    return cnt

def optimizedAtMostTarget(n,arr,target):
    if(target<0):
        return 0
    cnt=0
    left,right=0,0
    currentSum=0
    while (right<n):
        currentSum+=arr[right]
        while currentSum>target and left<=right:
            currentSum-=arr[left]
            left+=1
        cnt+=(right-left+1)
        right+=1
    return cnt
        
        
def optimized(n,arr,target):
    return optimizedAtMostTarget(n,arr,target)-optimizedAtMostTarget(n,arr,target-1)
    


arr=list(map(int,input().split()))
arr=[i&1 for i in arr]
n=len(arr)
target=int(input())
print(bruteForce(n,arr,target))
print(better(n,arr,target))
print(optimized(n,arr,target))
```

<h2>Number of substrings containing all three characters</h2>
<p>Given a string s consisting only of characters a, b and c.Return the number of substrings containing at least one occurrence of all these characters a, b and c.</p>
<p><strong>Examples</strong></p>
<p><strong>Input</strong> : s = "abcabc"</p>
<p><strong>Output</strong> : 10</p>
<p><strong>Explanation</strong> : The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). </p>
<p><strong>Input</strong> : s = "aaacb"</p>
<p><strong>Output</strong> : 3</p>
<p><strong>Explanation</strong> : The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". </p>
<p><strong>Input</strong> : s = "abc"</p>
<p><strong>Output</strong> : 1</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>
<p>In this problem, we have to find count of all possible substrings which contains a,b and c characters</p>

<p><strong>Bruteforce Approach</strong></p>
<p>In this approach, we will find all possible substrings and check whether it contains a,b,c</p>
<p>If any subtring contains, then we will increase the count by one</p>
<p>Finally, we will return count as our answer</p>

```python
def bruteforce(n,s):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            temp=[0,0,0]
            for k in range(i,j+1):
                temp[ord(s[k])-ord('a')]=1
                if(temp[0] and temp[1] and temp[2]):
                    cnt+=1
                    break
    return cnt

s=input()
n=len(s)
print(bruteforce(n,s))
```

<p><strong>Time Complexity</strong> : O(n**3)</p>
<p><strong>Space Complexity</strong> : O(1)</p>

<p><strong>Better Approach</strong></p>
<p>We can modify previous approach to reduce 3 loops to e loops as discussed previously</p>

```python
def better(n,s):
    cnt=0
    for i in range(n):
        temp=[0,0,0]
        for j in range(i,n):
            temp[ord(s[j])-ord('a')]=1
            if(temp[0] and temp[1] and temp[2]):
                cnt+=1
    return cnt

s=input()
n=len(s)
print(better(n,s))
```
<p><strong>Time Complexity</strong> : O(n**2)</p>
<p><strong>Space Complexity</strong> : O(1)</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, we can use two pointer approach</p>

<ul>
    <li><strong>Initialize Variables:</strong>
        <ul>
            <li><strong>left</strong> and <strong>right</strong> are pointers starting at the beginning of the string.</li>
            <li><strong>cnt</strong> is a counter to keep track of the number of valid substrings.</li>
            <li><strong>temp</strong> is an array of size 3 to count occurrences of 'a', 'b', and 'c'.</li>
        </ul>
    </li>
    <li><strong>Right Pointer Movement:</strong> The right pointer moves through the string to expand the window. For each character at the right pointer:
        <ul>
            <li>Update the <strong>temp</strong> array by incrementing the count of the character.</li>
        </ul>
    </li>
    <li><strong>Check Valid Substring:</strong> After updating the <strong>temp</strong> array:
        <ul>
            <li>If the window (substring) contains at least one 'a', one 'b', and one 'c', we have a valid substring.</li>
        </ul>
    </li>
    <li><strong>Count Valid Substrings:</strong>
        <ul>
            <li>For every valid substring, the number of substrings ending at <strong>right</strong> is <strong>n-right</strong> (since any substring starting from the current left to any position after the right is valid).</li>
            <li>Add <strong>n-right</strong> to <strong>cnt</strong>.</li>
        </ul>
    </li>
    <li><strong>Left Pointer Movement:</strong> Move the left pointer to the right to reduce the window size:
        <ul>
            <li>Decrement the count of the character at the left pointer in the <strong>temp</strong> array.</li>
            <li>Continue moving the left pointer until the window is no longer valid (i.e., it no longer contains at least one 'a', one 'b', and one 'c').</li>
        </ul>
    </li>
    <li><strong>Return Result:</strong> Finally, return the value of <strong>cnt</strong>, which represents the total number of valid substrings.</li>
</ul>

```python
def optimized(n,s):
    left,right=0,0
    cnt=0
    temp=[0,0,0]
    while right<n:
        temp[ord(s[right])-ord('a')]+=1
        while(temp[0] and temp[1] and temp[2]):
            cnt+=(n-right)
            temp[ord(s[left])-ord('a')]-=1
            left+=1
        right+=1
    return cnt

s=input()
n=len(s)
print(optimized(n,s))
```

<p><strong>Time Complexity</strong> : O(n)</p>
<p><strong>Space Complexity</strong> : O(1)</p>

<br>    
<br>    

<h2>Subarrays with K Different Integers</h2>
<p>Given an integer array nums and an integer k, return the number of good subarrays of nums.</p>
<p>A good array is an array where the number of different integers in that array is exactly k.</p>
<p>For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.</p>
<p>A subarray is a contiguous part of an array.</p>
<p><strong>Examples</strong></p>
<p><strong>Input</strong> : nums = [1,2,1,2,3], k = 2</p>
<p><strong>Output</strong> : 7</p>
<p><strong>Explanation</strong> : Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
</p>
<p><strong>Input</strong> : nums = [1,2,1,3,4], k = 3</p>
<p><strong>Output</strong> : 3</p>
<p><strong>Explanation</strong> : Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we can find all possible subarrays, and for each subarray we will check if it has k different integers are not</p>
<p>if it has, we will increment the count by one</p>
<p>Finally, we can return the count of all possible subarrays</p>

```python
def bruteForce(n,arr,target):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            visited={}
            for k in range(i,j+1):
                if(arr[k] in visited):
                    visited[arr[k]]+=1
                else:
                    visited[arr[k]]=1
                if(visited[arr[k]]==0):
                    del visited[arr[k]]
            if(len(visited)==target):
                cnt+=1
    return cnt
arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(bruteForce(n,arr,target))
```

<p><strong>Time Complexity</strong> : O(n**3)</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p>We can store atmost 256 characters in visited</p>

<p><strong>Better Approach</strong></p>
<p>In this apporoach, we will just modify the previous apporach to eliminate 3rd inner loop as previous problems</p>

```python
def better(n,arr,target):
    cnt=0
    for i in range(n):
        visited={}
        for j in range(i,n):
            if(arr[j] in visited):
                visited[arr[j]]+=1
            else:
                visited[arr[j]]=1
            if(visited[arr[j]]==0):
                del visited[arr[j]]
            if(len(visited)==target):
                cnt+=1
    return cnt
arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(better(n,arr,target))
```

<p><strong>Time Complexity</strong> : O(n**2)</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p>We can store atmost 256 characters in visited</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, we can use two pointer approach</p>
<p>We want to count the number of subarrays with exactly <strong>target</strong> distinct elements. Instead of directly counting subarrays with exactly <strong>target</strong> distinct elements, we can find the difference between:</p>
<ul>
  <li>The number of subarrays with at most <strong>target</strong> distinct elements.</li>
  <li>The number of subarrays with at most <strong>target - 1</strong> distinct elements.</li>
</ul>
<p>The difference between these two counts gives the number of subarrays with exactly <strong>target</strong> distinct elements.</p>

<p><strong>Function Definitions:</strong></p>

<ol>
  <li>
    <p><strong>optimizedAtMostTarget Function:</strong></p>
    <ul>
      <li>Initialize <strong>cnt</strong> (counter), <strong>left</strong>, <strong>right</strong> pointers, and <strong>visited</strong> dictionary.</li>
      <li>Traverse the array with the <strong>right</strong> pointer.</li>
      <li>Add elements to the <strong>visited</strong> dictionary and count their occurrences.</li>
      <li>If the number of distinct elements in <strong>visited</strong> exceeds <strong>target</strong>, increment the <strong>left</strong> pointer to shrink the window until the condition is met.</li>
      <li>Count all valid subarrays ending at <strong>right</strong> by adding <strong>(right - left + 1)</strong> to <strong>cnt</strong>.</li>
    </ul>
  </li>
  <li>
    <p><strong>optimized Function:</strong></p>
    <ul>
      <li>Calculate the number of subarrays with at most <strong>target</strong> distinct elements.</li>
      <li>Calculate the number of subarrays with at most <strong>target - 1</strong> distinct elements.</li>
      <li>The difference between these two counts gives the number of subarrays with exactly <strong>target</strong> distinct elements.</li>
    </ul>
  </li>
</ol>

```python
    cnt=0
    left,right=0,0
    visited={}
    while (right<n):
        if arr[right] in visited:
            visited[arr[right]]+=1
        else:
            visited[arr[right]]=1
        while len(visited)>target and left<=right:
            visited[arr[left]]-=1
            if(visited[arr[left]]==0):
                del visited[arr[left]]
            left+=1
        cnt+=(right-left+1)
        right+=1
    return cnt

def optimized(n,arr,target):
    tgtCnt=optimizedAtMostTarget(n,arr,target)
    tgtCnt2=optimizedAtMostTarget(n,arr,target-1)
    return tgtCnt-tgtCnt2

arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(optimized(n,arr,target))
```

<p><strong>Time Complexity</strong> : O(2n)</p>
<p><strong>Space Complexity</strong> : O(1)</p>
<p>We can store atmost 256 characters in visited</p>

<h2>Maximum Points You Can Obtain from Cards</h2>
<p>There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.</p>
<p>In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards</p>
<p>Your score is the sum of the points of the cards you have taken.</p>
<p>Given the integer array cardPoints and the integer k, return the maximum score you can obtain.</p>
<p><strong>Examples</strong></p>
<p><strong>Input</strong> : cardPoints = [1,2,3,4,5,6,1], k = 3</p>
<p><strong>Output</strong> : 12</p>
<p><strong>Explanation</strong> : After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.</p>
<p><strong>Input</strong> : cardPoints = [2,2,2], k = 2</p>
<p><strong>Output</strong> : 4</p>
<p><strong>Explanation</strong> : Regardless of which two cards you take, your score will always be 4.</p>
<p><strong>Input</strong> : cardPoints = [9,7,7,9,7,7,9], k = 7</p>
<p><strong>Output</strong> : 55</p>
<p><strong>Explanation</strong> : You have to take all the cards. Your score is the sum of points of all cards.</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>

<p><strong>BruteForce Approach</strong></p>
<p>We want to find the maximum sum we can get by picking a total of <strong>k</strong> elements from either the beginning or the end of the array.</p>

<p><strong>Approach:</strong></p>
<ul>
    <li>We can choose some elements from the start of the array and the rest from the end.</li>
    <li>We need to try all possible ways of distributing the <strong>k</strong> picks between the start and end of the array to find the best (maximum) sum.</li>
</ul>

<p><strong>Steps:</strong></p>
<ol>
    <li>Loop through all possible ways of splitting the <strong>k</strong> picks between the start and end.</li>
    <li>For each way, calculate the sum of the elements picked from the start and the sum of the elements picked from the end.</li>
    <li>Keep track of the maximum sum we can get from all these possible ways.</li>
</ol>

<p><strong>Example:</strong></p>
<ul>
    <li>Suppose we have an array <strong>[1, 2, 3, 4, 5]</strong> and <strong>k = 3</strong>.</li>
    <li>We can take:
        <ul>
            <li>0 elements from the start and 3 from the end: <strong>[3, 4, 5]</strong></li>
            <li>1 element from the start and 2 from the end: <strong>[1] + [4, 5]</strong></li>
            <li>2 elements from the start and 1 from the end: <strong>[1, 2] + [5]</strong></li>
            <li>3 elements from the start and 0 from the end: <strong>[1, 2, 3]</strong></li>
        </ul>
    </li>
    <li>We calculate the sum for each of these combinations and find the maximum.</li>
</ul>

<p><strong>Why It Works:</strong></p>
<ul>
    <li>By considering all possible splits of the <strong>k</strong> picks between the start and end, we ensure that we don't miss any potential combination that might give us the maximum sum.</li>
</ul>

```python
def bruteForce(n,arr,k):
    n=len(arr)
    maxi=0
    for i in range(k+1):
        leftSum=0
        for j in range(k-i):
            leftSum+=arr[j]
        rightSum=0
        for j in range(n-i,n):
            rightSum+=arr[j]
        total=leftSum+rightSum
        maxi=max(maxi,total)
    return maxi
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
```

<p><strong>Time Complexity</strong> : O(n**2)</p>
<p><strong>Space Complexity</strong> : O(1)</p>

<p><strong>Optimized Approach</strong></p>
<p><strong>Initial Sum:</strong></p>
<ul>
    <li>First, calculate the sum of the first <strong>k</strong> elements from the start of the array. This is our starting point.</li>
</ul>

<p><strong>Shift Elements:</strong></p>
<ol>
    <li>Gradually shift one element from the start to the end of the array:
        <ul>
            <li>Subtract the element we move away from the start from the <strong>leftSum</strong>.</li>
            <li>Add the new element we take from the end to the <strong>rightSum</strong>.</li>
        </ul>
    </li>
    <li>Each time you shift, calculate the new total sum (<strong>leftSum</strong> + <strong>rightSum</strong>).</li>
    <li>Update the maximum sum (<strong>maxi</strong>) if the new total is greater.</li>
</ol>

<p><strong>Why It Works:</strong></p>
<ul>
    <li>By shifting elements from the start to the end one by one, we consider all possible ways to split the <strong>k</strong> picks between the start and end.</li>
    <li>This way, we find the maximum possible sum efficiently without recalculating sums from scratch.</li>
</ul>

<p>In essence, you start by taking all <strong>k</strong> elements from the start, then move one element from the start to the end one by one while keeping track of the maximum sum encountered.</p>

```python
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
```

<p><strong>Time Complexity</strong> : O(n)</p>
<p><strong>Space Complexity</strong> : O(1)</p>