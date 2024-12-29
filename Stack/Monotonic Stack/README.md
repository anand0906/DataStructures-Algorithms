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

# Problems

---

## **1. Next Greater Element (NGE)**

### Problem:

For every element in the array, find the **next greater element** to its right. If no such element exists, return `-1`.

### Approach:

- Use a **non-increasing monotonic stack**:
  - As you iterate through the array, check if the current element is greater than the element at the top of the stack.
  - If it is, pop elements from the stack. The popped element's **next greater element** will be the current element.
  - Push the current index into the stack.

### Code:

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

### Example:

For `arr = [4, 5, 2, 10]`, the output will be `[5, 10, 10, -1]`.

---

## **2. Next Smaller Element (NSE)**

### Problem:

For every element in the array, find the **next smaller element** to its right. If no such element exists, return `-1`.

### Approach:

- Use a **non-decreasing monotonic stack**:
  - As you iterate through the array, check if the current element is smaller than the element at the top of the stack.
  - If it is, pop elements from the stack. The popped element's **next smaller element** will be the current element.
  - Push the current index into the stack.

### Code:

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

### Example:

For `arr = [4, 5, 2, 10]`, the output will be `[2, 2, -1, -1]`.

---

## **3. Previous Greater Element (PGE)**

### Problem:

For every element in the array, find the **previous greater element** to its left. If no such element exists, return `-1`.

### Approach:

- Use a **strictly decreasing monotonic stack**:
  - Before adding a new element, remove all elements smaller than or equal to it from the stack.
  - The top of the stack becomes the **previous greater element** for the current element.

### Code:

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

### Example:

For `arr = [4, 5, 2, 10]`, the output will be `[-1, -1, 5, -1]`.

---

## **4. Previous Smaller Element (PSE)**

### Problem:

For every element in the array, find the **previous smaller element** to its left. If no such element exists, return `-1`.

### Approach:

- Use a **strictly increasing monotonic stack**:
  - Before adding a new element, remove all elements larger than or equal to it from the stack.
  - The top of the stack becomes the **previous smaller element** for the current element.

### Code:

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

### Example:

For `arr = [4, 5, 2, 10]`, the output will be `[-1, 4, -1, 2]`.

---

##





