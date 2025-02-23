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

**Steps**:

1. Go through the number and find a digit that is **bigger than the next one**.
2. Remove that digit. ✂️
3. Do this `k` times.
4. Put the number back into a string and take away any leading zeros.

**Code**:

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

**Idea**:

Use a **stack** to keep digits in **non-decreasing order**:

1. Go through the number one digit at a time. 🔄
2. If the digit is smaller than the one on top of the stack, remove the bigger one. ✂️
3. Add the current digit to the stack. 📥
4. When done, if `k > 0`, take off the last digits from the stack.

**Code**:

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

# Use non-increasing monotonic stack
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

---

## Lexicographically Smallest and Largest Strings ✨📚✨

Lexicographical order is similar to dictionary order. In this context:

- A **lexicographically smaller string** appears earlier in the dictionary.
- A **lexicographically larger string** appears later. ✍️📖📜

**Key Concept** 🧩🔑🧩

- The comparison is made character by character, starting from the first character.
- The first differing character decides which string is smaller or larger.

---

**Lexicographically Smallest String** 🌟⬇️🌟

- A string where **smaller characters (a, b, c, etc.) come before larger characters (x, y, z, etc.)**.
- This is achieved by arranging the characters in **ascending order**.

**Lexicographically Largest String** 🌟⬆️🌟

- A string where **larger characters come before smaller characters**.
- This is achieved by arranging the characters in **descending order**.

---

**How Comparison Works** 🛠️⚖️🛠️

1. Compare the first character of both strings.
2. If the first character is the same, move to the next character and repeat.
3. The first string to have a "smaller" character is lexicographically smaller.

---

**Examples** 📝📊📝

1. **"ab" vs. "ba"**:
   - Compare first characters: `'a'` < `'b'`, so "ab" is smaller.
2. **"cat" vs. "car"**:
   - Compare character by character: `'c'` = `'c'`, `'a'` = `'a'`, but `'t'` > `'r'`.
   - So, "cat" is larger.

**Sorting a String** 🗂️🔡🗂️

Suppose we are given **"anand"**:

1. **Lexicographically Smallest**:

   - Arrange characters in ascending order: **"aadnn"**.
   - Smaller letters come first.

2. **Lexicographically Largest**:

   - Arrange characters in descending order: **"nndaa"**.
   - Larger letters come first.

---

| **Order**            | **Definition**                        | **Example (Input: "anand")** |
| -------------------- | ------------------------------------- | ---------------------------- |
| Smallest (Ascending) | Characters sorted in increasing order | "aadnn"                      |
| Largest (Descending) | Characters sorted in decreasing order | "nndaa"                      |


## Removing Duplicate Letters ✨✏✨
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
among all possible results.

In this problem, we need to find the smallest string after removing duplicate characters, while preserving the relative order of the characters in the original string. 📝⚙️🔥

**Example 1:**
Input: s = "bcabc"
Output: "abc"

**Example 2:**
Input: s = "cbacdcbc"
Output: "acdb"

---

**Brute Force Approach 🧠🔄🔀**

A brute-force solution involves:

1. Finding all subsequences of the string that do not contain duplicate characters.
2. Returning the smallest subsequence (lexicographically).

This approach, while correct, is highly inefficient because the number of subsequences grows exponentially with the size of the string. ⚠️🕱️⌛


```python
def bruteForce(n, s):
    ans = None  # To store the smallest lexicographical subsequence
    unqCnt = len(set(s))  # Total number of unique characters in the string

    def recursive(sub, pos, visited):
        nonlocal ans
        # Base Case: End of the string
        if pos == n:
            # Check if the current subsequence is smaller and valid
            if (ans is None or sub < ans) and sub != "" and len(visited) == unqCnt:
                ans = sub
            return

        # Exclude the current character and recurse
        recursive(sub, pos + 1, visited.copy())

        # Include the current character if not visited
        if s[pos] not in visited:
            visited[s[pos]] = 1  # Mark character as visited
            recursive(sub + s[pos], pos + 1, visited.copy())

    recursive("", 0, {})  # Start recursion with an empty subsequence
    return ans
```

---

**Key Observations and Optimized Approach 🔬⚖️🌐**

To solve the problem efficiently, we rely on these key observations:

1. **Lexicographically Smallest Order:**

   - To form a smaller string, characters should appear in **increasing order**.
   - However, we cannot simply sort the string because we need to preserve the **original order** of characters.

