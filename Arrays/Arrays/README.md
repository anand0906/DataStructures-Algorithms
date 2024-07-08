<h1>Arrays</h1>
<p>Array is a linear data structure that stores a collection of items of same data type in contiguous memory locations.</p>
<p><strong>Types of array</strong></p>
<p>Arrays can be classified in two ways:</p>
<ul>
	<li>On the basis of Memory Allocation</li>
	<li>On the basis of Dimensions</li>
</ul>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240408164951/Types-of-Arrays.webp">
<p>Basically there are two types of arrays based on memory allocation</p>
<h3>Static Arrays</h3>
<p>Static arrays are arrays with a fixed size determined at compile-time. The memory allocation for static arrays is done when the program is compiled, and this size cannot be altered during runtime.</p>
<p><strong>Characteristics of Static Arrays</strong></p>
<ul>
	<li><strong>Fixed Size</strong>: The size of the array is specified at compile-time and cannot be changed.</li>
	<li><strong>Compile-Time Memory Allocation</strong>: Memory is allocated during the compilation of the program.</li>
	<li><strong>Efficient Access </strong>: Accessing elements is efficient due to contiguous memory allocation.</li>
	<li><strong>Potential Memory Waste </strong>: If the array size is overestimated, it can lead to memory wastage. If underestimated, it can lead to insufficient memory.</li>
</ul>

<p><strong>Example of Static Array in C</strong></p>
<p>In C, static arrays are commonly used due to their simplicity and efficiency</p>

```c
#include <stdio.h>

int main() {
    int numbers[5] = {10, 20, 30, 40, 50};  // Fixed size array

    // Accessing elements
    printf("First element: %d\n", numbers[0]);  // Output: 10
    printf("Last element: %d\n", numbers[4]);   // Output: 50

    // Trying to access out of bounds will cause undefined behavior
    // printf("%d\n", numbers[5]);  // Not allowed, will cause runtime error

    return 0;
}

```


<ul>
	<li>The array numbers has a fixed size of 5.</li>
	<li>Elements are accessed using their index.</li>
	<li>Attempting to access an index outside the declared size results in undefined behavior.</li>
</ul>

<p><strong>Advantages</strong></p>
<ol>
	<li><strong>Simplicity</strong>: Easy to declare and use.</li>
	<li><strong>Predictability</strong>: Fixed size makes memory management predictable.</li>
	<li><strong>Performance</strong>: Fast access due to contiguous memory allocation.</li>
</ol>
<p><strong>Disadvantages</strong></p>
<ol>
	<li><strong>Fixed Size</strong>: Inflexible size can lead to memory waste or insufficient storage.</li>
	<li><strong>Memory Inefficiency</strong>: Overestimating the size results in unused memory allocation.</li>
	<li><strong>Memory Inefficiency</strong>: Overestimating the size results in unused memory allocation.</li>
</ol>
<p><strong>When to Use Static Arrays</strong></p>
<ul>
	<li><strong>Fixed Data Size</strong>: The number of elements is known and constant.</li>
	<li><strong>Performance-Critical Applications</strong>: Where predictable memory access patterns and speed are crucial.</li>
	<li><strong>Memory-Constrained Environments</strong>: Where dynamic memory allocation overhead is undesirable.</li>
</ul>

<h3>Dynamic Arrays</h3>
<p>Dynamic arrays, unlike static arrays, allow for flexible memory allocation at runtime. This means the size of the array can change as elements are added or removed, providing more flexibility and efficient use of memory.</p>

<h4>Characteristics of Dynamic Arrays</h4>
<ul>
    <li><strong>Variable Size</strong>: The size of the array can be adjusted at runtime.</li>
    <li><strong>Run-Time Memory Allocation</strong>: Memory is allocated as needed during program execution.</li>
    <li><strong>Efficient Memory Use</strong>: Allocates only as much memory as required, reducing wastage.</li>
    <li><strong>Automatic Resizing</strong>: Many dynamic array implementations automatically resize when they run out of space.</li>
</ul>

<h4>Dynamic Arrays in Python</h4>
<p>Python's built-in list is an example of a dynamic array. Lists in Python can grow and shrink in size as needed.</p>
    
```python
# Example in Python

# Initializing an empty list (dynamic array)
dynamic_array = []

# Adding elements to the list
dynamic_array.append(10)
dynamic_array.append(20)
dynamic_array.append(30)

print(dynamic_array)  # Output: [10, 20, 30]

# Accessing elements
print(dynamic_array[0])  # Output: 10
print(dynamic_array[2])  # Output: 30

# Removing an element
dynamic_array.pop()  # Removes the last element
print(dynamic_array)  # Output: [10, 20]

# Inserting an element at a specific position
dynamic_array.insert(1, 15)
print(dynamic_array)  # Output: [10, 15, 20]

# Extending the list with another list
dynamic_array.extend([25, 30, 35])
print(dynamic_array)  # Output: [10, 15, 20, 25, 30, 35]
```

<h4>Advantages of Dynamic Arrays</h4>
<ul>
    <li><strong>Flexible Size</strong>: Can grow or shrink as needed.</li>
    <li><strong>Efficient Memory Use</strong>: Allocates memory as required, minimizing waste.</li>
    <li><strong>Convenient Operations</strong>: Supports various operations like adding, removing, and inserting elements.</li>
