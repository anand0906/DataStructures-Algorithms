
<h1>Problems</h1>

<h2>Max Sum Subarray Of Size K</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given an array of integers <strong>arr</strong> and an integer <strong>k</strong>, find the maximum sum of any subarray of size <strong>k</strong>.</p>

<p><strong>Sample Test Cases:</strong></p>
<ol>
    <li><strong>Input:</strong> arr = [2, 1, 5, 1, 3, 2], k = 3<br>
    <strong>Output:</strong> 11<br>
    <strong>Explanation:</strong> The subarray [5, 1, 3] has the maximum sum of 11.</li>
    <li><strong>Input:</strong> arr = [1, 9, -1, -2, 7, 3, -1, 2], k = 4<br>
    <strong>Output:</strong> 16<br>
    <strong>Explanation:</strong> The subarray [9, -1, -2, 7] has the maximum sum of 16.</li>
</ol>

<p><strong>Approach 1: Brute Force</strong></p>

<p><strong>Intuition:</strong><br>
In the brute force approach, we calculate the sum for every possible subarray of size <strong>k</strong> by using two nested loops. For each subarray, we compute the sum and track the maximum sum found.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Use an outer loop to select the starting index of each subarray of size <strong>k</strong>.</li>
    <li>Use an inner loop to calculate the sum of elements from the starting index to the end of the subarray.</li>
    <li>Track the maximum sum as we iterate over all possible subarrays.</li>
    <li>Return the maximum sum found.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n, arr, k):
    maxi = -1
    for i in range(n - k + 1):  # Loop to generate all subarrays of size k
        currentSum = 0
        for j in range(i, i + k):  # Calculate the sum of each subarray
            currentSum += arr[j]
        maxi = max(maxi, currentSum)  # Update the maximum sum
    return maxi
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n * k), as we calculate the sum for each subarray.</li>
    <li><strong>Space Complexity:</strong> O(1), no extra space is used.</li>
</ul>

<p><strong>Approach 2: Optimized Approach (Sliding Window)</strong></p>

<p><strong>Intuition:</strong><br>
We can optimize this by using the **sliding window** technique. Instead of recalculating the sum for each subarray from scratch, we can adjust the sum by subtracting the element that is sliding out of the window and adding the element that is sliding into the window.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>First, calculate the sum of the initial window (the first <strong>k</strong> elements).</li>
    <li>Store this sum as the current maximum.</li>
    <li>For each subsequent subarray, update the sum by adding the next element in the array and subtracting the element that is sliding out of the window.</li>
    <li>Continue to update the maximum sum and return it after all subarrays have been processed.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def optimized(n, arr, k):
    maxi = -1
    currentSum = 0
    left, right = 0, 0
    
    # Calculate the sum of the first window of size k
    while right < k:
        currentSum += arr[right]
        right += 1
    maxi = max(maxi, currentSum)
    
    # Slide the window across the array
    while right < n:
        currentSum += arr[right]  # Add the next element in the window
        currentSum -= arr[left]   # Remove the element that is sliding out of the window
        maxi = max(maxi, currentSum)  # Update the maximum sum
        right += 1
        left += 1
    
    return maxi
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n), since we traverse the array once and update the sum in constant time.</li>
    <li><strong>Space Complexity:</strong> O(1), as no extra space is required.</li>
</ul>

<br>
<br>

<h2>Find All Maximum Elements Of Subarrays Of Size K</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given an array of integers <strong>arr</strong> and an integer <strong>k</strong>, find the maximum element in every subarray of size <strong>k</strong>. Return a list of these maximum values for all subarrays.</p>

<p><strong>Sample Test Cases:</strong></p>
<ol>
    <li><strong>Input:</strong> arr = [2, 1, 5, 1, 3, 2], k = 3<br>
    <strong>Output:</strong> [5, 5, 5, 3]<br>
    <strong>Explanation:</strong> The maximum values of the subarrays [2,1,5], [1,5,1], [5,1,3], and [1,3,2] are 5, 5, 5, and 3 respectively.</li>
    <li><strong>Input:</strong> arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3<br>
    <strong>Output:</strong> [3, 3, 5, 5, 6, 7]<br>
    <strong>Explanation:</strong> The maximum values of the subarrays are [3, 3, 5, 5, 6, 7].</li>
</ol>

<p><strong>Approach 1: Brute Force</strong></p>

