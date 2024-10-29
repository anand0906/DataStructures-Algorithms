<h1>Prefix Sum</h1>

<p>The <strong>Prefix Sum Algorithm</strong> is a technique used to efficiently compute the sum of elements in a subarray, typically in an array of numbers. Instead of recalculating the sum from scratch for every query, it preprocesses the array by computing cumulative sums, allowing for quick range sum calculations.</p>

<p>The basic idea is to create a new array, <strong>prefix_sum[]</strong>, where each element at index <strong>i</strong> represents the sum of elements from the start of the array up to index <strong>i</strong>. Once this array is created, the sum of any subarray can be computed in constant time.</p>

<p><strong>Steps for Solving a Prefix Sum Problem</strong></p>
<ol>
  <li><strong>Initialize the Prefix Sum Array</strong>: Create an array <strong>prefix_sum</strong> where each element at index <strong>i</strong> stores the sum of the elements up to index <strong>i</strong> in the original array.</li>
  <li><strong>Compute Prefix Sum</strong>: Traverse the original array, and for each element, compute the prefix sum iteratively.</li>
  <li><strong>Answer Queries in Constant Time</strong>: Once the <strong>prefix_sum</strong> array is ready, you can answer queries like "what is the sum of the subarray from index <strong>l</strong> to index <strong>r</strong>?" in constant time.</li>
</ol>

<p><strong>Key Formula</strong></p>
<p>To get the sum of elements in the subarray from index <strong>l</strong> to <strong>r</strong>:</p>

```python
sum(l, r) = prefix_sum[r] - prefix_sum[l-1]
```

<ul>
  <li>If <strong>l == 0</strong>, the sum is just <strong>prefix_sum[r]</strong>.</li>
</ul>

<p><strong>Python Code Example</strong></p>

<p>Let's implement the prefix sum algorithm with the above steps.</p>

<ol>
  <li><strong>Step 1: Define the Array and Initialize the Prefix Sum</strong></li>
</ol>

```python
def compute_prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * n
    
    # First element is the same as the original array
    prefix_sum[0] = arr[0]
    
    # Compute the prefix sum iteratively
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
    return prefix_sum
```

<ol>
  <li><strong>Step 2: Query Subarray Sum</strong></li>
</ol>

```python
def query_sum(prefix_sum, l, r):
    if l == 0:
        return prefix_sum[r]
    else:
        return prefix_sum[r] - prefix_sum[l - 1]
```

<ol>
  <li><strong>Step 3: Using the Prefix Sum Algorithm</strong></li>
</ol>

```python
# Sample Array
arr = [3, 2, 7, 4, 1, 9, 8]

# Compute the prefix sum for the array
prefix_sum = compute_prefix_sum(arr)

# Query the sum of a subarray from index 2 to 5
result = query_sum(prefix_sum, 2, 5)  # This is the sum of [7, 4, 1, 9]
print(f"Sum of subarray from index 2 to 5 is: {result}")
```

<p><strong>Output</strong></p>
<p><code>Sum of subarray from index 2 to 5 is: 21</code></p>

<p><strong>Explanation of Steps</strong></p>

<ol>
  <li><strong>Prefix Sum Computation</strong>:</li>
</ol>
<p>Given the array <strong>arr = [3, 2, 7, 4, 1, 9, 8]</strong>, we create the prefix sum array:
<ul>
  <li><strong>prefix_sum = [3, 5, 12, 16, 17, 26, 34]</strong></li>
</ul>
Each element in <strong>prefix_sum[i]</strong> is the sum of elements in <strong>arr[0]</strong> to <strong>arr[i]</strong>.</p>

<ol>
  <li><strong>Subarray Query</strong>:</li>
</ol>
<p>To find the sum of the subarray from index <strong>l = 2</strong> to <strong>r = 5</strong>, we apply:</p>
<p><strong>sum(2, 5) = prefix_sum[5] - prefix_sum[1] = 26 - 5 = 21</strong></p>
<p>This gives us the sum of the elements <strong>[7, 4, 1, 9]</strong>.</p>

<p><strong>Benefits of Using Prefix Sum</strong></p>
<ul>
  <li><strong>Efficient Queries</strong>: Once the prefix sum array is built (in O(n) time), any range sum query can be answered in O(1) time.</li>
  <li><strong>Space Efficiency</strong>: Requires O(n) extra space for storing the prefix sum array.</li>
</ul>

<p><strong>Applications</strong></p>
<ul>
  <li><strong>Range Sum Queries</strong>: Prefix sum is commonly used for problems where multiple range sum queries are made on a static array.</li>
  <li><strong>Subarray Sum Problems</strong>: Problems involving checking conditions for subarray sums (like counting subarrays that sum to a specific value) often use prefix sum for efficiency.</li>
</ul>

<p>This algorithm significantly reduces the time complexity for subarray sum calculations from O(n) (recomputing the sum each time) to O(1).</p>

<h1>Patterns</h1>
<p><strong>Guide to Prefix Sum Problems</strong></p>

<p>This guide focuses on problems that involve the prefix sum technique, often used to solve array or subarray problems where the sliding window approach does not work (e.g., when elements are negative or certain complex conditions exist). The prefix sum technique is efficient with a time complexity of O(n) and a space complexity of O(n) due to the use of hash maps or arrays.</p>

<p><strong>Sections of the Guide:</strong></p>
<ol>
    <li>Basic Prefix Sum Problems</li>
    <li>Divisibility and Modulo Problems</li>
    <li>Prefix Sum with XOR</li>
    <li>2D Prefix Sum Problems</li>
</ol>

<p><strong>Basic Idea Behind Prefix Sum</strong></p>

<p>Prefix Sum is used to handle problems involving sums over subarrays. It helps to quickly compute subarray sums without recalculating sums from scratch.</p>

<p><strong>Problem Example: 560. Subarray Sum Equals K</strong><br>
Given an array, the goal is to count how many subarrays sum up to a given value, K.</p>

<ul>
    <li>Let <strong>psum_i</strong> be the running sum at index <strong>i</strong>.</li>
    <li>If at index <strong>i</strong>, there was a previous index <strong>j</strong> such that <strong>psum_i - psum_j = K</strong>, it means the subarray between indices <strong>[j+1, i]</strong> sums to <strong>K</strong>.</li>
</ul>

<p><strong>Template to Solve Prefix Sum Problems</strong></p>

<ol>
    <li><strong>Initialization:</strong> Start with <strong>prefix_sum = 0</strong> and a hash map to store the prefix sums. Initialize <strong>map[0] = 1</strong> to handle cases where the sum of the subarray equals <strong>K</strong> from the start.</li>
    <li><strong>Iterate Through the Array:</strong> For each element, update <strong>prefix_sum</strong>. Check if <strong>prefix_sum - K</strong> exists in the map. If it does, increment the count. Update the hash map with the current prefix sum.</li>
    <li><strong>Key Variables:</strong> <strong>prefix_sum</strong>: running sum; <strong>hash_map</strong>: stores the count of prefix sums; <strong>answer</strong>: stores the result (e.g., count or length).</li>
</ol>

<p><strong>Section 1: Basic Prefix Sum Problems</strong></p>

<ol>
    <li><strong>303. Range Sum Query - Immutable</strong> Precompute the prefix sums and use them to quickly answer queries about subarray sums.</li>
    <li><strong>560. Subarray Sum Equals K</strong> Count the number of subarrays whose sum equals <strong>K</strong> using the prefix sum method and a hash map to track running sums.</li>
    <li><strong>1480. Running Sum of 1d Array</strong> A simple problem to compute the cumulative sum of an array as you iterate through it.</li>
    <li><strong>325. Maximum Size Subarray Sum Equals k</strong> Similar to 560 but asks for the maximum length of such a subarray. Update the index only when the sum is first seen to ensure the largest subarray.</li>
    <li><strong>1248. Count Number of Nice Subarrays</strong> The condition is based on odd numbers. Convert the array to a binary array (1 for odd, 0 for even) and solve it similarly to the subarray sum problem.</li>
</ol>

<p><strong>Section 2: Prefix Sum with Divisibility and Modulo</strong></p>

<p>Many problems focus on subarrays divisible by <strong>K</strong>. The key insight is that the difference between two prefix sums being divisible by <strong>K</strong> implies a valid subarray.</p>

<p><strong>Key Formula:</strong></p>
<ul>
    <li>For subarrays divisible by <strong>K</strong>: <strong>psum_i % K - psum_j % K = 0</strong> (The remainder should be the same).</li>
</ul>

<p><strong>Problems:</strong></p>

<ol>
    <li><strong>974. Subarray Sums Divisible by K</strong> Use the modulo operation and handle negative remainders by adjusting with <strong>+K</strong> before taking modulo again.</li>
    <li><strong>1590. Make Sum Divisible by P</strong> Find the smallest subarray such that removing it makes the remaining sum divisible by <strong>P</strong>.</li>
    <li><strong>523. Continuous Subarray Sum</strong> Similar to the above problems but requires subarray length to be at least 2.</li>
    <li><strong>1497. Check If Array Pairs Are Divisible by K</strong> Find if array elements can be paired such that their sum is divisible by <strong>K</strong>.</li>
    <li><strong>2845. Count of Interesting Subarrays</strong> Combine modular arithmetic with counting binary arrays converted based on some condition.</li>
</ol>

<p><strong>Section 3: Prefix Sum with XOR</strong></p>

<p>These problems often involve finding subarrays with certain even or odd occurrences of elements. XOR is used to detect even/odd occurrences efficiently.</p>

<p><strong>Key Idea:</strong></p>
<ul>
    <li>XOR cancels out even occurrences. For example, <strong>XOR(1, 1) = 0</strong>, so when the XOR of subarray elements results in 0, it means there are even occurrences of the elements.</li>
</ul>

<p><strong>Problems:</strong></p>

<ol>
    <li><strong>1442. Count Triplets That Can Form Two Arrays of Equal XOR</strong> Use XOR to cancel out elements and count subarrays that match the condition.</li>
    <li><strong>1371. Find the Longest Substring Containing Vowels in Even Counts</strong> Use XOR to track even counts of vowels and find the longest valid substring.</li>
    <li><strong>1542. Find Longest Awesome Substring</strong> Similar to the problem above but allows one odd occurrence, so track bit masks accordingly.</li>
</ol>

<p><strong>Section 4: 2D Prefix Sum Problems</strong></p>

<p>These problems extend the prefix sum idea to matrices, where you need to sum sub-matrices efficiently.</p>

<p><strong>Key Formula for 2D Prefix Sum:</strong></p>
<ul>
    <li>To get the sum of a sub-matrix <strong>(r1, c1)</strong> to <strong>(r2, c2)</strong>: <strong>psum[r2][c2] - psum[r1-1][c2] - psum[r2][c1-1] + psum[r1-1][c1-1]</strong></li>
</ul>

<p><strong>Problems:</strong></p>

<ol>
    <li><strong>304. Range Sum Query 2D - Immutable</strong> Precompute the 2D prefix sum for the matrix, and use the formula to find the sum of any sub-matrix efficiently.</li>
    <li><strong>1314. Matrix Block Sum</strong> For each cell in the matrix, compute the sum of a block around it using 2D prefix sum.</li>
    <li><strong>2201. Count Artifacts That Can Be Extracted</strong> Given certain areas in a grid, determine how many artifacts can be fully extracted using prefix sums to track excavated blocks.</li>
</ol>

<p><strong>Conclusion</strong></p>

<p>Prefix sum is a powerful technique for problems involving cumulative sums, divisibility, or XOR conditions. By efficiently computing sums in O(1) time after an initial O(n) or O(n^2) preprocessing step, many problems can be solved optimally using this approach. The guide covers a wide variety of such problems, showing how the template can be adapted to different types of constraints and conditions.</p>



<h1>Problems</h1>

<h2>Longest Subarray with given Sum K(Positives)/(Negatives)</h2>
<p>Given an array and a sum k, we need to print the length of the longest subarray that sums to k.</p>
<p><strong>Examples</strong></p>
<p>Input :  N = 3, k = 5, array[] = {2,3,5}</p>
<p>Output : 2</p>
<p>Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.</p>
<p>Input : N = 5, k = 10, array[] = {2,3,5,1,9}</p>
<p>Output: 3</p>
<p>Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.</p>

<p><strong>Solution</strong></p>
<p>This problem can be solve several approaches</p>
<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we can find out all possible subarrays and find its sum, if any sum equals to given k, then we can take that subarray length. we can take out maximum of all possible lengths will be our answer</p>
<ul>
    <li>First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = size of the array).</li>
    <li>Inside the loop, we will run another loop(say j) that will signify the ending index of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).</li>
    <li>After that for each subarray starting from index i and ending at index j (i.e. arr[i….j]), we will run another loop to calculate the sum of all the elements(of that particular subarray).</li>
    <li>If the sum is equal to k, we will consider its length i.e. (j-i+1). Among all such subarrays, we will consider the maximum length by comparing all the lengths.</li>
</ul>

```python
def bruteForce(n,arr,k):
    largest=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for l in range(i,j+1):
                sum+=arr[l]
            if(sum==k):
                length=j-i+1
                largest=max(largest,length)
    return largest
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
```

<p>Time Complexity: O(N3) approx., where N = size of the array.</p>
<p>Reason: We are using three nested loops, each running approximately N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Better Approach</strong></p>
<p>In this approach, we will just modify the previous approach, where we are trying to find out sum for each possible subarray everytime</p>
<p>If we carefully observe, we can notice that to get the sum of the current subarray we just need to add the current element(i.e. arr[j]) to the sum of the previous subarray i.e. arr[i….j-1].</p>
<p>Assume previous subarray = arr[i……j-1]</p>
<p>current subarray = arr[i…..j]</p>
<p>Sum of arr[i….j] = (sum of arr[i….j-1]) + arr[j]</p>
<p>This is how we can remove the third loop and while moving the j pointer, we can calculate the sum. this can reduce our complexity</p>

<ul>
    <li>First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = array size).</li>
    <li>Inside the loop, we will run another loop(say j) that will signify the ending index as well as the current element of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).</li>
    <li>Inside loop j, we will add the current element to the sum of the previous subarray i.e. sum = sum + arr[j]. </li>
    <li>If the sum is equal to k, we will consider its length i.e. (j-i+1). Among all such subarrays with sum k, we will consider the one with the maximum length by comparing all the lengths.</li>
</ul>

```python
def better(n,arr,k):
    largest=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum==k):
                length=j-i+1
                largest=max(largest,length)
    return largest

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(better(n,arr,k))
```

<p>Time Complexity: O(N2) approx., where N = size of the array.</p>
<p>Reason: We are using two nested loops, each running approximately N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Optimized approach</strong></p>
<p>In this approach, instead of generating all subsequences everytime. we can use prefix sum to find of k sum existed for current element included and as last element</p>
<p>Here, the prefix sum of a subarray ending at index i, simply means the sum of all the elements of that subarray.</p>
<p>Assume, the prefix sum of a subarray ending at index i is x. In that subarray, we will search for another subarray ending at index i, whose sum equals k</p>
<p>Here, we need to observe that if there exists another subarray ending at index i with sum k, then the prefix sum of the rest of the subarray will be x-k. The below image will clarify the concept:</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-13-004939.png">
<p>Now, for a subarray ending at index i with the prefix sum x, if we remove the part with the prefix sum x-k, we will be left with the part whose sum is equal to k. And that is what we want.</p>
<p>That is why, instead of searching the subarrays with sum k, we will keep track of the prefix sum of the subarrays generated at every index using a map data structure.</p>
<p>In the map, we will store every prefix sum calculated, with its index in a <key, value> pair. Now, at index i, we just need to check the map data structure to get the index i.e. preSumMap[x-k] where the subarrays with the prefix sum x-k occur. Then we will simply subtract the index i.e. preSumMap[x-k] from the current index i to get the length of the subarray i.e. len = i -preSumMap[x-k].</p>

<ul>
    <li>First, we will declare a map to store the prefix sums and the indices</li>
    <li>Then we will run a loop(say i) from index 0 to n-1(n = size of the array).</li>
    <li>For each index i, we will do the following</li>
    <ul>
        <li>We will add the current element i.e. a[i] to the prefix sum.</li>
        <li>If the sum is equal to k, we should consider the length of the current subarray i.e. i+1. We will compare this length with the existing length and consider the maximum one.</li>
        <li>We will calculate the prefix sum i.e. x-k, of the remaining subarray.</li>
        <li>If that sum of the remaining part i.e. x-k exists in the map, we will calculate the length i.e. i-preSumMap[x-k], and consider the maximum one comparing it with the existing length we have achieved until now.</li>
        <li>If the sum, we got after step 3.1, does not exist in the map we will add that with the current index into the map. We are checking the map before insertion because we want the index to be as minimum as possible and so we will consider the earliest index where the sum x-k has occurred. [Detailed discussion in the edge case section]</li>
    </ul>
</ul>

<p><strong>Edge Case</strong></p>
<p>If there are zeros and negative values present in given array, then prefix sum will have same sum at different places.</p>
<p>So,since we are trying to find out maximum length, we have ti consider the first prefix as considerable</p>
<p>so, we will add prefix sum only once, since we are coming from starting position, we will add its first occurance</p>
<p>Inorder to overcome its second occurance, we will check if it is already existed or not, if its there, we won't add it again</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-13-005443.png">
<p>In steps 2 and 3 the element at index i is 0. So, in those steps, the prefix sum remains the same but the index is getting updated in the map. Now, when index i reaches the end, it calculates the length i.e. i-preSumMap[rem] = 3-2 = 1. Here it is considering only the subarray [3] which is incorrect as the longest subarray we can get is [0, 0, 3] and hence the length should be 3.</p>
<p>Now, to avoid this edge case i.e. to maximize the calculated length, we need to observe the formula we are using to calculate the length i.e. len = i - preSumMap[rem].</p>
<p>Now, if we minimize the term preSumMap[rem] (i.e. the index where the subarray with sum x-k ends), we will get the maximum length. That is why we will consider only the first or the leftmost index where the subarray with sum x-k ends. After that, we will not update that particular index even if we get a similar subarray ending at a later index.</p>
<p>So, we will check the map before inserting the prefix sum. If it already exists in the map, we will not update it but if it is not present, we will insert it for the first time.</p>

```python
def optimized1(n,arr,k):
    prefix={}
    largest=0
    sum=0
    for i in range(n):
        sum+=arr[i]
        if(sum==k):
            largest=max(largest,i+1)
        rem=sum-k
        if(rem in prefix):
            length=i-prefix[rem]
            largest=max(largest,length)
        if sum not in prefix:
            prefix[sum]=i
    return largest

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(optimized1(n,arr,k))
```

<p>Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.</p>
<p>Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N)(though in the worst case, unordered_map takes O(N) to find an element and the time complexity becomes O(N2)) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array.</p>

<p>Space Complexity: O(N) as we are using a map data structure.</p>


<p><strong>Optimal Approach 2 (only for positive values)</strong></p>
<p>In this, we can use two pointer approach</p>
<p>We can use two pointers left and right, intially we will place them at 0 position, we will try to move right pointer forward direction and we will add elements to sum as we are moving forward</p>
<p>When sum equals to k, then subarray from left to right might be our answer, so we can find length and track its length</p>
<p>When sum crosses k, that means we have to reduce elements, so we will move left pointer forward and reduce the sum by left elements</p>
<p>As, above process continues, we can have multiple subarrays whose sum equals to k, among all possible lengths, we will take the largest as our answer</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-13-012512.png">
<ul>
    <li>First, we will take two pointers: left and right, initially pointing to the index 0.</li>
    <li>The sum is set to a[0] i.e. the first element initially.</li>
    <li>Now we will run a while loop until the right pointer crosses the last index i.e. n-1.</li>
    <li>Inside the loop, we will do the following:</li>
    <ul>
        <li>We will use another while loop and it will run until the sum is lesser or equal to k.</li>
        <ul>
            <li>Inside this second loop, from the sum, we will subtract the element that is pointed by the left pointer and increase the left pointer by 1.</li>
        </ul>
        <li>After this loop gets completed, we will check if the sum is equal to k. If it is, we will compare the length of the current subarray i.e. (right-left+1) with the existing one and consider the maximum one.</li>
        <li>Then we will move forward the right pointer by 1. If the right pointer is pointing to a valid index(< n) after the increment, we will add the element i.e. a[right] to the sum.</li>
    </ul>
    <li>Finally, we will return the maximum length.</li>
</ul>

```python
def optimized2(n,arr,k):
    largest=0
    left,right=0,0
    sum=arr[0]
    while right<n:

        while (left<=right and sum>k):
            sum-=arr[left]
            left-=1

        if(sum==k):
            length=right-left+1
            largest=max(largest,length)

        right+=1
        if(right<n):
            sum+=arr[right]
    return largest
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(optimized2(n,arr,k))  
```

<p>Time Complexity: O(2*N), where N = size of the given array.</p>
<p>Reason: The outer while loop i.e. the right pointer can move up to index n-1(the last index). Now, the inner while loop i.e. the left pointer can move up to the right pointer at most. So, every time the inner loop does not run for n times rather it can run for n times in total. So, the time complexity will be O(2*N) instead of O(N2).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>


<br>
<br>

<h2>Minimum Operations to Reduce X to Zero By Removing Elements From Ends</h2>
<p><strong>Problem Statement:</strong></p>
<p>You are given an integer array <strong>nums</strong> and an integer <strong>x</strong>. In one operation, you can either remove the leftmost or the rightmost element from the array <strong>nums</strong> and subtract its value from <strong>x</strong>. This modifies the array for future operations. The goal is to return the minimum number of operations needed to reduce <strong>x</strong> to exactly 0. If it's not possible, return -1.</p>

<p><strong>Test Cases:</strong></p>
<ul>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> nums = [1, 1, 4, 2, 3], x = 5</li>
            <li><strong>Output:</strong> 2</li>
            <li><strong>Explanation:</strong> We remove the last two elements [2, 3], which sum to 5. Only two operations are required.</li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> nums = [5, 6, 7, 8, 9], x = 4</li>
            <li><strong>Output:</strong> -1</li>
            <li><strong>Explanation:</strong> It's not possible to achieve x = 0 with the given operations.</li>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> nums = [3, 2, 20, 1, 1, 3], x = 10</li>
            <li><strong>Output:</strong> 5</li>
            <li><strong>Explanation:</strong> We remove elements from both ends: [3, 2, 1, 1, 3], and their sum equals 10.</li>
        </ul>
    </li>
    <li><strong>Test Case 4:</strong>
        <ul>
            <li><strong>Input:</strong> nums = [1, 1, 1, 1, 1, 1], x = 3</li>
            <li><strong>Output:</strong> 3</li>
            <li><strong>Explanation:</strong> We remove the first three elements, which sum to 3.</li>
        </ul>
    </li>
</ul>

<p><strong>Intuition:</strong></p>
<p>The core idea is to find the longest subarray whose sum equals <strong>total - x</strong>, where <strong>total</strong> is the sum of all elements in the array. The reason is as follows:</p>
<ol>
    <li>If we remove elements from both ends of the array, we are essentially left with a subarray in the middle. We need to find the longest subarray whose sum equals the difference between the total sum of the array and <strong>x</strong>. By removing the other elements (leftmost and rightmost), we can achieve the required reduction of <strong>x</strong> to zero.</li>
    <li>Finding the longest subarray helps minimize the number of operations because the remaining elements are exactly those that we need to keep. The minimum number of operations will be the size of the array minus the length of this subarray.</li>
