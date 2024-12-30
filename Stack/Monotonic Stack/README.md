# 🌐 Monotonic Stack 🌐

⬇️ **Monotonic Sequence** ⬇️

A **monotonic sequence** is a sequence of elements that consistently increases or decreases in value:

- **Increasing**: Each element is greater than or equal to the previous one.
- **Decreasing**: Each element is less than or equal to the previous one.

⭐ **Monotonic Stack** ⭐

A **monotonic stack** is a variation of the stack data structure that maintains its elements in either increasing or decreasing order.

Unlike a regular stack where you can freely push or pop elements, a monotonic stack enforces specific rules to ensure the elements follow a **monotonic order**.

✨ **Types of Monotonic Stacks** ✨

There are four types of monotonic stacks based on the order of elements (from bottom to top):

| Type                    | Definition                                                 | Example              |
| ----------------------- | ---------------------------------------------------------- | -------------------- |
| **Strictly Increasing** | Each element is strictly greater than the previous one.    | `[1, 4, 5, 8, 9]`    |
| **Non-decreasing**      | Each element is greater than or equal to the previous one. | `[1, 4, 5, 5, 8, 9]` |
| **Strictly Decreasing** | Each element is strictly less than the previous one.       | `[9, 8, 5, 4, 1]`    |
| **Non-increasing**      | Each element is less than or equal to the previous one.    | `[9, 9, 8, 5, 5, 1]` |

<img src="https://assets.leetcode.com/users/images/e290dfef-faf5-40aa-8615-574a50519c22_1715063778.8476539.jpeg"/>

---

### 🔢 Time and Space Complexity 🔢

- **Time Complexity**:&#x20;
  - Each element is pushed and popped from the stack at most once during traversal.
- **Space Complexity**:&#x20;
  - The external stack can hold up to  elements, where  is the size of the input array.

---

### 🔄 Building a Monotonic Stack 🔄

To maintain a monotonic property (increasing or decreasing), we carefully decide when to remove elements from the stack before pushing a new element.
In the following examples, stack will always maintain monotonic order.

---

#### 🔼 Strictly Increasing Stack 🔼

A **strictly increasing stack** means every element is greater than the previous one.

**Logic**:\
When adding a new element to the stack:

- If the new element is **less than or equal to** the top of the stack, it would violate the strictly increasing property.
- So, remove elements from the top of the stack until you find the right position for the new element.

**Algorithm**:

```python
for i in range(n):
    while stack and arr[i] <= stack[-1]:
        stack.pop()
    stack.append(arr[i])
```

---

#### ⬆️ Non-decreasing Stack ⬆️

A **non-decreasing stack** allows duplicate or equal values.

**Logic**:

- If the new element is **less than** the top of the stack, remove elements to preserve the monotonic property.

**Algorithm**:

```python
for i in range(n):
    while stack and arr[i] < stack[-1]:
        stack.pop()
    stack.append(arr[i])
```

---

#### 🔽 Strictly Decreasing Stack 🔽

A **strictly decreasing stack** means every element is less than the previous one.

**Logic**:

- If the new element is **greater than or equal to** the top of the stack, remove elements to preserve the strictly decreasing property.

**Algorithm**:

```python
for i in range(n):
    while stack and arr[i] >= stack[-1]:
        stack.pop()
    stack.append(arr[i])
```

---

#### ⬇️ Non-increasing Stack ⬇️

A **non-increasing stack** allows duplicate or equal values.

**Logic**:

- If the new element is **greater than** the top of the stack, remove elements to preserve the monotonic property.

**Algorithm**:

```python
for i in range(n):
    while stack and arr[i] > stack[-1]:
        stack.pop()
    stack.append(arr[i])
```

---

| Stack Type              | Remove Condition (While Loop) | Push Condition             |
| ----------------------- | ----------------------------- | -------------------------- |
| **Strictly Increasing** | `arr[i] <= stack[-1]`         | New element > all in stack |
| **Non-decreasing**      | `arr[i] < stack[-1]`          | New element ≥ all in stack |
| **Strictly Decreasing** | `arr[i] >= stack[-1]`         | New element < all in stack |
| **Non-increasing**      | `arr[i] > stack[-1]`          | New element ≤ all in stack |

This table summarizes the condition you check before deciding whether to remove elements from the stack while maintaining the monotonic property.

By following these rules, you can efficiently build and maintain different types of monotonic stacks.

# Problems 🌟

---

## 1. Next Greater Element (NGE) 🏆

**Problem:**
For every element in the array, find the **next greater element** to its right. If no such element exists, return `-1`. 🔄

**Approach:**

- Use a **non-increasing monotonic stack**:
  - As you iterate through the array, check if the current element is greater than the element at the top of the stack.
  - If it is, pop elements from the stack. The popped element's **next greater element** will be the current element.
  - Push the current index into the stack.

**Code:**

```python
def nge(n, arr):
    stack = []
    ans = [-1] * n  # Initialize result array with -1
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:  # New element is greater
            ind = stack.pop()
            ans[ind] = arr[i]  # Assign NGE
        stack.append(i)  # Push current index
    return ans
```

**Example:**
For `arr = [4, 5, 2, 10]`, the output will be `[5, 10, 10, -1]`. 🎮

---

## 2. Next Smaller Element (NSE) 🍎

**Problem:**
For every element in the array, find the **next smaller element** to its right. If no such element exists, return `-1`. 🚀

**Approach:**

- Use a **non-decreasing monotonic stack**:
  - As you iterate through the array, check if the current element is smaller than the element at the top of the stack.
  - If it is, pop elements from the stack. The popped element's **next smaller element** will be the current element.
  - Push the current index into the stack.

**Code:**