2. **Using a Monotonic Stack**:

   - A **monotonic increasing stack** helps maintain the increasing nature of characters while preserving their relative order.
   - This data structure will allow us to efficiently manage which characters to keep or discard. 🛠️🗃️📊

---

**Intuitive Explanation 🔨🤖🌌**

1. **Goal**:

   - Include every unique character exactly once.
   - Ensure the result is the smallest possible string lexicographically.

2. **Building the Result**:

   - Traverse the string from left to right.
   - Use a stack to store characters in the correct order.

3. **Decision Making**:

   - For each character, decide whether to include it in the stack based on the following rules:

     a. **Character is Already Visited**:
     - If the current character is already in the stack, skip it to avoid duplicates.
       b. **Maintain Increasing Order**:
     - If the current character is smaller than the top of the stack and the top character appears later in the string, pop the top character.
     - This ensures the result remains lexicographically smaller while ensuring that all characters are included eventually.

4. **Tracking Visits**:

   - Use a `visited` set to track characters already in the stack.
   - Use a `last_occurrence` map to know if a character appears again later in the string. ⚡️🔧🔬

---

**Step-by-Step Algorithm 🔢🔄🕴️**

1. Compute the **last occurrence** of each character in the string.
2. Initialize:
   - An empty stack.
   - A `visited` set to track characters already in the stack.
3. Traverse the string:
   - If the character is not in `visited`:
     - While the stack is not empty and:
       - The current character is smaller than the top of the stack.
       - The top character appears later in the string.
     - Pop the top character from the stack and remove it from `visited`.
     - Push the current character onto the stack and mark it as `visited`.
4. Convert the stack to the final string. ⚖️📁✔️


```python
def optimized(n, s):
    visited = {i: False for i in set(s)}  # Tracks if a character is in the stack
    lastPos = {i: s.rfind(i) for i in set(s)}  # Last occurrence index of each character
    stack = []  # Monotonic stack to store the result characters

    for i in range(n):
        # Skip characters already in the stack
        if visited[s[i]]:
            continue

        # Maintain stack's increasing order and remove characters that appear later
        while stack and s[i] < stack[-1] and lastPos[stack[-1]] > i:
            temp = stack.pop()  # Remove top of the stack
            visited[temp] = False  # Mark it as not visited

        # Add current character to the stack
        stack.append(s[i])
        visited[s[i]] = True  # Mark it as visited

    # Join the stack to form the final answer
    ans = "".join(stack)
    return ans
```

---

**Why It Works 🔄⚙️🔧**

1. **Maintains Order**:

   - By iterating from left to right and only removing characters that reappear later, the stack preserves the original relative order of characters.

2. **Ensures Smallest String**:

   - By maintaining an increasing stack, smaller characters are prioritized, ensuring a lexicographically smaller result.

3. **Efficiently Includes All Characters**:

   - The use of `last_occurrence` guarantees that even if a character is removed, it will be added later if needed. 🔄🔢🌍

---

**Example 📊🔢✨**

**Input: `"cbacdcbc"`**

1. **Last Occurrences**:

   - `'c'`: 7, `'b'`: 6, `'a'`: 2, `'d'`: 4

2. **Process Each Character**:

   - `'c'`: Add to stack (stack: `['c']`).
   - `'b'`: Add to stack (stack: `['c', 'b']`).
   - `'a'`: Remove `'b'` and `'c'` (stack: `['a']`). Add `'a'`.
   - `'c'`: Add to stack (stack: `['a', 'c']`).
   - `'d'`: Add to stack (stack: `['a', 'c', 'd']`).
   - `'c'`: Skip (already visited).
   - `'b'`: Add to stack (stack: `['a', 'c', 'd', 'b']`).
   - `'c'`: Skip (already visited).

3. **Final Stack**: `['a', 'c', 'd', 'b']`

4. **Result**: `"acdb"` ✨📖✔️


---

## **Find the Most Competitive Subsequence** ✨⚡✨

Given an integer array `nums` and a positive integer `k`, return the most competitive subsequence of `nums` of size `k`. ⚙✨⚡

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array. ✨✅⚡

We define that a subsequence `a` is more competitive than a subsequence `b` (of the same length) if in the first position where `a` and `b` differ, subsequence `a` has a number less than the corresponding number in `b`. For example, `[1,3,4]` is more competitive than `[1,3,5]` because the first position they differ is at the final number, and 4 is less than 5. ⚡✅✨

