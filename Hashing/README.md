<h1>Hashing</h1>
<p><strong>Operations in Different Data Structures</strong></p>

<p><strong>Arrays</strong></p>
<ul>
    <li><strong>Search:</strong> In an unsorted array, searching requires checking each element one by one (linear search), giving a time complexity of <strong>O(n)</strong>. In a sorted array, we can use binary search, which is faster with a time complexity of <strong>O(log n)</strong>.</li>
    <li><strong>Insert:</strong> Inserting into an unsorted array takes <strong>O(1)</strong> if we add the element at the end. However, inserting into a sorted array requires shifting elements to maintain order, making it <strong>O(n)</strong>.</li>
    <li><strong>Delete:</strong> Deleting in an unsorted array involves finding the element first (which takes <strong>O(n)</strong>) and then removing it (which also involves shifting elements), making it <strong>O(n)</strong>. In a sorted array, the process is similar.</li>
</ul>

<p><strong>Linked Lists</strong></p>
<ul>
    <li><strong>Search:</strong> Searching a specific element in a linked list requires traversing from the head to the desired node, resulting in <strong>O(n)</strong> time complexity.</li>
    <li><strong>Insert:</strong> Inserting at the beginning or end of a linked list takes <strong>O(1)</strong> time. Inserting at a specific position requires traversal, making it <strong>O(n)</strong>.</li>
    <li><strong>Delete:</strong> Deleting a node requires finding the node first (which is <strong>O(n)</strong>), followed by updating pointers. So overall, deletion is <strong>O(n)</strong>.</li>
</ul>

<p><strong>Trees (Balanced Binary Search Trees)</strong></p>
<ul>
    <li><strong>Search:</strong> Searching in a balanced binary search tree (like an AVL tree or Red-Black tree) is <strong>O(log n)</strong>, since the tree maintains order and allows binary search.</li>
    <li><strong>Insert:</strong> Inserting into a balanced binary search tree also takes <strong>O(log n)</strong>, as the tree may need to adjust its structure to stay balanced.</li>
    <li><strong>Delete:</strong> Deleting involves finding the node, replacing it, and then rebalancing the tree, all of which take <strong>O(log n)</strong>.</li>
</ul>
<p>So now we are looking for a data structure that can store the data and search in it in constant time, i.e. in O(1) time. This is how Hashing data structure came into play. With the introduction of the Hash data structure, it is now possible to easily store data in constant time and retrieve them in constant time as well</p>
<p><strong>Comparison Between Hashing and Other Data Structures</strong></p>
<ul>
    <li><strong>Array (Unsorted)</strong>: Search: <strong>O(n)</strong>, Insert: <strong>O(1)</strong>, Delete: <strong>O(n)</strong></li>
    <li><strong>Array (Sorted)</strong>: Search: <strong>O(log n)</strong>, Insert: <strong>O(n)</strong>, Delete: <strong>O(n)</strong></li>
    <li><strong>Linked List</strong>: Search: <strong>O(n)</strong>, Insert: <strong>O(1)</strong>, Delete: <strong>O(n)</strong></li>
    <li><strong>Balanced Tree</strong>: Search: <strong>O(log n)</strong>, Insert: <strong>O(log n)</strong>, Delete: <strong>O(log n)</strong></li>
    <li><strong>Hashing</strong>: Search: <strong>O(1)</strong>, Insert: <strong>O(1)</strong>, Delete: <strong>O(1)</strong></li>
</ul>

<h1>Applications</h1>

<p><strong>1. Database Indexing:</strong></p>
<p>Imagine you have a huge library with thousands of books. Instead of checking every single shelf to find a specific book, the library uses a system where each book is assigned a unique code (like a barcode). This code helps the librarian quickly locate the exact shelf where the book is stored, saving a lot of time.</p>
<p><strong>Hashing:</strong> In databases, hashing is like that barcode system. It quickly points to where your data is stored, making retrieval much faster.</p>

<p><strong>2. Password Storage:</strong></p>
<p>When you create an account on a website, you set a password. The website doesn’t store your actual password because that would be risky. Instead, it uses a special formula (hash function) to convert your password into a random-looking string of characters (hash). Even if someone gets hold of the hashed password, they can't easily figure out your original password.</p>
<p><strong>Hashing:</strong> This ensures your password is stored securely, making it hard for hackers to steal and use it.</p>

<p><strong>3. Data Compression:</strong></p>
<p>Suppose you want to send a large photo to a friend but want to reduce its size to save on data. Compression algorithms use hashing to find patterns in the image and represent them more efficiently. This makes the file smaller without losing quality.</p>
<p><strong>Hashing:</strong> Helps reduce the size of data files for easier storage and transmission.</p>

<p><strong>4. Search Algorithms:</strong></p>
<p>Imagine you're at a crowded concert and need to find your friend. Instead of searching randomly, you have a map with coordinates telling you exactly where they are. Hash tables work similarly in computers; they quickly find the exact location of the data you’re looking for.</p>
<p><strong>Hashing:</strong> Used in search algorithms to find data quickly without going through everything.</p>

<p><strong>5. Cryptography:</strong></p>
<p>When you send a confidential message, you want to make sure only the intended person can read it. Hashing is used to create a unique digital signature or code that confirms the message hasn’t been tampered with.</p>
<p><strong>Hashing:</strong> Ensures the security and authenticity of information in communications.</p>

<p><strong>6. Load Balancing:</strong></p>
<p>If you’re ordering food online and many people are placing orders at the same time, the system might assign orders to different chefs to manage the load. Hashing helps distribute the work evenly among the chefs so no one gets overwhelmed.</p>
<p><strong>Hashing:</strong> In IT systems, it distributes user requests across multiple servers to prevent any one server from getting overloaded.</p>

<p><strong>7. Blockchain:</strong></p>
<p>Think of a blockchain as a digital ledger that records every transaction. Hashing ensures that once a transaction is recorded, it can’t be changed without everyone knowing. It’s like sealing a document with a unique stamp that shows if someone has tampered with it.</p>
<p><strong>Hashing:</strong> Protects the integrity of data in blockchain technology, like in cryptocurrencies.</p>

<p><strong>8. Image Processing:</strong></p>
<p>Let’s say you want to check if someone uploaded the same photo twice on a social media platform. Hashing can generate a unique code for each image, making it easy to spot duplicates, even if the images look slightly different.</p>
<p><strong>Hashing:</strong> Helps identify and prevent duplicate or altered images from being stored or shared.</p>

<p><strong>9. File Comparison:</strong></p>
<p>If you download a file from the internet, you might want to ensure it wasn’t corrupted during the download. Hashing can be used to generate a code before and after the download to check if the file is exactly the same.</p>
<p><strong>Hashing:</strong> Verifies the integrity of files by comparing hash values.</p>