```python
def nse(n, arr):
    stack = []
    ans = [-1] * n  # Initialize result array with -1
    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:  # New element is smaller
            ind = stack.pop()
            ans[ind] = arr[i]  # Assign NSE
        stack.append(i)  # Push current index
    return ans
```

**Example:**
For `arr = [4, 5, 2, 10]`, the output will be `[2, 2, -1, -1]`. 🔼

---

## 3. Previous Greater Element (PGE) 🎨

**Problem:**
For every element in the array, find the **previous greater element** to its left. If no such element exists, return `-1`. 🔮

**Approach:**

- Use a **strictly decreasing monotonic stack**:
  - Before adding a new element, remove all elements smaller than or equal to it from the stack.
  - The top of the stack becomes the **previous greater element** for the current element.

**Code:**

```python
def pge(n, arr):
    stack = []
    ans = [-1] * n  # Initialize result array with -1
    for i in range(n):
        while stack and arr[i] >= arr[stack[-1]]:  # Remove smaller/equal elements
            stack.pop()
        if stack:
            ans[i] = arr[stack[-1]]  # Assign PGE
        stack.append(i)  # Push current index
    return ans
```

**Example:**
For `arr = [4, 5, 2, 10]`, the output will be `[-1, -1, 5, -1]`. 🎩

---

## 4. Previous Smaller Element (PSE) 🌱

**Problem:**
For every element in the array, find the **previous smaller element** to its left. If no such element exists, return `-1`. 🔇

**Approach:**

- Use a **strictly increasing monotonic stack**:
  - Before adding a new element, remove all elements larger than or equal to it from the stack.
  - The top of the stack becomes the **previous smaller element** for the current element.

**Code:**

```python
def pse(n, arr):
    stack = []
    ans = [-1] * n  # Initialize result array with -1
    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:  # Remove larger/equal elements
            stack.pop()
        if stack:
            ans[i] = arr[stack[-1]]  # Assign PSE
        stack.append(i)  # Push current index
    return ans
```

**Example:**
For `arr = [4, 5, 2, 10]`, the output will be `[-1, 4, -1, 2]`. 💪

---

## Solving Right To Left →← 😃

For some problems, it may be more intuitive or efficient to iterate through the array from right to left instead of left to right. This approach can simplify the logic for finding previous elements or reverse the logic for finding next elements. 🎉

**Approach:**

1. Reverse the traversal direction to iterate from the end of the array toward the beginning.
2. Use the same monotonic stack rules but adjust the comparison logic as needed.
3. The stack manipulations and result assignments remain the same, ensuring efficiency. 🎯

**Reverse NGE:**
Find the **next greater element** to the left by iterating from right to left. 🍅

```python
def reverse_nge(n, arr):
    stack = []
    ans = [-1] * n
    for i in range(n - 1, -1, -1):
        while stack and arr[i] > stack[-1]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(arr[i])
    return ans
```

**Reverse NSE:**
Find the **next smaller element** to the left by iterating from right to left. 🍒

```python
def reverse_nse(n, arr):
    stack = []
    ans = [-1] * n
    for i in range(n - 1, -1, -1):
        while stack and arr[i] < stack[-1]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(arr[i])
    return ans
```

Similarly, you can reverse the logic for previous greater and smaller elements by iterating in reverse order. The logic for stack manipulation remains the same. 🌐

---
## NGE Circular Array

You are given a circular array of integers `arr` of size `n`. For each element in the array, find the **next greater element (NGE)** in the circular manner.

- If no such element exists, return `-1` for that position.
- Circular means after the last element, the search continues from the beginning of the array.

---

**Sample Test Cases**

**Input 1:**

```plaintext
n = 4  
arr = [1, 2, 1, 3]
```

**Output 1:**

```plaintext
[2, 3, 3, -1]
```

Explanation :

- For `arr[0] = 1`: NGE is `2`.
- For `arr[1] = 2`: NGE is `3`.
- For `arr[2] = 1`: NGE is `3`.
- For `arr[3] = 3`: No NGE exists, so `-1`.

---

**Input 2:**

```plaintext
n = 3  
arr = [3, 1, 2]
```

**Output 2:**

```plaintext
[-1, 2, 3]
```

**Explanation :**

- For `arr[0] = 3`: No NGE exists.
- For `arr[1] = 1`: NGE is `2`.
- For `arr[2] = 2`: NGE is `3`.

---

**Brute Force Approach**

1. Use a nested loop to check the next greater element for each position.
2. For each element `arr[i]`, start checking from `i + 1` circularly.
3. If a greater element is found, record it as the NGE for `arr[i]` and break out of the loop.
4. If no greater element exists after traversing the entire array, store `-1` for that position.

```python
def bruteForceNGE(n, arr):
    ans = [-1] * n
    for i in range(n):
        for j in range(i + 1, i + n):
            index = j % n
            if arr[index] > arr[i]:
                ans[i] = arr[index]
                break
    return ans
```

---

**Optimized Approach (Using Stack)**

1. Use a stack to store indices of elements whose NGE is yet to be determined.
2. Traverse the array twice (to handle the circular nature).
3. For each element, check if it can serve as the NGE for elements indexed in the stack:
   - While the stack is not empty and the current element is greater than the element at the index stored at the top of the stack, assign the current element as the NGE.
   - Pop the index from the stack after finding its NGE.
4. Push the current index onto the stack if it hasn’t found its NGE yet.
5. Elements left in the stack after the traversal will have `-1` as their NGE.

---

```python
def optimizedNGE(n, arr):
    ans = [-1] * n
    stack = []
    for i in range(2 * n):  # Traverse twice for circular behavior
        i = i % n
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            ans[index] = arr[i]
        stack.append(i)
    return ans
```

---
