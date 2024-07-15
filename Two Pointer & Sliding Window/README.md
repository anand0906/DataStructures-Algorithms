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
<h3>Problems</h3>

| Problem | Article | Practice |
| :---         |     :---:      |     :---:     |
| Two Sum | <a href="../Arrays#two-sum--check-if-a-pair-with-given-sum-exists-in-array/">Click Here</a> | <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/">LeetCode</a> |
| Three Sum | <a href="../Arrays#3-sum--find-triplets-that-add-up-to-a-zero/">Click Here</a> | <a href="https://leetcode.com/problems/3sum/description/">LeetCode</a> |
| Four Sum | <a href="../Arrays#4-sum---find-quads-that-add-up-to-a-target-value/">Click Here</a> | <a href="https://leetcode.com/problems/4sum/description/">LeetCode</a> |