<p><strong>10. Fraud Detection:</strong></p>
<p>Banks monitor transactions for unusual patterns. Hashing can quickly process and analyze this data to detect if someone is trying to commit fraud, like using a stolen credit card.</p>
<p><strong>Hashing:</strong> Helps in identifying and preventing fraudulent activities by analyzing large amounts of data quickly.</p>

<p><strong>Advantages of Hashing:</strong></p>
<ul>
    <li><strong>Efficiency:</strong> Like using a barcode to quickly find a book in a library.</li>
    <li><strong>Security:</strong> Like turning a password into a secret code that’s hard to crack.</li>
    <li><strong>Speed:</strong> Like instantly knowing where something is without searching everywhere.</li>
</ul>


<h1>Direct Access Table</h1>
<p>A Direct Access Table (DAT), also known as a Direct Address Table</p>
<p>It is a data structure that allows direct access to elements based on their keys. It's particularly useful when the universe of possible keys is reasonably small and known in advance.</p>
<p>In a Direct Access Table, an array is used where the index corresponds to the key, allowing operations like insertion, deletion, and lookup to be performed in constant time O(1).</p>
<p><strong>How it Works</strong></p>
<ul>
    <li><strong>Array Representation : </strong> A Direct Access Table is represented by an array where each position corresponds to a key in the universe. The key serves as the index in the array.</li>
    <li><strong>Key-Value Storage : </strong>Each key directly points to a specific location in the array where the value associated with that key is stored.</li>
    <li><strong>Operations</strong></li>
    <ul>
        <li><strong>Insertion</strong> : Place the value at the array index corresponding to the key.</li>
        <li><strong>Deletion</strong> : Remove the value by setting the array index to null (or some sentinel value).</li>
        <li><strong>Lookup</strong> : Access the value by directly using the key as the index.</li>
    </ul>
</ul>

<p><strong>Example :</strong></p>
<p>Suppose you will be given random numbers between 1-100 as input, we need to create a data structure that should be capable of permforming operations of insertion , deleting and searching in o(1) time complexity</p>
<p>We can develop hash table for such kind of scenarios</p>
<p><strong>Step 1: Create the Direct Access Table</strong></p>
<p>Since the numbers range from 1 to 100, you can create an array of size 101 (index 0 to 100) to represent the Direct Access Table. The index of the array will correspond directly to the numbers you are storing.</p>
<p><strong>Step 2: Initialize the Table</strong></p>
<p>Let's initialize the table with a value indicating that no number is stored at any position, for instance, using False (or 0).</p>

```python
# Initialize a direct access table with size 101
direct_access_table = [False] * 101
```

<p>This array can now be used to track the presence of any number between 1 and 100.</p>

<p><strong>Step 3: Insert Operation</strong></p>
<p>To insert a number into the table, simply set the value at the index corresponding to the number to True (or 1).</p>

```python
def insert(number):
    direct_access_table[number] = True
```

<p>Now, the number 42 is stored in the table.</p>

<p><strong>Step 4: Search Operation</strong></p>
<p>To search for a number, check the value at the index corresponding to that number. If the value is True, the number is present; otherwise, it's absent.</p>
<p>For example, to check if 42 is in the table:</p>

```python
def search(number):
    return direct_access_table[number]
```

<p><strong>Step 5: Delete Operation</strong></p>
<p>To delete a number, set the value at the index corresponding to the number back to False (or 0).</p>
<p>For example, to delete the number 42:</p>

```python
def delete(number):
    direct_access_table[number] = False
```

<p><strong>Example in Action</strong></p>
<p>Here’s how the process works for inserting, searching, and deleting numbers:</p>

```python
# Initialize the direct access table
direct_access_table = [False] * 101

# Insert some numbers
insert(42)
insert(75)
insert(10)

# Search for a number
print(search(42))  # Output: True (42 is present)
print(search(50))  # Output: False (50 is not present)

# Delete a number
delete(42)

# Search again after deletion
print(search(42))  # Output: False (42 has been deleted)
```

<ul>
    <li><strong>Insertion</strong>: Inserting a number like 42 simply involves setting direct_access_table[42] = True.</li>
    <li><strong>Search</strong>: To search if 42 exists, check the value at direct_access_table[42].</li>
    <li><strong>Deletion</strong>: Deleting 42 involves setting direct_access_table[42] = False.</li>
</ul>

<p>All operations—search, insert, and delete—are performed in constant time O(1). This makes the Direct Access Table an efficient choice when you have a small, known range of possible keys.</p>

<p><strong>Disadvantages</strong></p>
<ul>
    <li>Not possible for float and string value to map as indexes in an array</li>
    <li>There will be memory wastage due to unused indexes</li>
</ul>


<h1>Hashing</h1>
<p>To address, all above limitations and to develop data structure whose insertion,deletion and searching complexity is O(1), we can use hashing technique</p>

<p>While Direct Access Tables (DATs) offer efficient O(1) time complexity for insertion, deletion, and lookup operations, they come with significant limitations:</p>
<ol>
    <li><strong>Large Key Space:</strong></li>
    <ul>
        <li><strong>Memory Usage:</strong>DATs require an array with a size equal to the entire universe of possible keys. If the key space is large (e.g., all possible 32-bit integers), the required memory becomes impractical.</li>
        <li><strong>Wasted Space:</strong>If the actual set of keys used is sparse within the large key space, most of the array will be empty, leading to inefficient memory usage.</li>
    </ul>
    <li><strong>Fixed Key Range</strong></li>
    <ul>
        <li><strong>Limited Flexibility:</strong>DATs are effective only when the range of possible keys is fixed and known in advance. They are not suitable for dynamic or unknown key ranges.</li>
    </ul>
    <li><strong>Inefficiency for Complex Keys</strong></li>
    <ul>
        <li><strong>Non-Integer Keys:</strong>DATs work best with simple integer keys. When dealing with complex keys (e.g., strings or objects), converting these keys to array indices becomes challenging without using a hash function, negating the simplicity of DATs.</li>
    </ul>
</ol>

<p>In Hashing, key can be any data type, we will use a hash function that converts the given key into a small index value, so that we can store that given key into array which is called as hash table</p>
<img src="https://www.geeksforgeeks.org/wp-content/uploads/HashingDataStructure-min.png">
<p>Let a hash function H(x) maps the value x at the index x%10 in an Array. For example if the list of values is [11,12,13,14,15] it will be stored at positions {1,2,3,4,5} in the array or Hash table respectively.</p>
<p>There are many hash functions that use numeric or alphanumeric keys.</p>

<p><strong>Components Of Hashing</strong></p>
<p>There are majorly three components of hashing:</p>
<ul>
    <li><strong>Key:</strong>A Key can be anything string or integer which is fed as input in the hash function the technique that determines an index or location for storage of an item in a data structure.</li>
    <li><strong>Hash Function:</strong>The hash function receives the input key and returns the index of an element in an array called a hash table. The index is known as the hash index.</li>
    <li><strong>Hash Table:</strong>Hash table is a data structure that maps keys to values using a special function called a hash function. Hash stores the data in an associative manner in an array where each data value has its own unique index.</li>