---

**Example 1:** 🔢⚡🌟

Input: `nums = [3,5,2,6]`, `k = 2`
Output: `[2,6]`

Explanation: Among the set of every possible subsequence: `{[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}`, `[2,6]` is the most competitive.

---

**Example 2:** 🔢⚡🌟

Input: `nums = [2,4,3,3,5,4,9,6]`, `k = 4`
Output: `[2,3,3,4]`

---

**Solution:** 🔢⚙✨

Here we need to find the smallest subsequence of length `k`.

It can be solved similarly to the "remove k digits" problem.

Here we need to find a subsequence of length `k`, which means we need to remove `n-k` elements from the array.

So, the answer would be the smallest subsequence obtained by removing `n-k` elements from it. ✨⚡✅


```python
def solve(n,arr,k):
    stack=[]
    k=n-k
    for i in range(n):
        while stack and arr[i]<stack[-1] and k>0:
            stack.pop()
            k-=1
        stack.append(arr[i])
    while stack and k>0:
        stack.pop()
        k-=1
    return stack


arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(solve(n,arr,k))
```

---

## **Detecting 132 Pattern in an Array**

Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers `nums[i]`, `nums[j]`, and `nums[k]` such that:

- `i < j < k`
- `nums[i] < nums[k] < nums[j]`

Return `true` if there exists a 132 pattern in `nums`, otherwise return `false`.

---

**Brute Force Approach**

In the brute force approach, we check all possible combinations of indices `i`, `j`, and `k` where `i < j < k` to verify if the condition `nums[i] < nums[k] < nums[j]` holds true.

```python
def bruteForce(n, arr):
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] < arr[k] < arr[j]:
                    return True
    return False
```

- **Time Complexity:** `O(n^3)`, due to three nested loops.
- **Space Complexity:** `O(1)`, as no extra space is used.

---

**Better Approach**

The condition `nums[i] < nums[k] < nums[j]` (with `i < j < k`) can be rearranged as:

- `nums[i] < nums[j] > nums[k]`
- `nums[i] < nums[k]`

This indicates:

1. `nums[j]` should be greater than `nums[k]` (Point 1).
2. `nums[i]` should be smaller than both `nums[j]` and `nums[k]` (Point 2).

To solve this efficiently:

1. Use a **Previous Greater Element (PGE)** approach to determine, for each index `k`, the previous index `j` where `nums[j] > nums[k]`.
2. Maintain an array of the smallest element encountered up to each index to check if there exists an `i` such that `nums[i] < nums[k]`.

```python
def better(n, arr):
    PGE = [None] * n
    stack = []

    # Calculate Previous Greater Element (PGE)
    for i in range(n):
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if stack:
            PGE[i] = stack[-1]
        stack.append(i)

    # Calculate minimum element up to each index
    MINI = [None] * n
    currentMin = float('inf')
    for i in range(n):
        MINI[i] = currentMin
        currentMin = min(currentMin, arr[i])

    # Check for 132 pattern
    for i in range(n):
        if PGE[i] is not None and arr[i] > MINI[PGE[i]]:
            return True

    return False
```

- **Time Complexity:** `O(n)`, due to linear traversals and stack operations.
- **Space Complexity:** `O(n)`, for the `PGE` and `MINI` arrays.

---

**Optimized Approach**

To further optimize, we can combine the logic of identifying `nums[j] > nums[k]` (Point 1) and tracking the minimum element (Point 2) into a single loop. Here:

1. Use a stack to maintain indices and values for elements that could potentially form the `132` pattern.
2. Track the smallest element encountered so far.

```python
def optimized(n, arr):
    stack = []  # Stack to store tuples of (index, minimum value so far)
    currentMin = float('inf')

    for i in range(n):
        # Remove elements from stack that are less than or equal to the current element
        while stack and arr[i] >= arr[stack[-1][0]]:
            stack.pop()

        # Check if current element can form a 132 pattern
        if stack and arr[i] > stack[-1][1]:
            return True

        # Push the current index and the current minimum value onto the stack
        stack.append((i, currentMin))

        # Update the current minimum value
        currentMin = min(currentMin, arr[i])

    return False
```

- **Time Complexity:** `O(n)`, as each element is processed at most twice.
- **Space Complexity:** `O(n)`, due to the stack.

