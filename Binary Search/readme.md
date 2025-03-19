
# Binary Search

### **What is Binary Search?**
Binary search is a fast way to find a specific item in a **sorted list**. Instead of checking each item one by one (like linear search), binary search **divides** the list into halves and focuses only on the relevant half in each step. This makes searching much faster.

---

### **How Binary Search Works?**
Imagine you have a **dictionary** and want to find the word "Tiger" quickly.

#### **Step-by-Step Process:**
1️⃣ **Open the dictionary in the middle**
   - If the middle word is **Zebra**, you know "Tiger" comes **before Zebra**, so you ignore the second half.
   - If the middle word is **Apple**, you know "Tiger" comes **after Apple**, so you ignore the first half.

2️⃣ **Repeat the process**
   - Open the middle of the remaining section and check again.
   - Keep reducing the search space until you find "Tiger" or confirm it's not there.

✅ **Each step cuts the number of pages in half, making the search very fast!**

---

### **Binary Search Example in Numbers**
Let's say we have a **sorted list of numbers**: 
`[10, 20, 30, 40, 50, 60, 70, 80, 90]`

We want to find **50**.

#### **Steps:**
1️⃣ Look at the middle number: **40** (position 4)
   - Since **50 is greater than 40**, ignore the left half.

2️⃣ Check the new middle number: **70** (position 6)
   - Since **50 is smaller than 70**, ignore the right half.

3️⃣ Check the new middle number: **50** (position 5)
   - ✅ Found the number!

Only **3 steps** instead of checking all numbers one by one!

---

### **Advantages of Binary Search**
✔ **Fast** - Reduces the search space by half each time.
✔ **Efficient** - Works well with large datasets.
✔ **Used in Real Life** - Searching in dictionaries, phone books, or even in Google search algorithms.

⏳ **Time Complexity:** `O(log n)` (logarithmic time, very fast for large lists!)

**Finding a Page Number in a Book - Normal vs. Efficient Approach**

### **1. What We Normally Do (Slow Method - Linear Search)**

- Suppose we want to find **page 250** in a book with **1000 pages**.
- We start from **page 1** and turn one page at a time: **1 → 2 → 3 → 4... → 250**.
- This takes **a lot of time**, especially if the page number is large.
- If the page is near the end, we may have to flip **hundreds of pages**!

✅ **Easy to understand** but **very slow**.\
❌ **Worst case:** Flipping **999 pages** if the page is at the end.\
⏳ **Time Complexity:** **O(n)** (checking pages one by one).

---

### **2. What We Can Do Efficiently (Fast Method - Binary Search)**

Instead of turning pages one by one, let's **divide and conquer** like Binary Search:

#### **Step-by-Step Efficient Search:**

1️⃣ **Open the book in the middle**

- If the book has **1000 pages**, open **page 500**.
- **Compare:**
  - If **500 > 250**, the page is in the **first half** (ignore pages 501-1000).
  - If **500 < 250**, the page is in the **second half** (ignore pages 1-499).

2️⃣ **Repeat the process**

- Now, open the middle of the new range (1-499).
- Check **page 250** again:
  - If you land on **page 300**, 250 is in the first half (ignore 301-499).
  - If you land on **page 200**, 250 is in the second half (ignore 1-199).

3️⃣ **Continue halving the search space**

- **300 → 275 → 250** (found it!).

✅ **Fast because we eliminate half the pages each time.**\
✅ **Only takes about 10 flips to find a page in a 1000-page book!**\
✅ **Much better than flipping one by one!**\
⏳ **Time Complexity:** **O(log n)** (search space reduces by half each time).

---