</ul>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220701080941/ComponentsofHashing-660x342.png">

<p><strong>Hash Functions: An In-Depth Look</strong></p>

<p>Hash functions play a crucial role in efficiently storing and retrieving data. Below are four common methods used to generate hash values: Division Method, Mid Square Method, Folding Method, and Multiplication Method. Each has its own approach to creating a hash value from a given key.</p>

<p><strong>1. Division Method</strong></p>
<p><strong>Overview:</strong> The Division Method is the simplest way to create a hash value. It involves dividing the key by the size of the hash table (denoted as M) and using the remainder as the hash value.</p>
<p><strong>Formula:</strong> h(K) = k mod M</p>
<ul>
  <li><strong>k:</strong> The key value.</li>
  <li><strong>M:</strong> The size of the hash table, ideally a prime number to ensure uniform distribution.</li>
</ul>
<p><strong>Example:</strong></p>
<ul>
  <li><strong>Given:</strong> k = 12345, M = 95</li>
  <li><strong>Calculation:</strong> h(12345) = 12345 mod 95 = 90</li>
</ul>
<p><strong>Pros:</strong></p>
<ul>
  <li>Simple and fast since it only requires one division operation.</li>
  <li>Works reasonably well for any value of M.</li>
</ul>
<p><strong>Cons:</strong></p>
<ul>
  <li>Can lead to poor performance if consecutive keys map to consecutive hash values.</li>
  <li>Extra care is needed in choosing M to avoid clustering.</li>
</ul>

<p><strong>2. Mid Square Method</strong></p>
<p><strong>Overview:</strong> The Mid Square Method involves squaring the key value and then extracting the middle digits of the result to form the hash value.</p>
<p><strong>Steps:</strong></p>
<ol>
  <li>Square the key (k × k).</li>
  <li>Extract the middle r digits.</li>
</ol>
<p><strong>Formula:</strong> h(K) = middle digits of (k × k)</p>
<ul>
  <li><strong>k:</strong> The key value.</li>
  <li><strong>r:</strong> Number of middle digits, determined by the size of the hash table.</li>
</ul>
<p><strong>Example:</strong></p>
<ul>
  <li><strong>Given:</strong> k = 60, Hash table size = 100 (requiring 2 digits)</li>
  <li><strong>Calculation:</strong> k × k = 60 × 60 = 3600, h(60) = middle 2 digits of 3600 = 60</li>
</ul>
<p><strong>Pros:</strong></p>
<ul>
  <li>Utilizes all digits of the key value, providing a more balanced distribution.</li>
  <li>Less affected by the distribution of digits in the original key.</li>
</ul>
<p><strong>Cons:</strong></p>
<ul>
  <li>Large keys can result in very large squares, complicating the process.</li>
  <li>Collisions can still occur, though they may be less frequent.</li>
</ul>

<p><strong>3. Digit Folding Method</strong></p>
<p><strong>Overview:</strong> The Digit Folding Method breaks the key into smaller parts, adds them together, and uses the sum as the hash value.</p>
<p><strong>Steps:</strong></p>
<ol>
  <li>Divide the key into parts (k1, k2, …, kn).</li>
  <li>Add the parts together.</li>
</ol>
<p><strong>Formula:</strong> h(K) = k1 + k2 + … + kn</p>
<ul>
  <li><strong>k:</strong> The key value divided into parts.</li>
</ul>
<p><strong>Example:</strong></p>
<ul>
  <li><strong>Given:</strong> k = 12345, Divide k into k1 = 12, k2 = 34, k3 = 5</li>
  <li><strong>Calculation:</strong> h(12345) = 12 + 34 + 5 = 51</li>
</ul>
<p><strong>Pros:</strong></p>
<ul>
  <li>Simple to implement and works well with different key lengths.</li>
</ul>
<p><strong>Cons:</strong></p>
<ul>
  <li>The sum may still lead to collisions.</li>
  <li>The division of the key into parts must be carefully managed to avoid losing information.</li>
</ul>

<p><strong>4. Multiplication Method</strong></p>
<p><strong>Overview:</strong> The Multiplication Method involves multiplying the key by a constant fractional value, extracting the fractional part, and then scaling it by the size of the hash table.</p>
<p><strong>Steps:</strong></p>
<ol>
  <li>Multiply the key by a constant A (where 0 < A < 1).</li>
  <li>Extract the fractional part of k × A.</li>
  <li>Multiply by the size of the hash table.</li>
  <li>Take the floor of the result.</li>
</ol>
<p><strong>Formula:</strong> h(K) = floor(M × (k × A mod 1))</p>
<ul>
  <li><strong>k:</strong> The key value.</li>
  <li><strong>M:</strong> The size of the hash table.</li>
  <li><strong>A:</strong> A constant value between 0 and 1.</li>
</ul>
<p><strong>Example:</strong></p>
<ul>
  <li><strong>Given:</strong> k = 12345, A = 0.357840, M = 100</li>
  <li><strong>Calculation:</strong> k × A = 12345 × 0.357840 = 4417.5348, h(12345) = floor(100 × 0.5348) = floor(53.48) = 53</li>
</ul>
<p><strong>Pros:</strong></p>
<ul>
  <li>Provides a good distribution of hash values even with non-prime table sizes.</li>
  <li>Less prone to clustering compared to the Division Method.</li>
</ul>
<p><strong>Cons:</strong></p>
<ul>
  <li>The choice of A can affect the distribution; it must be chosen carefully.</li>
  <li>Slightly more complex to compute due to the need for multiplication and fractional extraction.</li>
</ul>

<p><strong>Conclusion</strong></p>
<p>Each hash function has its strengths and weaknesses, making them suitable for different scenarios. The Division Method is simple but can lead to clustering. The Mid Square Method offers better distribution but can be complex with large keys. The Digit Folding Method is straightforward but might still result in collisions. The Multiplication Method is effective for non-prime table sizes but requires careful selection of constants. Choosing the right method depends on the specific requirements of the application and the nature of the data being hashed.</p>

<p><strong>Hashing of Strings</strong></p>

<p>Hashing strings involves converting a string (a sequence of characters) into a fixed-size integer value, which can be used as an index in a hash table. This process is essential in many applications, such as quick data retrieval, checking for duplicates, and more.</p>

<p><strong>1. Basic Idea</strong></p>
<p>When you hash a string, you aim to generate a unique or semi-unique integer (hash value) for each distinct string. This integer value is derived from the characters in the string and their positions. The main challenge is to ensure that different strings produce different hash values while minimizing collisions (where two different strings produce the same hash value).</p>

<p><strong>2. Common Methods for String Hashing</strong></p>