---
## **Sum of Subarray Minimums**

✨✨✨ Given an array of integers `arr`, you need to calculate the sum of the minimum values of all contiguous subarrays of `arr`. ✨✨✨

For example, if `arr = [3, 1, 2, 4]`, we calculate:

- Subarrays: `[3], [3, 1], [3, 1, 2], [3, 1, 2, 4], [1], [1, 2], [1, 2, 4], [2], [2, 4], [4]`
- Minimum values: `3, 1, 1, 1, 1, 1, 1, 2, 2, 4`
- Sum of minimums: `3 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 4 = 17` ✨✨✨

---

**1. Brute Force Approach**

✨✨✨ This method involves iterating over all possible subarrays and finding the minimum value in each. ✨✨✨

Steps:

1. Loop through all starting indices of subarrays (`i`).
2. For each `i`, loop through all possible ending indices (`j`).
3. Find the minimum value in the subarray `[i, j]`.
4. Add this minimum value to the total sum.

```python
def bruteForce(n, arr):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            mini = float('inf')
            for k in range(i, j + 1):
                mini = min(mini, arr[k])
            ans += mini
    return ans
```

Time Complexity:

- Finding all subarrays: O(N\*\*2)
- Calculating the minimum for each subarray: O(N)\
  Total\:O(N\*\*3)

Space Complexity\:O(1) ✨✨✨

---

**2. Better Approach**

✨✨✨ Instead of finding the minimum for every subarray repeatedly, maintain a rolling minimum while expanding the subarray. ✨✨✨

Steps:

1. Loop through all starting indices of subarrays (`i`).
2. Expand the subarray one element at a time (`j`) and update the rolling minimum.
3. Add this rolling minimum to the total sum.

```python
def better(n, arr):
    ans = 0
    for i in range(n):
        mini = float('inf')
        for j in range(i, n):
            mini = min(mini, arr[j])
            ans += mini
    return ans
```

Time Complexity: O(N\*\*2)\
Space Complexity: O(1) ✨✨✨

---

**Optimized Approach ✨✨✨**

Instead of finding the minimum element for every subarray individually, which can be computationally expensive, we can optimize the solution by calculating the contribution of every element as the minimum element in all subarrays where it is the minimum. Here's how:

---

Given an array `arr = [3, 1, 2, 4]`, we want to calculate the sum of all subarray minimums. Each element in the array contributes to the sum as the minimum element in multiple subarrays.

**Subarray-Minimum Calculation (Traditional Approach): 🔢🔢🔢**

1. For every possible subarray, find its minimum element.
2. Multiply this minimum value by the number of subarrays it contributes to.

Example:

For the array `[3, 1, 2, 4]`, the subarray minimums are:

| Subarray       | Minimum Element |
| -------------- | --------------- |
| `[3]`          | 3               |
| `[3, 1]`       | 1               |
| `[3, 1, 2]`    | 1               |
| `[3, 1, 2, 4]` | 1               |
| `[1]`          | 1               |
| `[1, 2]`       | 1               |
| `[1, 2, 4]`    | 1               |
| `[2]`          | 2               |
| `[2, 4]`       | 2               |
| `[4]`          | 4               |

The total sum is: 3×1+1×6+2×2+4×1=17 🎯🎯🎯

---

Instead of explicitly enumerating all subarrays and calculating the minimum, we determine **how many subarrays an element is the minimum in**. This depends on the position of the **Previous Smaller Element (PSE)** and the **Next Smaller Element (NSE)** for each element.

- **Left Contribution**: The subarrays that end at the current element where this element is the minimum.
- **Right Contribution**: The subarrays that start at the current element where this element is the minimum.

**Example for `[3, 1, 2, 4]`: 🔎🔎🔎**

- For `3`:

  - The nearest smaller element on the left is `None` (no such element exists).
  - The nearest smaller element on the right is `1` (at index 1).
  - Contribution: 1 subarray (`[3]`).

- For `1`:

  - The nearest smaller element on the left is `None`.
  - The nearest smaller element on the right is `None` (no smaller element exists).
  - Contribution: 6 subarrays (`[1]`, `[3, 1]`, `[1, 2]`, `[3, 1, 2]`, `[1, 2, 4]`, `[3, 1, 2, 4]`).

- For `2`:

  - The nearest smaller element on the left is `1`.
  - The nearest smaller element on the right is `None`.
  - Contribution: 2 subarrays (`[2]`, `[1, 2]`).