</ol>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Calculate the <strong>total</strong> sum of the array.</li>
    <li>If <strong>total</strong> equals <strong>x</strong>, then all elements must be removed, and the answer is the size of the array.</li>
    <li>Otherwise, set <strong>target = total - x</strong>. The problem is now to find the longest subarray with a sum equal to <strong>target</strong>.</li>
    <li>Use helper functions to find the longest subarray with the given sum efficiently:
        <ul>
            <li><strong>longestSubarrayWithGivenSum</strong>: This function uses a hash map (dictionary) to store prefix sums and their indices. It checks for the existence of a subarray that matches the target sum.</li>
            <li><strong>longestSubarrayWithGivenSumOptimized</strong>: This is an optimized version that uses the sliding window technique to find the longest subarray with the given sum in O(n) time complexity.</li>
        </ul>
    </li>
    <li>If such a subarray is found, return the number of operations as <strong>n - length</strong>. Otherwise, return -1 if it's not possible.</li>
</ol>



<p><strong>Code Implementation:</strong></p>


```python
def longestSubarrayWithGivenSum(n, arr, target):
    prefix = {}
    maxi = -1
    currentSum = 0
    for i in range(n):
        currentSum += arr[i]
        rem = currentSum - target
        if rem == 0:
            length = i + 1
            maxi = max(maxi, length)
        if rem in prefix:
            length = i - prefix[rem]
            maxi = max(maxi, length)
        if currentSum not in prefix:
            prefix[currentSum] = i
    return maxi

def longestSubarrayWithGivenSumOptimized(n, arr, target):
    maxi = -1
    left, right = 0, 0
    currentSum = 0
    while right < n:
        currentSum += arr[right]
        while currentSum > target and left <= right:
            currentSum -= arr[left]
            left += 1
        if currentSum == target:
            length = right - left + 1
            maxi = max(maxi, length)
        right += 1
    return maxi

def better(n, arr, x):
    total = sum(arr)
    if total == x:
        return n
    target = total - x
    length = longestSubarrayWithGivenSum(n, arr, target)
    if length == -1:
        return -1
    ans = n - length
    return ans

def optimized(n, arr, x):
    total = sum(arr)
    if total == x:
        return n
    target = total - x
    length = longestSubarrayWithGivenSumOptimized(n, arr, target)
    if length == -1:
        return -1
    ans = n - length
    return ans
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> The <strong>longestSubarrayWithGivenSumOptimized</strong> function runs in O(n) time, and since it is the most time-consuming part, the overall complexity is O(n).</li>
    <li><strong>Space Complexity:</strong> The optimized version uses O(1) extra space for the sliding window approach, making it efficient.</li>
</ul>

<br>
<br>



<h2>Count Subarray sum Equals K</h2>
<p>Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.</p>
<p>A subarray is a contiguous non-empty sequence of elements within an array.</p>
<p><strong>Examples</strong></p>
<p>Input :  N = 4, array[] = {3, 1, 2, 4}, k = 6</p>
<p>Output : 2</p>
<p>Explanation :  The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].</p>
<p>Input :  N = 3, array[] = {1,2,3}, k = 3</p>
<p>Output : 2</p>
<p>Explanation : The subarrays that sum up to 3 are [1, 2], and [3].</p>

<p><strong>Solution</strong></p>
<p>This problem can solved in several approaches</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we can all possible subarrays and find sum for each subarray, then if sum equals to k, then imcrease count</p>
<p>In this way, we can get the final answer</p>

```python
def bruteForce(n,arr,k):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            s=0
            for l in range(i,j+1):
                s+=arr[l]
            if(s==k):
                cnt+=1
    return cnt
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
```

<p>Time Complexity: O(N3), where N = size of the array.</p>
<p>Reason: We are using three nested loops here. Though all are not running for exactly N times, the time complexity will be approximately O(N3).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Better Approach</strong></p>
<p>In this approach, we will modify the existing approach eliminate the 3rd inner loop to find sum for each subarray</p>
<p>If we carefully observe, we can notice that to get the sum of the current subarray we just need to add the current element(i.e. arr[j]) to the sum of the previous subarray i.e. arr[i….j-1].</p>
<p>Assume previous subarray = arr[i……j-1]</p>
<p>current subarray = arr[i…..j]</p>
<p>Sum of arr[i….j] = (sum of arr[i….j-1]) + arr[j]</p>
<p>This is how we can remove the third loop and while moving the j pointer, we can calculate the sum. this can reduce our complexity</p>

```python
def better(n,arr,k):
    cnt=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            if(s==k):
                cnt+=1
    return cnt
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(better(n,arr,k))
```

<p>Time Complexity: O(N2), where N = size of the array.</p>
<p>Reason: We are using two nested loops here. As each of them is running for exactly N times, the time complexity will be approximately O(N2).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Optimized approach</strong></p>
<p>In this approach, we will use the concept of prefix sum</p>
<p>Here, the prefix sum of a subarray ending at index i, simply means the sum of all the elements of that subarray.</p>
<p>Assume, the prefix sum of a subarray ending at index i is x. In that subarray, we will search for another subarray ending at index i, whose sum equals k</p>
<p>Here, we need to observe that if there exists another subarray ending at index i with sum k, then the prefix sum of the rest of the subarray will be x-k. The below image will clarify the concept:</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-13-004939.png">
<p>Now, for a subarray ending at index i with the prefix sum x, if we remove the part with the prefix sum x-k, we will be left with the part whose sum is equal to k. And that is what we want.</p>

<p>Now, there may exist multiple subarrays with the prefix sum x-k. So, the number of subarrays with sum k that we can generate from the entire subarray ending at index i, is exactly equal to the number of subarrays with the prefix sum x-k, that we can remove from the entire subarray.</p>
<p>n the map, we will store every prefix sum calculated, with its occurrence in a <key, value> pair. Now, at index i, we just need to check the map data structure to get the number of times that the subarrays with the prefix sum x-k occur. Then we will simply add that number to our answer.</p>
<p>We will apply the above process for all possible indices of the given array. The possible values of the index i can be from 0 to n-1(where n = size of the array).</p>

<ul>
    <li>First, we will declare a map to store the prefix sums and their counts.</li>
    <li>Then, we will set the value of 0 as 1 on the map.</li>
    <li>Then we will run a loop(say i) from index 0 to n-1(n = size of the array).</li>
    <li>For each index i, we will do the following:</li>
    <ul>
        <li>We will add the current element i.e. arr[i] to the prefix sum.</li>
        <li>We will calculate the prefix sum i.e. x-k, for which we need the occurrence.</li>
        <li>We will add the occurrence of the prefix sum x-k i.e. mpp[x-k] to our answer.</li>
        <li>Then we will store the current prefix sum in the map increasing its occurrence by 1.</li>
    </ul>
</ul>

<p><strong>Why do we need to set the value of 0?</strong></p>
<p>Let’s understand this using an example. Assume the given array is [3, -3, 1, 1, 1] and k is 3</p>
<p>Now, for index 0, we get the total prefix sum as 3, and k is also 3. So, the prefix sum of the remove-part should be x-k = 3-3 = 0. Now, if the value is not previously set for the key 0 in the map, we will not count that subarray and it will not add to final answer.</p>
<p>This will mean that we have not found any subarray with sum 3 till now. But this should not be the case as index 0 itself is a subarray with sum k i.e. 3.</p>
<p>This will mean that we have not found any subarray with sum 3 till now. But this should not be the case as index 0 itself is a subarray with sum k i.e. 3.</p>

```python
def optimized(n,arr,k):
    prefixCnt={0:1}
    s=0
    cnt=0
    for i in range(n):
        s+=arr[i]
        rem=s-k
        if rem in prefixCnt:
            cnt+=prefixCnt[rem]
        if s in prefixCnt:
            prefixCnt[s]+=1
        else:
            prefixCnt[s]=1

    return cnt

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(optimized(n,arr,k))
```

<p>Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.</p>
<p>Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array.</p>
<p>Space Complexity: O(N) as we are using a map data structure.</p>

<br>
<br>

<h2>Count the number of subarrays with given xor K</h2>
<p>Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.</p>
<p><strong>Examples</strong></p>
<p>Input :  A = [4, 2, 2, 6, 4] , k = 6</p>
<p>Output : 4</p>
<p>Explanation :  The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]</p>

<p>Input :  A = [5, 6, 7, 8, 9], k = 5</p>
<p>Output : 2</p>
<p>Explanation :  The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]</p>

<p><strong>Solution</strong></p>
<p>This problem completely similar to previous problem "Count Subarray sum Equals K"</p>
<p>In this problem, we have to find xor value instead of sum</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we will find all possible sub arrays with given array and find its xor value</p>
<p>if any xor value equals to given k value, we will track count of it</p>

```python
def bruteForce(n,arr,k):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            xr=0
            for l in range(i,j+1):
                xr^=arr[l]
            if(xr==k):
                cnt+=1
    return cnt

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
```

<p>Time Complexity: O(N3) approx., where N = size of the array.</p>
<p>Reason: We are using three nested loops, each running approximately N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Better Approach</strong></p>
<p>This approach, slight modification to previous appoach, to remove the nested 3rd loop</p>
<p>If we carefully observe, we can notice that to get the XOR of the current subarray we just need to XOR the current element(i.e. arr[j]) to the XOR of the previous subarray i.e. arr[i….j-1].</p>
<p>Assume previous subarray = arr[i……j-1]</p>
<p>current subarray = arr[i…..j]</p>
<p>XOR of arr[i….j] = (XOR of arr[i….j-1]) ^ arr[j]</p>
<p>This is how we can remove the third loop and while moving j pointer, we can calculate the XOR.</p>

```python
def better(n,arr,k):
    cnt=0
    for i in range(n):
        xr=0
        for j in range(i,n):
            xr^=arr[j]
            if(xr==k):
                cnt+=1
    return cnt

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(better(n,arr,k))
```

<p>Time Complexity: O(N2), where N = size of the array.</p>
<p>Reason: We are using two nested loops here. As each of them is running for N times, the time complexity will be approximately O(N2).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Optimized approach</strong></p>
<p>In this approach, we are going to use the concept of the prefix XOR to solve this problem.</p>
<p>Here, the prefix XOR of a subarray ending at index i, simply means the XOR of all the elements of that subarray.</p>
<p>Assume, the prefix XOR of a subarray ending at index i is xr. In that subarray, we will search for another subarray ending at index i, whose XOR is equal to k. Here, we need to observe that if there exists another subarray ending at index i, with XOR k, then the prefix XOR of the rest of the subarray will be xr^k. The below image will clarify the concept</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/05/Screenshot-2023-05-02-011455.png">
<p>Now, for a subarray ending at index i with the prefix XOR xr, if we remove the part with the prefix XOR xr^k, we will be left with the part whose XOR is equal to k. And that is what we want.</p>
<p>Now, for a subarray ending at index i with the prefix XOR xr, if we remove the part with the prefix XOR xr^k, we will be left with the part whose XOR is equal to k. And that is what we want.</p>
<p>So, for a subarray ending at index i, instead of counting the subarrays with XOR k, we can count the subarrays with the prefix XOR xr^k present in it.</p>
<p>That is why, instead of searching the subarrays with XOR k, we will keep the occurrence of the prefix XOR of the subarrays using a map data structure. </p>
<p>In the map, we will store every prefix XOR calculated, with its occurrence in a <key, value> pair. Now, at index i, we just need to check the map data structure to get the number of times that the subarrays with the prefix XOR xr^k occur. Then we will simply add that number to our count.</p>
<p>We will apply the above process for all possible indices of the given array. The possible values of the index i can be from 0 to n-1(where n = size of the array).</p>

<ul>
    <li>First, we will declare a map to store the prefix XORs and their counts.</li>
    <li>Then, we will set the value of 0 as 1 on the map.</li>
    <li>Then we will run a loop(say i) from index 0 to n-1(n = size of the array).</li>
    <li>For each index i, we will do the following:</li>
    <ul>
        <li>We will XOR the current element i.e. arr[i] to the existing prefix XOR.</li>
        <li>Then we will calculate the prefix XOR i.e. xr^k, for which we need the occurrence.</li>
        <li>We will add the occurrence of the prefix XOR xr^k i.e. mpp[xr^k] to our answer.</li>
        <li>Then we will store the current prefix XOR, xr in the map increasing its occurrence by 1.</li>
    </ul>
</ul>
<p><strong>Why do we need to set the value of 0 beforehand?</strong></p>
<p>Question: Why do we need to set the value of 0 beforehand?
Let’s understand this using an example. Assume the given array is [3, 3, 1, 1, 1] and k is 3. Now, for index 0, we get the total prefix XOR as 3, and k is also 3. So, the prefix XOR xr^k will be = 3^3 = 0. Now, if the value is not previously set for the key 0 in the map, we will get the default value 0 and we will add 0 to our answer. This will mean that we have not found any subarray with XOR 3 till now. But this should not be the case as index 0 itself is a subarray with XOR k i.e. 3.</p>
<p>So, in order to avoid this situation we need to set the value of 0 as 1 on the map beforehand.</p>

```python
def optimized(n,arr,k):
    prefixCnt={0:1}
    xr=0
    cnt=0
    for i in range(n):
        xr^=arr[i]
        x=xr^k
        if x in prefixCnt:
            cnt+=prefixCnt[x]
        if xr in prefixCnt:
            prefixCnt[xr]+=1
        else:
            prefixCnt[xr]=1
    return cnt

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(optimized(n,arr,k))
```

<p>Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the arra</p>
<p>Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array. Point to remember for unordered_map in the worst case, the searching time increases to O(N), and hence the overall time complexity increases to O(N2). </p>
<p>Space Complexity: O(N) as we are using a map data structure.</p>

<br>
<br>

<h2>Longest Subarray Whose Sum Divisible By K</h2>
<p><strong>Problem Statement</strong></p>
<p>You are given an array <code>arr[]</code> of size <code>n</code> and an integer <code>k</code>. The goal is to find the length of the longest subarray whose sum is divisible by <code>k</code>.</p>

<p><strong>Sample Test Cases</strong></p>
<ul>
    <li><strong>Case 1</strong>: 
        <p>Input: <code>arr = [2, 7, 6, 1, 4, 5]</code>, <code>k = 3</code></p>
        <p>Output: <code>4</code> (Subarray <code>[7, 6, 1, 4]</code> has sum <code>18</code>, divisible by <code>3</code>)</p>
    </li>
    <li><strong>Case 2</strong>: 
        <p>Input: <code>arr = [5, 0, -5, 3, -4]</code>, <code>k = 5</code></p>
        <p>Output: <code>5</code> (Entire array has sum <code>-1</code>, but subarray <code>[5, 0, -5, 3, -4]</code> is divisible by <code>5</code>)</p>
    </li>
    <li><strong>Case 3</strong>: 
        <p>Input: <code>arr = [1, 2, 3]</code>, <code>k = 5</code></p>
        <p>Output: <code>0</code> (No subarray has sum divisible by <code>5</code>)</p>
    </li>
    <li><strong>Case 4</strong>: 
        <p>Input: <code>arr = [3, 1, 2, 6, 9, 3]</code>, <code>k = 3</code></p>
        <p>Output: <code>6</code> (Entire array is divisible by <code>3</code>)</p>
    </li>
</ul>

<p><strong>Approach 1: Brute Force</strong></p>
<p><strong>Intuition</strong></p>
<p>This is the most basic approach. We consider <strong>every possible subarray</strong> of the array and calculate its sum. If the sum of the subarray is divisible by <code>k</code>, we check if the length of this subarray is greater than the previously found subarrays.</p>

<p><strong>Steps to Solve</strong></p>
<ol>
    <li>Start with two nested loops. The first loop iterates over all the starting points of subarrays.</li>
    <li>For each starting point, the second loop iterates over all possible ending points.</li>
    <li>Calculate the sum of each subarray and check if it is divisible by <code>k</code>.</li>
    <li>Keep track of the maximum length of subarrays that meet the condition.</li>
</ol>

<p><strong>Code</strong></p>

```python
def bruteForce(n,arr,k):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for t in range(i,j+1):
                sum+=arr[t]
            if(sum%k==0):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi
```

<p><strong>Time and Space Complexity</strong></p>
<ul>
    <li><strong>Time Complexity</strong>: O(n³) because we have three nested loops (one for each subarray and another for calculating the sum).</li>
    <li><strong>Space Complexity</strong>: O(1) as no extra space is used except for a few variables.</li>
</ul>

<p><strong>Approach 2: Improved Brute Force</strong></p>
<p><strong>Intuition</strong></p>
<p>In this approach, we still check all subarrays but optimize by calculating the sum of subarrays on-the-fly instead of recalculating from scratch for each subarray. This avoids the innermost loop.</p>

<p><strong>Steps to Solve</strong></p>
<ol>
    <li>Start with two nested loops. The first loop iterates over the starting points of subarrays.</li>
    <li>In the inner loop, accumulate the sum from the current start to each ending point.</li>
    <li>If the accumulated sum is divisible by <code>k</code>, update the maximum length.</li>
</ol>

<p><strong>Code</strong></p>

```python
def better(n,arr,k):
    maxi=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum%k==0):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi
```

<p><strong>Time and Space Complexity</strong></p>
<ul>
    <li><strong>Time Complexity</strong>: O(n²) because we have two nested loops and we accumulate the sum in the inner loop.</li>
    <li><strong>Space Complexity</strong>: O(1) as no extra space is used except for a few variables.</li>
</ul>

<p><strong>Approach 3: Optimized Approach Using HashMap</strong></p>
<p><strong>Intuition</strong></p>
<p>Instead of checking all subarrays, we can use <strong>prefix sums</strong> and a hash map to store remainders when sums are divided by <code>k</code>. This helps us find subarrays efficiently.</p>
<p>The key insight is that <strong>if two prefix sums have the same remainder when divided by <code>k</code>, the subarray between them has a sum divisible by <code>k</code></strong>.</p>
<p>We keep track of the remainders and their first occurrence. This way, if we find the same remainder again, we know there exists a subarray between those indices whose sum is divisible by <code>k</code>.</p>

<p><strong>Steps to Solve</strong></p>
<ol>
    <li>Traverse the array and keep a running sum.</li>
    <li>Calculate the remainder (<code>mod</code>) of the running sum divided by <code>k</code>. If <code>mod</code> is negative, adjust it to be positive.</li>
    <li>If <code>mod == 0</code>, it means the subarray from the start to the current index is divisible by <code>k</code>.</li>
    <li>If the remainder has been seen before, it means the subarray between the two occurrences of this remainder has a sum divisible by <code>k</code>.</li>
    <li>Use a hash map to store the first occurrence of each remainder.</li>
</ol>

<p><strong>Code</strong></p>

```python
def optimized(n,arr,k):
    maxi=0
    modMap={}
    sum=0
    for i in range(n):
        sum+=arr[i]
        mod=sum%k
        mod=(mod+k)%k #for negative cases
        if(mod==0):
            length=i+1
            maxi=max(maxi,length)
        elif(mod not in modMap):
            modMap[mod]=i
        else:
            length=i-modMap[mod]
            maxi=max(maxi,length)
    return maxi
```

<p><strong>Time and Space Complexity</strong></p>
<ul>
    <li><strong>Time Complexity</strong>: O(n) because we only traverse the array once.</li>
    <li><strong>Space Complexity</strong>: O(k) because we store the remainder frequencies in a hash map, which can at most have <code>k</code> unique remainders.</li>
</ul>


<br>
<br>

<h2>Smallest Subarray Whose Sum Divisible By K</h2>
<p><strong>Problem Statement</strong></p>
<p>You are given an array <code>arr[]</code> of size <code>n</code> and an integer <code>k</code>. Your task is to find the length of the smallest subarray whose sum is divisible by <code>k</code>.</p>

<p><strong>Sample Test Cases</strong></p>
<ul>
    <li><strong>Case 1</strong>:
        <p>Input: <code>arr = [2, 7, 6, 1, 4, 5]</code>, <code>k = 3</code></p>
        <p>Output: <code>1</code> (Subarray <code>[6]</code> has sum <code>6</code>, divisible by <code>3</code>)</p>
    </li>
    <li><strong>Case 2</strong>:
        <p>Input: <code>arr = [5, 0, -5, 3, -4]</code>, <code>k = 5</code></p>
        <p>Output: <code>1</code> (Subarray <code>[5]</code> or <code>[0]</code> is divisible by <code>5</code>)</p>
    </li>
    <li><strong>Case 3</strong>:
        <p>Input: <code>arr = [1, 2, 3]</code>, <code>k = 5</code></p>
        <p>Output: <code>-1</code> (No subarray has sum divisible by <code>5</code>)</p>
    </li>
    <li><strong>Case 4</strong>:
        <p>Input: <code>arr = [3, 1, 2, 6, 9, 3]</code>, <code>k = 3</code></p>
        <p>Output: <code>1</code> (Smallest subarray <code>[3]</code> is divisible by <code>3</code>)</p>
    </li>
</ul>

<p><strong>Approach 1: Brute Force</strong></p>
<p><strong>Intuition</strong></p>
<p>This is the most basic approach. We consider <strong>every possible subarray</strong> of the array and calculate its sum. If the sum of the subarray is divisible by <code>k</code>, we check if the length of this subarray is smaller than the previously found subarrays.</p>

<p><strong>Steps to Solve</strong></p>
<ol>
    <li>Use two nested loops: the first loop iterates over all starting points of subarrays.</li>
    <li>The second loop iterates over all possible ending points.</li>
    <li>Calculate the sum of each subarray.</li>
    <li>If the sum is divisible by <code>k</code>, update the minimum length found.</li>
    <li>If no subarray is found, return <code>-1</code>.</li>
</ol>

<p><strong>Code</strong></p>

```python
def bruteForce(n,arr,k):
    mini=float('inf')
    for i in range(n):
        for j in range(i,n):
            sum=0
            for t in range(i,j+1):
                sum+=arr[t]
            if(sum%k==0):
                length=j-i+1
                mini=min(mini,length)
    return -1 if mini==float('inf') else mini
```
<ul>
    <li><strong>Time Complexity</strong>: O(n³) because we have three nested loops (one for each subarray and one to calculate the sum).</li>
    <li><strong>Space Complexity</strong>: O(1), as no extra space is used except for variables.</li>
</ul>

<p><strong>Approach 2: Improved Brute Force</strong></p>
<p><strong>Intuition</strong></p>
<p>This approach improves upon the brute force by avoiding recalculating sums from scratch. Instead, we accumulate the subarray sum on-the-fly and check if the current sum is divisible by <code>k</code>.</p>

<p><strong>Steps to Solve</strong></p>
<ol>
    <li>Use two nested loops: the first loop iterates over the starting points.</li>
    <li>In the inner loop, accumulate the sum for subarrays starting from <code>i</code>.</li>
    <li>If the accumulated sum is divisible by <code>k</code>, check if it's the smallest subarray.</li>
    <li>Return the minimum length or <code>-1</code> if no valid subarray is found.</li>
</ol>

<p><strong>Code</strong></p>

```python
def better(n,arr,k):
    mini=float('inf')
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum%k==0):
                length=j-i+1
                mini=min(mini,length)
    return -1 if mini==float('inf') else mini
```
<ul>
    <li><strong>Time Complexity</strong>: O(n²) because we have two nested loops.</li>
    <li><strong>Space Complexity</strong>: O(1), as only basic variables are used.</li>
</ul>

<p><strong>Approach 3: Optimized Approach Using HashMap</strong></p>
<p><strong>Intuition</strong></p>
<p>In this optimized approach, we use a <strong>prefix sum and remainder</strong> strategy. The key observation here is that if two prefix sums give the same remainder when divided by <code>k</code>, the subarray between those two indices is divisible by <code>k</code>.</p>
<p>We calculate a running prefix sum, store remainders when divided by <code>k</code>, and their first occurrence. If we encounter the same remainder again, the subarray between the two occurrences has a sum divisible by <code>k</code>.</p>

<p><strong>Steps to Solve</strong></p>
<ol>
    <li>Initialize a hash map to store the remainders of prefix sums and their corresponding indices.</li>
    <li>Traverse the array, calculating the running prefix sum.</li>
    <li>Compute the remainder (<code>mod</code>) of the sum when divided by <code>k</code>. Adjust for negative remainders.</li>
    <li>If the remainder has been seen before, the subarray between the two indices is divisible by <code>k</code>, and the length is checked.</li>
    <li>Store the remainder and its first occurrence in the map.</li>
</ol>

<p><strong>Code</strong></p>

```python
def optimized(n,arr,k):
    mini=float('inf')
    modMap={0:-1}
    sum=0
    for i in range(n):
        sum+=arr[i]
        mod=sum%k
        mod=(mod+k)%k #for negative cases
        if(mod in modMap):
            length=i-modMap[mod]
            mini=min(mini,length)
        modMap[mod]=i
    return -1 if mini==float('inf') else mini