<p><strong>1. Simple Hashing (Summing Character Codes)</strong></p>
<ul>
  <li><strong>Overview:</strong> The simplest method of hashing a string is to sum the ASCII (or Unicode) values of its characters.</li>
  <li><strong>Formula:</strong> h(S) = sum(ASCII value of each character in S)</li>
  <li><strong>Example:</strong> For the string "abc":
    <ul>
      <li>h("abc") = ASCII('a') + ASCII('b') + ASCII('c') = 97 + 98 + 99 = 294</li>
    </ul>
  </li>
  <li><strong>Pros:</strong> Simple to implement.</li>
  <li><strong>Cons:</strong> Poor distribution, as different strings can easily end up with the same sum.</li>
</ul>

<p><strong>2. Polynomial Hashing</strong></p>
<ul>
  <li><strong>Overview:</strong> This method treats the string as a polynomial, with each character representing a coefficient. A base value <em>p</em> is chosen, and the string is interpreted as a polynomial.</li>
  <li><strong>Formula:</strong> h(S) = (ASCII(S[0]) * p^(n-1)) + (ASCII(S[1]) * p^(n-2)) + ... + ASCII(S[n-1])</li>
  <li><strong>Example:</strong> For the string "abc" with p = 31:
    <ul>
      <li>h("abc") = 97 × 31^2 + 98 × 31^1 + 99 × 31^0 = 97 × 961 + 98 × 31 + 99 = 93614 + 3038 + 99 = 96751</li>
    </ul>
  </li>
  <li><strong>Pros:</strong> Provides a much better distribution of hash values.</li>
  <li><strong>Cons:</strong> Can be computationally intensive due to the power calculations.</li>
</ul>

<p><strong>3. DJB2 Hash Function</strong></p>
<ul>
  <li><strong>Overview:</strong> This is a popular and efficient hash function created by Daniel J. Bernstein. It uses bitwise operations and a prime number multiplier to mix the input string into a hash value.</li>
  <li><strong>Formula:</strong> 
    <ul>
      <li>h(S) = 5381</li>
      <li>h(S) = ((h(S) << 5) + h(S)) + ASCII(S[i])</li>
    </ul>
  </li>
  <li><strong>Example:</strong> For the string "abc":
    <ul>
      <li>Start with h = 5381</li>
      <li>For 'a': h = ((5381 << 5) + 5381) + 97 = 177670</li>
      <li>For 'b': h = ((177670 << 5) + 177670) + 98 = 5863208</li>
      <li>For 'c': h = ((5863208 << 5) + 5863208) + 99 = 193485963</li>
    </ul>
  </li>
  <li><strong>Pros:</strong> Efficient and widely used in many hash-based structures like hash tables.</li>
  <li><strong>Cons:</strong> While it's generally good, DJB2 is not cryptographically secure.</li>
</ul>


<h1>Hashing Collision</h1>
<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20220706102035/Collision-in-Hashing.png">
<p>A <strong>hash collision</strong> happens when two different inputs (keys) produce the same hash output. Since a hash function maps data of arbitrary size to fixed-size values, multiple inputs can theoretically map to the same hash value. When this happens, it's called a collision.</p>

<p><strong>Example of a Hash Function</strong></p>

<p>Let's take a simple hash function:</p>

<pre><code>
def simple_hash(key):
    return len(key) % 10
</code></pre>

<p>Here, the hash function is based on the length of the input string, and the hash value is the remainder when the length is divided by 10.</p>

<p><strong>Example of a Hash Collision</strong></p>

<ol>
    <li><strong>Input:</strong> "cat"<br>
        Length: 3<br>
        Hash: 3 % 10 = 3
    </li>
    <li><strong>Input:</strong> "dog"<br>
        Length: 3<br>
        Hash: 3 % 10 = 3
    </li>
</ol>

<p>Even though "cat" and "dog" are different strings, they produce the same hash value <strong>3</strong>. This is a hash collision.</p>

<p><strong>Handling Hash Collisions</strong></p>

<p>Hash collisions are inevitable due to the finite range of hash values. Common techniques to handle them include:</p>

<ul>
    <li><strong>Chaining:</strong> Each hash table slot points to a list (or chain) of entries that have the same hash value. If a collision occurs, the new element is added to the linked list.</li>
    <ul>
        <li>Example: For both "cat" and "dog", the hash table slot with index 3 will have a list containing both values.</li>
    </ul>
    <li><strong>Open Addressing:</strong> If a collision happens, the algorithm looks for another open slot in the table to place the value.</li>
    <ul>
        <li>Example: If index 3 is already taken by "cat", the algorithm might try index 4 to store "dog".</li>
    </ul>
</ul>

<p><strong>Real-World Example</strong></p>

<p>Imagine a hash table for storing employee IDs:</p>

<ul>
    <li>Hash function: <code>hash(id) = id % 100</code></li>
    <li>Suppose employee IDs 10523 and 20623 both result in the same hash value (23). The system must handle this collision to ensure both IDs are stored correctly.</li>
</ul>

<p><strong>Conclusion</strong></p>

<p>Hash collisions are a common problem when working with hash functions. Understanding how to detect and resolve them is key to implementing efficient hash-based data structures.</p>


<h1>Open Chaining</h1>
<p><strong>Open Chaining in Hash Tables</strong></p>

<p><strong>Open Chaining</strong> is a technique used to handle hash collisions in hash tables. In this method, each index of the hash table holds a reference to a linked list (or any other dynamic data structure like a list or a tree). When multiple keys hash to the same index, they are stored in that list, one after another.</p>

<p><strong>How Open Chaining Works</strong></p>

<ol>
    <li><strong>Hash Function Calculation:</strong> A hash function is applied to the key, which gives an index.</li>
    <li><strong>Collision Handling:</strong> If the index is already occupied (a collision), the new key-value pair is added to the linked list at that index.</li>
    <li><strong>Search Operation:</strong> To find an element, the index is calculated first. Then the linked list at that index is traversed to find the desired key.</li>
    <li><strong>Deletion Operation:</strong> To delete an element, the key is found in the linked list at the hashed index and removed.</li>
</ol>

<p><strong>Example of Open Chaining</strong></p>

<p>Consider a hash table with the following simple hash function:</p>

<pre><code>
def hash_function(key):
    return key % 10
</code></pre>

<p>Let's insert the following keys into the hash table: <strong>15</strong>, <strong>25</strong>, <strong>35</strong>, and <strong>20</strong>.</p>

<ol>
    <li><strong>Hashing 15:</strong><br>
        15 % 10 = 5<br>
        The key 15 is stored at index 5.</li>
    <li><strong>Hashing 25:</strong><br>
        25 % 10 = 5<br>
        Collision occurs since index 5 is already occupied by 15. Using open chaining, 25 is added to the linked list at index 5.</li>
    <li><strong>Hashing 35:</strong><br>
        35 % 10 = 5<br>
        Another collision occurs at index 5. 35 is added to the linked list at the same index.</li>
    <li><strong>Hashing 20:</strong><br>
        20 % 10 = 0<br>
        The key 20 is stored at index 0.</li>