- For `4`:

  - The nearest smaller element on the left is `2`.
  - The nearest smaller element on the right is `None`.
  - Contribution: 1 subarray (`[4]`).

---

*Formula: 🌐🌐🌐*

For each element at index , we calculate:

*Left Contribution=i−PSE[i]−1*\
*Right Contribution=NSE[i]−i−1*

*Total Contribution=((left×right)+right)×arr[i]*

---

Here’s the Python code:

```python
def solve(n,arr):
    PSE=[-1]*n
    stack=[]
    for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
            stack.pop()
        if stack:
            PSE[i]=stack[-1]
        stack.append(i)
    NSE=[n]*n
    stack=[]
    for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
            index=stack.pop()
            NSE[index]=i
        stack.append(i)
    ans=0
    for i in range(n):
        left=i-PSE[i]-1
        right=NSE[i]-i
        ans+=((left*right+right)*arr[i])
    return ans
```

---

1. **Time Complexity**: O(N)

   - The PSE and NSE calculations both require a single pass through the array with a stack, making them O(N)  each.
   - The final loop to calculate the total sum is O(N)
   - Overall: O(N)

2. **Space Complexity**: O(1)

   - We use two arrays (`PSE` and `NSE`) of size  and a stack, leading to  space O(N)

--- ✨✨✨

###

**More Optimized Approach: 🏆🏆🏆**

Given the input sequence `A = [3, 1, 2, 5, 4]`, we can cycle through the array and write out all subarrays ending with the i-th element:

- `[3]`
- `[3, 1]`, `[1]`
- `[3, 1, 2]`, `[1, 2]`, `[2]`
- `[3, 1, 2, 5]`, `[1, 2, 5]`, `[2, 5]`, `[5]`
- `[3, 1, 2, 5, 4]`, `[1, 2, 5, 4]`, `[2, 5, 4]`, `[5, 4]`, `[4]`

We can denote by `result[i]` the sum of the minimum values of those subarrays ending with the i-th element. Here are the results:

- `3`
- `1 + 1`
- `1 + 1 + 2`
- `1 + 1 + 2 + 5`
- `1 + 1 + 2 + 4 + 4`

Result: `[3, 2, 4, 9, 12]` 🌟🌟🌟

---

**Observed Pattern: 🧪🧪🧪**

1. If `A[i-1] <= A[i]`, then:

   `result[i] = result[i-1] + A[i]`

   - This happens because subarrays ending with the i-th element are essentially the same as subarrays for the (i-1)-th element with the extra element `A[i]` added to each of them, plus one extra subarray `[A[i]]`.

2. Otherwise, if we find the previous less or equal value `A[j] <= A[i] (j < i)`, then:

   `result[i] = result[j] + A[i] * (i-j)`

   - This is because the subarrays ending with the i-th element can be divided into:
     - Subarrays starting from the previous less value `A[j]`.
     - Subarrays consisting of only elements after `j` up to `i`.

---

This forms the basis of the solution. We build a monotonously increasing stack to find the previous less or equal value and reuse its sum:

```python
class Solution:
    def solve(self, n, arr):
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            if stack:
                prevSmaller = stack[-1]
                result[i] = result[prevSmaller] + (i - prevSmaller) * arr[i]
            else:
                result[i] = (i + 1) * arr[i]
            stack.append(i)
        return sum(result)
```

---

1. **Time Complexity**: O(N)

   - Each element is pushed and popped from the stack exactly once.

2. **Space Complexity**: O(N)

   - The stack and result array both have space complexity O(N).

---


## **Largest Rectangle in Histogram** 🎨🎯✨

The task is to find the **largest rectangular area** that can be formed in a histogram represented by an array of integers `heights`. Each bar has a width of 1.

---

<img src="https://www.danielleskosky.com/wp-content/uploads/media-uploads/largest-rectangle/lr-figK.png">



**1. Brute Force Approach** 🚀📊📐

This is the simplest approach where we consider every bar height as the height of a potential rectangle and calculate the maximum possible area.

**Steps:**

1. For each bar `i`, find the first smaller bar to its left (`leftMin`).
2. Similarly, find the first smaller bar to its right (`rightMin`).
3. Calculate the width of the rectangle that can be formed using the bar `i`:
4. Calculate the area of the rectangle:
5. Update the maximum area if the current rectangle's area is larger.

