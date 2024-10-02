<h1>Two Pointer & Sliding Window</h1>
<h2>Two Pointer</h2>
<p>The two-pointer technique is a fundamental algorithmic approach that plays a pivotal role in optimizing solutions to specific types of problems in computer science.</p>
<p>This strategy involves to use two/more pointers which points to indices of a data structure, that pointers traverse in data structure in different ways to achieve specific goal to solve problems efficiently.</p>
<p>By manipulating the positions of these two pointers , the technique aims to efficiently address a wide range of problems, making it a valuable tool in a programmer’s toolkit.</p>
<h3>When To Use ?</h3>
<ol>
	<li><strong>Searching for Pairs or Subarrays</strong></li>
	<ul>
		<li>When you need to find pairs of elements with certain properties, such as pairs that sum to a target value or pairs with a specific difference, the two-pointer technique can be very effective.</li>
		<li><strong>Example</strong> : Finding a pair of numbers in a sorted array that sums to a target value.</li>
	</ul>
	<li><strong>Checking for Palindrome</strong></li>
	<ul>
		<li>When you need to check if a sequence is a palindrome (reads the same forwards and backwards), you can use two pointers starting from both ends of the sequence and move them toward each other while comparing elements.</li>
		<li><strong>Example</strong> : Checking if a string is a palindrome.</li>
	</ul>
	<li><strong>Removing Duplicates in Sorted Arrays</strong></li>
	<ul>
		<li>When you have a sorted array and want to remove duplicate elements in-place, you can use two pointers to track the unique elements.</li>
		<li><strong>Example</strong> : Example: Removing duplicates from a sorted array.</li>
	</ul>
	<li><strong>Finding Triplets or Quadruplets</strong></li>
	<ul>
		<li>When you need to find triplets or quadruplets of elements with specific properties, you can use multiple pointers and combinations to explore different possibilities efficiently.</li>
		<li><strong>Example</strong> : Finding triplets in an array that sum to a target value.</li>
	</ul>
	<li><strong>Merging or Intersecting Arrays</strong></li>
	<ul>
		<li>When you have two sorted arrays and want to merge them or find their intersection, the two-pointer technique can be employed to compare and merge elements in a single pass.</li>
		<li><strong>Example</strong> : Merging two sorted arrays or finding the intersection of two sorted arrays.</li>
	</ul>
	<li><strong>Searching in a Sorted Matrix</strong></li>
	<ul>
		<li>When you have a 2D matrix with sorted rows and columns, you can use two pointers to navigate through the matrix efficiently while searching for a specific element.</li>
		<li><strong>Example</strong> : Searching for a target element in a sorted matrix.</li>
	</ul>
	<li><strong>Sliding Window Problems</strong></li>
	<ul>
		<li>When solving problems that involve finding a subarray of fixed or variable length with specific properties (e.g., maximum sum, minimum length, etc.), two pointers can help maintain the subarray efficiently as you slide the window.</li>
		<li><strong>Example</strong> : Finding the maximum sum of a subarray of a fixed size.</li>
	</ul>
	<li><strong>Partitioning and Sorting</strong></li>
	<ul>
		<li>When partitioning an array (e.g., QuickSort’s partition step) or sorting elements with specific conditions, the two-pointer technique can be used to rearrange elements efficiently.</li>
		<li><strong>Example</strong> : Implementing the partition step in QuickSort.</li>
	</ul>
	<li><strong>Linked List Problems</strong></li>
	<ul>
		<li>It can be used in problems involving linked lists, two pointers can be used to find cycles, determine intersections or merge sorted linked lists.</li>
		<li><strong>Example</strong> :Check cycle present in linked list </li>
	</ul>
	<li><strong>String Manipulation</strong></li>
	<ul>
		<li>Many string manipulation problems, such as checking for palindromes, finding sub-strings, or performing in-place replacements, can benefit from Two Pointers.</li>
		<li><strong>Example</strong> : Check given string is palindrome or not</li>
	</ul>
</ol>

<h3>How to use ?</h3>
<ul>
	<li>Determine if the problem involves any above pattern.Check if any two positions are need to move simultaneously to solve problem in a linear data struncture. Then we can use the approach</li>
	<li>Determine what pointers should represent in given problem, indices or values..etc</li>
	<li>Intialize pointers, depending up on the problem need, assing starting position for each pointer</li>
	<li>Find out the condition for moving pointers</li>
	<li>Determine, how pointers should move/change.Adjust pointers based on the current condition or requirement of the problem.</li>
	<li>Determine when to stop the moving of pointers</li>
	<li>Consider edge cases such as empty arrays, single-element arrays, or scenarios where no valid pairs or subarrays exist.</li>