</ul>

<h4>Disadvantages of Dynamic Arrays</h4>
<ul>
    <li><strong>Overhead for Resizing</strong>: Resizing operations can be costly in terms of time.</li>
    <li><strong>Fragmentation</strong>: Frequent resizing can lead to memory fragmentation.</li>
    <li><strong>Potential Performance Hit</strong>: Continuous reallocation and copying of elements can affect performance.</li>
</ul>

<h4>When to Use Dynamic Arrays</h4>
<p>Dynamic arrays are suitable when:</p>
<ul>
    <li><strong>Variable Data Size</strong>: The number of elements can change during program execution.</li>
    <li><strong>Ease of Use</strong>: Built-in support for common operations makes them convenient.</li>
    <li><strong>Efficient Memory Management</strong>: When efficient memory use is critical.</li>
</ul>


<h3>Types of Arrays on the Basis of Dimensions</h3>
    
<h4>1. One-Dimensional Arrays</h4>
<p>A one-dimensional array is a simple list of elements, each identified by a unique index.</p>
    
```python
# Example in Python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])  # Output: 10
print(numbers[4])  # Output: 50
```
    
<h4>2. Two-Dimensional Arrays</h4>
<p>A two-dimensional array, often referred to as a matrix, is an array of arrays. It can be visualized as a table with rows and columns.</p>
    
```python
# Example in Python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])  # Output: 1
print(matrix[1][2])  # Output: 6
```
    
<h4>3. Multi-Dimensional Arrays</h4>
<p>Arrays with more than two dimensions, like three-dimensional arrays and higher, are used for more complex data representations.</p>
    
```python
# Example in Python
tensor = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]
print(tensor[0][0][0])  # Output: 1
print(tensor[1][1][2])  # Output: 12
```

<h4>Practical Use Cases</h4>
<p>Arrays are used in various applications, such as:</p>
<ul>
    <li><strong>Storing Collections of Data</strong>: Lists of numbers, strings, or objects.</li>
    <li><strong>Matrix Operations</strong>: Scientific computing and graphics for representing grids, images, etc.</li>
    <li><strong>Buffer Storage</strong>: In I/O operations, arrays serve as buffers to store temporary data.</li>
</ul>


<h3>How Python List Increases Its Size Dynamically</h3>
<p>Python lists are dynamic arrays that can grow or shrink in size as needed. This dynamic resizing is handled automatically by Python's underlying list implementation. The process involves allocating a larger block of memory when the current block is full, copying the existing elements to the new block, and freeing the old block.</p>

<h4>Dynamic Resizing Mechanism</h4>
<p>When a list needs to grow beyond its current capacity, Python typically allocates a larger block of memory. The new size is usually more than the current size to accommodate future growth and minimize the frequency of resizing operations. This extra space allocation strategy is known as "over-allocation".</p>

<h4>Example of Dynamic Resizing</h4>
<p>Let's look at an example to understand how a Python list increases its size dynamically.</p>
    
```python
# Example in Python

import sys

# Initialize an empty list
dynamic_list = []

# Function to display size and capacity details
def display_list_info(lst):
    print(f"Length: {len(lst)}, Capacity: {sys.getsizeof(lst)}")

# Initial state
display_list_info(dynamic_list)  # Length: 0, Capacity: 56 (may vary)

# Add elements to the list and observe the changes
for i in range(20):
    dynamic_list.append(i)
    display_list_info(dynamic_list)
```

<p>In this example, as we append elements to the list, we can observe the changes in its length and capacity (size in bytes). The `sys.getsizeof()` function gives us the memory size of the list in bytes, which reflects the capacity changes.</p>

<h4>Explanation of Capacity Changes</h4>
<p>Initially, the list has a small capacity. As elements are appended, the capacity increases in a non-linear fashion. Python's list implementation over-allocates memory to minimize the number of resizing operations. Typically, the list's capacity grows by about 1.5 times its current size when more space is needed.</p>

<h4>Advantages of Dynamic Resizing</h4>
<ul>
    <li><strong>Flexible Size</strong>: Lists can grow or shrink as needed without the programmer having to manage memory manually.</li>
    <li><strong>Efficient Appends</strong>: The over-allocation strategy ensures that appending elements is generally efficient, with occasional resizing operations.</li>
</ul>

<h4>Disadvantages of Dynamic Resizing</h4>
<ul>
    <li><strong>Memory Overhead</strong>: Over-allocation can lead to memory overhead, as the list may occupy more memory than needed.</li>
    <li><strong>Resizing Cost</strong>: Resizing operations can be costly in terms of time, as they involve copying all elements to a new memory block.</li>
</ul>

<h4>Practical Use Cases</h4>
<p>Dynamic resizing of lists is particularly useful in scenarios where the number of elements is not known in advance, such as:</p>
<ul>
    <li>Reading data from a file or user input.</li>
    <li>Storing results of computations where the output size is dynamic.</li>
    <li>Implementing dynamic data structures like stacks, queues, and dynamic arrays.</li>
</ul>