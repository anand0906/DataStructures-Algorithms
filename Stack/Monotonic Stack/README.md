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
## Daily Temperatures 🌤⛅🔋

You are given an array `temperatures` where each element represents the temperature of a day. For each day `i`, you need to calculate how many days you would have to wait to get a warmer temperature. If there is no future day with a higher temperature, set `answer[i]` to `0`. 🌤⛅🔋

---

**Sample Test Cases** 📊🔢🔄

**Example 1: 🌡️🌇📈**

- **Input:** `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`
- **Output:** `[1, 1, 4, 2, 1, 1, 0, 0]` \
  **Explanation:**
  - For day 0 (73°F), the next warmer day is day 1 (74°F), so `answer[0] = 1`.
  - For day 1 (74°F), the next warmer day is day 2 (75°F), so `answer[1] = 1`.
  - For day 2 (75°F), the next warmer day is day 6 (76°F), so `answer[2] = 4`.
  - For day 6 (76°F), there is no warmer day, so `answer[6] = 0`. 🌡️🌇📈

---

**Example 2: 👆☀️🌤**

- **Input:** `temperatures = [30, 40, 50, 60]`
- **Output:** `[1, 1, 1, 0]`

**Example 3: 🌤🌱⛅**

- **Input:** `temperatures = [30, 60, 90]`
- **Output:** `[1, 1, 0]`

---

**Approach** 🌱🌧☀️

**1. Brute Force Approach 🌡️⚡️🌧**

1. Iterate through each temperature in the array using two nested loops.
2. For each day `i`, compare the temperature with all subsequent days `j > i` to find the first day with a warmer temperature.
3. Store the difference `(j - i)` in the result array.
4. If no such day exists, store `0`. 🌡️⚡️🌧

**Code:** 🔧🔥✨

```python
def bruteForce(n, arr):
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                days = j - i
                ans.append(days)
                break
        else:
            ans.append(0)
    return ans
```

**Time Complexity:** 🔢⌚✨

- Outer loop runs `n` times.
- Inner loop runs for up to `n - i` iterations.
- Worst-case complexity: **O(n²)**. 🔢⌚✨

**Space Complexity:** 📃🔧⭐

- Uses only an `ans` array, so **O(n)**. 📃🔧⭐

---

**2. Optimized Approach using Stack 🔼🌈☀️**

The optimized approach uses a **Next Greater Element Problems Approach**: 🔼🌈☀️

1. Traverse the temperatures from left to right.
2. Maintain a stack to keep track of indices of temperatures in decreasing order.
3. For the current day `i`, check the stack:
   - If the current temperature is warmer than the temperature at the index on top of the stack, calculate the difference in indices and update the answer.
   - Continue until the stack is empty or the condition fails.
4. Append the current index to the stack.

**Code:** 🔧🌤🔃

```python
def optimized(n, arr):
    ans = [0] * n  # Initialize answer array with zeros
    stack = []  # Stack to store indices

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            ind = stack.pop()
            ans[ind] = i - ind
        stack.append(i)
    
    return ans
```

**Time Complexity:** 🌡️✨📈

- Each temperature is pushed and popped from the stack at most once.
- Complexity: **O(n)**. 🌡️✨📈

**Space Complexity:** 📃⌚⭐

- The stack holds up to `n` indices.
- Complexity: **O(n)**. 📃⌚⭐

---

## **Stock Span** 🌟📊✨

You are given an array `prices` of stock prices where `prices[i]` represents the price of a stock on day `i`. Your task is to calculate the **span** of the stock's price for each day. 🌟📊✨

The **span** of the stock's price on a given day is the maximum number of consecutive days (including the current day) the price has been less than or equal to the price on that day.

---

**Sample Test Cases** 📉📈📋

**Example 1:**

**Input:**\
`prices = [100, 80, 60, 70, 60, 75, 85]`\
**Output:**\
`[1, 1, 1, 2, 1, 4, 6]` 📉📈📋

**Explanation:**