<p><strong>Intuition:</strong><br>
In the brute force approach, we calculate the maximum for every subarray of size <strong>k</strong> by using two nested loops. For each subarray, we find the maximum element by iterating over its elements and store the result in a list.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Use an outer loop to iterate over all starting indices of subarrays of size <strong>k</strong>.</li>
    <li>For each subarray, use an inner loop to find the maximum element.</li>
    <li>Store the maximum value of each subarray in a list.</li>
    <li>Return the list of maximum values.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n, arr, k):
    final = []
    for i in range(n - k + 1):  # Loop to generate all subarrays of size k
        maxi = float('-inf')  # Track the maximum value
        for j in range(i, i + k):  # Find the maximum in the current subarray
            maxi = max(maxi, arr[j])
        final.append(maxi)  # Store the maximum of the subarray
    return final
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n * k), as we calculate the maximum for each subarray.</li>
    <li><strong>Space Complexity:</strong> O(n), as we store the result in a list.</li>
</ul>

<p><strong>Approach 2: Optimized Approach (Sliding Window + Deque)</strong></p>

<p><strong>Intuition:</strong><br></p>
<pre>
The optimized approach utilizes a combination of the **sliding window technique** and a **deque** (double-ended queue) to efficiently find the maximum values of all subarrays of size <strong>k</strong>. 

1. **Sliding Window:** This technique involves maintaining a window of size <strong>k</strong> that moves across the array. As the window slides from left to right, we update the maximum value by removing elements that are no longer in the window and adding new elements.
  
2. **Using Deque:** The deque is particularly useful here because it allows us to maintain a list of indices of the array elements in such a way that we can quickly access the maximum element. By maintaining indices of the elements in decreasing order, we ensure that the front of the deque always points to the maximum element in the current window. If we encounter an element larger than the elements represented by the indices in the deque, we remove those indices from the back. This guarantees that the largest element is always available at the front of the deque, facilitating constant time retrieval of the maximum for the current window.

This combined approach ensures that we can efficiently calculate the maximum for each sliding window of size <strong>k</strong> in linear time.
</pre>

<p><strong>Detailed Steps to Solve:</strong></p>
<ol>
    <li><strong>Initialization:</strong>
        <ul>
            <li>Create a deque <strong>q</strong> to store indices of the elements in the current window.</li>
            <li>Create a list <strong>final</strong> to store the maximums of each subarray.</li>
        </ul>
    </li>
    <li><strong>Processing the First Window:</strong>
        <ul>
            <li>Iterate through the first <strong>k</strong> elements of the array.</li>
            <li>For each element, remove elements from the back of the deque while the current element is greater than or equal to the elements represented by those indices. This ensures that the deque will always contain indices of elements in decreasing order.</li>
            <li>Add the current index to the deque.</li>
        </ul>
    </li>
    <li><strong>Sliding the Window:</strong>
        <ul>
            <li>For each subsequent element in the array (from index <strong>k</strong> to <strong>n-1</strong>):</li>
            <ul>
                <li>Add the element at the index represented by the front of the deque to the <strong>final</strong> list. This index points to the maximum element of the previous window.</li>
                <li>Remove indices from the front of the deque that are out of the bounds of the current window (i.e., if the index at the front of the deque is less than or equal to <strong>i - k</strong>).</li>
                <li>Repeat the process of removing elements from the back of the deque that are less than or equal to the current element to maintain the decreasing order.</li>
                <li>Add the current index to the deque.</li>
            </ul>
        </ul>
    </li>
    <li><strong>Final Step:</strong>
        <ul>
            <li>Add the maximum of the last window (pointed to by the front of the deque) to the <strong>final</strong> list.</li>
        </ul>
    </li>
</ol>

<p><strong>Code:</strong></p>