```

<p><strong>Time and Space Complexity</strong></p>
<ul>
    <li><strong>Time Complexity</strong>: O(n) since we traverse the array once.</li>
    <li><strong>Space Complexity</strong>: O(k), as we store the remainder frequencies in a hash map, which can at most have <code>k</code> unique remainders.</li>
</ul>


<br>
<br>

<h2>Smallest Subarray To Remove To Make Sum of Array Divisible By K</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given an array of positive integers <strong>nums</strong>, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by <strong>p</strong>. You cannot remove the whole array.</p>

<p><strong>Sample Test Cases:</strong></p>
<ol>
    <li><strong>Input:</strong> nums = [3,1,4,2], p = 6<br>
    <strong>Output:</strong> 1<br>
    <strong>Explanation:</strong> The sum of <strong>nums</strong> is 10. We can remove [4] to make the remaining sum (6) divisible by 6.</li>  
    <li><strong>Input:</strong> nums = [6,3,5,2], p = 9<br>
    <strong>Output:</strong> 2<br>
    <strong>Explanation:</strong> The sum of <strong>nums</strong> is 16. Removing subarray [5,2] leaves the sum 9, which is divisible by 9.</li>
    <li><strong>Input:</strong> nums = [1,2,3], p = 3<br>
    <strong>Output:</strong> 0<br>
    <strong>Explanation:</strong> The sum is already divisible by 3, so no removal is necessary.</li>
</ol>

<p><strong>Approach 1: Brute Force</strong></p>

<p><strong>Intuition:</strong><br>
We calculate the sum of the entire array and check if it is divisible by <strong>p</strong>. If it is, we return <strong>0</strong> because no subarray needs to be removed. Otherwise, we try removing every possible subarray, calculate the sum of the remaining elements, and check if the sum is divisible by <strong>p</strong>.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Compute the total sum of the array.</li>
    <li>If the sum is divisible by <strong>p</strong>, return <strong>0</strong>.</li>
    <li>Use two nested loops to try removing every subarray and check if the sum of the remaining array is divisible by <strong>p</strong>.</li>
    <li>Track the length of the smallest subarray that can be removed.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n, arr, k):
    total = sum(arr)
    if total % k == 0:
        return 0
    mini = n
    for i in range(n):
        for j in range(i, n):
            subSum = 0
            for t in range(i, j + 1):
                subSum += arr[t]
            if (total - subSum) % k == 0:
                length = j - i + 1
                mini = min(mini, length)
    return -1 if mini == n else mini
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n³) due to three nested loops.</li>
    <li><strong>Space Complexity:</strong> O(1), as no extra space is used.</li>
</ul>

<p><strong>Approach 2: Better Approach</strong></p>

<p><strong>Intuition:</strong><br>
This approach improves upon the brute force by removing redundant recalculations of sums for subarrays. Instead, we maintain a running sum of the subarrays to avoid recalculating them from scratch.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Compute the total sum of the array.</li>
    <li>If the sum is divisible by <strong>p</strong>, return <strong>0</strong>.</li>
    <li>Use two nested loops: accumulate the sum of the subarray on-the-fly while iterating through the array.</li>
    <li>Check if the remaining sum is divisible by <strong>p</strong> after removing each subarray.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def better(n, arr, k):
    total = sum(arr)
    if total % k == 0:
        return 0
    mini = n
    for i in range(n):
        subSum = 0
        for j in range(i, n):
            subSum += arr[j]
            if (total - subSum) % k == 0:
                length = j - i + 1
                mini = min(mini, length)
    return -1 if mini == n else mini
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n²) since we use two nested loops.</li>
    <li><strong>Space Complexity:</strong> O(1), as only variables are used.</li>
</ul>

<p><strong>Approach 3: Optimized Approach Using Prefix Sum</strong></p>

<p><strong>Intuition:</strong></p>
<p>The core idea behind the optimized approach is to leverage <strong>prefix sums</strong> and <strong>modular arithmetic</strong> to efficiently find the smallest subarray that can be removed. We use a hash map to store the remainder of prefix sums modulo <strong>p</strong>, which helps us check whether removing a certain subarray will make the sum of the remaining array divisible by <strong>p</strong>.</p>

<p><strong>Key Concepts:</strong></p>
<ul>
    <li><strong>Prefix Sum:</strong> A prefix sum up to index <strong>i</strong> is the sum of all elements from the start of the array up to <strong>i</strong>.</li>
    <li><strong>Modular Arithmetic:</strong> By using modulo <strong>p</strong>, we can track remainders of the prefix sums and find subarrays that, when removed, leave the remaining sum divisible by <strong>p</strong>.</li>
    <li><strong>Hash Map:</strong> We use a hash map to store the remainders of prefix sums (mod <strong>p</strong>) and the corresponding indices. This allows us to quickly find matching remainders.</li>
</ul>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li><strong>Calculate the Total Sum:</strong> First, calculate the total sum of the array. If this sum is already divisible by <strong>p</strong> (<code>total % p == 0</code>), return <strong>0</strong> because no subarray needs to be removed.</li>
    <li><strong>Determine the Target Remainder:</strong> The remainder of the total sum modulo <strong>p</strong> is <code>targetSum = total % p</code>. To make the sum of the remaining elements divisible by <strong>p</strong>, we need to remove a subarray whose sum has the same remainder as <code>targetSum</code>.</li>
    <li><strong>Initialize Prefix Sum Tracking:</strong> We initialize a hash map <code>prefixMod = {0: -1}</code> to store the remainder of the prefix sums (mod <strong>p</strong>) and start iterating through the array while calculating the prefix sum.</li>
    <li><strong>Iterate Through the Array:</strong> For each index <strong>i</strong>, calculate the running prefix sum and its remainder (mod <strong>p</strong>). Check if removing a subarray with a matching remainder will make the remaining sum divisible by <strong>p</strong>. If we find such a subarray, update the minimum length.</li>
    <li><strong>Update Hash Map:</strong> For each prefix sum remainder, update the hash map to store the index where this remainder first occurred. This allows us to check future subarrays.</li>
    <li><strong>Return the Smallest Subarray:</strong> Once we've found all possible subarrays that can be removed, return the length of the smallest one. If no valid subarray is found, return <strong>-1</strong>.</li>
</ol>

<p><strong>Example Walkthrough:</strong></p>
<p><strong>Input:</strong><br>
<code>nums = [3, 1, 4, 2]</code>, <code>p = 6</code></p>

<ol>
    <li><strong>Step 1: Calculate Total Sum</strong><br>
    Total sum = <code>3 + 1 + 4 + 2 = 10</code><br>
    Target remainder (<code>targetSum</code>) = <code>10 % 6 = 4</code>
    </li>
    <li><strong>Step 2: Initialize Hash Map and Variables</strong><br>
    Initialize the hash map <code>prefixMod = {0: -1}</code> and start iterating through the array while calculating the prefix sum.
    </li>
    <li><strong>Step 3: Iterate and Check for Subarray Removal:</strong></li>
    <ul>
        <li><strong>Index 0:</strong><br>
        Prefix sum = <code>3</code>, remainder = <code>3 % 6 = 3</code><br>
        Needed remainder = <code>(3 - 4) % 6 = 5</code><br>
        <code>5</code> is not in the hash map. Update <code>prefixMod</code> to store <code>prefixMod[3] = 0</code>.
        </li>
        <li><strong>Index 1:</strong><br>
        Prefix sum = <code>3 + 1 = 4</code>, remainder = <code>4 % 6 = 4</code><br>
        Needed remainder = <code>(4 - 4) % 6 = 0</code><br>
        <code>0</code> is in the hash map at index <code>-1</code>, so we can remove the subarray from index <code>0</code> to <code>1</code>. The length is <code>1 - (-1) = 2</code>. Update <code>mini = 2</code>.<br>
        Update <code>prefixMod</code> to store <code>prefixMod[4] = 1</code>.
        </li>
        <li><strong>Index 2:</strong><br>
        Prefix sum = <code>3 + 1 + 4 = 8</code>, remainder = <code>8 % 6 = 2</code><br>
        Needed remainder = <code>(8 - 4) % 6 = 4</code><br>
        <code>4</code> is in the hash map at index <code>1</code>, so we can remove the subarray from index <code>2</code>. The length is <code>2 - 1 = 1</code>. Update <code>mini = 1</code>.<br>
        Update <code>prefixMod</code> to store <code>prefixMod[2] = 2</code>.
        </li>
    </ul>
</ol>

<p><strong>Code Explanation:</strong></p>

```python
def optimized(n, arr, p):
    total = sum(arr)  # Step 1: Calculate the total sum of the array
    
    targetSum = total % p  # Step 2: If total sum is divisible by p, no removal is needed
    if targetSum == 0:
        return 0
    
    mini = n  # Initialize the minimum length to the maximum possible value
    prefixMod = {0: -1}  # Hash map to store mod with index -1 for sum from the start
    currentSum = 0  # Prefix sum initialization
    
    for j in range(n):  # Step 4: Iterate through the array
        currentSum += arr[j]  # Update the prefix sum
        mod = currentSum % p
        mod = (mod + p) % p  # Adjust for negative mods
        
        neededMod = (currentSum - targetSum) % p  # Calculate the required mod value for the remaining sum to be divisible by p
        neededMod = (neededMod + p) % p  # Adjust for negative mods
        
        if neededMod in prefixMod:  # Step 5: Check if this mod value has been seen before
            i = prefixMod[neededMod]
            length = j - i
            mini = min(mini, length)
        
        prefixMod[mod] = j  # Step 6: Store the mod of the current prefix sum
    
    return -1 if mini == n else mini  # Step 7: Return the result
```

<p><strong>Time Complexity:</strong><br>
<code>O(n)</code> because we iterate through the array once and hash map operations take constant time.</p>

<p><strong>Space Complexity:</strong><br>
<code>O(n)</code> because we store the prefix sums and their mods in a hash map.</p>

<br>
<br>

<h2>Count Of Subarrays Whose Sum Divisible By K</h2>

<p><strong>Problem Statement:</strong></p>
<p>Given an array of integers <strong>arr</strong> and an integer <strong>k</strong>, count the number of subarrays whose sum is divisible by <strong>k</strong>.</p>

<p><strong>Sample Test Cases:</strong></p>
<ol>
    <li><strong>Input:</strong> arr = [4, 5, 0, -2, -3, 1], k = 5<br>
    <strong>Output:</strong> 7<br>
    <strong>Explanation:</strong> The subarrays that have a sum divisible by 5 are: [5], [5, 0], [0], [4, 5, 0, -2, -3, 1], [-2, -3], [0, -2, -3], [4, 5, 0].</li>
    <li><strong>Input:</strong> arr = [3, 1, 4, 2], k = 6<br>
    <strong>Output:</strong> 1<br>
    <strong>Explanation:</strong> Only one subarray has a sum divisible by 6: [3, 1, 4, 2].</li>
    <li><strong>Input:</strong> arr = [6, 3, 5, 2], k = 9<br>
    <strong>Output:</strong> 2<br>
    <strong>Explanation:</strong> The subarrays [6, 3] and [5, 2] have sums divisible by 9.</li>
</ol>

<p><strong>Approach 1: Brute Force</strong></p>

<p><strong>Intuition:</strong><br>
We can use three nested loops to check all possible subarrays, compute their sums, and then check if the sum is divisible by <strong>k</strong>.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Use two nested loops to generate all possible subarrays.</li>
    <li>For each subarray, calculate the sum.</li>
    <li>Check if the sum of the subarray is divisible by <strong>k</strong>.</li>
    <li>Count and return the number of subarrays that satisfy the condition.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n, arr, k):
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for t in range(i, j + 1):
                sum += arr[t]
            if sum % k == 0:
                cnt += 1
    return cnt
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n³) due to three nested loops.</li>
    <li><strong>Space Complexity:</strong> O(1), as no extra space is used.</li>
</ul>

<p><strong>Approach 2: Better Approach</strong></p>

<p><strong>Intuition:</strong><br>
Instead of recalculating the sum from scratch for each subarray, we can maintain a running sum of the current subarray as we generate it.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Use two nested loops to generate subarrays.</li>
    <li>Maintain a running sum as you expand the subarray.</li>
    <li>For each subarray, check if the running sum is divisible by <strong>k</strong>.</li>
    <li>Count and return the number of subarrays that satisfy the condition.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def better(n, arr, k):
    cnt = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum % k == 0:
                cnt += 1
    return cnt
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n²) due to two nested loops.</li>
    <li><strong>Space Complexity:</strong> O(1), as only variables are used.</li>
</ul>

<p><strong>Approach 3: Optimized Approach Using Prefix Sum and Modulo</strong></p>

<p><strong>Prefix Sum</strong></p>
<p><strong>Definition</strong>: The prefix sum (or cumulative sum) of an array is a new array where each element at index <em>i</em> represents the sum of the elements of the original array from the start up to <em>i</em>.</p>

<p><strong>Example</strong>:<br>
Given an array <code>arr = [1, 2, 3, 4, 5]</code>:
<ul>
    <li>The prefix sum array will be <code>prefixSum = [1, 3, 6, 10, 15]</code>.</li>
    <li>To find the sum of a subarray from index <em>i</em> to <em>j</em>, you can calculate it as:<br>
    <code>sum(i, j) = prefixSum[j] - prefixSum[i - 1]</code></li>
    <li>This allows querying the sum of any contiguous subarray in <strong>O(1)</strong> time.</li>
</ul>
</p>

<p><strong>Frequency Table</strong></p>
<p><strong>Definition</strong>: A frequency table keeps track of how many times each distinct value appears in a dataset. It can be implemented using a list or a hashmap.</p>

<p><strong>Purpose</strong>: This allows for quick lookups to determine how many times a specific value has occurred while traversing an array, enabling efficient calculations for problems involving counts.</p>

<p><strong>Algorithm Explanation</strong></p>
<p>The goal is to count the number of contiguous subarrays whose sums are divisible by <em>k</em>. The key insight is that if two prefix sums have the same remainder when divided by <em>k</em>, the subarray between them is guaranteed to have a sum divisible by <em>k</em>.</p>

<p><strong>Steps in the Algorithm</strong></p>
<ol>
    <li><strong>Initialize Variables</strong>:
        <ul>
            <li><code>cnt</code>: Counter for the number of valid subarrays.</li>
            <li><code>modMap</code>: A hashmap initialized with <code>{0: 1}</code> to handle cases where a prefix sum itself is directly divisible by <em>k</em>.</li>
            <li><code>sum</code>: A running total initialized to <code>0</code>.</li>
        </ul>
    </li>
    <li><strong>Iterate Through the Array</strong>:
        <ul>
            <li>For each element, update the running sum.</li>
            <li>Compute the current prefix sum's remainder when divided by <em>k</em>. Adjust for negative remainders by adding <em>k</em> and then taking the modulus again.</li>
            <li>If this remainder has been seen before (exists in <code>modMap</code>), it indicates that there are subarrays ending at the current index whose sums are divisible by <em>k</em>. Add the frequency of this remainder to <code>cnt</code>.</li>
            <li>Update the frequency of the current remainder in <code>modMap</code>.</li>
        </ul>
    </li>
    <li><strong>Return Result</strong>: After processing all elements, return the count of valid subarrays.</li>
</ol>

<p><strong>Python Code Implementation</strong></p>

```python
def optimized(n, arr, k):
    cnt = 0
    modMap = {0: 1}  # To handle cases where the sum from the start is divisible by k
    total_sum = 0
    
    for i in range(n):
        total_sum += arr[i]
        mod = total_sum % k
        mod = (mod + k) % k  # Handle negative mod cases
        
        if mod in modMap:
            cnt += modMap[mod]
            modMap[mod] += 1
        else:
            modMap[mod] = 1
            
    return cnt

```

<p><strong>Complexity Analysis</strong></p>
<ul>
    <li><strong>Time Complexity</strong>: <code>O(n)</code> because we traverse the array once.</li>
    <li><strong>Space Complexity</strong>: <code>O(k)</code> in the worst case for storing remainders in <code>modMap</code>.</li>
</ul>


<br>
<br>

<h2>Check If Array Pairs Are Divisible by k</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given an array of integers <strong>arr</strong> of even length <strong>n</strong> and an integer <strong>k</strong>, determine if it's possible to divide the array into exactly <strong>n / 2</strong> pairs such that the sum of each pair is divisible by <strong>k</strong>. Return <strong>true</strong> if a solution is found, otherwise return <strong>false</strong>.</p>

<p><strong>Test Cases (All Possible):</strong></p>
<ul>
    <li><strong>Test Case 1:</strong> arr = [2, 4, 6, 8], k = 4 → Output: True</li>
    <li><strong>Test Case 2:</strong> arr = [1, 2, 3, 4], k = 5 → Output: True</li>
    <li><strong>Test Case 3:</strong> arr = [1, 2, 3, 6], k = 5 → Output: False</li>
    <li><strong>Test Case 4:</strong> arr = [1, 9, 5, 7], k = 3 → Output: True</li>
</ul>

<p><strong>Brute Force Approach:</strong></p>
<p>The brute force approach iterates through the array and tries to form pairs manually while checking if their sum is divisible by <strong>k</strong>. A <strong>visited</strong> array is used to track the elements that have been paired.</p>

<p><strong>Intuition:</strong></p>
<p>By checking all possible combinations of pairs, we can verify if a pair’s sum is divisible by <strong>k</strong> and count the number of valid pairs formed. If we have exactly <strong>n / 2</strong> such pairs, then the condition is satisfied.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Check if the length <strong>n</strong> is odd. If yes, return <strong>false</strong>.</li>
    <li>Initialize a <strong>visited</strong> array of size <strong>n</strong> to track paired elements.</li>
    <li>For each element, try to find another element that, when added to it, gives a sum divisible by <strong>k</strong>.</li>
    <li>Count such pairs and verify if the count equals <strong>n / 2</strong>.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n, arr, k):
    if n & 1:
        return False
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if visited[i]:
            continue
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0 and not visited[j]:
                cnt += 1
                visited[j] = True
                break
    return cnt == n // 2
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n^2), as it checks all pairs in the array.</li>
    <li><strong>Space Complexity:</strong> O(n), due to the use of the <strong>visited</strong> array.</li>
</ul>

<p><strong>Optimized Approach:</strong></p>
<p>The optimized approach uses a hash map (dictionary) to count the frequency of remainders when elements are divided by <strong>k</strong>. This allows us to efficiently determine if pairs can be formed.</p>


<p><strong>Intuition</strong></p>
<p>The goal is to determine if the array can be rearranged in such a way that every element pairs with another element, and the sum of the pair is divisible by <strong>k</strong>. This boils down to understanding the remainder (or modulo) when each element is divided by <strong>k</strong> and ensuring these remainders can be paired.</p>

<p><strong>Step-by-Step Explanation</strong></p>

<ol>
    <li><strong>Check if n is even:</strong>
        <pre>

```python
if n & 1:
    return False
```
        </pre>
        <ul>
            <li>If the size of the array (<strong>n</strong>) is odd, it's impossible to divide it into pairs. Therefore, the function immediately returns <strong>False</strong>.</li>
            <li>This is because an odd number of elements cannot be grouped into pairs (since a pair requires two elements).</li>
        </ul>
    </li>
    <li><strong>Count the remainders:</strong>

```python
prefixMod = collections.defaultdict(int)
for i in range(n):
    mod = arr[i] % k
    mod = (mod + k) % k
    prefixMod[mod] += 1
```
        </pre>
        <ul>
            <li>A dictionary called <strong>prefixMod</strong> is used to store the frequency of each remainder when the elements of <strong>arr</strong> are divided by <strong>k</strong>.</li>
            <li>We calculate <strong>mod = arr[i] % k</strong> to get the remainder when <strong>arr[i]</strong> is divided by <strong>k</strong>.</li>
            <li><strong>(mod + k) % k</strong> ensures that the remainder is non-negative, even if <strong>arr[i]</strong> is negative (handling negative numbers in the array correctly).</li>
            <li>The frequency of each remainder is incremented in the <strong>prefixMod</strong> dictionary.</li>
        </ul>
    </li>
    <li><strong>Check if the remainder 0 can be paired:</strong>

```python
if prefixMod[0] % 2 != 0:
    return False