</ul>

<h3>Types of Two Pointers</h3>
<h4>Based on direction and movement of pointers</h4>
<ol>
	<li><strong>Collision</strong></li>
	<ul>
		<li>Two pointers start from opposite ends and move towards each other.</li>
		<li><strong>Example</strong> : Finding two numbers in a sorted array that sum up to a target.</li>
	</ul>
	<li><strong>Forward/Backward</strong></li>
	<ul>
		<li>Two pointers move either forward or backward in the same direction through a single array.</li>	
	</ul>
	<li><strong>Parallel</strong></li>
	<ul>
		<li>Two pointers simultaneously traverse two separate arrays or lists.</li>
		<li><strong>Example</strong> : Finding intersections between two lists of intervals.</li>
	</ul>
	<li><strong>Sliding Window</strong></li>
	<ul>
		<li>Two pointers move in the same direction with a fixed difference between them</li>
		<li><strong>Example</strong> : Finding the maximum sum of a subarray of size k in an array.</li>
	</ul>
	<li><strong>Fast/Slow</strong></li>
	<ul>
		<li>Two pointers where one moves faster than the other.</li>
		<li><strong>Example</strong> : Removing duplicates from a sorted array or detecting cycles in a linked list.</li>
	</ul>
</ol>


<h2>Sliding Window</h2>
<p><strong>Here’s a detailed explanation of each sliding window pattern with real-world examples:</strong></p>