```python
from collections import deque
def optimized(n,arr,k):
    q=deque()
    for i in range(k):
        while q and arr[i]>=arr[q[-1]]:
            q.pop()
        q.append(i)
    final=[arr[q[0]]]
    for i in range(k,n):
        while q and q[0]<=i-k:
            q.popleft()
        while q and arr[i]>=arr[q[-1]]:
            q.pop()
        q.append(i)
        final.append(arr[q[0]])
    return final
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n), since each element is added and removed from the deque at most once, leading to a linear pass through the array.</li>
    <li><strong>Space Complexity:</strong> O(k), as the deque stores at most <strong>k</strong> indices at a time, corresponding to the current window of size <strong>k</strong>.</li>
</ul>


<br>
<br>

<h2>Sum of minimum and maximum elements of subarray of size k</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given an array of integers <strong>arr</strong> and an integer <strong>k</strong>, calculate the sum of the minimum and maximum values in every contiguous subarray of size <strong>k</strong>. Return the total sum of these values for all subarrays.</p>

<p><strong>Sample Test Cases:</strong></p>
<ol>
    <li><strong>Input:</strong> arr = [1, 3, 2, 5, 4], k = 3<br>
    <strong>Output:</strong> 21<br>
    <strong>Explanation:</strong> The subarrays of size 3 are [1, 3, 2], [3, 2, 5], and [2, 5, 4]. Their minimum and maximum sums are (1+3) + (2+5) + (2+5) = 4 + 8 + 6 = 18.</li>
    <li><strong>Input:</strong> arr = [4, 2, 1, 3, 5], k = 2<br>
    <strong>Output:</strong> 22<br>
    <strong>Explanation:</strong> The subarrays are [4, 2], [2, 1], [1, 3], [3, 5]. Their minimum and maximum sums are (2+4) + (1+2) + (1+3) + (3+5) = 6 + 3 + 4 + 8 = 21.</li>
</ol>

<p><strong>Approach 1: Brute Force</strong></p>

<p><strong>Intuition:</strong><br>
In the brute force approach, we iterate through all possible contiguous subarrays of size <strong>k</strong>. For each subarray, we determine the minimum and maximum elements by iterating through the subarray elements. We then accumulate the sum of these min-max pairs for all subarrays.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize a variable <strong>total</strong> to store the cumulative sum.</li>
    <li>Use an outer loop to iterate over all starting indices of subarrays of size <strong>k</strong>.</li>
    <li>For each subarray, initialize <strong>mini</strong> to infinity and <strong>maxi</strong> to negative infinity.</li>
    <li>Use an inner loop to find the minimum and maximum in the current subarray.</li>
    <li>Add the sum of the minimum and maximum to <strong>total</strong>.</li>
    <li>Return <strong>total</strong>.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n, arr, k):
    total = 0
    for i in range(n - k + 1):  # Loop to generate all subarrays of size k
        mini, maxi = float('inf'), float('-inf')  # Track min and max
        for j in range(i, i + k):  # Find min and max in the current subarray
            mini = min(mini, arr[j])
            maxi = max(maxi, arr[j])
        total += (mini + maxi)  # Update total with min + max
    return total
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n * k), as we calculate the min and max for each subarray.</li>
    <li><strong>Space Complexity:</strong> O(1), since no extra space is required except for variables.</li>
</ul>

<p><strong>Approach 2: Optimized Approach (Sliding Window + Deque)</strong></p>

<p><strong>Intuition:</strong><br></p>
<pre>
The optimized approach uses a **sliding window technique** along with two deques to efficiently track the minimum and maximum values in the current window of size <strong>k</strong>. The deques store indices of the array elements in a way that allows quick access to the minimum and maximum values as the window slides across the array.

1. **Maintaining Deques:** We maintain two deques:
   - One for the minimum values, which stores indices of elements in increasing order (so the front always points to the smallest element).
   - Another for the maximum values, which stores indices in decreasing order (so the front always points to the largest element).

2. **Updating the Window:** As we slide the window across the array, we remove elements that are out of the current window from both deques and add the new element, ensuring the order is maintained. This allows us to get the min and max of the current window in constant time.

This method allows us to compute the sum of the minimum and maximum of all subarrays of size <strong>k</strong> in linear time.
</pre>

<p><strong>Detailed Steps to Solve:</strong></p>
<ol>
    <li><strong>Initialization:</strong>
        <ul>
            <li>Create two deques, <strong>smaller</strong> for tracking the minimums and <strong>greater</strong> for tracking the maximums.</li>
            <li>Initialize a variable <strong>total</strong> to accumulate the sums.</li>
        </ul>
    </li>
    <li><strong>Processing the First Window:</strong>
        <ul>
            <li>Iterate through the first <strong>k</strong> elements of the array.</li>
            <li>For each element, maintain the order in both deques by popping elements from the back if the current element is smaller (for min deque) or larger (for max deque).</li>
            <li>Add the current index to both deques.</li>
        </ul>
    </li>
    <li><strong>Sliding the Window:</strong>
        <ul>
            <li>For each subsequent element in the array (from index <strong>k</strong> to <strong>n-1</strong>):</li>
            <ul>
                <li>Add the current window's minimum and maximum (from the front of the respective deques) to <strong>total</strong>.</li>
                <li>Remove elements from the front of the deques that are out of the bounds of the current window.</li>
                <li>Maintain the order in both deques for the new element by removing smaller (for min) or larger (for max) elements from the back.</li>
                <li>Add the current index to both deques.</li>
            </ul>
        </ul>
    </li>
    <li><strong>Final Step:</strong>
        <ul>
            <li>Add the minimum and maximum of the last window (pointed to by the front of the deques) to <strong>total</strong>.</li>
        </ul>
    </li>
</ol>

<p><strong>Code:</strong></p>

```python
from collections import deque
def optimized(n, arr, k):
    total = 0
    smaller = deque()  # For min
    greater = deque()  # For max

    # Process the first k elements
    for i in range(k):
        while smaller and arr[i] <= arr[smaller[-1]]:
            smaller.pop()  # Remove indices of elements larger than current
        while greater and arr[i] >= arr[greater[-1]]:
            greater.pop()  # Remove indices of elements smaller than current
        smaller.append(i)  # Add current index for min
        greater.append(i)  # Add current index for max
    
    # Process the rest of the array
    for i in range(k, n):
        total += (arr[smaller[0]] + arr[greater[0]])  # Add min and max of the previous window
        
        # Remove elements out of the current window
        while smaller and smaller[0] <= i - k:
            smaller.popleft()
        while greater and greater[0] <= i - k:
            greater.popleft()
        
        # Maintain the order for the new element
        while smaller and arr[i] <= arr[smaller[-1]]:
            smaller.pop()
        while greater and arr[i] >= arr[greater[-1]]:
            greater.pop()
        smaller.append(i)  # Add current index for min
        greater.append(i)  # Add current index for max
    
    total += (arr[smaller[0]] + arr[greater[0]])  # Add min and max of the last window
    return total
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n), since each element is added and removed from the deques at most once.</li>
    <li><strong>Space Complexity:</strong> O(k), as the deques store at most <strong>k</strong> indices at a time.</li>
