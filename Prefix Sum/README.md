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