**Code:**

```python
def bruteForce(n, arr):
    maxi = 0
    for i in range(n):
        # Find the first smaller bar to the left
        leftMin = -1
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                leftMin = j
                break
        
        # Find the first smaller bar to the right
        rightMin = n
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                rightMin = j
                break
        
        # Calculate width and area
        width = rightMin - leftMin - 1
        area = arr[i] * width
        maxi = max(maxi, area)
    return maxi
```

**Time Complexity: O(n^2)**\
**Space Complexity: O(1)**

---

**2. Better Approach (Using Precomputed Arrays for Left and Right Boundaries)** 📊🛠️💡

Here, we improve the brute force approach by precomputing the nearest smaller elements to the left (`PSE`) and to the right (`NSE`) for all bars.

**Steps:**

1. Precompute the nearest smaller element (NSE) to the right using a **monotonic stack**.
2. Precompute the previous smaller element (PSE) to the left using a **monotonic stack**.
3. For each bar, calculate:

   and the area:
4. Update the maximum area.

**Code:**

```python
def better(n, arr):
    PSE = [-1] * n  # Previous Smaller Element
    NSE = [n] * n   # Next Smaller Element
    stack = []
    
    # Calculate NSE for each bar
    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            index = stack.pop()
            NSE[index] = i
        stack.append(i)
    
    stack = []
    # Calculate PSE for each bar
    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            index = stack.pop()
        if stack:
            PSE[i] = stack[-1]
        stack.append(i)
    
    # Calculate maximum area
    maxi = 0
    for i in range(n):
        width = NSE[i] - PSE[i] - 1
        area = arr[i] * width
        maxi = max(maxi, area)
    
    return maxi
```

**Time Complexity: O(n)**\
**Space Complexity: O(n)**

---

**3. Optimized Approach (Single Stack Method)** 🏗️🔢✨

This approach uses a single monotonic stack to calculate the maximum rectangle area in one traversal.

**Steps:**

1. Traverse the histogram bars.
2. For each bar, pop elements from the stack while the current bar height is smaller than the height at the top of the stack.
3. For each popped element:
   - Calculate the rectangle height as the height of the popped bar.
   - Calculate the width:
     - Left boundary: The new top of the stack after popping, or -1 if the stack is empty.
     - Right boundary: The current index.
   - Calculate the area and update the maximum area.
4. After the traversal, process any remaining elements in the stack similarly.

**Code:**

```python
def optimized(n, arr):
    stack = []
    maxi = 0
    
    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            index = stack.pop()
            height = arr[index]
            leftMin = stack[-1] if stack else -1
            rightMin = i
            width = rightMin - leftMin - 1
            maxi = max(maxi, width * height)
        stack.append(i)
    
    while stack:
        index = stack.pop()
        height = arr[index]
        leftMin = stack[-1] if stack else -1
        rightMin = n
        width = rightMin - leftMin - 1
        maxi = max(maxi, width * height)
    
    return maxi
```

**Time Complexity: O(n)**\
**Space Complexity: O(n)**

---

---

## **Maximal Rectangle** 🌟📏📋

The maximal rectangle problem asks for the largest rectangle containing only `'1'`s in a binary matrix. This can be solved by treating each row of the matrix as the base of a histogram and using the **optimized approach**.

<img src="https://www.algotree.org/images/Binary_Matrix.svg">

**Steps:**

1. Preprocess the matrix to calculate histogram heights for each row:
   - If `matrix[i][j] == '1'`, the height is incremented by 1 from the row above.
   - Otherwise, the height is reset to 0.
2. For each row's histogram, use the `optimized` function to calculate the maximum area.
3. Track and return the global maximum area.

**Code:**

```python
def solve(n, m, matrix):
    # Preprocess the matrix to calculate histogram heights
    mat = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                if i == 0:
                    mat[i][j] = 1
                else:
                    mat[i][j] = 1 + mat[i-1][j]
    
    # Find the maximal rectangle for each row's histogram
    maxi = 0
    for i in range(n):
        ans = optimized(m, mat[i])
        maxi = max(maxi, ans)
    
    return maxi
```

**Example Usage:**

```python
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
n, m = 4, 5
print(solve(n, m, matrix))  # Output: 6
```

**Time Complexity:** O(n×m) \
**Space Complexity:** O(n×m)

This solution is efficient for larger binary matrices and leverages the histogram technique for maximal rectangles. 🌈✨📊