</ul>

<br>
<br>

<h2>Count Of Distinct Elements In All Subarrays Of Size k</h2>
<p><strong>Problem Statement:</strong></p>
<p>Given an array of integers <strong>arr</strong> and an integer <strong>k</strong>, find the count of distinct integers in every contiguous subarray of size <strong>k</strong>.</p>

<p><strong>Sample Test Cases:</strong></p>
<ol>
    <li><strong>Input:</strong> arr = [1, 2, 1, 3, 4], k = 3<br>
    <strong>Output:</strong> [2, 3, 3]<br>
    <strong>Explanation:</strong> The subarrays of size 3 are: 
        <ul>
            <li>[1, 2, 1] - Distinct Count: 2</li>
            <li>[2, 1, 3] - Distinct Count: 3</li>
            <li>[1, 3, 4] - Distinct Count: 3</li>
        </ul>
    </li>
    <li><strong>Input:</strong> arr = [1, 1, 2, 2, 3], k = 2<br>
    <strong>Output:</strong> [2, 2, 2, 2]<br>
    <strong>Explanation:</strong> The subarrays of size 2 are: 
        <ul>
            <li>[1, 1] - Distinct Count: 2</li>
            <li>[1, 2] - Distinct Count: 2</li>
            <li>[2, 2] - Distinct Count: 2</li>
            <li>[2, 3] - Distinct Count: 2</li>
        </ul>
    </li>
</ol>

<p><strong>Approach 1: Brute Force</strong></p>

<p><strong>Intuition:</strong><br>
In the brute force approach, we iterate through all possible contiguous subarrays of size <strong>k</strong>. For each subarray, we use a dictionary to track the distinct elements and their counts. The size of this dictionary gives the count of distinct integers in the current subarray.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize an empty list <strong>ans</strong> to store the counts of distinct integers.</li>
    <li>Use an outer loop to iterate over all starting indices of subarrays of size <strong>k</strong>.</li>
    <li>For each subarray, initialize a dictionary <strong>distinct</strong> to track counts of elements.</li>
    <li>Use an inner loop to populate the dictionary with the elements in the current subarray.</li>
    <li>Add the length of the dictionary to <strong>ans</strong>.</li>
    <li>Return <strong>ans</strong>.</li>
</ol>

<p><strong>Code:</strong></p>