- On day 0, the span is 1 (just that day).  
- On day 3 (price = 70), the span is 2 (days 2 and 3).  
- On day 5 (price = 75), the span is 4 (days 2, 3, 4, and 5).  
- On day 6 (price = 85), the span is 6 (all previous days). 📉📈📋

---

**Example 2:**

**Input:**\
`prices = [10, 20, 30, 40]`\
**Output:**\
`[1, 2, 3, 4]` 📊🌞✨

**Explanation:**\
Every day the price increases, so the span is the number of days up to and including that day. 📊🌞✨

---

**Approach** 🛠️🔎📊

**1. Brute Force Approach** 🐢📉🔧

- For each day `i`, iterate backward to find the nearest day where the price is higher.  
- If no such day is found, the span is `i + 1`. 🐢📉🔧

---

```python
def bruteForce(n, arr):
    ans = [1] * n  # Initialize the span array with 1
    for i in range(n):
        for j in range(i - 1, -1, -1):  # Traverse backward from day i
            if arr[j] > arr[i]:  # Break if a higher price is found
                ans[i] = i - j
                break
        else:
            ans[i] = i + 1  # Span is the entire length up to day i
    return ans
```

**Time Complexity:** O(n²) due to the nested loops.\
**Space Complexity:** O(n) to store the result array. 🐢📉🔧

---

**2. Optimized Approach using a Stack** 🚀📈✨

We need to find previous greater element for each element and the difference between them will be our answer.\
So we can use PGE using strictly decreasing monotonic stack. 🚀📈✨

- For each day, find out a previous day where price is higher than current day's price. 🚀📈✨


```python
def optimized(n, arr):
    ans = [1] * n  # Initialize the span array with 1
    stack = []  # Stack to store indices
    for i in range(n):
        # Remove elements from the stack that are less than or equal to the current price
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if stack:  # If stack is not empty
            ans[i] = i - stack[-1]
        else:  # If stack is empty, span is the entire length up to day i
            ans[i] = i + 1
        stack.append(i)  # Add the current day to the stack
    return ans
```

**Time Complexity:** O(n) because each index is pushed and popped at most once.\
**Space Complexity:** O(n) for the stack. 🚀📈✨

---




## Removing K Digits 🌟✨🌟

We are given:

1. A **string** `num` 📜 showing a number (e.g., "1432219").
2. A number `k` 🔢, meaning how many digits to remove.

**Goal:**

Take away `k` digits so the number left is the **smallest possible**.
- The answer **can’t have extra zeros** unless it’s just "0".

---

🌟 **Key Points to Understand:** ✨🌟

**1. Place Value in Numbers:**

Digits in a number matter most depending on where they are.

- The **leftmost digits** are worth the most. 💵
- Example: In `1432219`, the `1` is worth millions, but the `9` is just worth 9. 📉

**To make the number smallest:**
1. **Keep the small digits on the left.**
2. **Remove bigger digits first**, as this will shrink the number the most. 📉🔢

**2. What Happens When We Remove Digits?**

When a digit goes away, the next digit slides over to fill its spot.
- Removing **bigger digits** early makes space for **smaller digits**. 🪄

**Example 1:**
`num = "1432219", k = 3`
- Taking out the first `4` gives "132219", which is smaller than leaving the `4`.

**Example 2:**
`num = "5432", k = 1`
- Removing `5` gives "432". 🏹
- Removing any other digit makes the number bigger.

**3. Which Digits Should Go?**

Look at each digit and the one after it:
- If the current digit is **bigger than the next one**, remove it to shrink the number. 📉
- If the current digit is **smaller**, leave it, as it helps keep the number small.

**Why This Works:**

- Removing digits that "break the order" puts smaller numbers first. 🪄
- This makes the smallest number possible.

---

🌟 **Step-by-Step Examples:** ✨🌟

**Case 1: Simple Example**

**Input:** `num = "1432219", k = 3`
We need to remove 3 digits.

1. **Step 1:** Compare digits one by one.
   - `1` vs `4`: `1 < 4` → Keep `1`. 👍
   - `4` vs `3`: `4 > 3` → Remove `4`. Result: "132219".

2. **Step 2:** Keep going.
   - `3` vs `2`: `3 > 2` → Remove `3`. Result: "12219". 🎯