<ol>
  <li><strong>Fixed Sliding Window Pattern</strong>
    <p>The window size is fixed, and you slide it over the array or string to perform calculations. This is useful when the window size is constant, and you need to process a sequence of consecutive elements.</p>
    <ul>
      <li><strong>Example 1: Maximum Sum Subarray of Size K</strong>
        <p>You are given an array, and you need to find the maximum sum of any contiguous subarray of size K.</p>
        <p><strong>Input:</strong> [2, 1, 5, 1, 3, 2], K = 3</p>
        <p><strong>Output:</strong> 9</p>
        <p><strong>Explanation:</strong> The subarrays of size 3 are [2, 1, 5], [1, 5, 1], [5, 1, 3], and [1, 3, 2]. The maximum sum is 9 from the subarray [5, 1, 3].</p>
      </li>
      <li><strong>Example 2: First Negative Integer in Every Window of Size K</strong>
        <p>In this problem, you are asked to find the first negative integer for every window of size K.</p>
        <p><strong>Input:</strong> [12, -1, -7, 8, 15, 30, 16, 28], K = 3</p>
        <p><strong>Output:</strong> [-1, -1, -7, -7, 0, 0]</p>
        <p><strong>Explanation:</strong> For each window, you slide and check the first negative integer. If none exists, return 0.</p>
      </li>
    </ul>
  </li>

  <li><strong>Dynamic Sliding Window Pattern</strong>
    <p>In dynamic sliding window problems, the window size varies based on conditions, and you dynamically expand or contract the window until the condition is satisfied.</p>
    <ul>
      <li><strong>Example 1: Smallest Subarray with a Given Sum</strong>
        <p>You are given an array and a target sum. Find the smallest contiguous subarray whose sum is greater than or equal to the target.</p>
        <p><strong>Input:</strong> [2, 1, 5, 2, 3, 2], Target = 7</p>
        <p><strong>Output:</strong> 2</p>
        <p><strong>Explanation:</strong> The smallest subarray with a sum of at least 7 is [5, 2] with a length of 2.</p>
      </li>
      <li><strong>Example 2: Longest Substring with K Distinct Characters</strong>
        <p>Given a string, find the length of the longest substring that contains exactly K distinct characters.</p>
        <p><strong>Input:</strong> "araaci", K = 2</p>
        <p><strong>Output:</strong> 4</p>
        <p><strong>Explanation:</strong> The longest substring with exactly 2 distinct characters is "araa" with a length of 4.</p>
      </li>
    </ul>
  </li>

  <li><strong>Caterpillar Method (Two-Pointer Sliding Window)</strong>
    <p>This method involves using two pointers (start and end) to expand and contract a window over the array. It’s often used when you need to count subarrays that meet a certain condition.</p>
    <ul>
      <li><strong>Example 1: Number of Subarrays with Sum Equals K</strong>
        <p>Find the number of contiguous subarrays that sum up to a given value K.</p>
        <p><strong>Input:</strong> [1, 1, 1], K = 2</p>
        <p><strong>Output:</strong> 2</p>
        <p><strong>Explanation:</strong> There are two subarrays [1, 1] that sum to 2.</p>
      </li>
      <li><strong>Example 2: Subarray Product Less Than K</strong>
        <p>Given an array of integers, count the number of contiguous subarrays where the product of the elements is less than K.</p>
        <p><strong>Input:</strong> [10, 5, 2, 6], K = 100</p>
        <p><strong>Output:</strong> 8</p>
        <p><strong>Explanation:</strong> The valid subarrays are [10], [5], [2], [6], [5, 2], [2, 6], [5, 2, 6], and [10, 5].</p>
      </li>
    </ul>
  </li>

  <li><strong>Expanding/Shrinking Sliding Window Pattern</strong>
    <p>This pattern is common for string problems where you need to adjust the window size dynamically by expanding and shrinking it to meet certain constraints (e.g., unique characters, distinct elements).</p>
    <ul>
      <li><strong>Example 1: Longest Substring Without Repeating Characters</strong>
        <p>Find the length of the longest substring without any repeating characters.</p>
        <p><strong>Input:</strong> "abcabcbb"</p>
        <p><strong>Output:</strong> 3</p>
        <p><strong>Explanation:</strong> The longest substring without repeating characters is "abc", which has a length of 3.</p>
      </li>
      <li><strong>Example 2: Longest Substring with At Most Two Distinct Characters</strong>
        <p>Given a string, find the length of the longest substring that contains at most 2 distinct characters.</p>
        <p><strong>Input:</strong> "eceba"</p>
        <p><strong>Output:</strong> 3</p>
        <p><strong>Explanation:</strong> The longest substring with at most two distinct characters is "ece" with a length of 3.</p>
      </li>
    </ul>
  </li>

  <li><strong>Exact Subarray Count Pattern</strong>
    <p>In this pattern, the goal is to count the number of subarrays with exactly K elements or features. It involves finding subarrays with at most K elements and subtracting subarrays with at most K-1 elements.</p>
    <ul>
      <li><strong>Example 1: Subarrays with Exactly K Distinct Integers</strong>
        <p>Find the number of subarrays with exactly K distinct integers.</p>
        <p><strong>Input:</strong> [1, 2, 1, 2, 3], K = 2</p>
        <p><strong>Output:</strong> 7</p>
        <p><strong>Explanation:</strong> The subarrays with exactly 2 distinct integers are [1, 2], [2, 1], [1, 2], [2, 3], [1, 2, 1], [2, 1, 2], and [1, 2, 3].</p>
      </li>
      <li><strong>Example 2: Subarrays with Exactly K Odd Numbers</strong>
        <p>Find the number of subarrays with exactly K odd numbers.</p>
        <p><strong>Input:</strong> [1, 2, 3, 4, 5], K = 2</p>
        <p><strong>Output:</strong> 4</p>
        <p><strong>Explanation:</strong> The subarrays with exactly two odd numbers are [1, 2, 3], [1, 2, 3, 4], [3, 4, 5], and [2, 3, 4, 5].</p>
      </li>
    </ul>
  </li>

  <li><strong>Important LeetCode Problems</strong>
    <p>Here are some well-known problems from LeetCode based on these patterns:</p>
    <ul>
      <li><strong>Fixed Sliding Window:</strong>
        <ul>
          <li>Maximum Sum of K Consecutive Elements</li>
          <li>First Negative Integer in Every Window of Size K</li>
          <li>Average of Subarrays of Size K</li>
        </ul>
      </li>
      <li><strong>Dynamic Sliding Window:</strong>
        <ul>
          <li>Smallest Subarray with a Given Sum</li>
          <li>Longest Substring with K Distinct Characters</li>
          <li>Fruits into Baskets (Longest Subarray with At Most Two Distinct Characters)</li>
        </ul>
      </li>
      <li><strong>Caterpillar Method:</strong>
        <ul>
          <li>Number of Subarrays with Sum Equals K</li>
          <li>Subarray Product Less than K</li>
        </ul>
      </li>
      <li><strong>Expanding/Shrinking Sliding Window:</strong>
        <ul>
          <li>Longest Substring Without Repeating Characters</li>
          <li>Minimum Window Substring</li>
        </ul>
      </li>
    </ul>
  </li>
</ol>