```python
from collections import defaultdict
def bruteForce(n, arr, k):
    ans = []
    for i in range(n - k + 1):  # Loop to generate all subarrays of size k
        distinct = defaultdict(lambda: 0)  # Track distinct elements
        for j in range(i, i + k):  # Populate distinct elements in the current subarray
            distinct[arr[j]] += 1
        ans.append(len(distinct))  # Append count of distinct elements
    return ans
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n * k), as we iterate over all subarrays and count elements.</li>
    <li><strong>Space Complexity:</strong> O(k), for the dictionary storing distinct elements in the current subarray.</li>
</ul>

<p><strong>Approach 2: Optimized Approach (Sliding Window)</strong></p>

<p><strong>Intuition:</strong><br>
The optimized approach uses a **sliding window technique** to maintain the count of distinct integers in the current window of size <strong>k</strong>. This is done by adjusting the counts of elements as the window slides over the array, allowing us to efficiently compute the number of distinct integers without re-evaluating the entire subarray.</p>

<p><strong>Detailed Steps to Solve:</strong></p>
<ol>
    <li><strong>Initialization:</strong>
        <ul>
            <li>Create a dictionary <strong>count</strong> to track counts of elements and a variable <strong>cnt</strong> to track the number of distinct elements.</li>
            <li>Set <strong>left</strong> and <strong>right</strong> pointers to define the window, starting with <strong>right</strong> at the end of the first window.</li>
        </ul>
    </li>
    <li><strong>Processing the First Window:</strong>
        <ul>
            <li>Iterate through the first <strong>k</strong> elements, updating <strong>count</strong> and <strong>cnt</strong> accordingly.</li>
        </ul>
    </li>
    <li><strong>Sliding the Window:</strong>
        <ul>
            <li>For each subsequent element in the array (from index <strong>k</strong> to <strong>n-1</strong>):</li>
            <ul>
                <li>Remove the element at <strong>left</strong> from <strong>count</strong>. If its count goes to zero, decrease <strong>cnt</strong>.</li>
                <li>Add the element at <strong>right</strong> to <strong>count</strong>. If it's a new element, increase <strong>cnt</strong>.</li>
                <li>Append <strong>cnt</strong> to <strong>ans</strong>.</li>
                <li>Move both <strong>left</strong> and <strong>right</strong> pointers forward.</li>
            </ul>
        </ul>
    </li>
    <li><strong>Return Result:</strong>
        <ul>
            <li>Return the list <strong>ans</strong> containing counts of distinct integers for all subarrays of size <strong>k</strong>.</li>
        </ul>
    </li>
</ol>

<p><strong>Code:</strong></p>

```python
from collections import defaultdict
def optimized(n, arr, k):
    ans = []
    left, right = 0, 0
    count = defaultdict(lambda: 0)  # Track counts of elements
    cnt = 0  # Count of distinct elements
    
    # Process the first k elements
    while right < k:
        if arr[right] not in count:  # New distinct element
            cnt += 1
        count[arr[right]] += 1  # Increment count of the current element
        right += 1
    ans.append(cnt)  # Append count for the first window
    
    # Process the rest of the array
    while right < n:
        # Remove the leftmost element
        if count[arr[left]] == 1:  # If it was unique
            cnt -= 1
        count[arr[left]] -= 1  # Decrement count
        left += 1  # Move left pointer forward
        
        # Add the new rightmost element
        if count[arr[right]] == 0:  # New distinct element
            cnt += 1
        count[arr[right]] += 1  # Increment count
        ans.append(cnt)  # Append count for the current window
        
        right += 1  # Move right pointer forward
    return ans
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n), since each element is processed at most twice (once added, once removed).</li>
    <li><strong>Space Complexity:</strong> O(k), for the dictionary storing counts of elements in the current window.</li>
</ul>

<br>
<br>

<h2>Find First Negative Number Of Subarray Of Size k</h2>

<p><strong>Problem Statement:</strong></p>
<p>Given an array of integers <strong>arr</strong> and an integer <strong>k</strong>, find the first negative integer in every contiguous subarray of size <strong>k</strong>. If there are no negative integers in a subarray, return 0 for that subarray.</p>

<p><strong>Sample Test Cases:</strong></p>
<ol>
    <li><strong>Input:</strong> arr = [1, -2, 3, -4, 5], k = 2<br>
    <strong>Output:</strong> [-2, -4, 0]<br>
    <strong>Explanation:</strong> 
        <ul>
            <li>Subarray [1, -2]: First negative integer is -2.</li>
            <li>Subarray [-2, 3]: First negative integer is -2.</li>
            <li>Subarray [3, -4]: First negative integer is -4.</li>
            <li>Subarray [-4, 5]: First negative integer is -4.</li>
        </ul>
    </li>
    <li><strong>Input:</strong> arr = [1, 2, 3, 4, 5], k = 3<br>
    <strong>Output:</strong> [0, 0]<br>
    <strong>Explanation:</strong> There are no negative integers in any of the subarrays of size 3.</li>