---

## **Next Greater Node In Linked List**🌐🌐🌐

You are given the head of a singly linked list with  nodes. For each node in the list, find the value of the next greater node. The next greater node for a given node is the first node after it with a strictly larger value.\
If no such node exists, the next greater node value is set to `0`.

Return an array `answer` where `answer[i]` is the value of the next greater node for the -th node (1-indexed).  🌐🌐🌐

---

**Sample Test Cases** 📊📊📊

**Test Case 1:**

**Input**: `head = [2, 1, 5]`\
**Output**: `[5, 5, 0]`\
**Explanation**:

- The next greater node for `2` is `5`.
- The next greater node for `1` is `5`.
- The next greater node for `5` does not exist, so it is `0`.

**Test Case 2:**

**Input**: `head = [2, 7, 4, 3, 5]`\
**Output**: `[7, 0, 5, 5, 0]`\
**Explanation**:

- The next greater node for `2` is `7`.
- The next greater node for `7` does not exist, so it is `0`.
- The next greater node for `4` is `5`.
- The next greater node for `3` is `5`.
- The next greater node for `5` does not exist, so it is `0`.  📊📊📊

---

**Intuition (in Simple Words)** 🧐🧐🧐

1. Use a **monotonic decreasing stack** to keep track of nodes whose next greater element is not yet found.
2. As you traverse the list:
   - If the current node's value is **greater** than the values in the stack, pop those nodes and update their next greater value in the result list.
   - If not, push the current node into the stack.
3. At the end of the traversal, the remaining nodes in the stack do not have any next greater nodes, so their result remains `0`.

The stack ensures we only process each node **once**, making it efficient.  🧐🧐🧐

---

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head):
    # Convert Linked List to an Array
    values = []
    while head:
        values.append(head.val)
        head = head.next
    
    n = len(values)
    ans = [0] * n  # Initialize result array with 0
    stack = []  # Stack to store indices of the values array
    
    for i in range(n):
        # Check for next greater elements in the stack
        while stack and values[i] > values[stack[-1]]:
            index = stack.pop()
            ans[index] = values[i]
        stack.append(i)  # Push current index to stack
    
    return ans
```


---

**Time and Space Complexity** ⏳⏳⏳

1. **Time Complexity**:  
   - Traversing the linked list: \( O(n) \)  
   - Each node is pushed and popped from the stack at most once: \( O(n) \)  
   **Overall**: \( O(n) \)

2. **Space Complexity**:  
   - Stack stores indices: \( O(n) \)  
   - Array `values` for storing the linked list values: \( O(n) \)  
   - Result array `ans`: \( O(n) \)  
   **Overall**: \( O(n) \)  ⏳⏳⏳

This approach is optimal for solving the problem. ⏳⏳⏳


---

## **Remove Nodes From Linked List**

✨✨✨

**Problem Statement**

You are given the head of a linked list. Your task is to remove every node from the linked list that has a node with a greater value to its right. Return the head of the modified linked list.

✨✨✨

---

**Input 1:**

```plaintext
head = [5, 2, 13, 3, 8]
```

**Output 1:**

```plaintext
[13, 8]
```

**Explanation:**

- Node `5` is removed because `13` is to its right.
- Node `2` is removed because `13` is to its right.
- Node `3` is removed because `8` is to its right.
- Nodes `13` and `8` are retained as there are no greater values to their right.

✨✨✨

---

**Input 2:**

```plaintext
head = [1, 1, 1, 1]
```

**Output 2:**

```plaintext
[1, 1, 1, 1]
```

**Explanation:**
Since all nodes have the same value, no nodes need to be removed.

✨✨✨

---

**Intuition**

✨✨✨

1. **Traverse the List Backwards:**

   - To efficiently determine whether a node has a greater value to its right, it's helpful to traverse the list from the end to the start.

2. **Use a Stack to Track Maximum Values:**

   - Use a stack to maintain a list of "valid" nodes that should remain in the list. As we traverse backward, if the current node's value is smaller than the top of the stack, it means the current node has a greater value to its right and should be removed.

3. **Build the New List:**

   - Once we identify the valid nodes using the stack, rebuild the linked list from these nodes.

✨✨✨

---

Here is an efficient Python implementation:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head):
    if not head:
        return None

    stack = []
    current = head

    # Traverse the linked list
    while current:
        # Remove nodes from the stack if their values are less than the current node's value
        while stack and stack[-1].val < current.val:
            stack.pop()
        stack.append(current)
        current = current.next

    # Build the new linked list from the stack
    dummy = ListNode(0)
    current = dummy
    for node in stack:
        current.next = node
        current = current.next

    # End the new linked list
    current.next = None

    return dummy.next
```