</ol>

<p>Now, the hash table looks like this:</p>

<table border="1">
    <tr>
        <th>Index</th>
        <th>Elements</th>
    </tr>
    <tr>
        <td>0</td>
        <td>20</td>
    </tr>
    <tr>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>2</td>
        <td></td>
    </tr>
    <tr>
        <td>3</td>
        <td></td>
    </tr>
    <tr>
        <td>4</td>
        <td></td>
    </tr>
    <tr>
        <td>5</td>
        <td>15 → 25 → 35</td>
    </tr>
    <tr>
        <td>6</td>
        <td></td>
    </tr>
    <tr>
        <td>7</td>
        <td></td>
    </tr>
    <tr>
        <td>8</td>
        <td></td>
    </tr>
    <tr>
        <td>9</td>
        <td></td>
    </tr>
</table>

<p>At index 5, the keys 15, 25, and 35 are stored in a linked list.</p>

<p><strong>Advantages of Open Chaining</strong></p>

<ul>
    <li><strong>Simple and Easy to Implement:</strong> Open chaining is conceptually straightforward.</li>
    <li><strong>Dynamic Growth:</strong> The linked lists can grow dynamically, so there is no limit on the number of collisions handled at a given index.</li>
</ul>

<p><strong>Disadvantages of Open Chaining</strong></p>

<ul>
    <li><strong>Increased Time Complexity:</strong> If many collisions occur, the linked list at a particular index can grow large, leading to slower search, insertion, and deletion operations.</li>
    <li><strong>Memory Overhead:</strong> Storing pointers for each element in the linked list requires additional memory.</li>
</ul>

<p><strong>When to Use Open Chaining</strong></p>

<p>Open chaining is useful when the load factor (ratio of the number of elements to the hash table size) is low or when the size of the hash table can be adjusted dynamically as more elements are inserted.</p>

<p><strong>Enhanced Explanation: Using Binary Search Trees and Python Lists in Open Chaining</strong></p>

<p>While open chaining typically uses linked lists to handle collisions, you can also implement more advanced data structures like binary search trees (BSTs), AVL trees, Red-Black trees, or even Python lists to improve performance.</p>

<p><strong>Using Binary Search Trees (BSTs) in Open Chaining</strong></p>

<p>Instead of storing colliding elements in a linked list, you can use a binary search tree. This provides better search, insertion, and deletion performance, especially when there are many collisions.</p>

<ol>
    <li><strong>AVL Trees:</strong> AVL trees are self-balancing binary search trees where the height difference between the left and right subtrees is maintained. This ensures that the tree remains balanced, providing <code>O(log n)</code> time complexity for search, insertion, and deletion operations.</li>
    <li><strong>Red-Black Trees:</strong> Red-Black trees are another type of self-balancing BST. Although slightly less balanced than AVL trees, they offer similar <code>O(log n)</code> performance while being easier to implement.</li>
</ol>

<p><strong>Advantages:</strong></p>
<ul>
    <li>Improved search performance compared to linked lists, especially for larger collision chains.</li>
    <li>Guarantees that the tree remains balanced, leading to more predictable performance.</li>
</ul>

<p><strong>Disadvantages:</strong></p>
<ul>
    <li>More complex to implement compared to simple linked lists.</li>
    <li>Increased memory overhead due to storing additional pointers and balancing information (like heights in AVL trees or color in Red-Black trees).</li>
</ul>

<p><strong>Using Python Lists for Open Chaining</strong></p>

<p>In Python, you can use a list (which is dynamic in size) to store elements at each index of the hash table:</p>

<pre><code>
hash_table = [[] for _ in range(10)]  # Create a hash table with 10 slots, each slot containing an empty list.

def insert(key):
    index = key % 10
    hash_table[index].append(key)
</code></pre>

<p>In this approach, each index holds a Python list that dynamically grows as new elements are added.</p>

<p><strong>Advantages:</strong></p>
<ul>
    <li>Simple and easy to implement in Python.</li>
    <li>Python lists offer <code>O(1)</code> average time complexity for appending elements.</li>
</ul>

<p><strong>Disadvantages:</strong></p>
<ul>
    <li>Search and deletion operations within the list are <code>O(n)</code> in the worst case.</li>
    <li>If there are many collisions, the list can grow large, leading to degraded performance.</li>
</ul>

<p><strong>Summary of the Alternatives</strong></p>

<table border="1">
    <tr>
        <th>Data Structure</th>
        <th>Time Complexity (Search, Insert, Delete)</th>
        <th>Memory Overhead</th>
        <th>Complexity of Implementation</th>
    </tr>
    <tr>
        <td>Linked List</td>
        <td>O(n)</td>
        <td>Low</td>
        <td>Simple</td>
    </tr>
    <tr>
        <td>AVL Tree</td>
        <td>O(log n)</td>
        <td>Moderate</td>
        <td>Complex</td>
    </tr>
    <tr>
        <td>Red-Black Tree</td>
        <td>O(log n)</td>
        <td>Moderate</td>
        <td>Complex</td>
    </tr>
    <tr>
        <td>Python List</td>
        <td>O(n) (worst case)</td>
        <td>Low</td>
        <td>Simple</td>
    </tr>
</table>

<p><strong>Conclusion</strong></p>

<p>While linked lists are a common choice for open chaining due to their simplicity, using more advanced structures like AVL or Red-Black trees can significantly improve performance in scenarios where there are many collisions. Python lists also offer a quick and simple alternative, though they may not be as efficient in highly congested hash tables.</p>

<p>By understanding these options, you can choose the right data structure for handling collisions in your specific use case.</p>


<h1>Python Implementation Of Open Chaining</h1>

```python
class MyHash:
    def __init__(self, b):
        self.BUCKET = b
        self.table = [[] for x in range(b)]

    def insert(self, x):
        i = x % self.BUCKET
        self.table[i].append(x)

    def remove(self, x):
        i = x % self.BUCKET
        if x in self.table[i]:
            self.table[i].remove(x)

    def search(self, x):
        i = x % self.BUCKET
        return x in self.table[i]


h = MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.remove(56)
print(h.search(56))
h.remove(56)
```


<h1>Open Addressing In Hashing</h1>

<h1>Open Addressing in Hashing</h1>

<p><strong>Open addressing</strong> is a collision resolution technique used in hash tables. Unlike chaining, where collisions are handled by maintaining a list of elements for each bucket, open addressing stores all elements within the hash table itself. When a collision occurs, the algorithm searches for the next available slot within the table using a probing sequence.</p>

<h2>Types of Probing in Open Addressing</h2>

