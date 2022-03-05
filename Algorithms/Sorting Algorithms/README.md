<h1>Sorting Algorithms</h1>
<h3>Sorting</h3>
<p>sorting is the process of organizing the set of elements in a specified order based on the relationship between them. (Or)<br>Sorting is method of arranging elements either lowest to highest or vice-versa.</p>
<p>They are mostly two types of sortings</p>
<ul>
<li>Sorting in Incresing Order(Ascending Order)-Low to High</li>
<li>Sorting in decresing Order(Descending Order)-High to Low</li>
</ul>
<h3>Application of sorting</h3>
<ul>
	<li>In Ecommerce webites like amazon,flipkart..etc. Inorder sort the products based on price,rating,availabity.Sorting technques are widely used.</li>	
	<li>There are social media applications, news applications, even your emails or file managers, where you want things to be arranged according to dates. You want the newest on top and oldest at the end. And this feature uses the method of sorting. And more specifically, sorting based on the date of publishing/modification</li>
	<li>most useful application is the dictionary.  In a dictionary, the words are sorted lexicographically for you to find any word easily. </li>
	<li>Another easy concept is that of binary search. If you remember, we discussed in the beginning that searching in a sorted array takes at most O(log N) time. And when it's not sorted, it can take up to O(n). So, when an array is sorted, it minimizes the effort to find an element. Retrieval becomes much faster</li>
</ul>
<h3>criteria for analyzing different sorting algorithms</h3>
<h6>Classification of sorting alogorithms based on following parameters</h6>
<ul>
	<li>Time Complexity</li>
	<li>Space Complexity</li>
	<li>Stability</li>
	<li>Adaptivity</li>
	<li>Internal & External Sorting</li>
</ul>
<h5>Time Complexity</h5>
<p>Time Complexity is defined as the number of times a particular instruction set is executed rather than the total time is taken. It is because the total time took also depends on some external factors like the compiler used, processor’s speed, etc</p>
<p>We observe the time complexity of an algorithm to see which algorithm works efficiently for larger data sets and which algorithm works faster with smaller data sets. What if one sorting algorithm sorts only 4 elements efficiently and fails to sort 1000 elements. What if it takes too much time to sort a large data set? These are the cases where we say the time complexity of an algorithm is very poor</p>
<p>Generally sorting algorithms will give two types of time complexities such as O(nlogn) and o(n^2)</p>
<p>O(N log N) is considered a better algorithm time complexity than O(N 2), and most of our algorithms’ time complexity revolves around these two</p>
<h5>Space Complexity</h5>
<p>Space Complexity is the total memory space required by the program for its execution.</p>
<p>The space complexity criterion helps us compare the space the algorithm uses to sort any data set. If an algorithm consumes a lot of space for larger inputs, it is considered a poor algorithm for sorting large data sets. In some cases, we might prefer a higher space complexity algorithm if it proposes exceptionally low time complexity, but not in general.</p>
<h5>Stabilty</h5>
<p>Stability is mainly important when we have key value pairs with duplicate keys possible (like people names as keys and their details as values). And we wish to sort these objects by keys.</p>
<p>A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.</p>
<img src="https://www.geeksforgeeks.org/wp-content/uploads/stability-sorting-660x343.jpg">
<h6>Stable Sorting Algorithms</h6>
<ul>
	<li>Bubble Sort</li>
	<li>Insertion Sort</li>
	<li>Merge Sort</li>
	<li>Tim Sort</li>
	<li>Counting Sort</li>
</ul>
<h6>UnStable Sorting Algorithms</h6>
<ul>
	<li>Quick Sort</li>
	<li>Heap Sort</li>
	<li>Insertion Sort</li>
</ul>
<h5>Adaptivity</h5>
<p>Algorithms that adapt to the fact that if the data are already sorted and it must take less time are called adaptive algorithms.  And algorithms which do not adapt to this situation are not adaptive.</p>
<h5>Internal & External Sorting</h5>
<p>If the data sorting process takes place entirely within the Random-Access Memory (RAM) of a computer, it’s called internal sorting. This is possible whenever the size of the dataset to be sorted is small enough to be held in RAM.</p>
<ul>
	<li>Bubble Sort</li>
	<li>Insertion Sort</li>
	<li>Quick Sort Sort</li>
</ul>
<p>For sorting larger datasets, it may be necessary to hold only a smaller chunk of data in memory at a time, since it won’t all fit in the RAM. The rest of the data is normally held on some larger, but slower medium, like a hard disk. The sorting of these large datasets will require different sets of algorithms which are called external sorting</p>
<ul>
	<li>Merge sort</li>
</ul>
<hr>
<h5>Resources</h5>
<a href="https://www.codewithharry.com/videos/data-structures-and-algorithms-in-hindi-48/">CodeWithHarry</a>
<a href="https://medium.com/@vaidehijoshi">medium</a>
<a href="https://www.freecodecamp.org/">freecodecamp</a>