```
        </pre>
        <ul>
            <li>Elements with a remainder of <strong>0</strong> (i.e., numbers already divisible by <strong>k</strong>) must be paired with other elements that also have a remainder of <strong>0</strong>.</li>
            <li>If there is an odd number of such elements, it is impossible to pair them all, so the function returns <strong>False</strong>.</li>
        </ul>
    </li>
    <li><strong>Check if other remainders can be paired:</strong>

```python
for i in range(1, k // 2 + 1):
    if prefixMod[i] != prefixMod[k - i]:
        return False
```
        </pre>
        <ul>
            <li>We iterate through remainders from <strong>1</strong> to <strong>k // 2</strong>.</li>
            <li>For each remainder <strong>i</strong>, there must be an equal count of elements with remainder <strong>i</strong> and remainder <strong>k - i</strong>.</li>
            <li>This is because these two remainders complement each other to form a sum divisible by <strong>k</strong>.</li>
            <li>If the counts do not match (<strong>prefixMod[i] != prefixMod[k - i]</strong>), it is impossible to form valid pairs, so the function returns <strong>False</strong>.</li>
        </ul>
    </li>
    <li><strong>Return True if all checks pass:</strong>
        <ul>
            <li>If none of the above conditions fail, the array can be partitioned into pairs where each pair's sum is divisible by <strong>k</strong>, so the function returns <strong>True</strong>.</li>
        </ul>
    </li>
</ol>

<p><strong>Code:</strong></p>

```python
import collections
def optimized(n, arr, k):
    if n & 1:
        return False
    prefixMod = collections.defaultdict(int)
    for i in range(n):
        mod = arr[i] % k
        mod = (mod + k) % k
        prefixMod[mod] += 1
    if prefixMod[0] % 2 != 0:
        return False
    for i in range(1, k // 2 + 1):
        if prefixMod[i] != prefixMod[k - i]:
            return False
    return True
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n), as it iterates through the array and processes remainders efficiently.</li>
    <li><strong>Space Complexity:</strong> O(n), due to the hash map storing the count of remainders.</li>
</ul>


<br>
<br>


<h2>Count Of Bad Pairs (j - i != nums[j] - nums[i])</h2>
<p><strong>Problem Statement:</strong></p>
<p>You are given a 0-indexed integer array <strong>nums</strong>. A pair of indices (i, j) is a <strong>bad pair</strong> if:</p>
<ul>
    <li>i < j</li>
    <li>j - i ≠ nums[j] - nums[i]</li>
</ul>
<p>Return the total number of bad pairs in the array.</p>

<p><strong>Test Cases:</strong></p>
<ul>
    <li><strong>Test Case 1:</strong> 
        <ul>
            <li><strong>Input:</strong> nums = [4, 1, 3, 3]</li>
            <li><strong>Output:</strong> 5</li>
            <li><strong>Explanation:</strong> The bad pairs are (0, 1), (0, 2), (0, 3), (1, 2), (2, 3). Total = 5 bad pairs.</li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong> 
        <ul>
            <li><strong>Input:</strong> nums = [1, 2, 3, 4, 5]</li>
            <li><strong>Output:</strong> 0</li>
            <li><strong>Explanation:</strong> All pairs satisfy the condition, so there are no bad pairs.</li>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong> 
        <ul>
            <li><strong>Input:</strong> nums = [7, 2, 5, 8, 4]</li>
            <li><strong>Output:</strong> 8</li>
        </ul>
    </li>
    <li><strong>Test Case 4:</strong> 
        <ul>
            <li><strong>Input:</strong> nums = [6]</li>
            <li><strong>Output:</strong> 0</li>
            <li><strong>Explanation:</strong> There's only one element, so no pairs can be formed.</li>
        </ul>
    </li>
    <li><strong>Test Case 5:</strong> 
        <ul>
            <li><strong>Input:</strong> nums = [1, 1, 1, 1]</li>
            <li><strong>Output:</strong> 0</li>
            <li><strong>Explanation:</strong> No bad pairs, as the difference between every pair is always equal.</li>
        </ul>
    </li>
</ul>

<p><strong>Brute Force Approach:</strong></p>

<p><strong>Intuition:</strong> The brute force approach checks every possible pair of indices (i, j) in the array and determines whether the pair is a bad pair by comparing j - i with nums[j] - nums[i]. If the condition holds, we increment the bad pair count.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize <strong>cnt</strong> as 0 to keep track of the number of bad pairs.</li>
    <li>Use a nested loop:
        <ul>
            <li>The outer loop runs from i = 0 to n-1.</li>
            <li>The inner loop runs from j = i+1 to n-1.</li>
        </ul>
    </li>
    <li>For each pair (i, j), check if j - i ≠ nums[j] - nums[i].</li>
    <li>If the condition holds, increment <strong>cnt</strong>.</li>
    <li>Return <strong>cnt</strong> as the result.</li>
</ol>

```python
def bruteForce(n, arr):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (j - i != arr[j] - arr[i]):
                cnt += 1
    return cnt
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n²) because we check each pair of indices.</li>
    <li><strong>Space Complexity:</strong> O(1) since no additional space is used besides the counter.</li>
</ul>

<p><strong>Optimized Approach:</strong></p>

<p><strong>Intuition:</strong></p>
<p>Given the condition for a bad pair:</p>
<p><strong>j - i ≠ nums[j] - nums[i]</strong></p>

<p>This can be rewritten as:</p>
<p><strong>j - nums[j] ≠ i - nums[i]</strong></p>

<p>So, for a pair (i, j), if the values j - nums[j] and i - nums[i] are equal, it is a <strong>good pair</strong>, otherwise, it is a <strong>bad pair</strong>.</p>

<p><strong>Optimized Approach:</strong></p>

<p>The optimized approach works as follows:</p>

<ol>
    <li><strong>Total Pairs:</strong> The total number of pairs (i, j) where i < j can be computed using the formula for combinations:</li>
    <p>Suppose n=3, possible combinations</p>
    <ol>
        <li>i=0 , j=1</li>
        <li>i=0 , j=2</li>
    </ol>
    <ol>
        <li>i=1 , j=2</li>
    </ol>
    <p>Suppose n=4, possible combinations</p>
    <ol>
        <li>i=0 , j=1</li>
        <li>i=0 , j=2</li>
        <li>i=0 , j=3</li>
    </ol>
    <ol>
        <li>i=1 , j=2</li>
        <li>i=1 , j=3</li>
    </ol>
    <ol>
        <li>i=2 , j=3</li>
    </ol>
    <p>Hence, For n, if m=n-1, total pairs will be 1+2+...n-1</p>
    <p><strong>totalCnt = m*(m+1)//2</strong></p>
    <p>This represents the total number of index pairs in the array.</p>
    <li><strong>Counting Good Pairs:</strong>
        <ul>
            <li>Define a hash map <strong>cntMap</strong> that tracks the frequency of each value of <strong>i - nums[i]</strong>.</li>
            <li>For every new <strong>i</strong>, if the value <strong>i - nums[i]</strong> already exists in <strong>cntMap</strong>, that means there are <strong>cntMap[temp]</strong> good pairs that satisfy the condition <strong>j - nums[j] = i - nums[i]</strong>.</li>
            <li>Accumulate this in <strong>goodCnt</strong>.</li>
        </ul>
    </li>
    <li><strong>Bad Pairs:</strong> Finally, the number of bad pairs is:</li>
    <p><strong>badCnt = totalCnt - goodCnt</strong></p>
</ol>


<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>For n, if m=n-1</li>
    <li>Compute the total number of pairs using <strong>m*(m+1)//2</strong>.</li>
    <li>Initialize a <strong>cntMap</strong> hash map to keep track of the frequency of <strong>i - nums[i]</strong>.</li>
    <li>Traverse the array and compute <strong>diff = i - nums[i]</strong> for each index.</li>
    <li>If the current <strong>diff</strong> is already in the hash map, it means we've found a good pair, so increment the good pair count.</li>
    <li>Update the hash map with the current <strong>diff</strong>.</li>
    <li>Finally, subtract the number of good pairs from the total pairs to get the number of bad pairs.</li>
</ol>

```python
def optimized(n, arr):
    totalCnt = (n * (n - 1)) // 2  # Total number of pairs
    
    goodCnt = 0
    cntMap = {}  # HashMap to store frequency of i - arr[i]
    
    for i in range(n):
        temp = i - arr[i]
        
        # Count how many previous occurrences of this diff exist
        if temp in cntMap:
            goodCnt += cntMap[temp]
            cntMap[temp] += 1
        else:
            cntMap[temp] = 1
    
    # Number of bad pairs is the total pairs minus the good pairs
    badCnt = totalCnt - goodCnt
    return badCnt
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n) because we only traverse the array once and use efficient hash map operations.</li>
    <li><strong>Space Complexity:</strong> O(n) due to the space used by the hash map.</li>
</ul>


<br>
<br>

<h2>Count Of Nice Pairs (nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]))</h2>
<p><strong>Problem Statement:</strong></p>
<p>You are given an array <strong>nums</strong> that consists of non-negative integers. Define <strong>rev(x)</strong> as the reverse of the non-negative integer <strong>x</strong>. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is <strong>nice</strong> if it satisfies all of the following conditions:</p>
<ul>
    <li>0 <= i < j < nums.length</li>
    <li>nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])</li>
</ul>
<p>Return the number of nice pairs of indices. Since the number of pairs can be too large, return it modulo 10^9 + 7.</p>

<p><strong>Test Cases:</strong></p>
<ul>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> nums = [42, 11, 1, 97]</li>
            <li><strong>Output:</strong> 2</li>
            <li><strong>Explanation:</strong> The two nice pairs are:
                <ul>
                    <li>(0, 3): 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.</li>
                    <li>(1, 2): 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> nums = [13, 10, 35, 24, 76]</li>
            <li><strong>Output:</strong> 4</li>
        </ul>
    </li>
</ul>

<p><strong>Brute Force Approach:</strong></p>

<p><strong>Intuition:</strong> The brute force approach checks every possible pair of indices (i, j) and compares the sum of nums[i] and rev(nums[j]) with the sum of nums[j] and rev(nums[i]). If the condition holds, we count it as a nice pair.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Reverse the digits of each number in the array to create a <strong>revArr</strong>.</li>
    <li>Use a nested loop:
        <ul>
            <li>The outer loop runs from i = 0 to n-1.</li>
            <li>The inner loop runs from j = i+1 to n-1.</li>
        </ul>
    </li>
    <li>For each pair (i, j), check if nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]).</li>
    <li>If the condition holds, increment the count.</li>
    <li>Return the count as the result.</li>
</ol>

```python
def bruteForce(n,arr):
    cnt=0
    revArr=[int(str(i)[::-1]) for i in arr]
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]+revArr[j]==arr[j]+revArr[i]):
                cnt+=1
    return cnt
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n²), as we check each pair of indices.</li>
    <li><strong>Space Complexity:</strong> O(n) for the reversed array.</li>
</ul>

<p><strong>Optimized Approach:</strong></p>

<p><strong>Intuition:</strong> Instead of checking every possible pair, we observe that the condition <strong>nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])</strong> can be rearranged to <strong>nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])</strong>. Thus, we can track the difference <strong>nums[i] - rev(nums[i])</strong> for each index in a hash map and count how many indices have the same difference.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Reverse the digits of each number in the array to create a <strong>revArr</strong>.</li>
    <li>Initialize a hash map <strong>cntMap</strong> to track the frequency of <strong>nums[i] - rev(nums[i])</strong>.</li>
    <li>Traverse the array:
        <ul>
            <li>For each number, calculate <strong>diff = nums[i] - rev(nums[i])</strong>.</li>
            <li>If the difference already exists in the hash map, it means we've found <strong>cntMap[diff]</strong> nice pairs, so increment the count by that value.</li>
            <li>Update the hash map with the current difference.</li>
        </ul>
    </li>
    <li>Return the total count of nice pairs.</li>
</ol>

```python
def optimized(n, arr):
    # Reverse each number in the array
    revArr = [int(str(i)[::-1]) for i in arr]
    
    cnt = 0  # Initialize count of valid pairs
    cntMap = {}  # Dictionary to store occurrences of the differences
    
    for i in range(n):
        # Calculate the difference between original and reversed number
        temp = arr[i] - revArr[i]
        
        # If the difference has been seen before, increment the count of valid pairs
        if temp in cntMap:
            cnt += cntMap[temp]
            cntMap[temp] += 1  # Increment the occurrence count
        else:
            cntMap[temp] = 1  # Initialize the count for this difference
    
    return cnt
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n), as we traverse the array once.</li>
    <li><strong>Space Complexity:</strong> O(n), due to the space used by the hash map and the reversed array.</li>
</ul>

<br>
<br>

<h2>Count Of Pairs Whose Absolute Difference Is Equal To K (|nums[i] - nums[j]| == k)</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given an integer array <strong>nums</strong> and an integer <strong>k</strong>, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.</p>

<p><strong>Test Cases:</strong></p>
<ul>
    <li><strong>Test Case 1:</strong>
        <ul>
            <li><strong>Input:</strong> nums = [1, 2, 3, 4], k = 1</li>
            <li><strong>Output:</strong> 3</li>
        </ul>
    </li>
    <li><strong>Test Case 2:</strong>
        <ul>
            <li><strong>Input:</strong> nums = [4, 4, 4], k = 0</li>
            <li><strong>Output:</strong> 3</li>
        </ul>
    </li>
    <li><strong>Test Case 3:</strong>
        <ul>
            <li><strong>Input:</strong> nums = [1, 5, 9], k = 3</li>
            <li><strong>Output:</strong> 0</li>
        </ul>
    </li>
</ul>

<p><strong>BruteForce Approach:</strong></p>
<p><strong>Intuition:</strong> We can check all pairs (i, j) where i < j and calculate the absolute difference between <strong>nums[i]</strong> and <strong>nums[j]</strong>. If the difference is equal to <strong>k</strong>, we increment our counter.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize a counter <strong>ans</strong> to 0.</li>
    <li>Use a nested loop where the outer loop iterates from 0 to n-1, and the inner loop iterates from i+1 to n.</li>
    <li>For each pair (i, j), calculate the absolute difference and compare it with <strong>k</strong>.</li>
    <li>If the difference equals <strong>k</strong>, increment the counter.</li>
    <li>Return the counter value.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n, arr, k):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) == k:
                ans += 1
    return ans
```

<p><strong>Time Complexity:</strong> O(n^2), where n is the size of the array.</p>
<p><strong>Space Complexity:</strong> O(1), as no additional space is used apart from variables.</p>

<p><strong>Optimized Approach:</strong></p>
<p><strong>Intuition:</strong> Instead of checking every pair, we can use a hash map to store the frequency of each number we have seen so far. For every number in the array, we check if its required difference (+k or -k) exists in the map. If it does, we add the frequency of that difference to the result.</p>
<p>You use a hash map <code>cntMap</code> to keep track of the frequency of each number encountered so far in the array.</p>
<p>For each element <code>arr[i]</code>, the code computes two potential differences:</p>
<ul>
    <li><code>diff1 = arr[i] + k</code></li>
    <li><code>diff2 = arr[i] - k</code></li>
</ul>
<p>The logic is that for every element <code>arr[i]</code>, if there are numbers in <code>cntMap</code> that differ by exactly <code>k</code> (either <code>arr[i] + k</code> or <code>arr[i] - k</code>), we have a valid pair.</p>
<p>If <code>diff1</code> or <code>diff2</code> exist in the <code>cntMap</code>, it means we’ve already encountered numbers that can form a valid pair with <code>arr[i]</code>. The count of such pairs is added to <code>ans</code>.</p>

<p>3. <strong>Updating the Hash Map:</strong></p>
<p>After checking for valid pairs, the current element <code>arr[i]</code> is added to the map or its count is incremented if it's already present.</p>

<p>4. <strong>Return the Result:</strong></p>
<p>Finally, the function returns <code>ans</code>, the total count of valid pairs.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize a counter <strong>ans</strong> to 0 and a hash map <strong>cntMap</strong> to store the frequency of numbers.</li>
    <li>Iterate through the array, and for each element, calculate two values: <strong>diff1 = arr[i] + k</strong> and <strong>diff2 = arr[i] - k</strong>.</li>
    <li>If <strong>diff1</strong> or <strong>diff2</strong> exist in <strong>cntMap</strong>, add their frequencies to the counter.</li>
    <li>Update the frequency of the current element in the hash map.</li>
    <li>Return the counter value.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def optimized(n, arr, k):
    ans = 0
    cntMap = {}
    for i in range(n):
        diff1 = arr[i] + k
        diff2 = arr[i] - k
        if diff1 in cntMap:
            ans += cntMap[diff1]
        if diff2 in cntMap:
            ans += cntMap[diff2]
        if arr[i] in cntMap:
            cntMap[arr[i]] += 1
        else:
            cntMap[arr[i]] = 1
    return ans
```

<p><strong>Time Complexity:</strong> O(n), where n is the size of the array.</p>
<p><strong>Space Complexity:</strong> O(n), as we are using a hash map to store frequencies.</p>

<br>
<br>
<h2>Count Of Unique Pairs (arr[i],arr[j]) With Difference Equal To K (|nums[i] - nums[j]| == k and i!=j)</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.</p>
<p>A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:</p>
<ul>
    <li>0 <= i, j < nums.length</li>
    <li>i != j</li>
    <li>|nums[i] - nums[j]| == k</li>
</ul>
<p>Notice that |val| denotes the absolute value of val.</p>

<p><strong>Test Cases:</strong></p>
<ul>
    <li><strong>Test Case 1:</strong> nums = [3, 1, 4, 1, 5], k = 2 <br>
        <strong>Explanation:</strong> The unique pairs are (1, 3) and (3, 5). These pairs satisfy the condition |nums[i] - nums[j]| = k. So, the output is 2.
    </li>
    <li><strong>Test Case 2:</strong> nums = [1, 2, 3, 4, 5], k = 1 <br>
        <strong>Explanation:</strong> The unique pairs are (1, 2), (2, 3), (3, 4), and (4, 5). Each of these pairs has a difference of 1, so the output is 4.
    </li>
    <li><strong>Test Case 3:</strong> nums = [1, 3, 1, 5, 4], k = 0 <br>
        <strong>Explanation:</strong> We are looking for pairs where the difference is zero, which means we need at least two occurrences of a number. In this case, only the pair (1, 1) satisfies this condition, so the output is 1.
    </li>
</ul>

<p><strong>Brute Force Approach:</strong></p>

<p><strong>Intuition:</strong></p>
<p>The brute force approach uses a nested loop to find all pairs of elements. For each pair (i, j), we check if the absolute difference |nums[i] - nums[j]| equals k. If it does, we store the pair in a set to ensure uniqueness. Since sorting the pair ensures that (a, b) and (b, a) are considered the same pair, using a set prevents duplicate pairs.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Iterate over all elements in the array using two loops.</li>
    <li>For each pair, calculate the absolute difference between the two elements.</li>
    <li>If the difference is equal to k, add the pair to a set (sorted to handle duplicates).</li>
    <li>After checking all pairs, return the size of the set, which contains only unique pairs.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n,arr,k):
    ans=set()
    for i in range(n):
        for j in range(i+1,n):
            if(abs(arr[i]-arr[j])==k):
                ans.add(tuple(sorted([arr[i],arr[j]])))
    return len(ans)
```

<p><strong>Time and Space Complexity:</strong></p>
<p>Time complexity: O(n^2), Space complexity: O(n)</p>

<p><strong>Better Approach:</strong></p>

<p><strong>Intuition:</strong></p>
<p>Instead of comparing each element with all others, we can use a hash map to store the count of each element. For each element, we check whether its complement (either nums[i] + k or nums[i] - k) has been seen before. This approach ensures that we only check for valid pairs once, and we store the valid pairs in a set to ensure uniqueness.</p>
<ul>
    <li><strong>Key Idea:</strong> Instead of checking all pairs, we can reduce the number of comparisons by leveraging a hash map.</li>
    <li><strong>Observation:</strong> For each number <strong>nums[i]</strong>, if we know that either <strong>nums[i] + k</strong> or <strong>nums[i] - k</strong> exists earlier in the array, we can instantly form a valid pair without checking all previous elements.</li>
    <li><strong>Steps:</strong>
        <ol>
            <li>For each element <strong>nums[i]</strong>, calculate:
                <ul>
                    <li><strong>nums[i] + k:</strong> this would be a number that forms a valid pair if it exists earlier.</li>
                    <li><strong>nums[i] - k:</strong> this would be another number that forms a valid pair if it exists earlier.</li>
                </ul>
            </li>
            <li>Use a hash map to store the frequency of numbers we have encountered so far, and check if either <strong>nums[i] + k</strong> or <strong>nums[i] - k</strong> exists in this map.</li>
            <li>Add each valid pair to a set (to ensure uniqueness).</li>
        </ol>
    </li>
</ul>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Use a hash map to store the frequency of each element.</li>
    <li>For each element, check if its complement (nums[i] + k or nums[i] - k) is already in the hash map.</li>
    <li>If the complement exists, add the pair to a set.</li>
    <li>Return the size of the set, which gives the number of unique k-diff pairs.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def better(n,arr,k):
    ans=set()
    cntMap={}
    for i in range(n):
        diff1=arr[i]+k
        diff2=arr[i]-k
        if diff1 in cntMap:
            ans.add(tuple(sorted([diff1,arr[i]])))
        if diff2 in cntMap:
            ans.add(tuple(sorted([diff2,arr[i]])))
        if arr[i] not in cntMap:
            cntMap[arr[i]]=1
    return len(ans)
```

<p><strong>Time and Space Complexity:</strong></p>
<p>Time complexity: O(n), Space complexity: O(n)</p>

<p><strong>Optimized Approach:</strong></p>

<p><strong>Intuition:</strong></p>
<p>The optimized approach leverages a hash map to reduce the number of comparisons. Instead of checking all pairs, we use a hash map to store the frequency of numbers and check for complements that form a valid k-diff pair.</p>
<ul>
    <li><strong>Key Idea:</strong> The most efficient solution builds upon the idea of using a hash map but optimizes further by focusing on the <strong>difference between numbers</strong> rather than their absolute values.</li>
    <li>The equation we are solving is:
        <ul>
            <li><strong>|nums[i] - nums[j]| = k</strong></li>
        </ul>
        This means there are two cases to consider for each number:
        <ol>
            <li><strong>Case 1:</strong> nums[i] - nums[j] = k, which simplifies to checking if <strong>nums[i] + k = nums[j]</strong>.</li>
            <li><strong>Case 2:</strong> nums[i] - nums[j] = -k, which simplifies to checking if <strong>nums[i] - k = nums[j]</strong>.</li>
        </ol>
    </li>
    <li><strong>Steps:</strong>
        <ol>
            <li>Use a hash map to keep track of the count of each number as we process the array.</li>
            <li>For each number <strong>nums[i]</strong>, we check two possible values:
                <ul>
                    <li>If <strong>nums[i] + k</strong> exists in the map, it means we've found a valid pair.</li>
                    <li>If <strong>nums[i] - k</strong> exists in the map, it means we've found another valid pair.</li>
                </ul>
            </li>
            <li>Additionally, if <strong>k = 0</strong>, we only want to count pairs where a number appears at least twice (i.e., <strong>nums[i] = nums[j]</strong>).</li>
        </ol>
    </li>
</ul>
<p>By checking these conditions and counting valid pairs, we can efficiently solve the problem in linear time.</p>

<p><strong>Why This Works:</strong></p>
<ul>
    <li>By focusing on the difference between the numbers and using a hash map, we eliminate the need to check every possible pair. Instead, we only check for the existence of potential valid pairs in constant time (via hash map lookups).</li>
    <li>The map helps us store the frequency of numbers, so we can instantly know if a complement (either <strong>nums[i] + k</strong> or <strong>nums[i] - k</strong>) exists in the array.</li>
</ul>

<p>This optimized solution reduces the time complexity to <strong>O(n)</strong>, which is much more efficient for large arrays.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Iterate through the array and use a hash map to store the count of each number.</li>
    <li>For each number, check if its complement (nums[i] + k or nums[i] - k) exists in the hash map.</li>
    <li>If k = 0, count pairs where a number appears at least twice.</li>
    <li>Return the total count of unique pairs.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def optimized(n,arr,k):
    cnt=0
    cntMap={i:0 for i in arr}
    for i in arr:
        cntMap[i]+=1
    for element in cntMap:
        if k==0:
            if(cntMap[element]>=2):
                cnt+=1
        else:
            if(element+k in cntMap):
                cnt+=1
    return cnt
```

<p><strong>Time and Space Complexity:</strong></p>
<p>Time complexity: O(n), Space complexity: O(n)</p>


<br>
<br>

<h2>Count Equal and Divisible Pairs in an Array</h2>
 <p><strong>Problem Statement:</strong></p>
    <p>Given a 0-indexed integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>, return the number of pairs   
 (i, j) where 0 <= i < j < n, such that <code>nums[i] == nums[j]</code> and (i * j) is divisible by <code>k</code>.</p>

<p><strong>Test Cases (All Possible):</strong></p>
<ol>
    <li>Empty array: <code>nums = []</code>, <code>k = 1</code>. Expected output: 0.</li>
    <li>Single element array: <code>nums = [1]</code>, <code>k = 2</code>. Expected output: 0.</li>
    <li>Two elements with different values: <code>nums = [1, 2]</code>, <code>k = 3</code>. Expected output: 0.</li>
    <li>Two elements with same value and divisible by k: <code>nums = [2, 2]</code>, <code>k = 2</code>. Expected output: 1.</li>
    <li>Multiple elements with same value and divisible by k: <code>nums = [3, 3, 3]</code>, <code>k = 3</code>. Expected output: 3.</li>
    <li>Elements with same value but not divisible by k: <code>nums = [4, 4]</code>, <code>k = 3</code>. Expected output: 0.</li>
    <li>Mixed elements with some divisible by k and some not: <code>nums = [5, 5, 6, 6, 7]</code>, <code>k = 5</code>. Expected output: 3.</li>
    <li>Large array with many elements: <code>nums = [100, 100, 100, ..., 100]</code>, <code>k = 100</code>. Expected output: 4950.</li>
</ol>

<p><strong>BruteForce Approach:</strong></p>
<ul>
    <li><strong>Intuition:</strong> The brute force approach iterates through every possible pair of indices (i, j) and checks if the elements at those indices are equal and their product is divisible by k.</li>
    <li><strong>Steps to Solve:</strong>
        <ol>
            <li>Initialize a variable <code>ans</code> to 0 to store the count of valid pairs.</li>
            <li>Iterate through the array <code>nums</code> from index 0 to <code>n-1</code> (outer loop).</li>
            <li>For each index <code>i</code>, iterate through the array from index <code>i+1</code> to <code>n-1</code> (inner loop).</li>
            <li>If the elements at indices <code>i</code> and <code>j</code> are equal and their product is divisible by <code>k</code>, increment <code>ans</code>.</li>
            <li>Return the final value of <code>ans</code>.</li>
        </ol>
    </li>
    <li><strong>Code:</strong></li>

```python
        def bruteForce(n, arr, k):
            ans = 0
            for i in range(n):
                for j in range(i+1, n):
                    if arr[i] == arr[j] and (i * j) % k == 0:
                        ans += 1
            return ans