✨✨✨

---

**Time and Space Complexity**

✨✨✨

1. **Time Complexity:**

   - Each node is pushed and popped from the stack exactly once, resulting in an  time complexity where  is the number of nodes in the linked list.

2. **Space Complexity:**

   - The stack stores up to  nodes in the worst case, giving a space complexity of .

✨✨✨

---


 &#x20;**Steps to Make Array Non-decreasing**📚🌟✨

You are given a 0-indexed integer array `nums`. In one step, remove all elements `nums[i]` where `nums[i - 1] > nums[i]` for all . 📈🌟✨

Return the number of steps performed until `nums` becomes a non-decreasing array. 📈🌟✨

---

**Sample Test Cases** 📈🚀✨

Example 1 📈🌟✨

**Input:**\
`nums = [5,3,4,4,7,3,6,11,8,5,11]`\
**Output:**\
`3` 📈🌟✨

**Explanation:**

- Step 1: `[5,3,4,4,7,3,6,11,8,5,11]` becomes `[5,4,4,7,6,11,11]`.
- Step 2: `[5,4,4,7,6,11,11]` becomes `[5,4,7,11,11]`.
- Step 3: `[5,4,7,11,11]` becomes `[5,7,11,11]`.

The final array `[5,7,11,11]` is non-decreasing. 📈🌟✨

---

Example 2 📈🌟✨

**Input:**\
`nums = [4,5,7,7,13]`\
**Output:**\
`0` 📈🌟✨

**Explanation:**\
The array is already non-decreasing. 📈🌟✨

---

**Intuition** 🧐🌟✨

The key is understanding how elements are "eaten" by larger elements. The number of steps required depends on how many elements a larger number can eat while maintaining the correct order. 🧐🌟✨

Observations:

1. If a larger number comes before smaller numbers, it will "eat" all smaller numbers it can, but the smaller numbers will simultaneously "eat" the numbers smaller than themselves. 🧐🌟✨
2. This means the process happens in parallel, and we need to track the maximum "eating" steps required for any element. 🧐🌟✨

---

**Steps to Solve** 🔍🌟✨

1. **Maintain a Stack:** Use a stack to keep track of indices of elements in decreasing order from the back of the array. 🔍🌟✨

   - This helps us simulate the "eating" process efficiently. 🔍🌟✨

2. **Track Maximum Eating Steps:** Use an auxiliary array `maxEat` to track the number of steps each element takes to stabilize. 🔍🌟✨

   - If a larger element eats a smaller element, its eating count will depend on the count of the smaller element. 🔍🌟✨

3. **Update Maximum:** At each step, calculate the global maximum of eating steps required. 🔍🌟✨

---


```python
def solve(n, arr):
    stack = []
    maxEat = [0] * n
    maxi = 0
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            maxEat[i] = max(maxEat[i] + 1, maxEat[index])
        
        stack.append(i)
        maxi = max(maxi, maxEat[i])
    
    return maxi
```

---

**Time and Space Complexity** ⌛🌟✨

**Time Complexity:**

- O(n) : Each element is pushed and popped from the stack once. ⌛🌟✨

**Space Complexity:**

- O(n) : Stack and `maxEat` array require  space. ⌛🌟✨

---

**Explanation of the Example** 📊🌟✨

For `nums = [5,3,4,4,7,3,6,11,8,5,11]`: 📊🌟✨

1. **Initialization:**

   - `maxEat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` 📊🌟✨
   - `stack = []` 📊🌟✨

2. **Processing Elements:**\
   Traverse from the right to the left and update `maxEat` as elements "eat" others. 📊🌟✨

   **Step-by-step Updates:**

   - Process `11`: Push to `stack`.
   - Process `5`: No smaller elements to eat. Push to `stack`.
   - Process `8`: Eats `5`. Update `maxEat[8]`.
   - Continue... 📊🌟✨

   Final `maxEat` will indicate the maximum number of steps. 📊🌟✨

3. **Result:** The maximum in `maxEat` gives the result: `3`. 📊🌟✨