<ul>
    <li><strong>Linear Probing:</strong>
        <p>In linear probing, if a collision occurs, the algorithm checks the next consecutive slot (by adding a fixed constant, usually 1) until an empty slot is found.</p>
        <p>Formula: <code>hash(key, i) = (hash(key) + i) % table_size</code></p>
        <p><strong>Disadvantage:</strong> Primary clustering (consecutive elements grouped together).</p>
    </li>
    <li><strong>Quadratic Probing:</strong>
        <p>Quadratic probing uses a quadratic function to find the next slot when a collision occurs.</p>
        <p>Formula: <code>hash(key, i) = (hash(key) + i²) % table_size</code></p>
        <p><strong>Disadvantage:</strong> Secondary clustering (groups of elements far apart may cluster).</p>
    </li>
    <li><strong>Double Hashing:</strong>
        <p>Double hashing uses a second hash function to determine the step size for probing.</p>
        <p>Formula: <code>hash(key, i) = (hash1(key) + i * hash2(key)) % table_size</code></p>
        <p><strong>Advantage:</strong> Reduces clustering problems compared to linear and quadratic probing.</p>
    </li>
</ul>

<h2>Example: Linear Probing</h2>

<p>Let’s insert the following keys into a hash table using linear probing:</p>
<p>Keys: <strong>50, 700, 76, 85, 92, 73, 101</strong></p>
<p>Assume the hash function is:</p>
<p><code>hash(key) = key % 10</code></p>

<table border="1">
    <thead>
        <tr>
            <th>Index</th>
            <th>0</th>
            <th>1</th>
            <th>2</th>
            <th>3</th>
            <th>4</th>
            <th>5</th>
            <th>6</th>
            <th>7</th>
            <th>8</th>
            <th>9</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Keys</td>
            <td>50</td>
            <td>700</td>
            <td>92</td>
            <td>73</td>
            <td>101</td>
            <td>85</td>
            <td>76</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

<h3>Step-by-step Insertion:</h3>
<ol>
    <li><strong>Insert 50:</strong> <br>
        <code>hash(50) = 50 % 10 = 0</code> <br>
        Slot 0 is empty, so place 50 at index 0.
    </li>
    <li><strong>Insert 700:</strong> <br>
        <code>hash(700) = 700 % 10 = 0</code> <br>
        Slot 0 is occupied by 50. Check the next slot (index 1). <br>
        Slot 1 is empty, so place 700 at index 1.
    </li>
    <li><strong>Insert 76:</strong> <br>
        <code>hash(76) = 76 % 10 = 6</code> <br>
        Slot 6 is empty, so place 76 at index 6.
    </li>
    <li><strong>Insert 85:</strong> <br>
        <code>hash(85) = 85 % 10 = 5</code> <br>
        Slot 5 is empty, so place 85 at index 5.
    </li>
    <li><strong>Insert 92:</strong> <br>
        <code>hash(92) = 92 % 10 = 2</code> <br>
        Slot 2 is empty, so place 92 at index 2.
    </li>
    <li><strong>Insert 73:</strong> <br>
        <code>hash(73) = 73 % 10 = 3</code> <br>
        Slot 3 is empty, so place 73 at index 3.
    </li>
    <li><strong>Insert 101:</strong> <br>
        <code>hash(101) = 101 % 10 = 1</code> <br>
        Slot 1 is occupied by 700. Check the next slot (index 2). <br>
        Slot 2 is occupied by 92. Check the next slot (index 3). <br>
        Slot 3 is occupied by 73. Check the next slot (index 4). <br>
        Slot 4 is empty, so place 101 at index 4.
    </li>
</ol>

<h2>Example: Quadratic Probing</h2>

<p>Let’s use the same keys and hash function but with quadratic probing.</p>
<p>Formula: <code>hash(key, i) = (key % 10 + i²) % 10</code></p>

<table border="1">
    <thead>
        <tr>
            <th>Index</th>
            <th>0</th>
            <th>1</th>
            <th>2</th>
            <th>3</th>
            <th>4</th>
            <th>5</th>
            <th>6</th>
            <th>7</th>
            <th>8</th>
            <th>9</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Keys</td>
            <td>50</td>
            <td>700</td>
            <td>92</td>
            <td>73</td>
            <td></td>
            <td>85</td>
            <td>76</td>
            <td>101</td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

<h3>Step-by-step Insertion:</h3>
<ol>
    <li><strong>Insert 50:</strong> <br>
        <code>hash(50, 0) = (50 % 10 + 0²) % 10 = 0</code> <br>
        Slot 0 is empty, so place 50 at index 0.
    </li>
    <li><strong>Insert 700:</strong> <br>
        <code>hash(700, 0) = (700 % 10 + 0²) % 10 = 0</code> <br>
        Slot 0 is occupied by 50. Try the next slot using <code>i = 1</code>. <br>
        <code>hash(700, 1) = (700 % 10 + 1²) % 10 = 1</code> <br>
        Slot 1 is empty, so place 700 at index 1.
    </li>
    <li><strong>Insert 76:</strong> <br>
        <code>hash(76, 0) = (76 % 10 + 0²) % 10 = 6</code> <br>
        Slot 6 is empty, so place 76 at index 6.
    </li>
    <li><strong>Insert 85:</strong> <br>
        <code>hash(85, 0) = (85 % 10 + 0²) % 10 = 5</code> <br>
        Slot 5 is empty, so place 85 at index 5.
    </li>
    <li><strong>Insert 92:</strong> <br>
        <code>hash(92, 0) = (92 % 10 + 0²) % 10 = 2</code> <br>
        Slot 2 is empty, so place 92 at index 2.
    </li>
    <li><strong>Insert 73:</strong> <br>
        <code>hash(73, 0) = (73 % 10 + 0²) % 10 = 3</code> <br>
        Slot 3 is empty, so place 73 at index 3.
    </li>
    <li><strong>Insert 101:</strong> <br>
        <code>hash(101, 0) = (101 % 10 + 0²) % 10 = 1</code> <br>
        Slot 1 is occupied by 700. Try the next slot using <code>i = 1</code>. <br>
        <code>hash(101, 1) = (101 % 10 + 1²) % 10 = 2</code> <br>
        Slot 2 is occupied by 92. Try the next slot using <code>i = 2</code>. <br>
        <code>hash(101, 2) = (101 % 10 + 2²) % 10 = 5</code> <br>
        Slot 5 is occupied by 85. Try the next slot using <code>i = 3</code>. <br>
        <code>hash(101, 3) = (101 % 10 + 3²) % 10 = 0</code> <br>
        Slot 0 is occupied by 50. Try the next slot using <code>i = 4</code>. <br>
        <code>hash(101, 4) = (101 % 10 + 4²) % 10 = 7</code> <br>
        Slot 7 is empty, so place 101 at index 7.
    </li>
</ol>