```
    <li><strong>Time and Space Complexity:</strong>
        <ul>
            <li>Time complexity: O(n^2) due to nested loops.</li>
            <li>Space complexity: O(1) as only constant extra space is used.</li>
        </ul>
    </li>
</ul>

<p><strong>Optimized Approach:</strong></p>
<ul>
    <li><strong>Intuition:</strong> The optimized approach uses a hash map to store the indices of elements that have been encountered so far. When a new element is encountered, it checks if it already exists in the hash map. If it does, it iterates through the indices stored for that element and checks if the product of the current index and the stored index is divisible by <code>k</code>. This reduces the time complexity from O(n^2) to O(n).</li>
    <li><strong>Steps to Solve:</strong>
        <ol>
            <li>Initialize a variable <code>ans</code> to 0 to store the count of valid pairs.</li>
            <li>Create an empty hash map <code>cntMap</code> to store the indices of elements.</li>
            <li>Iterate through the array <code>nums</code> from index 0 to <code>n-1</code>.</li>
            <li>If the current element <code>arr[i]</code> already exists in <code>cntMap</code>, iterate through the indices stored for that element and check if the product of <code>i</code> and the stored index is divisible by <code>k</code>. If so, increment <code>ans</code>.</li>
            <li>Add the current index <code>i</code> to the <code>cntMap</code> for the element <code>arr[i]</code>.</li>
            <li>Return the final value of <code>ans</code>.</li>
        </ol>
    </li>
    <li><strong>Code:</strong></li>

```python
        def optimized(n, arr, k):
            ans = 0
            cntMap = {}
            for i in range(n):
                if arr[i] in cntMap:
                    for j in cntMap[arr[i]]:
                        if (i * j) % k == 0:
                            ans += 1
                if arr[i] in cntMap:
                    cntMap[arr[i]].append(i)
                else:
                    cntMap[arr[i]] = [i]
            return ans
```
    <li><strong>Time and Space Complexity:</strong>
        <ul>
            <li>Time complexity: O(n) on average, as each element is processed at most once.</li>
            <li>Space complexity: O(n) in the worst case, when all elements are distinct.</li>
        </ul>
    </li>
</ul>


<br>
<br>

<h2>Count Of Inequality Pairs</h2>

<p><strong>Problem Statement:</strong></p>
<p>You are given two integer arrays <strong>nums1</strong> and <strong>nums2</strong>, each of size <strong>n</strong>, and an integer <strong>diff</strong>. You need to find the number of pairs (i, j) such that:</p>
<ul>
    <li>0 <= i < j <= n - 1</li>
    <li>nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff</li>
</ul>
<p>The objective is to return the number of such pairs.</p>

<p><strong>Test Cases:</strong></p>
<ol>
    <li>
        <p><strong>Example Case 1:</strong></p>
        <ul>
            <li>nums1 = [3, 1, 4]</li>
            <li>nums2 = [1, 2, 3]</li>
            <li>diff = 1</li>
            <li>Output: 2</li>
        </ul>
    </li>
    <li>
        <p><strong>Example Case 2:</strong></p>
        <ul>
            <li>nums1 = [1, 4, 2]</li>
            <li>nums2 = [3, 1, 3]</li>
            <li>diff = 0</li>
            <li>Output: 1</li>
        </ul>
    </li>
    <li>
        <p><strong>Example Case 3:</strong></p>
        <ul>
            <li>nums1 = [5, 5, 5]</li>
            <li>nums2 = [2, 2, 2]</li>
            <li>diff = 1</li>
            <li>Output: 3</li>
        </ul>
    </li>
</ol>

<p><strong>Brute Force Approach:</strong></p>
<p>In the brute force approach, you simply iterate over all possible pairs (i, j) and check if they satisfy the condition:</p>

<p><strong>Code:</strong></p>

```python
def bruteForce(n,arr1,arr2,k):
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if(arr1[i]-arr1[j]<=arr2[i]-arr2[j]+k):
                ans+=1
    return ans
```

<p><strong>Intuition:</strong></p>
<p>The brute force approach checks each pair (i, j) in <strong>O(n<sup>2</sup>)</strong> time to see if the given condition holds. This is straightforward but inefficient for large arrays.</p>

<p><strong>Steps to Solve (Brute Force):</strong></p>
<ol>
    <li>Iterate through each element <strong>i</strong> in <strong>nums1</strong>.</li>
    <li>For each <strong>i</strong>, iterate through each <strong>j</strong> where <strong>j &gt; i</strong>.</li>
    <li>Check if the condition <strong>nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff</strong> holds.</li>
    <li>If it does, increment the count.</li>
    <li>Return the total count.</li>
</ol>

<p><strong>Time and Space Complexity (Brute Force):</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n<sup>2</sup>) since it involves two nested loops.</li>
    <li><strong>Space Complexity:</strong> O(1) as no extra space is required apart from a few variables.</li>
</ul>

<p><strong>Optimized Approach:</strong></p>
<p>The optimized solution uses a modified <strong>merge sort</strong> approach to efficiently count the pairs that satisfy the condition. Let’s go through the intuition in detail, step by step, to understand why this method works and how it reduces time complexity to O(n log n).</p>

<ol>
    <li>
        <strong>Understanding the Problem Statement</strong>
        <p>The problem asks us to find pairs (i, j) such that:</p>
        <p>0 ≤ i < j ≤ n - 1 and nums1[i] - nums1[j] ≤ nums2[i] - nums2[j] + diff</p>
        <p>To simplify this expression, let’s rearrange:</p>
        <p>nums1[i] - nums2[i] ≤ nums1[j] - nums2[j] + diff</p>
        <p>Let’s define a new array <strong>diffArr</strong> where:</p>
        <p>diffArr[i] = nums1[i] - nums2[i]</p>
        <p>Now, the condition becomes:</p>
        <p>diffArr[i] ≤ diffArr[j] + diff</p>
    </li>
    <li>
        <strong>Simplifying the Problem with diffArr</strong>
        <p>By transforming the original arrays into <strong>diffArr</strong>, the problem reduces to finding pairs (i, j) such that:</p>
        <p>diffArr[i] ≤ diffArr[j] + diff</p>
        <p>This allows us to work with a simpler, single-dimensional array instead of considering both nums1 and nums2.</p>
    </li>
    <li>
        <strong>Using Merge Sort for Efficient Counting</strong>
        <p>Instead of using a brute force approach, which checks each pair and has a time complexity of O(n<sup>2</sup>), we leverage the merge sort algorithm to count pairs efficiently. Here's how merge sort helps:</p>
        <ul>
            <li><strong>Divide and Conquer</strong>: Merge sort splits the array into halves, sorts them, and then merges the sorted halves back together. While merging, we can count the pairs that satisfy the condition.</li>
            <li><strong>Counting During the Merge Phase</strong>: As merge sort processes and combines the two halves, it uses the <strong>two-pointer</strong> technique to count the valid pairs in O(n) time per merge operation.</li>
        </ul>
    </li>
    <li>
        <strong>Detailed Explanation of the Algorithm</strong>
        <ul>
            <li>
                <strong>Step 1: Creating diffArr</strong>
                <p>We first create <strong>diffArr</strong> based on the given arrays:</p>
                <p>diffArr = [arr1[i] - arr2[i] for i in range(n)]</p>
                <p>This transformation allows us to work with a single array where the original condition can be directly applied.</p>
            </li>
            <li>
                <strong>Step 2: Applying Merge Sort</strong>
                <p>We use a modified merge sort that counts pairs during the merging phase:</p>
                <ul>
                    <li><strong>Recursive Division</strong>: The array is divided into smaller halves recursively until each half has a single element.</li>
                    <li><strong>Count Valid Pairs</strong>: During the merge step, for each element in the left half, we use a pointer to find the first element in the right half that satisfies: diffArr[l] ≤ diffArr[r] + k. For each such valid element diffArr[r], all subsequent elements in the right half are also valid because the array is partially sorted at this stage.</li>
                </ul>
            </li>
            <li>
                <strong>Step 3: Merging and Counting Pairs</strong>
                <p>Here’s how the modified merge step works:</p>
                <ol>
                    <li><strong>Initialization</strong>: Two pointers: l (pointing to the left half) and r (pointing to the right half). As we iterate through elements in the left half using l, we move r to find all right-half elements that satisfy the condition.</li>
                    <li><strong>Counting Valid Pairs</strong>: If diffArr[l] ≤ diffArr[r] + k, all elements from r to the end of the right half (high) are valid. We count all these elements as valid pairs. This is efficient because once a valid r is found, all subsequent elements are automatically valid.</li>
                    <li><strong>Merge the Halves</strong>: After counting, we merge the two halves into a sorted array using the standard merge process.</li>
                </ol>
            </li>
        </ul>
    </li>
</ol>

<p><strong>Code Implementation (Optimized Approach):</strong></p>

```python
def merge(arr,low,mid,high):
    left=low
    right=mid+1
    temp=[]
    while(left<=mid and right<=high):
        if(arr[left] <= arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while(left<=mid):
        temp.append(arr[left])
        left+=1

    while(right<=high):
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i]=temp[i-low]
def countPairs(arr,low,mid,high,k):
    cnt=0
    l=low
    r=mid+1
    while l<=mid and r<=high:
        if arr[l]<=arr[r]+k:
            cnt+=high-r+1
            l+=1
        else:
            r+=1
    return cnt

def mergeSort(arr,low,high,k):
    cnt=0
    if(low>=high):
        return cnt
    mid=(low+high)//2
    cnt+=mergeSort(arr,low,mid,k)
    cnt+=mergeSort(arr,mid+1,high,k)
    cnt+=countPairs(arr,low,mid,high,k)
    merge(arr,low,mid,high)
    return cnt
    


def optimized(n,arr1,arr2,k):
    diffArr=[arr1[i]-arr2[i] for i in range(n)]
    ans=mergeSort(diffArr,0,n-1,k)
    return ans
    