</ol>

<p><strong>Approach 1: Brute Force</strong></p>

<p><strong>Intuition:</strong><br>
In the brute force approach, we iterate through all possible contiguous subarrays of size <strong>k</strong> and check each element to find the first negative integer. If we find one, we break out of the inner loop and store that value; if there is none, we store 0.</p>

<p><strong>Steps to Solve:</strong></p>
<ol>
    <li>Initialize an empty list <strong>ans</strong> to store the first negative integers.</li>
    <li>Use an outer loop to iterate over all starting indices of subarrays of size <strong>k</strong>.</li>
    <li>For each subarray, use an inner loop to check for the first negative integer.</li>
    <li>If a negative integer is found, append it to <strong>ans</strong>; otherwise, append 0.</li>
    <li>Return <strong>ans</strong>.</li>
</ol>

<p><strong>Code:</strong></p>

```python
def bruteForce(n, arr, k):
    ans = []
    for i in range(n - k + 1):  # Loop to generate all subarrays of size k
        neg = 0
        for j in range(i, i + k):  # Check each element in the current subarray
            if arr[j] < 0:  # If negative, store it and break
                neg = arr[j]
                break
        ans.append(neg)  # Append found negative or 0
    return ans
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n * k), as we iterate over all subarrays and check each element.</li>
    <li><strong>Space Complexity:</strong> O(k), for the list storing the first negative integers for each subarray.</li>
</ul>

<p><strong>Approach 2: Optimized Approach (Sliding Window)</strong></p>

<p><strong>Intuition:</strong><br>
The optimized approach uses a **deque** (double-ended queue) to keep track of the indices of negative integers in the current window of size <strong>k</strong>. This allows us to efficiently find the first negative integer as the window slides, without needing to re-evaluate all elements in the current window.</p>

<p><strong>Detailed Steps to Solve:</strong></p>
<ol>
    <li><strong>Initialization:</strong>
        <ul>
            <li>Create a deque <strong>q</strong> to store indices of negative integers.</li>
            <li>Set <strong>left</strong> and <strong>right</strong> pointers to define the window, starting with <strong>right</strong> at the end of the first window.</li>
        </ul>
    </li>
    <li><strong>Processing the First Window:</strong>
        <ul>
            <li>Iterate through the first <strong>k</strong> elements and fill the deque with indices of negative integers.</li>
        </ul>
    </li>
    <li><strong>Sliding the Window:</strong>
        <ul>
            <li>For each subsequent element in the array (from index <strong>k</strong> to <strong>n-1</strong>):</li>
            <ul>
                <li>If the deque is not empty, append the first element (the first negative integer) to <strong>ans</strong>.</li>
                <li>Remove indices that are out of the bounds of the current window from the front of the deque.</li>
                <li>If the new element is negative, add its index to the deque.</li>
            </ul>
        </ul>
    </li>
    <li><strong>Return Result:</strong>
        <ul>
            <li>After processing all elements, append the first negative integer of the last window to <strong>ans</strong>.</li>
            <li>Return the list <strong>ans</strong> containing the first negative integers for all subarrays of size <strong>k</strong>.</li>
        </ul>
    </li>
</ol>

<p><strong>Code:</strong></p>

```python
from collections import deque
def optimized(n, arr, k):
    ans = []
    q = deque()
    
    # Process the first k elements
    for i in range(k):
        if arr[i] < 0:  # If it's negative, store its index
            q.append(i)

    # Process the rest of the array
    for i in range(k, n):
        if q:  # If there are negative numbers, take the first one
            ans.append(arr[q[0]])
        else:
            ans.append(0)  # No negative number in the current window

        # Remove indices that are out of the bounds of the current window
        while q and q[0] <= i - k:
            q.popleft()

        if arr[i] < 0:  # If the new element is negative, add its index to the deque
            q.append(i)

    # Process the last window
    ans.append(arr[q[0]] if q else 0)
    return ans
```

<p><strong>Time and Space Complexity:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n), as each element is processed at most twice (once added, once removed).</li>
    <li><strong>Space Complexity:</strong> O(k), for the deque storing indices of negative elements in the current window.</li>
</ul>
