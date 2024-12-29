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