<h2>Advantages and Disadvantages</h2>
<ul>
    <li><strong>Advantages:</strong>
        <ul>
            <li>No extra memory is required for linked lists as in chaining.</li>
            <li>Simpler in implementation compared to some other methods.</li>
        </ul>
    </li>
    <li><strong>Disadvantages:</strong>
        <ul>
            <li>Open addressing suffers from clustering problems.</li>
            <li>Performance degrades as the table becomes fuller.</li>
            <li>Requires a good probing sequence to avoid clustering.</li>
        </ul>
    </li>
</ul>


```python
class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self._hash(key)
        i = 0
        while self.table[(index + i) % self.size] is not None:
            i += 1
        self.table[(index + i) % self.size] = key

    def search(self, key):
        index = self._hash(key)
        i = 0
        while self.table[(index + i) % self.size] is not None:
            if self.table[(index + i) % self.size] == key:
                return True
            i += 1
        return False

    def __str__(self):
        return str(self.table)


class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self._hash(key)
        i = 0
        while self.table[(index + i * i) % self.size] is not None:
            i += 1
        self.table[(index + i * i) % self.size] = key

    def search(self, key):
        index = self._hash(key)
        i = 0
        while self.table[(index + i * i) % self.size] is not None:
            if self.table[(index + i * i) % self.size] == key:
                return True
            i += 1
        return False

    def __str__(self):
        return str(self.table)


class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash1(self, key):
        return key % self.size

    def _hash2(self, key):
        return 1 + (key % (self.size - 1))

    def insert(self, key):
        index = self._hash1(key)
        step_size = self._hash2(key)
        i = 0
        while self.table[(index + i * step_size) % self.size] is not None:
            i += 1
        self.table[(index + i * step_size) % self.size] = key

    def search(self, key):
        index = self._hash1(key)
        step_size = self._hash2(key)
        i = 0
        while self.table[(index + i * step_size) % self.size] is not None:
            if self.table[(index + i * step_size) % self.size] == key:
                return True
            i += 1
        return False

    def __str__(self):
        return str(self.table)


# Example usage
if __name__ == "__main__":
    keys = [50, 700, 76, 85, 92, 73, 101]

    # Linear Probing
    print("Linear Probing Hash Table:")
    lp_table = LinearProbingHashTable(size=10)
    for key in keys:
        lp_table.insert(key)
    print(lp_table)

    # Quadratic Probing
    print("\nQuadratic Probing Hash Table:")
    qp_table = QuadraticProbingHashTable(size=10)
    for key in keys:
        qp_table.insert(key)
    print(qp_table)

    # Double Hashing
    print("\nDouble Hashing Hash Table:")
    dh_table = DoubleHashingHashTable(size=10)
    for key in keys:
        dh_table.insert(key)
    print(dh_table)
```


<h1>Double Hashing</h1>
<p><strong>Double Hashing</strong></p>
<p>Double hashing is an open addressing collision resolution technique used in hash tables. It improves on linear and quadratic probing by using a second hash function to calculate the probing interval, which helps to reduce clustering and spread out the keys more uniformly.</p>

<p><strong>How Double Hashing Works</strong></p>
<p>In double hashing, when a collision occurs (i.e., when the desired slot is already occupied), a second hash function is used to determine the step size for probing. This means that instead of simply checking the next slot (as in linear probing) or following a quadratic sequence (as in quadratic probing), double hashing uses a more complex approach to find the next slot.</p>

<p><strong>Formula</strong></p>
<p>Double hashing uses two hash functions:</p>
<ul>
    <li><strong>Primary Hash Function:</strong> <code>hash1(key)</code> determines the initial index for the key.</li>
    <li><strong>Secondary Hash Function:</strong> <code>hash2(key)</code> determines the interval between probes.</li>
</ul>
<p>The formula for double hashing is:</p>
<p><code>hash(key, i) = ( hash1(key) + i × hash2(key) ) % table_size</code></p>
<p>Where:</p>
<ul>
    <li><code>i</code> is the probing attempt number (0, 1, 2, ...).</li>
    <li><code>hash1(key)</code> is the primary hash function.</li>
    <li><code>hash2(key)</code> is the secondary hash function, which must be non-zero.</li>
</ul>


<p><strong>Double Hashing</strong> is an open addressing collision resolution technique used in hash tables. It improves on linear and quadratic probing by using a second hash function to calculate the probing interval, which helps to reduce clustering and spread out the keys more uniformly.</p>

<p><strong>How Double Hashing Works:</strong></p>
<p>In double hashing, when a collision occurs (i.e., when the desired slot is already occupied), a second hash function is used to determine the step size for probing.</p>

<p><strong>Formula:</strong></p>
<p>Double hashing uses two hash functions:</p>
<ul>
    <li><strong>Primary Hash Function:</strong> hash1(key) = key % table_size</li>
    <li><strong>Secondary Hash Function:</strong> hash2(key) = 1 + (key % (table_size - 1))</li>
</ul>
<p>The formula for double hashing is:</p>
<p><strong>hash(key, i) = (hash1(key) + i × hash2(key)) % table_size</strong></p>
<ul>
    <li>i is the probing attempt number (0, 1, 2, ...).</li>
    <li>hash1(key) is the primary hash function.</li>
    <li>hash2(key) is the secondary hash function, which must be non-zero.</li>
</ul>

<p><strong>Example:</strong></p>
<p>Let's illustrate double hashing with an example:</p>
<ul>
    <li><strong>Hash Table Size:</strong> 10</li>
    <li><strong>Keys to Insert:</strong> 50, 700, 76, 85, 92, 73, 101</li>
</ul>

<p><strong>Steps for Insertion:</strong></p>