```

<p><strong>Time and Space Complexity (Optimized Approach):</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n log n) due to merge sort.</li>
    <li><strong>Space Complexity:</strong> O(n) for the temporary array used during the merge process.</li>
</ul>


<br>
<br>

<h2>Wonderful Substrings : Count of substring having atmost one odd frequency character.</h2>
<p><strong>Problem Statement</strong><br>
A "wonderful" substring is defined as a substring with at most one character appearing an odd number of times. For example:</p>
<ul>
    <li>"ccjjc" and "abab" are wonderful.</li>
    <li>"ab" is not wonderful since both 'a' and 'b' appear once, which is odd.</li>
</ul>
<p>Given a string <code>word</code> (consisting only of the first ten lowercase English letters 'a' to 'j'), we aim to return the number of non-empty "wonderful" substrings in <code>word</code>, counting each occurrence of the same substring separately if it appears multiple times.</p>

<p><strong>(or)</strong></p>

<p>Given a string, the goal is to count the number of substrings that can be rearranged to form a palindrome.</p>
<p>For a substring to be a valid candidate for rearranging into a palindrome:</p>
<ul>
    <li><strong>If the length of the substring is even</strong>, all characters should have even frequencies.</li>
    <li><strong>If the length is odd</strong>, only one character can have an odd frequency; all others must have even frequencies.</li>
</ul>
<p>Thus, we’re looking for substrings that have at most one character with an odd frequency.</p>


<p><strong>Sample Test Cases</strong></p>

<p><strong>Test Case 1</strong></p>
<p><strong>Input:</strong><br>
<code>word = "ccjjc"</code><br>
<code>n = len(word)</code></p>
<p><strong>Output:</strong><br>
<code>Output: 10</code></p>
<p><strong>Explanation:</strong><br>
The "wonderful" substrings of <code>"ccjjc"</code> are:</p>
<ul>
    <li>Single characters: "c", "c", "j", "j", "c"</li>
    <li>Pairs: "cc", "jj", "jc"</li>
    <li>Larger substrings: "ccj", "cjjc"</li>
</ul>
<p>In total, there are <strong>10</strong> substrings that meet the "wonderful" condition.</p>

<p><strong>Test Case 2</strong></p>
<p><strong>Input:</strong><br>
<code>word = "abab"</code><br>
<code>n = len(word)</code></p>
<p><strong>Output:</strong><br>
<code>Output: 6</code></p>
<p><strong>Explanation:</strong><br>
The "wonderful" substrings of <code>"abab"</code> are:</p>
<ul>
    <li>Single characters: "a", "b", "a", "b"</li>
    <li>Larger substrings: "aba", "bab"</li>
</ul>
<p>In total, there are <strong>6</strong> wonderful substrings.</p>

<p><strong>Test Case 3</strong></p>
<p><strong>Input:</strong><br>
<code>word = "aaa"</code><br>
<code>n = len(word)</code></p>
<p><strong>Output:</strong><br>
<code>Output: 6</code></p>
<p><strong>Explanation:</strong><br>
The "wonderful" substrings of <code>"aaa"</code> are:</p>
<ul>
    <li>Single characters: "a", "a", "a"</li>
    <li>Pairs: "aa", "aa"</li>
    <li>The entire substring: "aaa"</li>
</ul>
<p>In total, there are <strong>6</strong> wonderful substrings.</p>

<p><strong>Test Case 4</strong></p>
<p><strong>Input:</strong><br>
<code>word = "abcd"</code><br>
<code>n = len(word)</code></p>
<p><strong>Output:</strong><br>
<code>Output: 4</code></p>
<p><strong>Explanation:</strong><br>
The "wonderful" substrings of <code>"abcd"</code> are only the single characters:</p>
<ul>
    <li>"a", "b", "c", "d"</li>
</ul>
<p>Since each character appears once, these are the only substrings that satisfy the condition.</p>

<p><strong>Test Case 5</strong></p>
<p><strong>Input:</strong><br>
<code>word = "aaabaaa"</code><br>
<code>n = len(word)</code></p>
<p><strong>Output:</strong><br>
<code>Output: 15</code></p>
<p><strong>Explanation:</strong><br>
The "wonderful" substrings of <code>"aaabaaa"</code> include:</p>
<ul>
    <li>Single characters: "a", "a", "a", "b", "a", "a", "a"</li>
    <li>Pairs: "aa", "aa", "ba", "aa", "aa"</li>
    <li>Larger substrings: "aaa", "aabaa", "aaabaa", "aaabaaa"</li>
</ul>
<p>In total, there are <strong>15</strong> substrings that meet the "wonderful" condition.</p>

<p><strong>Approach 1: Brute Force</strong></p>

<p><strong>Intuition</strong><br>
To solve this problem using a brute-force approach:</p>
<ol>
    <li>Consider all possible substrings of the given word.</li>
    <li>For each substring, check if it meets the condition (at most one character appears an odd number of times).</li>
    <li>Count all substrings that meet this "wonderful" condition.</li>
</ol>

<p><strong>Steps to Solve</strong></p>
<ol>
    <li>Loop through every possible starting index of a substring (<code>i</code>).</li>
    <li>For each <code>i</code>, loop through every possible ending index (<code>j</code>).</li>
    <li>Within the substring <code>word[i:j+1]</code>, count the frequency of each character.</li>
    <li>Check the number of characters with odd frequencies (<code>oddCnt</code>). If <code>oddCnt <= 1</code>, count this substring as "wonderful."</li>
    <li>Return the count of "wonderful" substrings.</li>
</ol>

<p><strong>Code</strong></p>

```python
from collections import defaultdict
def bruteForce(n,word):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            freq=defaultdict(int)
            for k in range(i,j+1):
                freq[word[k]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                cnt+=1
    return cnt
```

<p><strong>Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <code>O(n^3)</code> due to three nested loops.</li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code> additional space for counting characters.</li>
</ul>

<p><strong>Approach 2: Better Approach</strong></p>

<p><strong>Intuition</strong><br>
Instead of recalculating character frequencies from scratch for each substring, maintain a running frequency dictionary from each starting index <code>i</code>. This way, we only add one character at a time, reducing redundant calculations.</p>

<p><strong>Steps to Solve</strong></p>
<ol>
    <li>Loop through each starting index <code>i</code>.</li>
    <li>Initialize a frequency dictionary for tracking character frequencies.</li>
    <li>For each ending index <code>j</code> starting from <code>i</code>, increment the frequency of <code>word[j]</code>.</li>
    <li>Check if the current substring has at most one odd frequency. If so, count it as "wonderful."</li>
    <li>Continue to the next starting index after processing all substrings starting from <code>i</code>.</li>
</ol>

<p><strong>Code</strong></p>

```python
def better(n,word):
    cnt=0
    for i in range(n):
        freq=defaultdict(int)
        for j in range(i,n):
            freq[word[j]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                cnt+=1
    return cnt
```

<p><strong>Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <code>O(n^2)</code>, as we reduced the nested loops from three to two.</li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code>, constant space for frequency dictionary.</li>
</ul>

<p><strong>Optimized Approach</strong></p>
<p>In this problem, we need to find substrings with atmost one odd charcter. that means we can have</p>
<ul>
    <li>Substrings can have even frequency of charcters</li>
    <li>Substrings can have one odd charcter frequency</li>
</ul>
<p>To solve this problem, we can track frequency of each charcter like above approaches, and check if it is satisfying requirement.</p>
<p>We can Divide this problem into two things</p>
<p><strong>Even frequency substrings</strong></p>
<p>As we are traversing through given string, we can track the count of each character up till current position</p>
<p>Since we are taking care of odd or even only, we can represent</p>
<ul>
    <li>Odd Frequency With -> 1</li>
    <li>Even Frequency With -> 0</li>
</ul>
<p>For example, in the string "aabacacabc", if we track each character frequency, it will be as follows</p>

<table>
  <tr>
    <th>Index</th>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
    <td>9</td>
  </tr>
  <tr>
    <th>Character</th>
    <td>a</td>
    <td>a</td>
    <td>b</td>
    <td>a</td>
    <td>c</td>
    <td>a</td>
    <td>c</td>
    <td>a</td>
    <td>b</td>
    <td>c</td>
  </tr>
  <tr>
    <th>Prefix - 'a'</th>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <th>Prefix - 'b'</th>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <th>Prefix - 'c'</th>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
  </tr>
</table>

<p><strong>Explanation</strong></p>

<ul>
  <li>Each row under <strong>Prefix - 'x'</strong> shows a binary value (0 or 1) that indicates whether the count of that character up to that point is <strong>even (0)</strong> or <strong>odd (1)</strong>.</li>
  <li><strong>Prefix - 'a'</strong>: Tracks the parity of the count of 'a'.</li>
  <li><strong>Prefix - 'b'</strong>: Tracks the parity of the count of 'b'.</li>
  <li><strong>Prefix - 'c'</strong>: Tracks the parity of the count of 'c'.</li>
</ul>

<ol>
  <li>For instance, at index 7, the prefix for <strong>'a'</strong>, <strong>'b'</strong>, and <strong>'c'</strong> is <strong>1 1 0</strong>, which means:</li>
  <ul>
    <li>'a' and 'b' appear an odd number of times up to that index.</li>
    <li>'c' appears an even number of times up to that index.</li>
  </ul>
</ol>
<p>As mentioned in the above table, at any index, if the current frequency pattern occurs the same as a previous prefix pattern, then removing that previously existing pattern will result in a substring with an even frequency for all characters.</p>

<p><strong>Example</strong></p>

<ul>
  <li>Consider the string <strong>"aabacacabc"</strong>.</li>
  <li>Let's say we have tracked the prefix patterns up to index 7, where the prefix pattern (or binary representation of frequencies) is <strong>b110</strong>, meaning:</li>
  <ul>
    <li><strong>'a'</strong> and <strong>'b'</strong> have an odd count up to index 7.</li>
    <li><strong>'c'</strong> has an even count up to index 7.</li>
  </ul>
  <li>Now, if we find that this prefix pattern <strong>b110</strong> has already been encountered at a previous index, say index 3, it indicates that the substring between indices 4 and 7 has all characters with even frequencies.</li>
</ul>

<p><strong>Why?</strong></p>

<ul>
  <li>Because the same prefix pattern at two different indices means that removing the substring between them gives us a balanced frequency count for each character.</li>
  <li>So, any substring between two identical prefix patterns will have <strong>even frequencies</strong> for all characters, as these repeated patterns cancel out any odd counts in between.</li>
</ul>

<p>This principle allows us to quickly identify even-frequency substrings by using prefix patterns efficiently, without checking each substring individually.</p>

<p><strong>One Odd Frequency</strong></p>
<p>Just like in the even frequency case, if we find that the current prefix pattern differs by exactly one bit from a previously seen pattern, then removing the substring between these two indices will result in a substring where only one character has an odd frequency, while all others have even frequencies.</p>

<p><strong>Example</strong></p>

<ul>
  <li>Consider the string <strong>"aabacacabc"</strong>.</li>
  <li>Let’s say that at index 7, we have a prefix pattern represented as <strong>b110</strong> (meaning:</li>
  <ul>
    <li><strong>'a'</strong> and <strong>'b'</strong> have an odd count up to index 7.</li>
    <li><strong>'c'</strong> has an even count up to index 7.</li>
  </ul>
  <li>Now, we can check if there exists any previous prefix pattern that differs from <strong>b110</strong> by only one bit.</li>
</ul>

<p><strong>How Does This Work?</strong></p>

<ul>
  <li>If we find a previous pattern that differs by one bit, say <strong>b010</strong>, it would mean:</li>
  <ul>
    <li>The substring between these two points will have the same even/odd frequency for each character, except for one specific character, which will appear an odd number of times.</li>
  </ul>
  <li>In this case, the resulting substring will have <strong>only one character with an odd frequency</strong>, meeting the "at most one odd" requirement.</li>
</ul>

<p>This technique allows us to efficiently find substrings with exactly one odd frequency by comparing the current prefix pattern with past patterns that differ by one bit, without manually counting frequencies for each character in each substring.</p>

<p>So, now we got some approach to solve problem</p>
<p>Inorder to achieve above table, we can use bit manipulation</p>
<p>We can assign specific bit position to represent unique character like as follows</p>
<ul>
    <li>a -> 0000000001</li>
    <li>b -> 0000000010</li>
    <li>c -> 0000000100</li>
    <li>d -> 0000001000</li>
    <li>e -> 0000010000</li>
    <li>f -> 0000100000</li>
    <li>g -> 0001000000</li>
    <li>h -> 0010000000</li>
    <li>i -> 0100000000</li>
    <li>j -> 1000000000</li>
    <li>....so on</li>
</ul>
<p>since this problem deals with a-j, we can track only above bits</p>
<p>This particular pattern we can get using left shift</p>

```python
print(1<<0) #1
print(1<<1) #10
print(1<<2) #100

print(1<<(ord(word[i])-ord('a'))) # we can use this while iterating in word
```
<p>We can use XOR operation , to track frequnecy for each character at each position</p>
<p><strong>Example:</strong> For the string <strong>"aabac"</strong>:</p>

<ul>
  <li>Starting with a bit mask of <strong>0</strong> (all bits are 0 initially).</li>
  <li>At each character, we toggle the bit for that character using XOR.</li>
  <li>Let’s go through each character and update the bit mask:</li>
  <ul>
    <li><strong>Character 'a' (index 0)</strong>: Toggle the 0th bit → bit mask becomes <strong>b0001</strong>.</li>
    <li><strong>Character 'a' (index 1)</strong>: Toggle the 0th bit again → bit mask becomes <strong>b0000</strong> (even count of 'a').</li>
    <li><strong>Character 'b' (index 2)</strong>: Toggle the 1st bit → bit mask becomes <strong>b0010</strong>.</li>
    <li><strong>Character 'a' (index 3)</strong>: Toggle the 0th bit → bit mask becomes <strong>b0011</strong>.</li>
    <li><strong>Character 'c' (index 4)</strong>: Toggle the 2nd bit → bit mask becomes <strong>b0111</strong>.</li>
  </ul>
</ul>
<p>So, by the end of "aabac", our bit mask is <strong>b0111</strong>, meaning that:</p>

<ul>
  <li><strong>'a'</strong>, <strong>'b'</strong>, and <strong>'c'</strong> have odd counts.</li>
</ul>

<p><strong>2. Using XOR to Track Frequency Changes</strong></p>

<ul>
  <li>As seen in the example above, XOR allows us to toggle the specific bit for a character.</li>
  <li>When we encounter a character, we use XOR to switch its bit:</li>
  <ul>
    <li>If the bit was 0 (even count), XOR will make it 1 (odd count).</li>
    <li>If the bit was 1 (odd count), XOR will make it 0 (even count).</li>
  </ul>
</ul>
<p>This will create same pattern as above table</p>
<p><strong>Why XOR is Useful:</strong></p>
<ul>
  <li>Using XOR to toggle bits means that, as we go through the string, we only need one variable (the bit mask) to keep track of the entire pattern of even/odd frequencies.</li>
  <li>This bit mask is enough to quickly check if we’ve seen the same frequency pattern before, or one that differs by one bit, allowing us to efficiently count valid substrings without re-checking character frequencies manually.</li>
</ul>

<p>This function <code>optimized(n, word)</code> counts the number of substrings in <code>word</code> where at most one character appears an odd number of times. Let's break down each part to understand how it works.</p>

<p><strong>Step-by-Step Explanation</strong></p>

<ol>
  <li>
    <p><strong>Initialize Variables:</strong></p>
    <code>
      ans = 0<br>
      prefix = {}<br>
      prefix[0] = 1<br>
      currentXor = 0
    </code>
    <ul>
      <li><code>ans</code>: This variable stores the total count of valid substrings.</li>
      <li><code>prefix</code>: This dictionary keeps track of previously seen bit masks (or frequency patterns) and their counts.</li>
      <li><code>prefix[0] = 1</code>: We initialize <code>prefix[0]</code> to 1 to handle cases where a valid substring starts from the beginning of <code>word</code>.</li>
      <li><code>currentXor</code>: This variable will store the bit mask representing the even/odd frequency pattern for characters up to the current position.</li>
    </ul>
  </li>
  
  <li>
    <p><strong>Loop Through Each Character in the Word:</strong></p>
    <code>for i in range(n):</code>
    <ul>
      <li>For each character in <code>word</code>, we update the <code>currentXor</code> bit mask to track the frequency pattern up to that point.</li>
    </ul>
  </li>

  <li>
    <p><strong>Calculate the Bit Mask for the Current Character:</strong></p>
    <code>
      mask = 1 << (ord(word[i]) - ord('a'))<br>
      currentXor ^= mask
    </code>
    <ul>
      <li><code>mask</code> is calculated by shifting <code>1</code> to the left by <code>(ord(word[i]) - ord('a'))</code> positions. This shifts the bit corresponding to the current character to its unique position in the 26-bit representation for lowercase letters.</li>
      <li><code>currentXor ^= mask</code> uses XOR to toggle the bit for the current character:</li>
      <ul>
        <li>If the bit is 0, XOR makes it 1 (odd count).</li>
        <li>If the bit is 1, XOR makes it 0 (even count).</li>
      </ul>
    </ul>
  </li>

  <li>
    <p><strong>Check for Substrings with All Characters Having Even Frequencies:</strong></p>
    <code>
      if currentXor in prefix:<br>
          ans += prefix[currentXor]
    </code>
    <ul>
      <li>If <code>currentXor</code> has been seen before in <code>prefix</code>, it means we’ve encountered the same frequency pattern at a previous position.</li>
      <li>We add <code>prefix[currentXor]</code> to <code>ans</code>, which counts the number of valid even-frequency substrings ending at this position.</li>
    </ul>
  </li>

  <li>
    <p><strong>Check for Substrings with Exactly One Odd Frequency:</strong></p>
    <code>
      for k in range(10):<br>
          mask = 1 << k<br>
          oddXor = currentXor ^ mask<br>
          if oddXor in prefix:<br>
              ans += prefix[oddXor]
    </code>
    <ul>
      <li>For each possible character (from 'a' to 'j'), we calculate <code>oddXor</code>, which represents a frequency pattern where only one character has an odd count.</li>
      <li><code>oddXor = currentXor ^ mask</code> toggles each bit individually, simulating one character having an odd count.</li>
      <li>If this <code>oddXor</code> pattern exists in <code>prefix</code>, it means we have valid substrings with exactly one odd-frequency character, so we add <code>prefix[oddXor]</code> to <code>ans</code>.</li>
    </ul>
  </li>

  <li>
    <p><strong>Update the Prefix Dictionary:</strong></p>
    <code>
      if currentXor in prefix:<br>
          prefix[currentXor] += 1<br>
      else:<br>
          prefix[currentXor] = 1
    </code>
    <ul>
      <li>Finally, we update <code>prefix</code> to record the current bit mask <code>currentXor</code>.</li>
      <li>If <code>currentXor</code> is already in <code>prefix</code>, we increment its count by 1; otherwise, we set it to 1.</li>
    </ul>
  </li>

  <li>
    <p><strong>Return the Answer:</strong></p>
    <code>return ans</code>
    <ul>
      <li>After processing all characters, <code>ans</code> contains the total number of valid substrings where at most one character appears an odd number of times.</li>
    </ul>
  </li>
</ol>

<p><strong>Summary of Logic</strong></p>

<ul>
  <li><strong>Bit Mask with XOR</strong>: Each character toggles its bit in <code>currentXor</code>, giving us an efficient way to track even/odd frequency patterns.</li>
  <li><strong>Prefix Dictionary</strong>: By keeping track of previously seen patterns in <code>prefix</code>, we can check for valid substrings with all even frequencies or with exactly one odd frequency in constant time.</li>
  <li><strong>Efficient Substring Counting</strong>: Instead of counting characters in each substring individually, we use bit masks and XOR to quickly calculate valid substrings.</li>
</ul>

<p><strong>Code</strong></p>

```python
def optimized(n,word):
    ans=0
    prefix={}
    prefix[0]=1
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(currentXor in prefix):
            ans+=prefix[currentXor] # for adding even subtring count
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if oddXor in prefix:
                ans+=prefix[oddXor] # for adding one odd subtring count
        if(currentXor in prefix):
            prefix[currentXor]+=1
        else:
            prefix[currentXor]=1
    return ans
```

<p><strong>Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code>, since we process each character once.</li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code>, with fixed-size prefix array for tracking.</li>
</ul>


<p><strong>Space Optimized Approach</strong></p>

<p>Instead of using map, we can use an array</p>
<p>Since max xor value can be, 1111111111 , if all charcters are unique</p>
<p>So, we can have array of size 1<<10 (10000000000), then we can store all values</p>

<p><strong>Code</strong></p>

```python
def optimized2(n,word):
    ans=0
    prefix=[None]*1024 # at most j(9 position), so max value 1<<10 == 1024
    prefix[0]=1
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(prefix[currentXor] is not None):
            ans+=prefix[currentXor] # for adding even subtring count
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if prefix[oddXor] is not None:
                ans+=prefix[oddXor] # for adding one odd subtring count
        if(prefix[currentXor] is not None):
            prefix[currentXor]+=1
        else:
            prefix[currentXor]=1
    return ans
```

<p><strong>Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code>, since we process each character once.</li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code>, with fixed-size prefix array for tracking.</li>
</ul>


<br>
<br>

<h2>Find All Substrings Having Atmost Having One Odd Charcter Frequency</h2>
<p>It is similar to previous problem, here we are printing all substrings instead of counting</p>
<p>So, here we have to track indices and print that substring</p>

<p><strong>Code</strong></p>

```python
from collections import defaultdict
def bruteForce(n,word):
    ans=[]
    for i in range(n):
        for j in range(i,n):
            freq=defaultdict(int)
            for k in range(i,j+1):
                freq[word[k]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                ans.append(word[i:j+1])
    return sorted(ans)

def better(n,word):
    ans=[]
    for i in range(n):
        freq=defaultdict(int)
        for j in range(i,n):
            freq[word[j]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                ans.append(word[i:j+1])
    return sorted(ans)

def optimized(n,word):
    ans=[]
    prefix={}
    prefix[0]=[-1]
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(currentXor in prefix):
            for j in prefix[currentXor]:
                ans.append(word[j+1:i+1])
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if oddXor in prefix:
                for j in prefix[oddXor]:
                    ans.append(word[j+1:i+1])
        if(currentXor in prefix):
            prefix[currentXor].append(i)
        else:
            prefix[currentXor]=[i]
    return sorted(ans)

def optimized2(n,word):
    ans=[]
    prefix=[None]*1024 # at most j(9 position), so max value 1<<10 == 1024
    prefix[0]=[-1]
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(prefix[currentXor] is not None):
            for j in prefix[currentXor]:
                ans.append(word[j+1:i+1])
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if(prefix[oddXor] is not None):
                for j in prefix[oddXor]:
                    ans.append(word[j+1:i+1])
        if(prefix[currentXor] is not None):
            prefix[currentXor].append(i)
        else:
            prefix[currentXor]=[i]
    return sorted(ans)
            

word=input()
n=len(word)
print(bruteForce(n,word))
print(better(n,word))
print(optimized(n,word))
print(optimized2(n,word))

```

<br>
<br>

<h2>Largest Substring Having At Most One Odd Charcter Frequency</h2>
<p>It is also similar to previous problem, here we are just fiding length of longest substring</p>
<p><strong>Problem Statement</strong></p>
<p>Given a string <code>s</code>, an "awesome" substring is defined as a substring that can be rearranged into a palindrome by swapping its characters. The task is to return the length of the longest awesome substring in <code>s</code>.</p>

<p><strong>Sample Test Cases</strong></p>

<p><strong>Input :</strong>s = "3242415"</p>
<p><strong>Output :</strong>5</p>
<p><strong>Explanation :</strong>"24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.</p>

<p><strong>Input :</strong>s = "12345678"</p>
<p><strong>Output :</strong>1</p>

<p><strong>Input :</strong>s = "213123"</p>
<p><strong>Output :</strong>6</p>
<p><strong>Explanation :</strong>"213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.</p>


<p><strong>Approaches</strong></p>

<p><strong>1. Brute Force Approach</strong></p>
<p>This approach uses a nested loop to consider all possible substrings and checks each for palindrome potential by counting character frequencies.</p>

<p><strong>Steps</strong></p>
<ol>
    <li>Loop through each starting index <code>i</code> of the substring.</li>
    <li>For each <code>i</code>, loop through every ending index <code>j</code>.</li>
    <li>Within the substring <code>s[i:j+1]</code>, count the frequency of each character using a dictionary.</li>
    <li>Count characters with odd frequencies.</li>
    <li>If there’s at most one odd frequency, calculate the substring length and update the maximum length if this substring is longer.</li>
    <li>Return the maximum length found.</li>
</ol>

<p><strong>Code</strong></p>

```python
from collections import defaultdict
def bruteForce(n,word):
    ans=0
    for i in range(n):
        for j in range(i,n):
            freq=defaultdict(int)
            for k in range(i,j+1):
                freq[word[k]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                length=j-i+1
                ans=max(ans,length)
    return ans
```

<p><strong>Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <code>O(n^3)</code> due to three nested loops.</li>
    <li><strong>Space Complexity:</strong> <code>O(n)</code> for the frequency dictionary.</li>
</ul>

<p><strong>2. Better Approach</strong></p>
<p>This approach reduces the number of redundant computations by maintaining a running frequency dictionary from each starting index <code>i</code>.</p>

<p><strong>Steps</strong></p>
<ol>
    <li>Loop through each starting index <code>i</code>.</li>
    <li>Maintain a dictionary <code>freq</code> for character frequencies.</li>
    <li>For each ending index <code>j</code> starting from <code>i</code>, update <code>freq</code> with the character at <code>s[j]</code>.</li>
    <li>Count characters with odd frequencies.</li>
    <li>If there’s at most one odd frequency, calculate the substring length and update the maximum length if this substring is longer.</li>
    <li>Return the maximum length found.</li>
</ol>

<p><strong>Code</strong></p>

```python
from collections import defaultdict
def better(n,word):
    ans=0
    for i in range(n):
        freq=defaultdict(int)
        for j in range(i,n):
            freq[word[j]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                length=j-i+1
                ans=max(ans,length)
    return ans
```

<p><strong>Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <code>O(n^2)</code> due to two nested loops.</li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code> for the frequency dictionary.</li>
</ul>

<p><strong>3. Optimized Approach</strong></p>
<p>This approach leverages the XOR bit manipulation trick to track even and odd character counts more efficiently using a "mask" that represents each character's occurrence count.</p>

<p>Here we are just tracking first occurance xor pattern, so that we can track largest length</p>

<p><strong>Steps</strong></p>
<ol>
    <li>Initialize a prefix dictionary <code>prefix</code> to store XOR results with the starting index <code>-1</code>.</li>
    <li>Use <code>currentXor</code> to track the cumulative XOR of characters.</li>
    <li>For each character, update <code>currentXor</code> using its mask.</li>
    <li>If <code>currentXor</code> exists in <code>prefix</code>, compute the substring length and update the maximum length.</li>
    <li>For each bit, check if toggling that bit in <code>currentXor</code> yields a value in <code>prefix</code> (allows for one odd frequency).</li>
    <li>Update <code>prefix</code> with <code>currentXor</code> if it doesn’t already exist.</li>
</ol>

<p><strong>Code</strong></p>

```python
def optimized(n,word):
    ans=0
    prefix={}
    prefix[0]=-1
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(currentXor in prefix):
            length=i-prefix[currentXor]
            ans=max(ans,length)
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if oddXor in prefix:
                length=i-prefix[oddXor]
                ans=max(ans,length)
        if(currentXor not in prefix):
            prefix[currentXor]=i
    return ans
```

<p><strong>Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code> as each character is processed once.</li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code> with fixed-size prefix dictionary.</li>
</ul>

<p><strong>4. More Optimized Approach</strong></p>
<p>This approach optimizes further by using a fixed-size list for tracking XOR prefixes up to 1024, as the mask for each character fits in a 10-bit integer.</p>

<p><strong>Steps</strong></p>
<ol>
    <li>Initialize a list <code>prefix</code> of size 1024 for XOR results.</li>
    <li>Use <code>currentXor</code> to track the cumulative XOR.</li>
    <li>For each character, update <code>currentXor</code> with its mask.</li>
    <li>Check if <code>currentXor</code> has been encountered before in <code>prefix</code>, and update <code>ans</code> if it gives a longer substring.</li>
    <li>For each bit, toggle the bit in <code>currentXor</code> and check if it’s in <code>prefix</code> (for one odd character).</li>
    <li>Update <code>prefix</code> with the current XOR if it’s the first time seeing it.</li>
</ol>

<p><strong>Code</strong></p>

```python
def optimized2(n,word):
    ans=0
    prefix=[None]*1024 # at most j(9 position), so max value 1<<10 == 1024
    prefix[0]=-1
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(prefix[currentXor] is not None):
            length=i-prefix[currentXor]
            ans=max(ans,length)
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if prefix[oddXor] is not None:
                length=i-prefix[oddXor]
                ans=max(ans,length)
        if(prefix[currentXor] is None):
            prefix[currentXor]=i
    return ans
```


<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code> as each character is processed once.</li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code> with fixed-size prefix array.</li>
</ul>

<br>
<br>

<h2>Smallest Substring Having Atmost One Odd Charcter Frequency</h2>
<p>It is simlar to previous problem, here we are finding length of smallest substring</p>

<p><strong>Code</strong></p>

```python
from collections import defaultdict
def bruteForce(n,word):
    ans=n+1
    for i in range(n):
        for j in range(i,n):
            freq=defaultdict(int)
            for k in range(i,j+1):
                freq[word[k]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                length=j-i+1
                ans=min(ans,length)
    return ans

def better(n,word):
    ans=n+1
    for i in range(n):
        freq=defaultdict(int)
        for j in range(i,n):
            freq[word[j]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                length=j-i+1
                ans=min(ans,length)
    return ans


#We can track latest position of xor pattern, so that we can track smallest length

def optimized(n,word):
    ans=n+1
    prefix={}
    prefix[0]=-1
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(currentXor in prefix):
            length=i-prefix[currentXor]
            ans=min(ans,length)
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if oddXor in prefix:
                length=i-prefix[oddXor]
                ans=min(ans,length)
        prefix[currentXor]=i
    return ans

def optimized2(n,word):
    ans=n+1
    prefix=[None]*1024 # at most j(9 position), so max value 1<<10 == 1024
    prefix[0]=-1
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(prefix[currentXor] is not None):
            length=i-prefix[currentXor]
            ans=min(ans,length)
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if prefix[oddXor] is not None:
                length=i-prefix[oddXor]
                ans=min(ans,length)
        prefix[currentXor]=i
    return ans
            

word=input()
n=len(word)
print(bruteForce(n,word))
print(better(n,word))
print(optimized(n,word))
print(optimized2(n,word))
```

<br>
<br>

<h2>Find the Longest Substring Containing Vowels in Even Count</h2>
<p><strong>Problem Statement</strong></p>
<p>Given the string <code>s</code>, return the size of the longest substring containing each vowel an even number of times. The vowels are 'a', 'e', 'i', 'o', and 'u'.</p>

<p><strong>Example Test Cases</strong></p>
<ul>
    <li><strong>Example 1:</strong></li>
    <ul>
        <li><strong>Input:</strong> <code>s = "eleetminicoworoep"</code></li>
        <li><strong>Output:</strong> <code>13</code></li>
        <li><strong>Explanation:</strong> The longest substring is "leetminicowor" which contains two each of the vowels: e, i, and o, and zero of the vowels: a and u.</li>
    </ul>
    <li><strong>Example 2:</strong></li>
    <ul>
        <li><strong>Input:</strong> <code>s = "leetcodeisgreat"</code></li>
        <li><strong>Output:</strong> <code>5</code></li>
        <li><strong>Explanation:</strong> The longest substring is "leetc" which contains two e's.</li>
    </ul>
    <li><strong>Example 3:</strong></li>
    <ul>
        <li><strong>Input:</strong> <code>s = "bcbcbc"</code></li>
        <li><strong>Output:</strong> <code>6</code></li>
        <li><strong>Explanation:</strong> In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o, and u appear zero times.</li>
    </ul>
</ul>

<p><strong>Approaches</strong></p>

<p><strong>1. Brute Force Approach</strong></p>
<p>This approach checks all possible substrings and counts the occurrences of vowels.</p>

<p><strong>Steps</strong></p>
<ol>
    <li>Loop through each starting index <code>i</code>.</li>
    <li>For each starting index, loop through each ending index <code>j</code>.</li>
    <li>Count the occurrences of each vowel in the substring <code>s[i:j+1]</code>.</li>
    <li>Check if all vowels have even counts.</li>
    <li>If yes, update the maximum length of valid substrings found.</li>
    <li>Return the maximum length.</li>
</ol>

<p><strong>Code</strong></p>

```python
def bruteForce(n,word):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            cntVowels={k:0 for k in 'aeiou'}
            for k in range(i,j+1):
                if(word[k] in 'aeiou'):
                    cntVowels[word[k]]+=1
            flag=True
            for ch,cnt in cntVowels.items():
                if(cnt%2!=0):
                    flag=False
                    break
            if(flag):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi
```

<p><strong>Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <code>O(n^3)</code> due to three nested loops.</li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code> for the vowel count dictionary.</li>
</ul>

<p><strong>2. Better Approach</strong></p>
<p>This approach reduces redundant computations by maintaining a running frequency dictionary from each starting index <code>i</code>.</p>

<p><strong>Steps</strong></p>
<ol>
    <li>Loop through each starting index <code>i</code>.</li>
    <li>Maintain a dictionary <code>cntVowels</code> for character frequencies.</li>
    <li>For each ending index <code>j</code> starting from <code>i</code>, update <code>cntVowels</code> with the character at <code>s[j]</code>.</li>
    <li>Check if all vowels have even counts.</li>
    <li>If yes, update the maximum length found.</li>
    <li>Return the maximum length.</li>
</ol>

<p><strong>Code</strong></p>

```python
def better(n,word):
    maxi=0
    for i in range(n):
        cntVowels={k:0 for k in 'aeiou'}
        for j in range(i,n):
            if(word[j] in 'aeiou'):
                cntVowels[word[j]]+=1
            flag=True
            for ch,cnt in cntVowels.items():
                if(cnt%2!=0):
                    flag=False
                    break
            if(flag):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi
```

<p><strong>Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <code>O(n^2)</code> due to two nested loops.</li>
    <li><strong>Space Complexity:</strong> <code>O(1)</code> for the vowel count dictionary.</li>
</ul>

<p><strong>3. Optimized Approach</strong></p>
<p>This approach leverages bit manipulation to track the even and odd occurrences of vowels more efficiently using a mask.</p>

<p>It is similar to wonderful substrings, where we are tracking every character, but here we will take care of only vowels</p>

<p><strong>Steps</strong></p>
<ol>
    <li>Initialize a prefix dictionary to store XOR results with the starting index <code>-1</code>.</li>
    <li>Use <code>currentXor</code> to track the cumulative XOR of vowel occurrences.</li>
    <li>For each character, if it is a vowel, update <code>currentXor</code> using its mask.</li>
    <li>Check if <code>currentXor</code> exists in the prefix; if so, compute the substring length.</li>
    <li>For each bit (representing vowels), toggle it in <code>currentXor</code> and check if the resulting value has been seen before.</li>
    <li>Update the prefix with <code>currentXor</code> if it’s the first time seeing it.</li>
</ol>

<p><strong>Code</strong></p>

```python
def optimized(n,word):
    prefix={0:-1}
    currentXor=0
    maxi=0
    for i in range(n):
        if(word[i] in 'aeiou'):
            mask=1<<(ord(word[i])-ord('a'))
            currentXor^=mask
        if(currentXor in prefix):
            length=i-prefix[currentXor]
            maxi=max(maxi,length)
        if(currentXor not in prefix):
            prefix[currentXor]=i
    return maxi
```

<p><strong>Complexity</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <code>O(n)</code> due to a single loop.</li>
    <li><strong>Space Complexity:</strong> <code>O(n)</code> for the prefix dictionary in the worst case.</li>
</ul>

<br>
<br>

<h2>Smallest Substring Containing Vowels in Even Counts</h2>
<p>It is similar to previous problem, but here we are tracking length of smallest substring</p>

<p><strong>Code</strong></p>

```python
def bruteForce(n,word):
    mini=n+1
    for i in range(n):
        for j in range(i,n):
            cntVowels={k:0 for k in 'aeiou'}
            for k in range(i,j+1):
                if(word[k] in 'aeiou'):
                    cntVowels[word[k]]+=1
            flag=True
            for ch,cnt in cntVowels.items():
                if(cnt%2!=0):
                    flag=False
                    break
            if(flag):
                length=j-i+1
                mini=min(mini,length)
    return mini

def better(n,word):
    mini=n+1
    for i in range(n):
        cntVowels={k:0 for k in 'aeiou'}
        for j in range(i,n):
            if(word[j] in 'aeiou'):
                cntVowels[word[j]]+=1
            flag=True
            for ch,cnt in cntVowels.items():
                if(cnt%2!=0):
                    flag=False
                    break
            if(flag):
                length=j-i+1
                mini=min(mini,length)
    return mini

def optimized(n,word):
    prefix={0:-1}
    currentXor=0
    mini=n+1
    for i in range(n):
        if(word[i] in 'aeiou'):
            mask=1<<(ord(word[i])-ord('a'))
            currentXor^=mask
        if(currentXor in prefix):
            length=i-prefix[currentXor]
            mini=min(mini,length)
        prefix[currentXor]=i
    return mini
word=input()
n=len(word)
print(bruteForce(n,word))
print(better(n,word))
print(optimized(n,word))
```

<br>
<br>

<h2>Count Of Substrings Having Even Number Of Vowels</h2>
<p>It is similar to previous problem, but here finding count of all possible substrings</p>

<p><strong>Code</strong></p>

```python
def bruteForce(n,word):
    ans=0
    for i in range(n):
        for j in range(i,n):
            cntVowels={k:0 for k in 'aeiou'}
            for k in range(i,j+1):
                if(word[k] in 'aeiou'):
                    cntVowels[word[k]]+=1
            flag=True
            for ch,cnt in cntVowels.items():
                if(cnt%2!=0):
                    flag=False
                    break
            if(flag):
                ans+=1
    return ans

def better(n,word):
    ans=0
    for i in range(n):
        cntVowels={k:0 for k in 'aeiou'}
        for j in range(i,n):
            if(word[j] in 'aeiou'):
                cntVowels[word[j]]+=1
            flag=True
            for ch,cnt in cntVowels.items():
                if(cnt%2!=0):
                    flag=False
                    break
            if(flag):
                ans+=1
    return ans

def optimized(n,word):
    prefix={0:1}
    currentXor=0
    cnt=0
    for i in range(n):
        if(word[i] in 'aeiou'):
            mask=1<<(ord(word[i])-ord('a'))
            currentXor^=mask
        if(currentXor in prefix):
            cnt+=prefix[currentXor]
        if(currentXor in prefix):
            prefix[currentXor]+=1
        else:
            prefix[currentXor]=1
    return cnt
word=input()
n=len(word)
print(bruteForce(n,word))
print(better(n,word))
print(optimized(n,word))
```

<br>
<br>

<h2>Print All SubStrings Having Even Count Of Vowels</h2>
<p>It is similar to previous problem, here we are printing all possible substrings</p>

<p><strong>Code</strong></p>

```python
def bruteForce(n,word):
    ans=[]
    for i in range(n):
        for j in range(i,n):
            cntVowels={k:0 for k in 'aeiou'}
            for k in range(i,j+1):
                if(word[k] in 'aeiou'):
                    cntVowels[word[k]]+=1
            flag=True
            for ch,cnt in cntVowels.items():
                if(cnt%2!=0):
                    flag=False
                    break
            if(flag):
                ans.append(word[i:j+1])
    return sorted(ans)

def better(n,word):
    ans=[]
    for i in range(n):
        cntVowels={k:0 for k in 'aeiou'}
        for j in range(i,n):
            if(word[j] in 'aeiou'):
                cntVowels[word[j]]+=1
            flag=True
            for ch,cnt in cntVowels.items():
                if(cnt%2!=0):
                    flag=False
                    break
            if(flag):
                ans.append(word[i:j+1])
    return sorted(ans)

def optimized(n,word):
    prefix={0:[-1]}
    currentXor=0
    ans=[]
    for i in range(n):
        if(word[i] in 'aeiou'):
            mask=1<<(ord(word[i])-ord('a'))
            currentXor^=mask
        if(currentXor in prefix):
            for j in prefix[currentXor]:
                ans.append(word[j+1:i+1])
        if(currentXor in prefix):
            prefix[currentXor].append(i)
        else:
            prefix[currentXor]=[i]
    return sorted(ans)
word=input()
n=len(word)
print(bruteForce(n,word))
print(better(n,word))
print(optimized(n,word))
```

<br>
<br>

<h2>Prefix Sum 2D</h2>
<p><strong>2D Prefix Sum</strong> is a method used to quickly calculate the sum of elements within any sub-rectangle (subset) of a 2D matrix. By creating a new matrix, called the <strong>prefix sum matrix</strong>, we can access these sums without repeatedly adding up elements from the original matrix. This approach is especially useful when we need to perform multiple sum queries on the same matrix.</p>

<p><strong>Step-by-Step Explanation of 2D Prefix Sum</strong></p>

<ol>
    <li>
        <strong>Definition of Prefix Sum Matrix:</strong>
        <ul>
            <li>A <strong>prefix sum matrix</strong> is a new matrix where each element at position (i, j) represents the sum of all elements in the original matrix from the top-left corner (0,0) to that position (i, j).</li>
            <li>Each cell in the prefix sum matrix contains the cumulative sum of all cells to its left, above it, and at its position in the original matrix.</li>
        </ul>
    </li>
    <li>
        <strong>Goal of Using 2D Prefix Sum:</strong>
        <ul>
            <li>To quickly compute the sum of elements in any rectangular area within the matrix without recalculating from scratch each time.</li>
            <li>This is particularly efficient for matrices with large dimensions or when there are many queries to handle.</li>
        </ul>
    </li>
</ol>

<p><strong>Constructing the Prefix Sum Matrix</strong></p>

<p>Given a matrix <strong>matrix</strong> with dimensions <em>n x m</em>, we create a new matrix <strong>prefix</strong> with the same dimensions. We fill each cell in the prefix matrix according to the position in the original matrix, using these rules:</p>

<ol>
    <li><strong>Starting Cell (Top-left corner):</strong> 
        <ul>
            <li>For the cell at position (0,0), we directly copy the value from the original matrix:
                <ul>
                    <li>prefix[0][0] = matrix[0][0]</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>First Row (i=0, j>0):</strong>
        <ul>
            <li>For cells in the first row, each cell’s value is the sum of the previous cell in the prefix matrix and the current cell in the original matrix. This accumulates values horizontally:
                <ul>
                    <li>prefix[0][j] = prefix[0][j-1] + matrix[0][j]</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>First Column (i>0, j=0):</strong>
        <ul>
            <li>For cells in the first column, each cell’s value is the sum of the cell above it in the prefix matrix and the current cell in the original matrix. This accumulates values vertically:
                <ul>
                    <li>prefix[i][0] = prefix[i-1][0] + matrix[i][0]</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>Remaining Cells (i>0, j>0):</strong>
        <ul>
            <li>For other cells, we combine values from the left, above, and the current cell. Because the top and left areas are added twice, we need to subtract the top-left overlap:
                <ul>
                    <li>prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] + matrix[i][j] - prefix[i-1][j-1]</li>
                </ul>
            </li>
            <li>Explanation of terms:
                <ul>
                    <li>prefix[i][j-1]: Adds the sum from the left.</li>
                    <li>prefix[i-1][j]: Adds the sum from above.</li>
                    <li>matrix[i][j]: Adds the current element.</li>
                    <li>prefix[i-1][j-1]: Subtracts the overlap (top-left), which was added twice.</li>
                </ul>
            </li>
        </ul>
    </li>
</ol>

<img src="https://assets.leetcode.com/users/images/a79d8b57-1ae3-4735-b862-95898d574521_1715589271.9132378.png">

```python
def prefixSum(n, m, matrix):
    prefix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                prefix[i][j] = matrix[i][j]
            elif i == 0 and j != 0:
                prefix[i][j] = prefix[i][j - 1] + matrix[i][j]
            elif i != 0 and j == 0:
                prefix[i][j] = prefix[i - 1][j] + matrix[i][j]
            else:
                prefix[i][j] = (prefix[i][j - 1] + prefix[i - 1][j] + matrix[i][j] - prefix[i - 1][j - 1])
    return prefix

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
print(prefixSum(n, m, matrix))
```

<br>
<br>

<h2>Range Sum Query 2D</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given a 2D matrix <code>matrix</code>, handle multiple queries of the following type:</p>
<ul>
    <li>Calculate the sum of the elements of <code>matrix</code> inside the rectangle defined by its upper-left corner (<code>row1, col1</code>) and lower-right corner (<code>row2, col2</code>).</li>
</ul>
<p><strong>Implement the <code>NumMatrix</code> class:</strong></p>
<ul>
    <li><code>NumMatrix(int[][] matrix)</code>: Initializes the object with the integer matrix <code>matrix</code>.</li>
    <li><code>int sumRegion(int row1, int col1, int row2, int col2)</code>: Returns the sum of the elements of <code>matrix</code> inside the rectangle defined by its upper-left corner (<code>row1, col1</code>) and lower-right corner (<code>row2, col2</code>).</li>
</ul>
<p>Design an algorithm where <code>sumRegion</code> works in <strong>O(1)</strong> time complexity.</p>

<p><strong>Sample Test Cases</strong></p>

```python
Input: matrix = [[3, 0, 1, 4, 2],
                   [5, 6, 3, 2, 1],
                   [1, 2, 0, 1, 5],
                   [4, 1, 0, 1, 7],
                   [1, 0, 3, 0, 5]]
Queries: [(2, 1, 4, 3), (1, 1, 2, 2), (1, 2, 2, 4)]
Output: [8, 11, 12]
```

<p><strong>Brute Force Approach:</strong></p>
<p><strong>Intuition:</strong> For each query, traverse the elements within the defined rectangle by iterating through each row and column within the boundaries and summing the elements.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize an empty list <code>ans</code> to store the sum results for each query.</li>
    <li>For each query <code>(row1, col1, row2, col2)</code>:
        <ul>
            <li>Initialize <code>sum</code> to 0.</li>
            <li>Loop through rows from <code>row1</code> to <code>row2</code> and columns from <code>col1</code> to <code>col2</code>.</li>
            <li>Add each element in the range to <code>sum</code>.</li>
        </ul>
    </li>
    <li>Append <code>sum</code> to <code>ans</code>.</li>
    <li>Return <code>ans</code> with the sum results for all queries.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n, m, matrix, q, queries):
    ans = []
    for row1, col1, row2, col2 in queries:
        sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += matrix[i][j]
        ans.append(sum)
    return ans
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li>Time Complexity: <strong>O(n * m * q)</strong> where <code>q</code> is the number of queries.</li>
    <li>Space Complexity: <strong>O(1)</strong> for each query since we use only variables for storage.</li>
</ul>

<p><strong>Optimized Approach:</strong></p>
<p><strong>Intuition:</strong> Precompute a prefix sum matrix where each cell <code>prefix[i][j]</code> stores the cumulative sum from the top-left corner (0, 0) to the cell <code>(i, j)</code> in <code>matrix</code>. This allows us to retrieve the sum of any sub-rectangle using the inclusion-exclusion principle.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Build a <code>prefix</code> matrix where each cell <code>prefix[i][j]</code> stores the cumulative sum of elements from the top-left corner (0, 0) to (i, j).
        <ul>
            <li>If <code>(i, j) = (0, 0)</code>: <code>prefix[i][j] = matrix[i][j]</code></li>
            <li>If <code>i == 0</code>: <code>prefix[i][j] = prefix[i][j - 1] + matrix[i][j]</code></li>
            <li>If <code>j == 0</code>: <code>prefix[i][j] = prefix[i - 1][j] + matrix[i][j]</code></li>
            <li>Else: <code>prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] + matrix[i][j] - prefix[i - 1][j - 1]</code></li>
        </ul>
    </li>
    <li>For each query <code>(row1, col1, row2, col2)</code>:
        <ul>
            <li>Compute the sum of the sub-rectangle as <code>sum = prefix[row2][col2]</code>.</li>
            <li>If <code>col1 > 0</code>, subtract <code>prefix[row2][col1 - 1]</code>.</li>
            <li>If <code>row1 > 0</code>, subtract <code>prefix[row1 - 1][col2]</code>.</li>
            <li>If both <code>row1 > 0</code> and <code>col1 > 0</code>, add back <code>prefix[row1 - 1][col1 - 1]</code> to avoid double subtraction.</li>
        </ul>
    </li>
</ol>

<img src="https://assets.leetcode.com/users/hiepit/image_1578762431.png">
<img src="https://assets.leetcode.com/users/images/68d54210-31f6-4ca1-880a-e48d32a464ba_1620808878.5816271.png">
<img src="https://assets.leetcode.com/users/images/81c7aa53-31f1-4780-bda4-780f41c47828_1654237502.484498.png">

<p><strong>Code:</strong></p>

```python
def prefixSum(n, m, matrix):
    prefix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                prefix[i][j] = matrix[i][j]
            elif i == 0:
                prefix[i][j] = prefix[i][j - 1] + matrix[i][j]
            elif j == 0:
                prefix[i][j] = prefix[i - 1][j] + matrix[i][j]
            else:
                prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] + matrix[i][j] - prefix[i - 1][j - 1]
    return prefix

def optimized(n, m, matrix, q, queries):
    ans = []
    prefix = prefixSum(n, m, matrix)
    for row1, col1, row2, col2 in queries:
        sum = prefix[row2][col2]
        if col1 > 0:
            sum -= prefix[row2][col1 - 1]
        if row1 > 0:
            sum -= prefix[row1 - 1][col2]
        if row1 > 0 and col1 > 0:
            sum += prefix[row1 - 1][col1 - 1]
        ans.append(sum)
    return ans
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li>Time Complexity: <strong>O(n * m + q)</strong> where <code>O(n * m)</code> is for constructing the prefix matrix and <code>O(q)</code> is for each query.</li>
    <li>Space Complexity: <strong>O(n * m)</strong> for storing the prefix matrix.</li>
</ul>

<br>
<br>

<h2>Matrix Block Sum</h2>
<p><strong>Problem Statement</strong></p>
<p>Given a matrix <code>mat</code> of dimensions <code>m x n</code> and an integer <code>k</code>, you need to return another matrix <code>answer</code> where each element <code>answer[i][j]</code> is the sum of all elements in the <code>mat</code> that are within a <code>k</code> distance from <code>mat[i][j]</code>. This includes any element <code>mat[r][c]</code> for which:</p>
<code>
i - k ≤ r ≤ i + k, 
j - k ≤ c ≤ j + k
</code>
<p>where <code>(r, c)</code> should be a valid position in the matrix.</p>

<p><strong>Intuition Behind the Solution</strong></p>
<ul>
  <li><strong>Efficient Summation</strong>: Using prefix sums allows us to efficiently calculate the sum of elements in a rectangular submatrix in constant time.</li>
  <li><strong>Bounding Box</strong>: We define a bounding box with <code>(row1, col1)</code> as the top-left corner and <code>(row2, col2)</code> as the bottom-right corner around <code>mat[i][j]</code>, where all elements in this box contribute to the sum.</li>
  <li><strong>Handling Edge Cases</strong>: For cells near the matrix edges, we adjust the bounding box to stay within the matrix boundaries.</li>
</ul>

<p><strong>Steps to Solve</strong></p>
<ol>
  <li><strong>Calculate Prefix Sum</strong>: Create a <code>prefix</code> matrix where each element at <code>(i, j)</code> holds the sum of all elements from <code>(0, 0)</code> to <code>(i, j)</code>.</li>
  <li><strong>Define the Bounding Box</strong>: For each element <code>(i, j)</code> in <code>mat</code>, determine a submatrix with <code>(i-k, j-k)</code> as the top-left corner and <code>(i+k, j+k)</code> as the bottom-right corner.</li>
  <li><strong>Adjust Boundaries</strong>: Ensure the bounding box doesn’t exceed matrix boundaries by clamping values between <code>0</code> and <code>n-1</code> for rows and <code>0</code> and <code>m-1</code> for columns.</li>
  <li><strong>Compute Sum Using Prefix Matrix</strong>: Use the prefix sum array to compute the sum for each submatrix efficiently.</li>
</ol>

<p><strong>Code Implementation</strong></p>

```python
def prefixSum(n, m, matrix):
    prefix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                prefix[i][j] = matrix[i][j]
            elif i == 0:
                prefix[i][j] = prefix[i][j - 1] + matrix[i][j]
            elif j == 0:
                prefix[i][j] = prefix[i - 1][j] + matrix[i][j]
            else:
                prefix[i][j] = (prefix[i][j - 1] + prefix[i - 1][j] 
                                + matrix[i][j] - prefix[i - 1][j - 1])
    return prefix

def optimized(prefix, row1, col1, row2, col2):
    sum = prefix[row2][col2]
    if col1 > 0:
        sum -= prefix[row2][col1 - 1]
    if row1 > 0:
        sum -= prefix[row1 - 1][col2]
    if row1 > 0 and col1 > 0:
        sum += prefix[row1 - 1][col1 - 1]
    return sum

class Solution:
    def matrixBlockSum(self, mat, k):
        n, m = len(mat), len(mat[0])
        ans = [[0] * m for _ in range(n)]
        prefix = prefixSum(n, m, mat)
        
        for i in range(n):
            for j in range(m):
                row1, col1 = max(0, i - k), max(0, j - k)
                row2, col2 = min(n - 1, i + k), min(m - 1, j + k)
                
                ans[i][j] = optimized(prefix, row1, col1, row2, col2)
        
        return ans

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

ans = Solution().matrixBlockSum(matrix, k)
print(ans)

```

<p><strong>Explanation of the Code</strong></p>
<ul>
  <li><code>prefixSum()</code>: Constructs the prefix sum matrix, which helps to compute the sum of elements in any submatrix in constant time.</li>
  <li><code>optimized()</code>: Uses the prefix sum matrix to get the sum of elements within any bounding box.</li>
  <li><code>matrixBlockSum()</code>: Initializes the <code>answer</code> matrix and calculates each cell’s sum by defining and adjusting the bounding box according to the value of <code>k</code>.</li>
</ul>

<p><strong>Sample Test Case</strong></p>
<p><strong>Input</strong>:</p>
<code>
n = 3, m = 3
matrix = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
</code>
<p><strong>Output</strong>:</p>
<code>
[[12,21,16],
 [27,45,33],
 [24,39,28]]
</code>

<p><strong>Time and Space Complexity</strong></p>
<ul>
  <li><strong>Time Complexity</strong>: \(O(n \times m)\) for calculating the prefix sum matrix, and \(O(n \times m)\) for computing each answer cell using the prefix sum array, resulting in an overall complexity of \(O(n \times m)\).</li>
  <li><strong>Space Complexity</strong>: \(O(n \times m)\) for the prefix sum matrix and the answer matrix.</li>
</ul>


<br>
<br>

<h2>Constant time range add operation on an array</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given an array of size <strong>N</strong>, initialized with all zeros, you have a series of range update queries. Each query contains a starting index, an ending index, and a value to add to all elements in this range (inclusive). After applying all queries, the goal is to print the final array.</p>

<p><strong>Input Example:</strong></p>
<ul>
    <li>N = 5</li>
    <li>Array = [0, 0, 0, 0, 0]</li>
    <li>Queries = [(1, 3, 2), (2, 4, 3)]</li>
</ul>
<p>Expected Output: [0, 2, 5, 5, 3]</p>

<p><strong>Sample Test Cases:</strong></p>
<ol>
    <li><strong>Test Case 1:</strong> N = 5, Queries = [(1, 3, 2), (2, 4, 3)] <br> Output: [0, 2, 5, 5, 3]</li>
    <li><strong>Test Case 2:</strong> N = 6, Queries = [(0, 2, 1), (1, 4, 2)] <br> Output: [1, 3, 3, 2, 2, 0]</li>
</ol>

<p><strong>Brute Force Approach:</strong></p>
<p>In the brute force approach, for each query, you loop through every index in the specified range and add the given value. This results in a much higher time complexity.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize an array arr of size N with all zeros.</li>
    <li>For each query (start, end, val), iterate from start to end, adding val to each element in this range.</li>
    <li>After applying all queries, print or return the final array.</li>
</ol>

<p><strong>Code (Brute Force Solution):</strong></p>

```python
def apply_queries_brute_force(N, queries):
    # Step 1: Initialize array
    arr = [0] * N

    # Step 2: Apply each query directly
    for start, end, val in queries:
        for i in range(start, end + 1):
            arr[i] += val

    return arr
```

<p><strong>Time and Space Complexity (Brute Force Solution):</strong></p>
<ul>
    <li>Time Complexity: O(N * Q), where N is the size of the array, and Q is the number of queries.</li>
    <li>Space Complexity: O(N) for storing the array.</li>
</ul>

<p><strong>Optimized Approach:</strong></p>
<p>Using a <strong>Difference Array</strong> is efficient for this type of range update. The idea is to mark the beginning and end of each range update, which allows us to process all ranges in one pass when we finally calculate the array values.</p>

<ol>
    <li>For each query (start, end, val), increment the element at the start index by val.</li>
    <li>Decrement the element at the end + 1 index by val (if it’s within bounds).</li>
</ol>
<p>Once all queries are applied, the difference array only contains markers. Performing a cumulative sum across the array translates these markers into the final array values.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize an array arr of size N with all zeros.</li>
    <li>For each query (start, end, val):</li>
    <ul>
        <li>Add val to arr[start].</li>
        <li>Subtract val from arr[end + 1] if end + 1 < N.</li>
    </ul>
    <li>Perform a cumulative sum on arr to get the final updated values.</li>
</ol>

<p><strong>Code (Optimized Solution):</strong></p>

```python
def apply_queries(N, queries):
    # Step 1: Initialize array
    arr = [0] * N

    # Step 2: Apply range updates using difference array concept
    for start, end, val in queries:
        arr[start] += val
        if end + 1 < N:
            arr[end + 1] -= val

    # Step 3: Perform cumulative sum to get the final values in the array
    for i in range(1, N):
        arr[i] += arr[i - 1]

    return arr
```

<p><strong>Time and Space Complexity (Optimized Solution):</strong></p>
<ul>
    <li>Time Complexity: O(N + Q), where N is the size of the array, and Q is the number of queries.</li>
    <li>Space Complexity: O(N), since we only use the array of size N.</li>
</ul>

<br>
<br>


<h2>Constant time range add operation on 2-d Array</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given a 2D array of size <strong>N x M</strong>, initialized with all zeros, you have a series of range update queries. Each query contains a top-left and bottom-right coordinate along with a value to add to all elements in this subarray (inclusive). After applying all queries, the goal is to print the final 2D array.</p>

<p><strong>Input Example:</strong></p>
<ul>
    <li>N = 4, M = 4</li>
    <li>Array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]</li>
    <li>Queries = [((1, 1), (2, 2), 3), ((0, 0), (3, 3), 2)]</li>
</ul>
<p>Expected Output: [[2, 2, 2, 2], [2, 5, 5, 2], [2, 5, 5, 2], [2, 2, 2, 2]]</p>

<p><strong>Sample Test Cases:</strong></p>
<ol>
    <li><strong>Test Case 1:</strong> N = 4, M = 4, Queries = [((1, 1), (2, 2), 3), ((0, 0), (3, 3), 2)] <br> Output: [[2, 2, 2, 2], [2, 5, 5, 2], [2, 5, 5, 2], [2, 2, 2, 2]]</li>
    <li><strong>Test Case 2:</strong> N = 3, M = 3, Queries = [((0, 0), (1, 1), 5), ((1, 1), (2, 2), 2)] <br> Output: [[5, 5, 0], [5, 7, 2], [0, 2, 2]]</li>
</ol>

<p><strong>Brute Force Solution:</strong></p>
<p>In the brute force approach, for each query, you loop through every index in the specified 2D range and add the given value. This results in a much higher time complexity.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize a 2D array arr of size N x M with all zeros.</li>
    <li>For each query ((top_left_x, top_left_y), (bottom_right_x, bottom_right_y), val):</li>
    <ul>
        <li>For each i from top_left_x to bottom_right_x, and each j from top_left_y to bottom_right_y, add val to arr[i][j].</li>
    </ul>
</ol>

<p><strong>Code (Brute Force Solution):</strong></p>

```python
def apply_2d_queries_brute_force(N, M, queries):
    arr = [[0] * M for _ in range(N)]
    
    for (tl_x, tl_y), (br_x, br_y), val in queries:
        for i in range(tl_x, br_x + 1):
            for j in range(tl_y, br_y + 1):
                arr[i][j] += val
                
    return arr
```



<p><strong>Intuition (Optimized Solution):</strong></p>
<p>For 2D range updates, we can use a <strong>2D Difference Array</strong>. The idea is to mark the top-left and bottom-right boundaries of each subarray range. This allows us to efficiently process all ranges in a single pass when calculating the final array values.</p>

<ol>
    <li>For each query ((top_left_x, top_left_y), (bottom_right_x, bottom_right_y), val):</li>
    <ul>
        <li>Add val to arr[top_left_x][top_left_y].</li>
        <li>Subtract val from arr[bottom_right_x + 1][top_left_y] if bottom_right_x + 1 is within bounds.</li>
        <li>Subtract val from arr[top_left_x][bottom_right_y + 1] if bottom_right_y + 1 is within bounds.</li>
        <li>Add val to arr[bottom_right_x + 1][bottom_right_y + 1] if both are within bounds.</li>
    </ul>
</ol>
<p>Finally, apply a 2D prefix sum to translate these markers into the final values.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize a 2D array arr of size N x M with all zeros.</li>
    <li>For each query ((top_left_x, top_left_y), (bottom_right_x, bottom_right_y), val):</li>
    <ul>
        <li>Add val to arr[top_left_x][top_left_y].</li>
        <li>If bottom_right_x + 1 < N, subtract val from arr[bottom_right_x + 1][top_left_y].</li>
        <li>If bottom_right_y + 1 < M, subtract val from arr[top_left_x][bottom_right_y + 1].</li>
        <li>If both conditions above are met, add val to arr[bottom_right_x + 1][bottom_right_y + 1].</li>
    </ul>
    <li>Apply a cumulative 2D prefix sum to calculate the final values in the array.</li>
</ol>

<p><strong>Code (Optimized Solution):</strong></p>

```python
def apply_2d_queries(N, M, queries):
    arr = [[0] * M for _ in range(N)]
    
    # Apply the difference array concept for each query
    for (tl_x, tl_y), (br_x, br_y), val in queries:
        arr[tl_x][tl_y] += val
        if br_x + 1 < N:
            arr[br_x + 1][tl_y] -= val
        if br_y + 1 < M:
            arr[tl_x][br_y + 1] -= val
        if br_x + 1 < N and br_y + 1 < M:
            arr[br_x + 1][br_y + 1] += val
    
    # Compute the prefix sums for rows and columns to get the final values
    for i in range(N):
        for j in range(M):
            if i > 0:
                arr[i][j] += arr[i - 1][j]
            if j > 0:
                arr[i][j] += arr[i][j - 1]
            if i > 0 and j > 0:
                arr[i][j] -= arr[i - 1][j - 1]
    
    return arr
```

<p><strong>Time and Space Complexity (Optimized Solution):</strong></p>
<ul>
    <li>Time Complexity: O(N * M + Q), where N and M are the dimensions of the array, and Q is the number of queries.</li>
    <li>Space Complexity: O(N * M) for the 2D array.</li>
</ul>

<br>
<br>

<h2>Stamping The Grid</h2>
<p><strong>Problem Statement:</strong></p>

<p>You are given:</p>
<ul>
    <li>A binary matrix <code>grid</code> of size <code>m x n</code>, where each cell is either <code>0</code> (empty) or <code>1</code> (occupied).</li>
    <li>Stamps of size <code>stampHeight x stampWidth</code>.</li>
</ul>

<p>The task is to determine if it’s possible to fit the stamps on <code>grid</code> such that:</p>
<ul>
    <li>All empty cells (<code>0</code>s) are covered.</li>
    <li>No occupied cells (<code>1</code>s) are covered.</li>
    <li>Stamps can overlap, but they cannot be rotated.</li>
    <li>Stamps must remain entirely within the grid’s boundaries.</li>
</ul>

<p>If it’s possible to cover all empty cells under these conditions, return <strong>True</strong>; otherwise, return <strong>False</strong>.</p>

<p><strong>Example Test Cases</strong></p>

<p><strong>Example 1</strong></p>
<pre>
Input:
grid = [[1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0]], 
stampHeight = 4, stampWidth = 3
Output: true
Explanation: We can place two overlapping stamps to cover all empty cells.
We have two overlapping stamps (labeled 1 and 2 in the image) that are able to cover all the empty cells.
</pre>
<img src="https://assets.leetcode.com/uploads/2021/11/03/ex1.png">

<p><strong>Example 2</strong></p>
<pre>
Input:
grid = [[1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]], 
stampHeight = 2, stampWidth = 2
Output: false
Explanation: We cannot cover all empty cells without covering any occupied cells.
There is no way to fit the stamps onto all the empty cells without the stamps going outside the grid.
</pre>
<img src="https://assets.leetcode.com/uploads/2021/11/03/ex2.png">

<p><strong>Intuition:</strong></p>

<ol>
    <li><strong>Prefix Sum Optimization:</strong> To efficiently check if a sub-matrix (of size <code>stampHeight x stampWidth</code>) is entirely empty (all <code>0</code>s), we use a <strong>prefix sum array</strong>. This helps compute the sum of elements within any sub-matrix in constant time, allowing us to quickly identify valid stamp placement locations.</li>
    <li><strong>Marking Coverage with Stamps:</strong> Using a difference array approach, we increment and decrement specific matrix positions to mark where stamps start and end. This helps in tracking regions where stamps overlap, allowing us to verify if all <code>0</code>s are covered.</li>
</ol>

<p><strong>Steps to Solve:</strong></p>

<ol>
    <li><strong>Compute the Prefix Sum Array:</strong> Create a <code>prefix</code> array, where <code>prefix[i][j]</code> represents the sum of elements from the top-left corner <code>(0, 0)</code> to <code>(i, j)</code> in <code>grid</code>.</li>
    <li><strong>Identify Valid Stamp Positions:</strong> Use the <code>getSum()</code> function to check if a region of size <code>stampHeight x stampWidth</code> is empty (<code>sum == 0</code>). If it is, adjust the values in a new <code>mat</code> array to mark where stamps start and stop.</li>
    <li><strong>Apply Difference Array Technique:</strong> After marking potential stamp regions, compute another prefix sum (<code>prefixMat</code>) on <code>mat</code> to determine which cells are covered by stamps. This array tells us if a cell is stamped by checking for non-zero values in <code>prefixMat</code>.</li>
    <li><strong>Validate All Empty Cells:</strong> Finally, iterate through <code>grid</code> to ensure all <code>0</code>s in the original <code>grid</code> are covered in <code>prefixMat</code>.</li>
</ol>

<p><strong>Code Implementation:</strong></p>

```python
def prefixSum(n, m, matrix):
    prefix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            sum = matrix[i][j]
            if i > 0:
                sum += prefix[i - 1][j]
            if j > 0:
                sum += prefix[i][j - 1]
            if i > 0 and j > 0:
                sum -= prefix[i - 1][j - 1]
            prefix[i][j] = sum
    return prefix

def getSum(n, m, prefix, row1, col1, row2, col2):
    sum = prefix[row2][col2]
    if row1 > 0:
        sum -= prefix[row1 - 1][col2]
    if col1 > 0:
        sum -= prefix[row2][col1 - 1]
    if row1 > 0 and col1 > 0:
        sum += prefix[row1 - 1][col1 - 1]
    return sum

def optimized(n, m, matrix, height, width):
    prefix = prefixSum(n, m, matrix)
    mat = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(m):
            if i + height > n or j + width > m:
                continue
            if getSum(n, m, prefix, i, j, i + height - 1, j + width - 1) == 0:
                mat[i][j] += 1
                mat[i][j + width] -= 1
                mat[i + height][j] -= 1
                mat[i + height][j + width] += 1
                
    prefixMat = prefixSum(n + 1, m + 1, mat)
    
    for i in range(n):
        for j in range(m):
            if prefixMat[i][j] == 0 and matrix[i][j] != 1:
                return False
    return True

# Input handling
n, m = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]
height = int(input())
width = int(input())
print(optimized(n, m, matrix, height, width))
```

<p><strong>Complexity Analysis:</strong></p>

<ul>
    <li><strong>Time Complexity:</strong> Calculating the prefix sum for <code>grid</code>: <code>O(m x n)</code>. Checking all possible positions for the stamp and marking them: <code>O(m x n)</code>. Calculating <code>prefixMat</code> for coverage validation: <code>O(m x n)</code>. Overall: <code>O(m x n)</code>.</li>
    <li><strong>Space Complexity:</strong> Extra space for <code>prefix</code>, <code>mat</code>, and <code>prefixMat</code>: <code>O(m x n)</code>.</li>
</ul>

<br>
<br>

<h2>Count Artifacts That Can Be Extracted</h2>
<p><strong>Problem Statement:</strong></p>

<p>Given:</p>
<ul>
    <li>An <code>n x n</code> grid with buried artifacts, represented as a rectangular section of the grid.</li>
    <li>A 2D integer array <code>artifacts</code> where each artifact is defined by four coordinates: <code>artifacts[i] = [r1i, c1i, r2i, c2i]</code>. Here:</li>
    <ul>
        <li><code>(r1i, c1i)</code> is the coordinate of the top-left cell of the artifact.</li>
        <li><code>(r2i, c2i)</code> is the coordinate of the bottom-right cell of the artifact.</li>
    </ul>
    <li>A 2D integer array <code>dig</code>, where each element <code>dig[i] = [ri, ci]</code> indicates that the cell <code>(ri, ci)</code> will be excavated, removing any mud and uncovering any artifact beneath it.</li>
</ul>

<p>The task is to return the number of artifacts that can be extracted completely, meaning all parts of each artifact are uncovered.</p>

<p><strong>Sample Test Cases:</strong></p>
<pre>
Example 1:
Input: n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]
Output: 1
<img src="https://assets.leetcode.com/uploads/2019/09/16/untitled-diagram.jpg">
The different colors represent different artifacts. Excavated cells are labeled with a 'D' in the grid.
There is 1 artifact that can be extracted, namely the red artifact.
The blue artifact has one part in cell (1,1) which remains uncovered, so we cannot extract it.
Thus, we return 1.

Example 2:
Input: n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]
Output: 2
<img src="https://assets.leetcode.com/uploads/2019/09/16/untitled-diagram-1.jpg">
Both the red and blue artifacts have all parts uncovered (labeled with a 'D') and can be extracted, so we return 2. 
</pre>

<p><strong>Brute Force Approach</strong></p>

<p><strong>Intuition:</strong></p>
<p>The brute force method involves checking each artifact to see if it is fully uncovered by excavated cells. This is a straightforward method, iterating through each artifact and checking each cell within the artifact's bounds.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Create an <code>n x n</code> matrix initialized to 0.</li>
    <li>Mark the excavated cells in the matrix (set to 1).</li>
    <li>For each artifact, iterate over its covered cells.</li>
    <li>If all cells of an artifact are marked as excavated (1), increment the counter for extractable artifacts.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n, artifacts, dig):
    ans = 0
    matrix = [[0] * n for _ in range(n)]
    for i, j in dig:
        matrix[i][j] = 1
    
    for row1, col1, row2, col2 in artifacts:
        covered = True
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                if matrix[i][j] != 1:
                    covered = False
                    break
            if not covered:
                break
        if covered:
            ans += 1
    return ans
```

<p><strong>Time Complexity:</strong> <code>O(n^2 * k)</code>, where <code>k</code> is the number of artifacts.</p>
<p><strong>Space Complexity:</strong> <code>O(n^2)</code> for the excavation matrix.</p>

<p><strong>Optimized Approach</strong></p>

<p><strong>Intuition:</strong></p>
<p>The optimized approach utilizes a prefix sum matrix to efficiently count how many excavated cells are in any rectangular area defined by the artifacts. This allows for quick checks on whether an artifact is fully uncovered.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Create an <code>n x n</code> matrix initialized to 0.</li>
    <li>Mark the excavated cells in the matrix (set to 1).</li>
    <li>Compute the prefix sum matrix for quick area sum queries.</li>
    <li>For each artifact, calculate the total number of cells it covers.</li>
    <li>Using the prefix sum, quickly check if the total excavated cells equal the total cells covered by the artifact.</li>
    <li>If they match, increment the counter for extractable artifacts.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def prefix(n, m, matrix):
    prefixSum = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            sum = matrix[i][j]
            if i > 0:
                sum += prefixSum[i - 1][j]
            if j > 0:
                sum += prefixSum[i][j - 1]
            if i > 0 and j > 0:
                sum -= prefixSum[i - 1][j - 1]
            prefixSum[i][j] = sum
    return prefixSum

def optimized(n, artifacts, dig):
    ans = 0
    matrix = [[0] * n for _ in range(n)]
    for i, j in dig:
        matrix[i][j] = 1
    
    prefixSum = prefix(n, n, matrix)
    for row1, col1, row2, col2 in artifacts:
        totalCells = (row2 - row1 + 1) * (col2 - col1 + 1)
        sum = prefixSum[row2][col2]
        
        if row1 > 0:
            sum -= prefixSum[row1 - 1][col2]
        if col1 > 0:
            sum -= prefixSum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            sum += prefixSum[row1 - 1][col1 - 1]
        
        if sum == totalCells:
            ans += 1
    return ans
```

<p><strong>Time Complexity:</strong> <code>O(n^2)</code> for calculating prefix sums and checking each artifact.</p>
<p><strong>Space Complexity:</strong> <code>O(n^2)</code> for the excavation matrix and prefix sum matrix.</p>

<br>
<br>

<h2>Grid Game</h2>
<p><strong>Problem Statement:</strong></p>

<p>You are given a 0-indexed 2D array <code>grid</code> of size <code>2 x n</code>, where <code>grid[r][c]</code> represents the number of points at position <code>(r, c)</code> on the matrix. Two robots start at <code>(0, 0)</code> and want to reach <code>(1, n-1)</code> by only moving right or down.</p>

<p>After the first robot moves to <code>(1, n-1)</code> and collects points, it sets the points in the cells it traverses to 0. The second robot then moves, trying to maximize its collected points from the remaining cells. The goal is to return the number of points collected by the second robot if both robots play optimally.</p>

<p><strong>Sample Test Cases:</strong></p>
<pre>
Example 1:
Input: grid = [[2,5,4],[1,5,1]]
Output: 4
<img src="https://assets.leetcode.com/uploads/2021/09/08/a1.png">

Example 2:
Input: grid = [[3,3,1],[8,5,2]]
Output: 4
<img src="https://assets.leetcode.com/uploads/2021/09/08/a2.png">

Example 3:
Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
<img src="https://assets.leetcode.com/uploads/2021/09/08/a3.png">
</pre>

<p><strong>Intuition:</strong></p>
<p>To solve this problem, we need to calculate how the first robot's path affects the second robot's potential score. The first robot's objective is to minimize the points available for the second robot while still reaching the end. Hence, both robots will choose paths that are optimal for their respective goals.</p>

<p><strong>Steps to Solve:<p><strong>
<ol>
    <li>Compute the prefix sums for both rows. This will allow efficient calculation of points collected up to each column.</li>
    <li>Iterate through each column to simulate the first robot's decision to stop at that column.</li>
    <li>Calculate the remaining points for the second robot based on the prefix sums after the first robot's path is considered:</li>
    <ul>
        <li>For the top row, calculate the total points after the first robot has collected points until the current column.</li>
        <li>For the bottom row, consider only the points to the left of the current column.</li>
    </ul>
    <li>Determine the maximum points the second robot can collect from the remaining options.</li>
    <li>Find the minimum points the second robot can achieve across all column stops of the first robot.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def optimized(n, m, matrix):
    prefix1, prefix2 = matrix[0].copy(), matrix[1].copy()
    for i in range(1, m):
        prefix1[i] += prefix1[i - 1]
        prefix2[i] += prefix2[i - 1]

    ans = float('inf')
    for i in range(m):
        top = prefix1[-1] - prefix1[i]
        bottom = prefix2[i - 1] if (i > 0) else 0
        points = max(top, bottom)
        ans = min(ans, points)
    
    return ans

n, m = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for i in range(n)]
print(optimized(n, m, matrix))
```


<p><strong>Time Complexity:</strong> <code>O(n + m)</code>, where <code>n</code> is the number of rows (which is fixed as 2) and <code>m</code> is the number of columns.</p>
<p><strong>Space Complexity:</strong> <code>O(m)</code> for storing prefix sums for the two rows.</p>

<br>
<br>

<h2>Maximal Square</h2>
<p><strong>Problem Statement:</strong></p>

<p>Given an <code>m x n</code> binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.</p>

<p><strong>Example Test Cases:</strong></p>
<pre>
Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
<img src="https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg">

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1
<img src="https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg">

Example 3:
Input: matrix = [["0"]]
Output: 0
</pre>

<p><strong>Brute Force Approach:</strong></p>
<p>The brute force solution involves checking every possible square in the matrix. We define a helper function to check if a square of a given length starting from a specific cell is filled with 1's.</p>

<p><strong>Steps to Solve (Brute Force):</strong></p>
<ol>
    <li>Initialize a variable <code>maxi</code> to keep track of the largest square length found.</li>
    <li>Iterate through each cell in the matrix.</li>
    <li>If the current cell is 1, attempt to create squares of increasing sizes, checking if they are all 1's using the <code>check</code> function.</li>
    <li>Update <code>maxi</code> with the largest side length found.</li>
    <li>The area of the largest square is <code>maxi * maxi</code>.</li>
</ol>

<p><strong>Code (Brute Force):</strong></p>

```python
def bruteForce(n, m, matrix):
    maxi = 0
    def check(row, col, length):
        for r in range(row, row + length):
            for c in range(col, col + length):
                if matrix[r][c] == '0':
                    return False
        return True
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                for sideLen in range(1, min(n - i, m - j) + 1):
                    temp = check(i, j, sideLen)
                    if temp:
                        maxi = max(maxi, sideLen)
    area = maxi * maxi
    return area
```

<p><strong>Time and Space Complexity (Brute Force):</strong></p>
<p><strong>Time Complexity:</strong> <code>O(n^2 * m^2)</code> because for each cell, we may check a square of size up to <code>min(n, m)</code>.</p>
<p><strong>Space Complexity:</strong> <code>O(1)</code>, as we are using only a few additional variables.</p>

<p><strong>Optimized Approach:</strong></p>
<p>The optimized solution uses dynamic programming to store the maximum side length of squares ending at each cell.</p>

<p><strong>Steps to Solve (Optimized):</strong></p>s
<ol>
    <li>Create a <code>dp</code> array where <code>dp[i][j]</code> stores the size of the largest square whose bottom-right corner is at <code>(i, j)</code>.</li>
    <li>Initialize the first row and column of the <code>dp</code> array based on the input matrix.</li>
    <li>For each cell that contains a 1, calculate the value of <code>dp[i][j]</code> as:</li>
    <ul>
        <li><code>dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1</code></li>
    </ul>
    <li>Track the maximum value in the <code>dp</code> array during the calculation.</li>
    <li>The area of the largest square is the maximum side length squared.</li>
</ol>

<p><strong>Code (Optimized):</strong></p>


```python
def optimized(n, m, matrix):
    dp = [[0] * m for i in range(n)]
    for i in range(n):
        dp[i][0] = int(matrix[i][0])
    for j in range(m):
        dp[0][j] = int(matrix[0][j])
    
    maxi = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != '1':
                continue
            left = dp[i][j-1] if j > 0 else 0
            top = dp[i-1][j] if i > 0 else 0
            diagonal = dp[i-1][j-1] if i > 0 and j > 0 else 0
            
            dp[i][j] = min(left, top, diagonal) + 1
            maxi = max(dp[i][j], maxi)
    
    area = maxi * maxi
    return area
```

<p><strong>Time and Space Complexity (Optimized):</strong></p>
<p><strong>Time Complexity:</strong> <code>O(n * m)</code>, as we traverse each cell once.</p>
<p><strong>Space Complexity:</strong> <code>O(n * m)</code> for the <code>dp</code> array to store intermediate results.</p>


<br>
<br>

<h2>Maximum Difference Score in a Grid</h2>
<p><strong>Problem Statement:</strong></p>

<p>You are given an <code>m x n</code> matrix <code>grid</code> consisting of positive integers. You can move from a cell in the matrix to any other cell that is either to the bottom or to the right (not necessarily adjacent). The score of a move from a cell with the value <code>c1</code> to a cell with the value <code>c2</code> is <code>c2 - c1</code>.</p>

<p>You can start at any cell, and you have to make at least one move.</p>

<p>Return the maximum total score you can achieve.</p>

<p><strong>Example Test Cases:</strong></p>
<pre>
Example 1:
Input: grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
Output: 9

Explanation: We start at the cell (0, 1), and we perform the following moves:
- Move from the cell (0, 1) to (2, 1) with a score of 7 - 5 = 2.
- Move from the cell (2, 1) to (2, 2) with a score of 14 - 7 = 7.
The total score is 2 + 7 = 9.

Example 2:
Input: grid = [[4,3,2],[3,2,1]]
Output: -1

Explanation: We start at the cell (0, 0), and we perform one move: (0, 0) to (0, 1). The score is 3 - 4 = -1.
</pre>

<p><strong>Brute Force Approach:</strong></p>
<p>The brute force solution would involve trying every possible starting point and then exploring all possible moves to calculate the score. This is inefficient as it would require examining all potential paths in the grid.</p>

<p><strong>Steps to Solve (Brute Force):</strong></p>
<ol>
    <li>For each cell in the grid, start from that cell and recursively explore all paths moving only downwards or to the right.</li>
    <li>At each step, calculate the score of moving to the next cell and accumulate this score.</li>
    <li>Keep track of the maximum score found during this exploration.</li>
</ol>

<p><strong>Code (Brute Force):</strong></p>

```python
def bruteForce(n, m, grid):
    max_score = -float('inf')

    def dfs(x, y, prev_value, current_score):
        nonlocal max_score
        # Calculate the score for this path
        max_score = max(max_score, current_score)
        
        # Explore all valid moves
        for i in range(x + 1, n):
            for j in range(y, m):
                score = grid[i][j] - prev_value
                dfs(i, j, grid[i][j], current_score + score)
    
    for i in range(n):
        for j in range(m):
            dfs(i, j, grid[i][j], 0)
    
    return max_score
```

<p><strong>Time and Space Complexity (Brute Force):</strong></p>
<p><strong>Time Complexity:</strong> Exponential in the worst case due to exploring all paths.</p>
<p><strong>Space Complexity:</strong> <code>O(n * m)</code> for the recursion stack in the worst case.</p>

<p><strong>Optimized Approach:</strong></p>
<p>The optimized solution uses dynamic programming to keep track of the maximum score achievable from each cell.</p>

<p><strong>Steps to Solve (Optimized):</strong></p>
<ol>
    <li>Create a <code>dp</code> array where <code>dp[i][j]</code> holds the maximum score achievable when reaching cell <code>(i, j)</code>.</li>
    <li>For each cell in the grid, calculate the possible moves from above and left, and update the score accordingly.</li>
    <li>Track the overall maximum score in a separate variable.</li>
</ol>

<p><strong>Code (Optimized):</strong></p>

```python
def optimized(n, m, matrix):
    ans = -float('inf')
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            top = left = float('inf')
            if i > 0:
                top = matrix[i-1][j]
            if j > 0:
                left = matrix[i][j-1]
                
            includeTop = dp[i-1][j] + matrix[i][j] - top if i > 0 else float('-inf')
            excludeTop = matrix[i][j] - top if i > 0 else float('-inf')
            includeLeft = dp[i][j-1] + matrix[i][j] - left if j > 0 else float('-inf')
            excludeLeft = matrix[i][j] - left if j > 0 else float('-inf')
            
            dp[i][j] = max(includeTop, excludeTop, includeLeft, excludeLeft)
            ans = max(ans, dp[i][j])
    
    return ans
```

<p><strong>Time and Space Complexity (Optimized):</strong></p>
<p><strong>Time Complexity:</strong> <code>O(n * m)</code>, since we iterate through each cell once.</p>
<p><strong>Space Complexity:</strong> <code>O(n * m)</code> for the <code>dp</code> array to store intermediate results.</p>