3. **Step 3:** Keep going again.
   - `2` vs `2`: `2 = 2` → Keep the first `2`. 👍
   - `2` vs `1`: `2 > 1` → Remove the second `2`. Result: "1219".

**Final Result:** "1219" 🏆

---

**Case 2: Numbers That Grow**

**Input:** `num = "12345", k = 2`
We need to remove 2 digits.

1. **Step 1:** Compare digits.
   - `1` vs `2`: `1 < 2` → Keep `1`. 👍
   - `2` vs `3`: `2 < 3` → Keep `2`.
   - `3` vs `4`: `3 < 4` → Keep `3`.

2. **Step 2:** Remove the last two digits (`4` and `5`). Result: "123". 🎯

**Final Result:** "123" 🏆

---

**Case 3: Numbers That Shrink**

**Input:** `num = "54321", k = 2`
We need to remove 2 digits.

1. **Step 1:** Compare digits.
   - `5` vs `4`: `5 > 4` → Remove `5`. Result: "4321". 🎯
   - `4` vs `3`: `4 > 3` → Remove `4`. Result: "321".

**Final Result:** "321" 🏆

---

**Case 4: Watch Out for Zeros**

**Input:** `num = "10200", k = 1`
We need to remove 1 digit.

1. **Step 1:** Compare digits.
   - `1` vs `0`: `1 > 0` → Remove `1`. Result: "0200". 🎯

2. **Step 2:** Take off the leading zero.
   - "0200" → "200".

**Final Result:** "200" 🏆

---

**Case 5: Edge Case**

**Input:** `num = "10", k = 2`
We need to remove all digits.

1. Remove both digits: "10" → "0". 🎯

**Final Result:** "0" 🏆

---

🌟 **Ways to Solve It** ✨🌟

**1. Simple Brute Force Way:**

#### Steps:

1. Go through the number and find a digit that is **bigger than the next one**.
2. Remove that digit. ✂️
3. Do this `k` times.
4. Put the number back into a string and take away any leading zeros.

#### Code:

```python
def bruteForce(num, k):
    num = list(num)  # Turn into a list to make changes
    for _ in range(k):
        n = len(num)
        i = 1
        # Find the first digit bigger than the next one
        while i < n and num[i] >= num[i - 1]:
            i += 1
        # Remove the digit
        if i < n:
            del num[i - 1]
        else:
            del num[-1]  # If no bigger digit is found, remove the last one
    # Put it back into a string and remove leading zeros
    return "".join(num).lstrip('0') or "0"
```

---

**2. Faster Stack-Based Way:**

#### Idea:

Use a **stack** to keep digits in **non-decreasing order**:

1. Go through the number one digit at a time. 🔄
2. If the digit is smaller than the one on top of the stack, remove the bigger one. ✂️
3. Add the current digit to the stack. 📥
4. When done, if `k > 0`, take off the last digits from the stack.

#### Code:

```python
def optimized(num,k):
    arr=list(num)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[i]<stack[-1] and k>0:
            stack.pop()
            k-=1
        stack.append(arr[i])
    while stack and k>0:
        stack.pop()
        k-=1
    ans="".join(stack).lstrip('0')
    return "0" if ans=="" else ans
```

---

| **Making the Largest Number Instead:** |
| --------------------------------------- |

```python
def bruteForce(num, k):
    num = list(num)  # Turn into a list to make changes
    for _ in range(k):
        n = len(num)
        i = 1
        # Find the first digit smaller than the next one
        while i < n and num[i] <= num[i - 1]:
            i += 1
        # Remove the digit
        if i < n:
            del num[i - 1]
        else:
            del num[-1]  # If no smaller digit is found, remove the last one
    # Put it back into a string and remove leading zeros
    return "".join(num).lstrip('0') or "0"

def optimized(num,k):
    arr=list(num)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[i]>stack[-1] and k>0:
            stack.pop()
            k-=1
        stack.append(arr[i])
    while stack and k>0:
        stack.pop()
        k-=1
    ans="".join(stack).lstrip('0')
    return "0" if ans=="" else ans
```