<ol>
    <li><strong>Insert 50:</strong>
        <ul>
            <li>hash1(50) = 50 % 10 = 0</li>
            <li>hash2(50) = 1 + (50 % 9) = 1 + 5 = 6</li>
            <li>Slot 0 is empty.</li>
            <li><strong>Insert 50 at index 0.</strong></li>
        </ul>
        <table border="1">
            <tr>
                <th>Index</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>0</td>
                <td>50</td>
            </tr>
            <tr>
                <td>1</td>
                <td></td>
            </tr>
            <tr>
                <td>2</td>
                <td></td>
            </tr>
            <tr>
                <td>3</td>
                <td></td>
            </tr>
            <tr>
                <td>4</td>
                <td></td>
            </tr>
            <tr>
                <td>5</td>
                <td></td>
            </tr>
            <tr>
                <td>6</td>
                <td></td>
            </tr>
            <tr>
                <td>7</td>
                <td></td>
            </tr>
            <tr>
                <td>8</td>
                <td></td>
            </tr>
            <tr>
                <td>9</td>
                <td></td>
            </tr>
        </table>
    </li>
    <li><strong>Insert 700:</strong>
        <ul>
            <li>hash1(700) = 700 % 10 = 0</li>
            <li>hash2(700) = 1 + (700 % 9) = 1 + 7 = 8</li>
            <li>Slot 0 is occupied. Compute next slot: (0 + 1 * 8) % 10 = 8</li>
            <li>Slot 8 is empty.</li>
            <li><strong>Insert 700 at index 8.</strong></li>
        </ul>
        <table border="1">
            <tr>
                <th>Index</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>0</td>
                <td>50</td>
            </tr>
            <tr>
                <td>1</td>
                <td></td>
            </tr>
            <tr>
                <td>2</td>
                <td></td>
            </tr>
            <tr>
                <td>3</td>
                <td></td>
            </tr>
            <tr>
                <td>4</td>
                <td></td>
            </tr>
            <tr>
                <td>5</td>
                <td></td>
            </tr>
            <tr>
                <td>6</td>
                <td></td>
            </tr>
            <tr>
                <td>7</td>
                <td></td>
            </tr>
            <tr>
                <td>8</td>
                <td>700</td>
            </tr>
            <tr>
                <td>9</td>
                <td></td>
            </tr>
        </table>
    </li>
    <li><strong>Insert 76:</strong>
        <ul>
            <li>hash1(76) = 76 % 10 = 6</li>
            <li>hash2(76) = 1 + (76 % 9) = 1 + 4 = 5</li>
            <li>Slot 6 is empty.</li>
            <li><strong>Insert 76 at index 6.</strong></li>
        </ul>
        <table border="1">
            <tr>
                <th>Index</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>0</td>
                <td>50</td>
            </tr>
            <tr>
                <td>1</td>
                <td></td>
            </tr>
            <tr>
                <td>2</td>
                <td></td>
            </tr>
            <tr>
                <td>3</td>
                <td></td>
            </tr>
            <tr>
                <td>4</td>
                <td></td>
            </tr>
            <tr>
                <td>5</td>
                <td></td>
            </tr>
            <tr>
                <td>6</td>
                <td>76</td>
            </tr>
            <tr>
                <td>7</td>
                <td></td>
            </tr>
            <tr>
                <td>8</td>
                <td>700</td>
            </tr>
            <tr>
                <td>9</td>
                <td></td>
            </tr>
        </table>
    </li>
    <li><strong>Insert 85:</strong>
        <ul>
            <li>hash1(85) = 85 % 10 = 5</li>
            <li>hash2(85) = 1 + (85 % 9) = 1 + 4 = 5</li>
            <li>Slot 5 is empty.</li>
            <li><strong>Insert 85 at index 5.</strong></li>
        </ul>
        <table border="1">
            <tr>
                <th>Index</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>0</td>
                <td>50</td>
            </tr>
            <tr>
                <td>1</td>
                <td></td>
            </tr>
            <tr>
                <td>2</td>
                <td></td>
            </tr>
            <tr>
                <td>3</td>
                <td></td>
            </tr>
            <tr>
                <td>4</td>
                <td></td>
            </tr>
            <tr>
                <td>5</td>
                <td>85</td>
            </tr>
            <tr>
                <td>6</td>
                <td>76</td>
            </tr>
            <tr>
                <td>7</td>
                <td></td>
            </tr>
            <tr>
                <td>8</td>
                <td>700</td>
            </tr>
            <tr>
                <td>9</td>
                <td></td>
            </tr>
        </table>
    </li>
    <li><strong>Insert 92:</strong>
        <ul>
            <li>hash1(92) = 92 % 10 = 2</li>
            <li>hash2(92) = 1 + (92 % 9) = 1 + 2 = 3</li>
            <li>Slot 2 is empty.</li>
            <li><strong>Insert 92 at index 2.</strong></li>
        </ul>
        <table border="1">
            <tr>
                <th>Index</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>0</td>
                <td>50</td>
            </tr>
            <tr>
                <td>1</td>
                <td></td>
            </tr>
            <tr>
                <td>2</td>
                <td>92</td>
            </tr>
            <tr>
                <td>3</td>
                <td></td>
            </tr>
            <tr>
                <td>4</td>
                <td></td>
            </tr>
            <tr>
                <td>5</td>
                <td>85</td>
            </tr>
            <tr>
                <td>6</td>
                <td>76</td>
            </tr>
            <tr>
                <td>7</td>
                <td></td>
            </tr>
            <tr>
                <td>8</td>
                <td>700</td>
            </tr>
            <tr>
                <td>9</td>
                <td></td>
            </tr>
        </table>
    </li>
    <li><strong>Insert 73:</strong>
        <ul>
            <li>hash1(73) = 73 % 10 = 3</li>
            <li>hash2(73) = 1 + (73 % 9) = 1 + 1 = 2</li>
            <li>Slot 3 is empty.</li>
            <li><strong>Insert 73 at index 3.</strong></li>
        </ul>
        <table border="1">
            <tr>
                <th>Index</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>0</td>
                <td>50</td>
            </tr>
            <tr>
                <td>1</td>
                <td></td>
            </tr>
            <tr>
                <td>2</td>
                <td>92</td>
            </tr>
            <tr>
                <td>3</td>
                <td>73</td>
            </tr>
            <tr>
                <td>4</td>
                <td></td>
            </tr>
            <tr>
                <td>5</td>
                <td>85</td>
            </tr>
            <tr>
                <td>6</td>
                <td>76</td>
            </tr>
            <tr>
                <td>7</td>
                <td></td>
            </tr>
            <tr>
                <td>8</td>
                <td>700</td>
            </tr>
            <tr>
                <td>9</td>
                <td></td>
            </tr>
        </table>
    </li>
    <li><strong>Insert 101:</strong>
        <ul>
            <li>hash1(101) = 101 % 10 = 1</li>
            <li>hash2(101) = 1 + (101 % 9) = 1 + 2 = 3</li>
            <li>Slot 1 is empty.</li>
            <li><strong>Insert 101 at index 1.</strong></li>
        </ul>
        <table border="1">
            <tr>
                <th>Index</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>0</td>
                <td>50</td>
            </tr>
            <tr>
                <td>1</td>
                <td>101</td>
            </tr>
            <tr>
                <td>2</td>
                <td>92</td>
            </tr>
            <tr>
                <td>3</td>
                <td>73</td>
            </tr>
            <tr>
                <td>4</td>
                <td></td>
            </tr>
            <tr>
                <td>5</td>
                <td>85</td>
            </tr>
            <tr>
                <td>6</td>
                <td>76</td>
            </tr>
            <tr>
                <td>7</td>
                <td></td>
            </tr>
            <tr>
                <td>8</td>
                <td>700</td>
            </tr>
            <tr>
                <td>9</td>
                <td></td>
            </tr>
        </table>
    </li>
</ol>

<p><strong>Summary:</strong></p>
<p>Double hashing provides a more distributed placement of keys compared to linear and quadratic probing by using two hash functions. This reduces clustering and improves the efficiency of the hash table, especially when the table is almost full.</p>

