<h2>Find the Largest element in an array</h2>
<p>Given an array ‘arr’ of size ‘n’ find the largest element in the array.</p>
<p><strong>Example : </strong></p>
<p>Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]</p>
<p>Output: 5</p>
<p>Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.</p>
<p><strong>Solution : </strong></p>
<p>This Problem Can be Solved In Several Approches</p>
<p><strong>BruteForce : </strong></p>
<p>Sort the given array in ascending order</p>
<p>Print last element in sorted array</p>

```python
def bruteForce(arr,n):
    arr.sort()
    return arr[n-1]
```

<p>Time Complexity: O(N*log(N))</p>
<p>Space Complexity: O(n)</p>

<p><strong>Optimized : </strong></p>
<p>Create a temporary variable (large) to track largest element</p>
<p>Loop through given array and check if current element greate than large , then update large to current element</p>
<p>After loop, we can get the large element in the array</p>

```python
def optimized(arr,n):
    large=arr[0]
    for i in range(1,n):
        current=arr[i]
        if(current>large):
            large=current
    return large
```

<p>Time Complexity: O(N)</p>
<p>Space Complexity: O(1)</p>

<h2>Check if an Array is Sorted</h2>
<p>You have been given an array ‘a’ of ‘n’ non-negative integers.You have to check whether the given array is sorted in the non-decreasing order or not.</p>
<p>Your task is to return 1 if the given array is sorted. Else, return 0.</p>
<p><strong>Example : </strong></p>
<p>Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]</p>
<p>Output: 1</p>
<p>The given array is sorted in non-decreasing order; hence the answer will be 1.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>BruteForce Approach : </strong></p>
<p>In This approach, we will compare each element with its all next elements</p>
<p>if current element is greater than any of its next member, then will return 0, since it is not sorted</p>
<p>if any element matches condition, then return 1</p>

```python
def bruteForce(arr,n):
    for i in range(n):
        for j in range(i,n):
            if(arr[i]>arr[j]):
                return 0
    return 1
```

<p>Time Complexity: O(N^2)</p>
<p>Space Complexity: O(1)</p>

<p><strong>Optimized : </strong></p>
<p>In This approach, we will just compare consecutive elements in the given array</p>
<p>As we know that for a sorted array the previous of every element is smaller than or equal to its current element</p>
<p>if any element is greater then next element, then we need to return 0</p>
<p>Otherwise return 1</p>

```python
def optimized(arr,n):
    for i in range(1,n):
        if(arr[i-1]>arr[i]):
            return 0
    return 1
```

<p>Time Complexity: O(N)</p>
<p>Space Complexity: O(1)</p>

<h2>Find Second Smallest and Second Largest Element in an array</h2>
<p>You have been given an array ‘a’ of ‘n’ unique non-negative integers.</p>
<p>Find the second largest and second smallest element from the array.</p>
<p>Return the two elements (second largest and second smallest) as another array of size 2.</p>
<p><strong>Example : </strong></p>
<p>Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]</p>
<p>Output: [4, 2]</p>
<p>The second largest element after 5 is 4, and the second smallest element after 1 is 2.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>

<p><strong>BruteForce Approach : </strong></p>
<p>In This Approach, First we will find the smallest and largest element in given array</p>
<p>Then, we will loop through given array </p>
<p>find small element and not equals to smallest element and find large element and not equals to largest element</p>

```python
def bruteForce(arr,n):
    smallest=arr[0]
    largest=arr[0]
    for i in range(1,n):
        if(arr[i]<smallest):
            smallest=arr[i]
        if(arr[i]>largest):
            largest=arr[i]
    second_smallest=float('inf')
    second_largest=float('-inf')
    for i in range(n):
        if(arr[i]<second_smallest and arr[i]!=smallest):
            second_smallest=arr[i]
        if(arr[i]>second_largest and arr[i]!=largest):
            second_largest=arr[i]
    if(second_smallest==float('inf')): # for array having same elements
        second_smallest=smallest
    if(second_largest==float('-inf')): # for array having same elements
        second_largest=largest
    return [second_smallest,second_largest]
```

<p>Time Complexity: O(N), We do two linear traversals in our array</p>
<p>Space Complexity: O(1)</p>

<p><strong>Optimized : </strong></p>
<p>In this appraoch, we will declare largest, second_larget, smallest, second_smallest variables</p>
<p>Then We will loop through given array elements.</p>
<p>if current element less than smallest, then update smallest with current and update second_smallest with smallest</p>
<p>if current element greater than largest, then update largest with current and update second_largest with largest</p>

```python
def optimized(arr,n):
    smallest,second_smallest=float('inf'),float('inf')
    largest,second_largest=float('-inf'),float('-inf')
    for i in range(n):
        if(arr[i]<smallest):
            second_smallest=smallest
            smallest=arr[i]
        elif(arr[i]<second_smallest and arr[i]!=smallest):
            second_smallest=arr[i]

        if(arr[i]>largest):
            second_largest=largest
            largest=arr[i]
        elif(arr[i]>second_largest and arr[i]!=largest):
            second_largest=arr[i]
            
    return [second_smallest,second_largest]
```

<p>Time Complexity: O(N), Single-pass solution</p>
<p>Space Complexity: O(1)</p>

<h2>Linear Search In Array</h2>
<p>Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.</p>
<p><strong>Example : </strong></p>
<p>Input: arr[]= 1 2 3 4 5, num = 3</p>
<p>Output: 2</p>
<p>Explanation: 3 is present in the 2nd index</p>
<p>Input: arr[]= 5 4 3 2 1, num = 5</p>
<p>Output: 0</p>
<p>Explanation: 5 is present in the 0th index</p>

<p><strong>Solution : </strong></p>
<p>We will loop through given array and compare each element with given num and if equals then return position</p>
<p>Otherwise, return -1</p>

```python
def solve(arr,n,num):
    for i in range(n):
        if(arr[i]==num):
            return i+1
    return -1
```

<p>TC : O(N)</p>
<p>SC : O(1)</p>

<h2>Left Rotate the Array by One</h2>
<p>Given an array 'arr' containing 'n' elements, rotate this array left once and return it.</p>
<p>Rotating the array left by one means shifting all elements by one place to the left and moving the first element to the last position in the array.</p>
<p><strong>Example : </strong></p>
<p>Input: 'a' = 5, 'arr' = [1, 2, 3, 4, 5]</p>
<p>Output: [2, 3, 4, 5, 1]</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p>The rotated array has just a difference that its first element is present at the last index of the array. So if we can just store the element at the first index and then shift all the elements towards the left and at last put the stored element at the last index. We will get th rotated array.</p>
<p><strong>Bruteforce Approach : </strong></p>
<p>In this approach, we will create a dummy array of given array size</p>
<p>We will add given array elements to dummy array by one index ahead , i.e from 2nd position</p>
<p>finally, we can add first element in last position of dummy</p>
<p>return dummy array as rotated array</p>
<img src="https://lh5.googleusercontent.com/8BuHbQZpYQm_rH6CxXtSGBWmSWlUMyv5dxZlBHzaSV2p-faShTFL2lKJMr4ijazihHO6ro8Q8zqVZdQ8UM2pTgNUyaBzp2-a2HgGSkNSiduily08ln1hMHnCQolaCn5jpCd8Mp_u">

```python
def bruteForce(arr,n):
    temp=[0]*n
    for i in range(1,n):
        temp[i-1]=arr[i]
    temp[n-1]=arr[0]
    return temp
```

<p>Time Complexity: O(n), as we iterate through the array only once.</p>
<p>Space Complexity: O(n) as we are using another array of size, same as the given array.</p>

<p><strong>Optimized : </strong></p>
<p>In this approach, first we will store arr[0] element in temp variable</p>
<p>then we will loop into array untill n-1 position</p>
<p>We will assign current element to its next element</p>
<p>finally, we will update last element with temp</p>
<p>then return arr as rotated arrays</p>

```python
def optimized(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
    return arr
```

<p>Time Complexity: O(n), as we iterate through the array only once.</p>
<p>Space Complexity: O(1) as no extra space is used</p>

<h2>Count Maximum Consecutive One's in the array</h2>
<p>Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.</p>
<p><strong>Example </strong></p>
<p>Input: prices = {1, 1, 0, 1, 1, 1}</p>
<p>Output: 3</p>
<p>Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.</p>
<p>Input: prices = {1, 0, 1, 1, 0, 1} </p>
<p>Output: 2</p>
<p>Explanation: There are two consecutive 1's in the array.</p>

<p><strong>Solution : </strong></p>
<p>We need to find length longest consecutive one's</p>
<p>We will create two varibales</p>
<p>currentCount->to find length of consecutive one's</p>
<p>maxCount -> this stores max of lengths of consecutive one's</p>
<p>Start loop from beginning of given array</p>
<p>if current element is equal to one then increase currentCount by one</p>
<p>if not equal to 1, then set currentCount to zero</p>
<p>for each iteration, update maxCount with max(maxCount,currentCount)</p>
<p>finally, return maxCount as answer</p>

```python
def solve(arr,n):
    currentCount=0
    maxCount=0
    for i in range(n):
        if(arr[i]==1):
            currentCount+=1
        else:
            currentCount=0
        maxCount=max(maxCount,currentCount)
    return maxCount
```

<p>TC : O(N)</p>
<p>SC : O(1)</p>

<h2>Move all Zeros to the end of the array</h2>
<p>Given an array 'arr' of 'n' non-negative integers, your task is to move all the zeros to the end of the array while keeping the non-zero elements at the start of the array in their original order. Return the modified array.</p>
<p><strong>Example : </strong></p>
<p>Input: ‘n’ = 5, ‘arr’ = [1, 2, 0, 0, 2, 3]</p>
<p>Output: [1, 2, 2, 3, 0, 0]</p>
<p>Explanation: Moved all the 0’s to the end of an array, and the rest of the elements retain the order at the start.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>BruteForce Solution : </strong></p>
<p>In This approach, first we will store all non zero values in temp array</p>
<p>Then, we can update this temp array to starting of original array</p>
<p>them we can update remaining places with zero</p>

```python
def bruteForce(arr,n):
    temp=[]
    for i in range(n):
        if(arr[i]!=0):
            temp.append(arr[i])
    nz=len(temp)
    
    for i in range(nz):
        arr[i]=temp[i]
        
    for i in range(nz,n):
        arr[i]=0
    return arr
```

<p>Time Complexity: O(N) + O(X) + O(N-X) ~ O(2*N), where N = total no. of elements</p>
<p>Space Complexity: O(N), as we are using a temporary array to solve this problem and the maximum size of the array can be N in the worst case.</p>

<p><strong>Optimized Solution : </strong></p>
<p>In this, We can optimize the approach using 2 pointers i.e. i and j. The pointer j will point to the first 0 in the array and i will point to the next index.</p>
<p>Assume, the given array is {1, 0, 2, 3, 2, 0, 0, 4, 5, 1}. Now, initially, we will place the 2-pointers like the following</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/06/Screenshot-2023-06-26-162005.png">
<p><strong>Steps To Solve : </strong></p>
<ul>
	<li>First, using a loop, we will place the pointer j. If we don’t find any 0, we will not perform the following steps.</li>
	<li>After that, we will point i to index j+1 and start moving the pointer using a loop.</li>
	<li>While moving the pointer i, we will do the following:</li>
	<ul>
		<li>If a[i] != 0 i.e. a[i] is a non-zero element: We will swap a[i] and a[j]. Now, the current j is pointing to the non-zero element a[i]. So, we will shift the pointer j by 1 so that it can again point to the first zero.</li>
	</ul>
	<li>Finally, our array will be set in the right manner.</li>
</ul>
<img src="https://static.takeuforward.org/wp/uploads/2023/06/Screenshot-2023-06-26-162339.png">

```python
def optimized(arr,n):
    j=-1
    for i in range(n):
        if(arr[i]==0):
            j=i
            break
    if(j==-1):
        return arr
    for i in range(j+1,n):
        if(arr[i]!=0):
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
```

<p>Time Complexity: O(N), N = size of the array.Reason: We have used 2 loops and using those loops, we are basically traversing the array once.</p>
<p>Space Complexity: O(1) as we are not using any extra space to solve this problem.</p>

<h2>Rotate array by K elements</h2>
<p>Given an array of integers, rotating array of elements by k elements either left or right.</p>
<p><strong>Example : </strong></p>
<p>Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right</p>
<p>Output: 6 7 1 2 3 4 5</p>
<p>Explanation: array is rotated to right by 2 position .</p>
<p>Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left </p>
<p>Output: 9 10 11 3 7 8</p>
<p>Explanation: Array is rotated to left by 3 position.</p>

<p><strong>BruteForce : </strong></p>
<p>We know that, how to shift array by one position as discussed above</p>
<p>we can perform same operation k times on the same array</p>
<p>so, we can get array rotated by k times</p>

```python
def bruteForceLeftShift(arr,n,k):
    for j in range(k):
        temp=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp
    return arr

def bruteForceRightShift(arr,n,k):
    for j in range(k):
        temp=arr[n-1]
        for i in range(n-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
    return arr
```

<p>TC : O(N*N)</p>
<p>SC : O(1)</p>

<p><strong>Better : </strong></p>
<p><strong>For Right Shift : </strong></p>
<p>First, we will store last k elements in temp array</p>
<p>Then, we will shift , n-k elements to its right position from starting position</p>
<p>Then, we will fill up first k positions with temp elements</p>

```python
def betterRightShift(arr,n,k):
    temp=[]
    k=k%n
    for i in range(n-k,n):
        temp.append(arr[i])
    for i in range(n-1,n-k-1,-1):
        arr[i]=arr[i-k]
    j=0
    for i in range(k):
        arr[i]=temp[j]
        j+=1
    return arr
```

<p>TC : O(N)</p>
<p>SC : O(N)</p>

<p><strong>For Left Shift : </strong></p>
<p>First, we will store first k elements in temp array</p>
<p>Then, we will shift , n-k elements to its left position from end position</p>
<p>Then, we will fill up last k positions with temp elements</p>

```python
def betterLeftShift(arr,n,k):
    temp=[]
    k=k%n
    for i in range(k):
        temp.append(arr[i])
    for i in range(k,n):
        arr[i-k]=arr[i]
    j=0
    for i in range(n-k,n):
        arr[i]=temp[j]
        j+=1
    return arr
```

<p>TC : O(N)</p>
<p>SC : O(N)</p>

<h2>Remove Duplicates from Sorted Array</h2>
<p>Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.</p>
<p>If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.</p>
<p>Note: Return k after placing the final result in the first k slots of the array.</p>
<p><strong>Example : </strong></p>
<p>Input: arr = [1,1,2,2,2,3,3]</p>
<p>Output: arr[1,2,3]</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several ways</p>
<p><strong>BruteForce : </strong></p>
<p>In this approach, create a set</p>
<p>loop through given elements and add elements to set</p>
<p>since set doesn't stores any duplicate values, it stores only non-duplocate values</p>
<p>update array by set elements</p>
<p>return array</p>

```python
def bruteForce(arr,n):
    temp=set()
    for i in arr:
        temp.add(i)
    k=len(temp)
    j=0
    for i in temp:
        arr[j]=i
        j+=1
    return arr
```

<p>Time complexity: O(n*log(n))+O(n)</p>
<p>Space Complexity: O(n)</p>

<p><strong>Optimized Solution : </strong></p>
<p>In this approach, we will iterate through given array and modify the array by certain conditions using two pointers approach</p>
<ul>
	<li>Take a variable i as 0</li>
	<li>Use a for loop by using a variable ‘j’ from 1 to length of the array.</li>
	<li>If arr[j] != arr[i], increase ‘i’ and update arr[i] == arr[j].</li>
	<li>After completion of the loop return i+1, i.e size of the array of unique elements.</li>
</ul>
<img src="https://lh6.googleusercontent.com/D1_q-K0TApMsT9iQeH6dteFiDaxAIRoZ6hzcUvaTzolo9UwhBzUuEm7kBZGDlJFIQREch1n4nh0tq1y61qOG7YsLwkECdZnhBRdEmWdMFWVd8n4mk5HGQfbMgRFMmMzaT75OGoCN">

```python
def optimized(arr,n):
    i=0
    for j in range(1,n):
        if(arr[j]!=arr[i]):
            i+=1
            arr[i]=arr[j]
    return arr
```

<p>Time Complexity: O(N)</p>
<p>Space Complexity: O(1)</p>

<h2>Find the missing number in an array</h2>
<p>Given an array ‘a’ of size ‘n’-1 with elements of range 1 to ‘n’. The array does not contain any duplicates. Your task is to find the missing num</p>
<p><strong>Example : </strong></p>
<p>Input : 'a' = [1, 2, 4, 5], 'n' = 5</p>
<p>Output : 3</p>
<p>Explanation: 3 is the missing value in the range 1 to 5.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches.</p>
<p><strong>Bruteforce Approach : </strong></p>
<p>In This approach, we will loop through each element from 1 to n and check if existed in given array</p>
<p>if any element not found in given array, return as answer</p>
<p>if every element existed, then return -1</p>

```python
def bruteForce(arr,n):
    for i in range(1,n+1):
        flag=False
        for j in arr:
            if(j==i):
                flag=True
                break
        if(flag==False):
            return i
    return -1
```

<p>Time Complexity: O(N2), where N = size of the array+1.</p>
<p>Reason: In the worst case i.e. if the missing number is N itself, the outer loop will run for N times, and for every single number the inner loop will also run for approximately N times. So, the total time complexity will be O(N2).</p>

<p>Space Complexity: O(1)  as we are not using any extra space.</p>

<p><strong>Better Approach : </strong></p>
<p>In this approach, we store each array element in an hashmap</p>
<p>Then we will check each integer from 1 to N, if it is there in hashmap or not, if not return it as answer</p>

```python
def better(arr,n):
    visited={}
    for i in arr:
        visited[i]=True
    for i in range(1,n+1):
        if(not visited.get(i)):
            return i
    return -1
```

<p>Time Complexity: O(N) + O(N) ~ O(2*N),  where N = size of the array+1.</p>
<p>Space Complexity: O(N), where N = size of the array+1. Here we are using an extra hash array of size N+1.</p>

<p><strong>Optimized Approach : </strong></p>
<p>In this approach, first we will find the sum given array elements</p>
<p>We can also find sum of first n integers using formula</p>
<p>We can take differnce between given Array sum and actual sum with n integers, this will give the answee</p>

```python
def optimal(arr,n):
    givenSum=0
    for i in arr:
        givenSum+=i
    expSum=((n*(n+1))//2)
    return expSum-givenSum
```

<p>TC : O(N)</p>
<p>SC : O(1)</p>

<h2><strong>Optimized Appraoch 2 : </strong></h2>
<p>In this approach, we can xor of given array elements and expected 1 to N integers</p>
<p>We know that, xor of same elements will be zero</p>
<p>We know that, xor of element and zero will be element</p>
<p>So that, all numbers which are exited will be calculated as zero, so missed number will be the answer</p>


```python
def optimal2(arr,n):
    xor1=0
    xor2=0
    for i in range(n-1):
        xor1=xor1^arr[i]
        xor2=xor2^(i+1)
    xor2=xor2^(n)
    return xor1^xor2
```

<p>TC : O(N)</p>
<p>SC : O(1)</p>

<h2>Find the number that appears once, and the other numbers twice</h2>
<p>You are given a sorted array 'arr' of positive integers of size 'n'.</p>
<p>It contains each number exactly twice except for one number, which occurs exactly once.</p>
<p>Find the number that occurs exactly once.</p>
<p><strong>Example : </strong></p>
<p>Input: ‘arr’ = {1, 1, 2, 3, 3, 4, 4}.</p>
<p>Output: 2</p>
<p>Explanation: 1, 3, and 4 occur exactly twice. 2 occurs exactly once. Hence the answer is 2.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>BruteForce Solution : </strong></p>
<p>In this apporach, simply we will create a hashmap and stores count of occurances of each number in given array</p>
<p>Then, we can check if any number count equals to 1, then that is the answer</p>

```python
def bruteForce(arr,n):
    count={}
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i,j in count.items():
        if(j==1):
            return i
    return -1
```

<p>TC : O(N)</p>
<p>SC : O(N)</p>

<p><strong>Optimized Solution : </strong></p>
<p>As discussed in above problem, we can simply apply xor to all elements</p>
<p>Then, resultant will be single element only</p>

```python
def optimized(arr,n):
    xor=0
    for i in arr:
        xor=xor^i
    return xor
```

<p>TC : O(N)</p>
<p>SC : O(1)</p>

<h2>Union of Two Sorted Arrays</h2>
<p>Given two sorted arrays, ‘a’ and ‘b’, of size ‘n’ and ‘m’, respectively, return the union of the arrays.</p>
<p>The union of two sorted arrays can be defined as an array consisting of the common and the distinct elements of the two arrays. The final array should be sorted in ascending order</p>
<p>Note: 'a' and 'b' may contain duplicate elements, but the union array must contain unique elements.</p>
<p><strong>Example:</strong></p>
<p>Input: ‘n’ = 5 ‘m’ = 3</p>
<p>‘a’ = [1, 2, 3, 4, 6]</p>
<p>‘b’ = [2, 3, 5]</p>
<p>Output :  [1, 2, 3, 4, 5, 6]</p>
<p>Explanation: Common elements in ‘a’ and ‘b’ are: [2, 3]</p>
<p>Distinct elements in ‘a’ are: [1, 4, 6]</p>
<p>Distinct elements in ‘b’ are: [5]</p>
<p>Union of ‘a’ and ‘b’ is: [1, 2, 3, 4, 5, 6]</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solve in several approaches</p>
<p><strong>BruteForce Approach : </strong></p>
<p>In this approach, simply will create an set data structure</p>
<p>We can iterate through both arrays, add elements to set</p>
<p>Since, set won't store the duplicates, that will be our final answer</p>

```python
def bruteForce(arr1,arr2):
    s=set()
    for i in arr1:
        s.add(i)
    for j in arr2:
        s.add(j)
    return list(s)
```

<p>Time Compleixty : O( (m+n)log(m+n) ) . Inserting an element in a set takes logN time, where N is no of elements in the set. At max set can store m+n elements {when there are no common elements and elements in arr,arr2 are distntict}. So Inserting m+n th element takes log(m+n) time. Upon approximation across inserting all elements in worst, it would take O((m+n)log(m+n) time.</p>
<p>Space Complexity : O(m+n) {If Space of Union ArrayList is considered} </p>
<p>O(1) {If Space of union ArrayList is not considered}</p>

<p><strong>Optimized approach : </strong></p>
<p>Since, The arrays arr1 and arr2 are sorted , we solve using two pointers approach</p>
<ul>
    <li>Take two pointers let’s say i,j pointing to the 0th index of arr1 and arr2.</li>
    <li>Create an empty vector for storing the union of arr1 and arr2.</li>
    <li>From solution 2 we know that the union is nothing but the distinct elements in arr1 + arr2 </li>
    <li>Let’s traverse the arr1 and arr2 using pointers i and j and insert the distinct elements found into the union vector.</li>
</ul>
<p>While traversing we may encounter three cases.</p>
<ul>
    <li>arr1[ i ] == arr2[ j ]</li>
    <p>Here we found a common element, so insert only one element in the union. Let’s insert arr[i] in union and increment i.</p>
    <p>NOTE: There may be cases like the element to be inserted is already present in the union, in that case, we are inserting duplicates which is not desired. So while inserting always check whether the last element in the union vector is equal or not to the element to be inserted. If equal we are trying to insert duplicates, so don’t insert the element, else insert the element in the union. This makes sure that we are not inserting any duplicates in the union because we are inserting elements in sorted order.</p>
    <li>arr1[ i ]  < arr2[ j ]</li>
    <p>arr1[ i ] < arr2[ j ] so we need to insert arr1[ i ] in union.IF last element in  union vector is not equal to arr1[ i ],then insert in union else don’t insert. After checking Increment i.</p>
    <li>arr1[ i ] > arr2[ j ]</li>
    <p>arr1[ i ] > arr2[ j ] so we need to insert arr2[ j ] in union. IF the last element in the union vector is not equal to arr2[ j ], then insert in the union, else don’t insert. After checking Increment j. After traversing if any elements are left in arr1 or arr2 check for condition and insert in the union.</p>
</ul>
<p>finally return union array</p>

```python
def optimized(arr1,arr2):
    n1,n2=len(arr1),len(arr2)
    i,j=0,0
    union=[]
    while i<n1 and j<n2:
        if(arr1[i]==arr2[j]):
            if(len(union)==0 or arr1[i]!=union[-1]):
                union.append(arr1[i])
            i+=1
        elif(arr1[i] < arr2[j]):
            if(len(union)==0 or arr1[i]!=union[-1]):
                union.append(arr1[i])
            i+=1
        elif(arr1[i] > arr2[j]):
            if(len(union)==0 or arr2[j]!=union[-1]):
                union.append(arr2[j])
            j+=1
    while i<n1:
        if(len(union)==0 or arr1[i]!=union[-1]):
            union.append(arr1[i])
        i+=1
    while j<n2:
        if(len(union)==0 or arr2[j]!=union[-1]):
            union.append(arr2[j])
        j+=1
    return union
```

<p>Time Complexity: O(m+n), Because at max i runs for n times and j runs for m times. When there are no common elements in arr1 and arr2 and all elements in arr1, arr2 are distinct. </p>
<p>Space Complexity : O(m+n) {If Space of Union ArrayList is considered} </p>
<p>O(1) {If Space of union ArrayList is not considered}</p>


<h2>Two Sum : Check if a pair with given sum exists in Array</h2>
<p>Given an array of integers arr[] and an integer target.</p>
<p>Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.</p>
<p>ou are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.</p>

<p><strong>Example :</strong></p>
<p>Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14</p>
<p>Result: YES</p>
<p>Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.</p>

<p>Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15</p>
<p>Result: NO</p>
<p>Explanation: There exist no such two numbers whose sum is equal to the target.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>Bruteforce Approach : </strong></p>
<p>In this approach, first we will loop through given array</p>
<p>for each element, we will loop through remaining elements</p>
<p>We will check sum of two elements of main loop element and nested loop element</p>
<p>if sum equals to target, then return "YES"</p>
<p>if non sum equals to given sum, then return "NO"</p>

```python
def bruteForce(arr,n,target):
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]+arr[j]==target):
                return "YES"
    return "NO"
```

<p>Time Complexity: O(N2), where N = size of the array.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Better Approach : </strong></p>
<p>Basically, in the previous approach we selected one element and then searched for the other one using a loop. Here instead of using a loop, we will use the HashMap to check if the other element i.e. target-(selected element) exists.</p>
<p>create a hashmap</p>
<p>Loop through given array, and store each element in given array</p>
<p>Check remaining_sum=target-current_element in map</p>
<p>if remaining sum exists map, then return "YES</p>
<p>if not found and loop ends, then return "NO </p>

```python
def better(arr,n,target):
    hashMap={}
    for i in range(n):
        current=arr[i]
        required=target-arr[i]
        if(hashMap.get(required)!=None):
            return "YES"
        hashMap[current]=i
    return "NO"
```

<p>Time Complexity: O(N), where N = size of the array.</p>
<p>Space Complexity: O(N) as we use the map data structure.</p>

<p><strong>Optimized Approach : </strong></p>
<p> In this approach, we will first sort the array and will try to choose the numbers in a greedy way.</p>
<p>We will keep a left pointer at the first index and a right pointer at the last index.</p>
<p>Now until left < right, we will check the sum of arr[left] and arr[right]. </p>
<p>Now if the sum < target, we need bigger numbers and so we will increment the left pointer. </p>
<p> But if sum > target, we need to consider lesser numbers and so we will decrement the right pointer.</p>
<p>If sum == target we will return either “YES”.
But if the left crosses the right pointer, we will return “NO”.</p>

```python
def optimized(arr,n,target):
    arr.sort()
    left,right=0,n-1
    while left<right:
        temp=arr[left]+arr[right]
        if(temp==target):
            return "YES"
        if(temp<target):
            left+=1
        else:
            right-=1
    return "NO"
```

<p>Time Complexity: O(N) + O(N*logN), where N = size of the array.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<h2>Search in a sorted 2D matrix</h2>
<p>You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. </p>
<p>The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists). </p>
<p>You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.</p>

<p><strong>Example : </strong></p>
<p> N = 3, M = 4, target = 8</p>
<p>mat[] =</p>
<p>1 2 3 4</p>
<p>5 6 7 8</p> 
<p>9 10 11 12</p>

<p>Result : True</p>

<p>Explanation:The ‘target’  = 8 exists in the 'mat' at index (1, 3).</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches.</p>
<p><strong>BruteForce Approach : </strong></p>
<p>In this approach, we will loop through each element and given matrix</p>
<p>We can compare each element and if any element matches , then return True</p>
<p>If none matches, then return False</p>

```python
def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    # traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    return False
```
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print("true" if result else "false")
```

<p>Time Complexity: O(N X M), where N = given row number, M = given column number.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Better Approach : </strong></p>
<p>In this approach, we will loop through each row in given matrix</p>
<p>We can apply binary search to find target in the row</p>
<p>In this way, we can check target in the matrix</p>


```python
def binarySearch(nums, target):
    n = len(nums) # size of the array
    low, high = 0, n - 1

    # Perform the steps:
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if matrix[i][0] <= target <= matrix[i][m - 1]:
            return binarySearch(matrix[i], target)
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print("true" if result else "false")

```


<p>Time Complexity: O(N + logM), where N = given row number, M = given column number.</p>
<p>Reason: We are traversing all rows and it takes O(N) time complexity. But for all rows, we are not applying binary search rather we are only applying it once for a particular row. That is why the time complexity is O(N + logM) instead of O(N*logM).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Optimized Approach : </strong></p>
<p>In this approach, we will represent the 2D mtarix ad 1D Array hypothetically</p>
<p>Then we will apply binary search algorithm to find the target</p>

```python
def optimized(mat,n,m,target):
    low=0
    high=(n*m)-1
    while low<=high:
        mid=(low+high)//2
        row,col=mid//m , mid%m
        if(mat[row][col]==target):
            return True
        elif(mat[row][col]<target):
            low=mid+1
        else:
            high=mid-1
    return False
```

<p>Time Complexity: O(log(NxM)), where N = given row number, M = given column number.</p>
<p>Reason: We are applying binary search on the imaginary 1D array of size NxM.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<h2>Leaders in an Array : Greater than all of the elements on its right side in the array.</h2>
<p>There is an integer array ‘a’ of size ‘n’.</p>
<p>An element is called a Leader Element if it is greater than all the elements present to its right.</p>
<p>You must return an array all Leader Elements in the array ‘a’.</p>
<p>The last element of the array is always a Leader Element. </p>
<p><strong>Example : </strong></p>
<p>Input: a = [1, 2, 3, 2], n = 4</p>
<p>Output: 2 3</p>
<p>Explanation : </p>
<p>a[ 2 ] = 3 is greater than a[ 3 ]. Hence it is a Superior Element. </p>
<p>a[ 3 ] = 2 is the last element. Hence it is a Superior Element.</p>
<p>The final answer is in sorted order.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in different approaches</p>
<p><strong>BruteForce Approach : </strong></p>
<p>In this approach, we will loop through given array</p>
<p>For Each element, we will check all its right elements, if all elements are less than current element</p>
<p>Then it is leader, we will add that element to final answer</p>

```python
def bruteForce(arr,n):
    final=[]
    for i in range(n):
        flag=True
        for j in range(i+1,n):
            if(arr[j]>=arr[i]):
                flag=False
                break
        if(flag):
            final.append(arr[i])
    final.sort()
    return final
```

<p>TC : O(N^2)</p>
<p>SC : O(1)</p>

<p><strong>Optimized Approach : </strong></p>
<p>In this approach, we will iterate in reverse of array</p>
<p>We will track max element from last</p>
<p>if current element is greater than maxi, the update maxi and add current element to final list</p>
<p>if current element is greater than maxi means, it is greater than all to its right elements,since maxi is maximum all its right</p>

```python
def optimized(arr,n):
    maxi=arr[n-1]
    final=[maxi]
    for i in range(n-1,-1,-1):
        if(arr[i]>maxi):
            maxi=arr[i]
            final.append(arr[i])
    final.sort()
    return final
```

<p>TC : O(N)</p>
<p>SC : O(1)</p>

<h2>Spiral Traversal of Matrix</h2>
<p>You are given a 2D matrix ‘MATRIX’ of ‘N’*’M’ dimension. You have to return the spiral traversal of the matrix</p>
<p><strong>Example:</strong></p>
<p>Input:</p>
<p>MATRIX = [ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60] ]</p>
<p>Output:</p>
<p>1 3 5 7 20 60 34 30 23 10 11 16</p>

<img src="https://lh5.googleusercontent.com/hZPzGMsKGm29AE34ZtOii2D76g2_M0mXxbnceTnuxSyodzJTUSYWJz3umCeyEWMas0OtAQVWE17WEDSQ_nbg6B_7m1mFyNfmzsN34GDhQjHDa4eV20u1wG4mBjPefJyRU53fAAe5hFQ2ZYChxw">

<p><strong>Solution : </strong></p>
<p>In this approach, we will be using four loops to print all four sides of the matrix.</p>
<ul>
    <li>1st loop: This will print the elements from left to right.</li>
    <li>2nd loop: This will print the elements from top to bottom.</li>
    <li>3rd loop: This will print the elements from right to left.</li>
    <li>4th loop: This will print the elements from bottom to top.</li>
</ul>

<img src="https://lh4.googleusercontent.com/Xq3R-xwSRxUx3EEjKQIMaHTM9qGqj81nPFe2nGoSnxnd36bStjU989Sf-CsWAnFZf4jHS68xr4l49QqKXeo7o7lLF1V38SJYaxC1CWWNzvk-eBNevdWhduS6mBSX9QGXGATwQw0OkFXkP18JWw">

<ul>
    <li>Create and initialize variables top as starting row index, bottom as ending row index left as starting column index, and right as ending column index. As shown in the image given below.</li>
    <li>In each outer loop traversal print the elements of a square in a clockwise manner.</li>
    <li>Print the top row, i.e. Print the elements of the top row from column index left to right and increase the count of the top so that it will move to the next row.</li>
    <li>Print the right column, i.e. Print the rightmost column from row index top to bottom and decrease the count of right.</li>
    <li>Print the bottom row, i.e. if top <= bottom, then print the elements of a bottom row from column right to left and decrease the count of bottom</li>
    <li>Print the left column, i.e. if left <= right, then print the elements of the left column from the bottom row to the top row and increase the count of left.</li>
    <li>Run a loop until all the squares of loops are printed.</li>
</ul>
<p>Note: As we can see in the code snippet below, two edge conditions are being added in the last two ‘for’ loops: when we are moving from right to left and from bottom to top. </p>
<p>These conditions are added to check if the matrix is a single column or a single row. So, whenever the elements in a single row are traversed they cannot be traversed again backward so the condition is checked in the right-to-left loop. When a single column is present, the condition is checked in the bottom-to-top loop as elements from bottom to top cannot be traversed again.</p>

```python
def solve(matrix,n,m):
    left,right=0,m-1
    top,bottom=0,n-1
    final=[]
    while(left<=right and top<=bottom):
        for i in range(left,right+1):
            final.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            final.append(matrix[i][right])
        right-=1
        if(top<=bottom):
            for i in range(right,left-1,-1):
                final.append(matrix[bottom][i])
            bottom-=1
        if(left<=right):
            for i in range(bottom,top-1,-1):
                final.append(matrix[i][left])
            left+=1
    return final
```

<p>Time Complexity: O(m x n)</p>
<p>Space Complexity: O(n) </p>


<h2>Rotate Matrix By 90 degrees ClockWise</h2>
<p>You are given a square matrix ‘Mat’ of size ‘N’. You need to rotate ‘Mat’ by 90 degrees in the clockwise direction</p>
<p>You must rotate the matrix in place, i.e., you must modify the given matrix itself. You must not allocate another square matrix for rotation.s</p>
<p><strong>Example : </strong></p>
<p>‘N’ = 2 and ‘Mat’ = {{1, 2}, {3, 4}}, we must modify ‘Mat’ to {{3, 1}, {4, 2}}.</p>
<p>Input : </p>
<pre>
1 2 3
4 5 6
7 8 9
</pre>
<p>Output : </p>
<pre>
7 4 1
8 5 2
9 6 3
</pre>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches : </p>
<p><strong>BruteForce Approach :</strong></p>
<p>Take another dummy matrix of n*n, and then take the first row of the matrix and put it in the last column of the dummy matrix, take the second row of the matrix, and put it in the second last column of the matrix and so.</p>
<p>In This approach, just we will place matrix elements in required places</p>

```python
def bruteForce(matrix,n,m):
    final=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(n):
            final[j][n-i-1]=matrix[i][j]
    return final
```

<p>TC : O(N*M)</p>
<p>SC : O(N*M)</p>

<p><strong>Optimized Approach : </strong></p>
<p>By observation, we see that the first column of the original matrix is the reverse of the first row of the rotated matrix</p>
<p>so that’s why we transpose the matrix and then reverse each row, and since we are making changes in the matrix itself space complexity gets reduced to O(1).</p>
<p>Transpose the matrix.(transposing means changing columns to rows and rows to columns)</p>
<p>Reverse each row of the matrix.</p>

<p>Transpose of a matrix is obtained by changing rows to columns and columns to rows. In other words, transpose of A[][] is obtained by changing A[i][j] to A[j][i]. </p>
<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/matrix-transpose.jpg">


```python
def optimized(matrix,n,m):
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i]=matrix[i][::-1]
    return matrix
```

<p>TC : O(N*M)</p>
<p>SC : O(1)</p>


<h2>Stock Buy And Sell</h2>
<p>You are given an array of prices where prices[i] is the price of a given stock on an ith day.</p>
<p>You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock</p>
<p>Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.</p>
<p>You can buy and sell the stock only once.You can’t sell without buying first.</p>
<p><strong>Example : </strong></p>
<p>For the given array [ 2, 100, 150, 120],</p>
<p>The maximum profit can be achieved by buying the stock at minute 0 when its price is Rs. 2 and selling it at minute 2 when its price is Rs. 150.</p>
<p>So, the output will be 148.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>Bruteforce Approach : </strong></p>
<p>In this approach, We will loop through given array and consider each elment as buy stock</p>
<p>And, again loop thorough remaining elements, try to sell at each price</p>
<p>Get max out of possible scenarios</p>
<ul>
    <li>Use a for loop of ‘i’ from 0 to n.</li>
    <li>Use another for loop of j from ‘i+1’ to n.</li>
    <li>let's say, buy=arr[i] and sell=arr[j]</li>
    <li>If sell > buy , take the difference and compare  and store it in the profit variable.</li>
    <li>Return profit.</li>
</ul>

<img src="https://lh3.googleusercontent.com/5Iu4UFZnIzSqBK3wcGL_1jgfWCPc5xA9Et5B1pZ7FMft0K6jGmvSQVcRomUALDccPiqLb9NMoKwlpkqil1Z5aYmaxE8N2spKCNpGqrFywqah6EKa5DLEYmPYXeBsXEjRMqYcyiAf">


```python
def bruteForce(arr,n):
    profit=0
    for i in range(n):
        for j in range(i+1,n):
            buy=arr[i]
            sell=arr[j]
            if(sell > buy):
                profit=max(profit,(sell-buy))
    return profit
```

<p>TC : O(N^2)</p>
<p>SC : O(1)</p>

<p><strong>Optimized Appraoch : </strong></p>
<p>In this approach , We will loop through given array and track minimum value in mini till current value</p>
<p>Then, we will consider current item as sell stock and mini value as buy stock</p>
<p>If sell > buy, then we will update profit</p>
<p>then, we will update mini, if current item less than mini</p>

<img src="https://lh3.googleusercontent.com/Zwj-rUiRi1lK2BKJWV1CGMnaL9V1enNIJ4sarYszDc_J966Fi0KJwi1cQ1bxrQ74nf5eWkdau4AlEwreBEUqiNSRAe-ElC3R1ZicJpK-BVDW8aZJCIRb__oB15g6TQg9r-PLI5UZ">

```python
def optimized(arr,n):
    mini=arr[0]
    profit=0
    for i in range(1,n):
        if(arr[i] > mini):
            profit=max(profit,arr[i]-mini)
        mini=min(mini,arr[i])
    return profit
```

<p>TC : O(N)</p>
<p>SC : O(1)</p>

<h2>Rearrange the array in alternating positive and negative items</h2>
<p>There is an array ‘A’ of size ‘N’ with an equal number of positive and negative elements.</p>
<p>Without altering the relative order of positive and negative numbers, you must return an array of alternative positive and negative values.</p>
<p>Start the array with a positive number. </p>
<p><strong>Example : </strong></p>
<p>Input : A = [1, 2, -4, -5], N = 4</p>
<p>Output : 1 -4  2 -5</p>
<p>Explanation: </p>
<p>Positive elements = 1, 2 and Negative elements = -4, -5</p>
<p>To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>BruteForce Approach : </strong></p>
<p>In this approach, we will store both positive numbers and negative numbers in separate arrays</p>
<p>Then, we can update the array such that, odd even positions with positives and odd positions with negtives</p>
<p>Since the array must begin with a positive number and the start index is 0, so all the positive numbers would be placed at even indices (2*i) and negatives at the odd indices (2*i+1), where i is the index of the pos or neg array while traversing them simultaneously.</p>

```python
def bruteForce(arr,n):
    pos,neg=[],[]
    for i in range(n):
        if(arr[i]<0):
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    for i in range(len(pos)):
        arr[i*2]=pos[i]
    for i in range(len(neg)):
        arr[i*2+1]=neg[i]
    return arr
```

<p>Time Complexity: O(N+N/2) { O(N) for traversing the array once for segregating positives and negatives and another O(N/2) for adding those elements alternatively to the array, where N = size of the array A}.</p>
<p>Space Complexity:  O(N/2 + N/2) = O(N) { N/2 space required for each of the positive and negative element arrays, where N = size of the array A}.</p>

<p><strong>Optimized Approach : </strong></p>
<p>In this optimal approach, we will try to solve the problem in a single pass and try to arrange the array elements in the correct order in that pass only.</p>
<p>We know that the resultant array must start from a positive element so we initialize the positive index as 0 and negative index as 1 and start traversing the array such that whenever we see the first positive element, it occupies the space at 0 and then posIndex increases by 2 (alternate places).</p>
<p>Similarly, when we encounter the first negative element, it occupies the position at index 1, and then each time we find a negative number, we put it on the negIndex and it increments by 2.</p>
<p>When both the negIndex and posIndex exceed the size of the array, we see that the whole array is now rearranged alternatively according to the sign</p>

```python
def optimized(arr,n):
    posIndex,negIndex=0,1
    final=[0]*n
    for i in range(n):
        if(arr[i]<0):
            final[negIndex]=arr[i]
            negIndex+=2
        else:
            final[posIndex]=arr[i]
            posIndex+=2
    return final
```

<p>Time Complexity: O(N) { O(N) for traversing the array once and substituting positives and negatives simultaneously using pointers, where N = size of the array A}.</p>
<p>Space Complexity:  O(N) { Extra Space used to store the rearranged elements separately in an array, where N = size of array A}.</p>


<h2>Find the duplicate in an array of N+1 integers</h2>
<p>Given an array of N + 1 size, where each element is between 1 and N. Assuming there is only one duplicate number, your task is to find the duplicate number.</p>
<p><strong>Example : </strong></p>
<p>Input: arr=[1,3,4,2,2]</p>
<p>Output: 2</p>
<p>Explanation: Since 2 is the duplicate number the answer will be 2.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>BruteForce Approach : </strong></p>
<p>In this approach, We will sort the given array</p>
<p>then, we will loop through given array</p
>
<p>If any consecutive numbers are equal, that will be our answer</p>

```python
def bruteForce(arr,n):
    arr.sort()
    for i in range(n-1):
        if(arr[i]==arr[i+1]):
            return arr[i]
    return -1
```

<p>Time Complexity:O(Nlogn + N)</p>
<p>Reason: NlogN for sorting the array and O(N) for traversing through the array and checking if adjacent elements are equal or not. But this will distort the array.</p>
<p>Space Complexity:O(1)</p>


<p><strong>Optimized Approach : </strong></p>
<p>In this approach, we will store count of each element</p>
<p>Then will check the count of each element, if any element count greater than 1, then it is the answer</p>

```python
def optimized(arr,n):
    count={i:0 for i in range(1,n+1)}
    for i in range(n):
        count[arr[i]]+=1
    for i in range(n):
        if(count[arr[i]]>1):
            return arr[i]
    return -1
```

<p>Time Complexity: O(N), as we are traversing through the array only once.</p>
<p>Space Complexity: O(N), as we are using extra space for frequency array.</p>

<h2><strong>More optimized approach :</strong></h2>
<p>In this approach, we will use finding staring point of loop in linkd list method</p>
<img src="Space Complexity: O(N), as we are using extra space for frequency array.">
<p>Initially, we have 2, then we got to the second index, we have 9, then we go to the 9th index, we have 1, then we go to the 1st index, we again have 5, then we go to the 5th index, we have 3, then we go to the 3rd index, we get 6, then we go to the 6th index, we get 8, then we go to the 8th index, we get 7, then we go to the 7th index and we get 9 and here cycle is formed.</p>
<img src="https://lh3.googleusercontent.com/mYvFYPFwnRv0jscFZYhlQGNhD5eF48gEQmo-obJEdm_Bl7t3BhS_BGWV2Mn9K8qTasZywFUCWLVmknEiLqlvtShTtyEGl-yDfGobZiFPe2McrRV9eI5hvg83gK1bqmG3GZn2WpG8">
<p>Now initially, the slow and fast pointer is at the start, the slow pointer moves by one step, and the fast pointer moves by 2 steps.</p>
<img src="https://lh4.googleusercontent.com/uvbCcCkBRoj_9X79yN9CCiy-Jir2Hd9wH1TNbN1vnfBlfIpye9w498sj1o8mTVHyYEbs3Ie1tH363dL6WfOQuZl54YT7SaKEHuZ-VWPHgnjOK_EKpWsAHPOGkwyKiU-Kk3PNepof">
<img src="https://lh4.googleusercontent.com/ODoVmsWg-ASUd1iY6q2Pieia9esc9-2a9F2p9jcaH9G-QOaF0jxBX7u5iKOumgjqUvWIqD8u6JvOfb2EAUCnrV_ALjzIQcA49LkjXlaPPhabBhrHdiCmpbQUk2I2M_hwRP4O2CEk">
<img src="https://lh3.googleusercontent.com/SRwQtAwmDP5C8DwyPlibAGisxGGkt_jMYdpEPzX_Zf1P0jdfdibct1I9erKWFRg7jdR0l65VPjYUGANniSWSgKBsSVXACMdyGXjJfI-D-RjLY6u6iEQP7bziCpwxNeHvDAmUhzSv">
<img src="https://lh6.googleusercontent.com/PSGLq_y4eqy5yecZzeyt_FjLNrz35aOnL78DxgIn7SfSNblXZQS1kGxL4uxtMqBVmKlPDrZFp8lDSiLTta52u6E_2Yziy5TvNmAm-mZsEJ1xsIUyFj7A5LfBmRbqLbb0OuNaFRCx">
<img src="https://lh4.googleusercontent.com/Hxx9V-V3mL3BuKknpm6IIoAPEUFc7Mi9xyRTxXMgx6l7fizm9_FtIHCU9-AFpS12hknei5FE1882Riil9G4rys99GxAlj-e_B-7G-KreCC_SQFCc8VlbaivsSZriyj5WEcG7IP0u">
<img src="https://lh5.googleusercontent.com/z3p0nsOIBGXlp1q92pF2IP-TY-R1P1RFhu8Q-Y2d1IdhQhQH3kKqBB0OtGFbQFi-y-yf-xiNoYIdZgUO4NGIT7RiHYrAu5J7TF2EDWa92OILtU2esP6MW8Bwsv82cpxDHM4c_ces">
<img src="https://lh5.googleusercontent.com/z3p0nsOIBGXlp1q92pF2IP-TY-R1P1RFhu8Q-Y2d1IdhQhQH3kKqBB0OtGFbQFi-y-yf-xiNoYIdZgUO4NGIT7RiHYrAu5J7TF2EDWa92OILtU2esP6MW8Bwsv82cpxDHM4c_ces">

<p>The slow and fast pointers meet at 7. Now take the fast pointer and place it at the first element i.e 2 and move the fast and slow pointer both by 1 step. The point where they collide will be the duplicate number.</p>

<img src="https://lh5.googleusercontent.com/oTtT1I74FY-MFk-4ch5r1lJ9DkqQAjS0k_rtYpKIHGhaWzznQDRltcGOfUVL-faajQB_5uA5GKiAl0j_7ynLmAxiIa6dkudH0A2rCXjmA4W_C70xp9GqjQ4G0IS4I466VZ3zR65r">
<img src="https://lh5.googleusercontent.com/kBQ_1w1QUaS4cBFx0neodYqh23JWO_d0noTdlbdNKw1wqw8tqulyfTRraj_qOegKAV6V3mY0LgIagiJKv4E_eApBVWP-b6qzZzg_RO4N1RxqSgV85SqULkjMD8blq7vDhf-6riC8">

<p>So 9 is the duplicate number.</p>
<p>Intuition: Since there is a duplicate number, we can always say that cycle will be formed.</p>
<p>The slow pointer moves by one step and the fast pointer moves by 2 steps and there exists a cycle so the first collision is bound to happen.</p>
<img src="https://lh3.googleusercontent.com/vVj4BsjxjTuSpU65MR8szuYCEBWAk2xRWwyN3NP8BOHUyIMStWwBYlp6hYFGXAlwzVYWTq1DW-d65oeYaBwCcIWFmVOhSYjtXY-KNlK--f6OF9Stym9_7jZP3HHTI6m-vysRdW4x">
<p>Let’s assume the distance between the first element and the first collision is a. So slow pointer has traveled a distance while fast(since moving 2 steps at a time) has traveled 2a distance. For slow and a fast pointer to collide 2a-a=a should be multiple of the length of cycle, Now we place a fast pointer to start. Assume the distance between the start and duplicate to be x. So now the distance between slow and duplicate shows also be x, as seen from the diagram, and so now fast and slow pointer both should move by one step.</p>

```python
def efficient(arr,n):
    slow=arr[0]
    fast=arr[0]
    while True:
        slow=arr[slow]
        fast=arr[arr[fast]]
        if(slow==fast):
            break
    fast=arr[0]
    while slow!=fast:
        slow=arr[slow]
        fast=arr[fast]
    return slow
```

<p>Time complexity: O(N). Since we traversed through the array only once.</p>
<p>Space complexity: O(1).</p>


<h2>Kadane's Algorithm : Maximum Subarray Sum in an Array</h2>
<p>Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.</p>
<p><strong>Example : </strong></p>
<p>Input: arr = [-2,1,-3,4,-1,2,1,-5,4]</p>
<p>Output: 6 </p>
<p>Explanation:[4,-1,2,1] has the largest sum = 6. </p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches.</p>
<p>BruteForce Approach : </p>
<p>In this approach, we will find out all contigous subarray's and will find sum of each subarray.</p>
<p>We will track the max sum out of all possible cases</p>
<ul>
    <li>First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = size of the array).</li>
    <li>Inside the loop, we will run another loop(say j) that will signify the ending index of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).</li>
    <li>After that for each subarray starting from index i and ending at index j (i.e. arr[i….j]), we will calculate the sum of all the elements(of that particular subarray).</li>
</ul>

<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-04-004717.png">

```python
def bruteForce(arr,n):
    maxi=0
    for i in range(n):
        for j in range(i,n+1):
            currentSum=sum(arr[i:j])
            maxi=max(maxi,currentSum)
    return maxi
```

<p>Time Complexity: O(N3), where N = size of the array.
Reason: We are using three nested loops, each running approximately N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Better Approach : </strong></p>
<p>In this approach, instead of find whole subarray, we will just find the sum of each subarray and can track max of all possible sums</p>
<p>To The previous proble, Inside second loop j, we will add the current element to the sum of the previous subarray i.e. sum = sum + arr[j]. Among all the sums the maximum one will be the answer.</p>

```python
def better(arr,n):
    maxi=0
    for i in range(n):
        currentSum=0
        for j in range(i,n):
            currentSum+=arr[j]
            maxi=max(maxi,currentSum)
    return maxi
```

<p>Time Complexity: O(N2), where N = size of the array.
Reason: We are using two nested loops, each running approximately N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Optimized Approach (Kaden's Algorithm) : </strong></p>
<p>In this approach, instead of finding all possible cases, . A subarray with a sum less than 0 will always reduce our answer and so this type of subarray cannot be a part of the subarray with maximum sum.</p>
<p>Here, we will iterate the given array with a single loop and while iterating we will add the elements in a sum variable.</p>
<p>Now, if at any point the sum becomes less than 0, we will set the sum as 0 as we are not going to consider any subarray with a negative sum.</p>
<p>Among all the sums calculated, we will consider the maximum one.</p>
<ul>
    <li>We will run a loop(say i) to iterate the given array.</li>
    <li>Now, while iterating we will add the elements to the sum variable and consider the maximum one.</li>
    <li>If at any point the sum becomes negative we will set the sum to 0 as we are not going to consider it as a part of our answer.</li>
</ul>

```python
def optimized(arr,n):
    maxi=0
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        if(currentSum>maxi):
            maxi=currentSum
        if(currentSum<0):
            currentSum=0
    return maxi
```

<p>Time Complexity: O(N), where N = size of the array.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<h2>Print Maximum Subarray Sum in an Array</h2>
<p>This is similar to previous problem, we just need to print subarray with maximum sum</p>
<p>We can just track the starting and ending index of each possible case and we can track max subarray and print the subarray with those starting and ending</p>
<p><strong>BruteForce Approach : </strong></p>
<p>In This approach, we will track starting and ending index of max subarray</p>

```python
def bruteForce(arr,n):
    maxi=0
    start,end=0,0
    for i in range(n):
        for j in range(i,n+1):
            currentSum=sum(arr[i:j])
            if(currentSum>maxi):
                maxi=currentSum
                start,end=i,j
    return arr[start:end]
```

<p>Time Complexity: O(N3), where N = size of the array.
Reason: We are using three nested loops, each running approximately N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Optimized Solution : </strong></p>
<p>Our approach is to store the starting index and the ending index of the subarray. Thus we can easily get the subarray afterward without actually storing the subarray elements.</p>
<p>If we carefully observe our algorithm, we can notice that the subarray always starts at the particular index where the sum variable is equal to 0, and at the ending index, the sum always crosses the previous maximum sum(i.e. maxi).</p>
<ul>
    <li>So, we will keep a track of the starting index inside the loop using a start variable.</li>
    <li>We will take two variables ansStart and ansEnd initialized with -1. And when the sum crosses the maximum sum, we will set ansStart to the start variable and ansEnd to the current index i.e. i.</li>
</ul>

```python
def optimized(arr,n):
    maxi=0
    currentSum=0
    start,end=0,0
    for i in range(n):
        if(currentSum==0):
            start=i
        currentSum+=arr[i]
        if(currentSum>maxi):
            maxi=currentSum
            end=i
        if(currentSum<0):
            currentSum=0
    return arr[start:end+1]
```

<p>Time Complexity: O(N), where N = size of the array.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>



<h2>Grid Unique Paths</h2>
<p>Given a matrix m X n, count paths from left-top to the right bottom of a matrix with the constraints that from each cell you can either only move to the rightward direction or the downward direction.</p>
<p><strong>Input Format: m = 2, n= 2</strong></p>
<p><strong>Output: 2</strong></p>
<p><strong>Solution : </strong></p>
<p>We can solve this problem in several approaches</p>
<p>We can solve in dp approach, this can be referred in dp section</p>
<p>Combinatorics Solution : (using combinations)</p>
<p>If we observe examples there is a similarity in paths from start to end. Each time we are taking an exactly m+n-2 number of steps to reach the end.</p>
<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fmath.stackexchange.com%2Fquestions%2F636128%2Fcalculating-the-number-of-possible-paths-through-some-squares&psig=AOvVaw32OTGv6au9ebkO-rpjo25Q&ust=1717084103512000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLjJ7vGas4YDFQAAAAAdAAAAABAE">
<p>From start to reach the end we need a certain number of rightward directions and a certain number of downward directions. So we can figure out we need n-1 no. of rightward direction and m-1 no. of downward direction to reach the endpoint.</p>
<p>Since we need an m+n-2 number of steps to reach the end among those steps if we choose n-1 rightward direction or m-1 downward direction and calculate the combinations ( ie: m+n-2Cn-1 or m+n-2Cm-1) we’ll get the total number of paths.</p>
<p>The approach of this solution is very simple just use a for loop to calculate the m+n-2Cn-1  or m+n-2Cm-1 </p>

```
nCr = n! / (r! * (n-r)!)
```
<p>We can separately calculate n!, r!, (n-r)! and using their values we can calculate nCr. This is an extremely naive way to calculate. The time complexity will be O(n)+O(r)+O(n-r).</p>
<p>We can optimize this calculation by the following observation. 
Assume, given r = 7, c = 4. </p>
<p>Now, n = r-1 = 7-1 = 6 and r = c-1 = 4-1 = 3</p>
<p>Let’s calculate 6C3 = 6! / (3! *(6-3)!) = (6*5*4*3*2*1) / ((3*2*1)*(3*2*1))</p>
<p>This will boil down to (6*5*4) / (3*2*1)</p>
<p>So, nCr = (n*(n-1)*(n-2)*.....*(n-r+1)) / (r*(r-1)*(r-2)*....1)</p>
<p>Now, we will use this optimized formula to calculate the value of nCr. But while implementing this into code we will take the denominator in the forward direction like: </p>
<p>(n / 1)*((n-1) / 2)*.....*((n-r+1) / r).</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-30-210349.png">

```python
def solve(n,m):
    N=n+m-2
    R=m-1
    final=1
    for i in range(R):
        final=final*(N-i)
        final=final//(i+1)
    return final

n,m=list(map(int,input().split()))
print(solve(n,m))
```

<p>Time Complexity: The time complexity of this solution will be O(n-1) or  O(m-1) depending on the formula we are using.</p>
<p>Space Complexity: As we are not using any extra space the space complexity of the solution will be  O(1).</p>

<h2>Sort an array of 0s,1s and 2s</h2>
<p>Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)</p>
<p>Examples</p>
<p><strong>Input:</strong></p>
<p>nums = [2,0,2,1,1,0]</p>
<p><strong>Output:</strong></p>
<p>[0,0,1,1,2,2]</p>
<p><strong>Input:</strong></p>
<p>nums = [2,0,1]</p>
<p><strong>Output:</strong></p>
<p>[0,1,2]</p>
<p><strong>Input:</strong></p>
<p>nums = [0]</p>
<p><strong>Output:</strong></p>
<p>[0]</p>

<p><strong>solution</strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>BruteForce Approach : </strong></p>
<p>We can apply any sorting algorithm or inbuilt sort function on given array</p>

```python
def bruteForce(n,arr):
    return sorted(arr)
```

<p><strong>Time Complexity: O(N*logN)</strong></p>
<p><strong>Space Complexity: O(1)</strong></p>

<p><strong>Better approach : </strong></p>
<p>In this approach, since given array only contains 0,1 and 2s</p>
<p>Loop through given array and count each value occurance and store in variables</p>
<p>Then, run loop based on calculated count and update existing array</p>

```python
def better(n,arr):
    zeros,ones,twos=0,0,0
    for i in range(n):
        if(arr[i]==0):
            zeros+=1
        if(arr[i]==1):
            ones+=1
        if(arr[i]==2):
            twos+=1
    for i in range(zeros):
        arr[i]=0
    for j in range(zeros,zeros+ones):
        arr[j]=1
    for k in range(zeros+ones,n):
        arr[k]=2
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(better(n,arr))
```

<p><strong>Time Complexity: O(N) + O(N), where N = size of the array. First O(N) for counting the number of 0’s, 1’s, 2’s, and second O(N) for placing them correctly in the original array.</strong></p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Optimized Approach : </strong></p>
<p>This approach is based on a variation of the popular Dutch National flag algorithm.</p>
<p>In this alogirthm, we will be having three pointers low,mid, and high</p>
<p>let us assume</p>
<ul>
    <li>0 to low-1 will contain zeros (0's)</li>
    <li>low to mid-1 will contain ones (1's)</li>
    <li>mid to high will contain twos (2's)</li>
</ul>
<p>since we have unsorted array as input, let us assume low,mid is pointed to 0 and high is pointed to n-1</p>
<p>now we have to sort mid to high elements of given array, such that it should be arranged as above rules</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/03/Screenshot-2023-03-18-171206.png">
<img src="https://static.takeuforward.org/wp/uploads/2023/03/Screenshot-2023-03-18-171326.png">
<p>Now, run a loop untill mid<=high and perform following operations</p>
<ul>
    <li>There can be three different values of mid pointer i.e. arr[mid]</li>
    <li>If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.</li>
    <li>If arr[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.</li>
    <li>If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2.In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. So, we will check the value of mid again in the next iteration.</li>
</ul>
<p>Finally, our array should be sorted.</p>

```python
def optimized(n,arr):
    low,mid,high=0,0,n-1
    while mid<=high:
        if(arr[mid]==0):
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        if(arr[mid]==1):
            mid+=1
        if(arr[mid]==2):
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
            mid+=1
    return arr

arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```

<p>Time Complexity: O(N), where N = size of the given array.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<h2>Pascal's Traingle</h2>
<p>Pascal’s triangle is a triangular array of binomial coefficients. Write a function that takes an integer value N as input and prints the first N lines of Pascal’s triangle.</p>
<p><strong>Example : </strong></p>
<p>The below image shows the Pascal’s Triangle for N=6</p>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20231019163940/Pascal's-Triangle-for-first-6-Rows.jpg">

<p><strong>Solution : </strong></p>
<p>As problem states, we will be having n rows</p>
<p>Each ith row containe  i number of elements</p>
<p>The values of ith element in nth row is calculated as (n-1)C(i-1), as shown in figure</p>
<img src="https://i.stack.imgur.com/nqaiV.png">
<p>We know how to find combinations, nCr</p>
<p>nCr = n! / (r! * (n-r)!)</p>
<p>We can separately calculate n!, r!, (n-r)! and using their values we can calculate nCr. This is an extremely naive way to calculate. The time complexity will be O(n)+O(r)+O(n-r).</p>
<p>In optimal way, Assume, given r = 7, c = 4. </p>
<p>Now, n = r-1 = 7-1 = 6 and r = c-1 = 4-1 = 3</p>
<p>Let’s calculate 6C3 = 6! / (3! *(6-3)!) = (6*5*4*3*2*1) / ((3*2*1)*(3*2*1))</p>
<p>This will boil down to (6*5*4) / (3*2*1)</p>
<p>So, nCr = (n*(n-1)*(n-2)*.....*(n-r+1)) / (r*(r-1)*(r-2)*....1)</p>
<p>Now, we will use this optimized formula to calculate the value of nCr. But while implementing this into code we will take the denominator in the forward direction like: </p>
<p>nCr=(n / 1)*((n-1) / 2)*.....*((n-r+1) / r).</p>

```python
def nCr(N,R):
    final=1
    for i in range(R):
        final=final*(N-i)
        final=final//(i+1)
    return final
```

<p>So, in Bruteforce approach, we can loop through each row and we can find ncr and print</p>
<ul>
    <li>Loop through 0 to n-1 as n times, for rows</li>
    <ul>
        <li>For, each row, loop through 0 to n-1 as r times, for columns</li>
        <li>print nCr for each column</li>
    </ul>
</ul>

```python
def nCr(N,R):
    final=1
    for i in range(R):
        final=final*(N-i)
        final=final//(i+1)
    return final

def printPascal(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(nCr(row-1,col-1),end=" ")
        print()
n=int(input())
printPascal(n)
```

<p><strong>Time Complexity : O(n*n*n)</strong></p>
<p><strong>Space Complexity : O(1)</strong></p>

<p><strong>Optimal Approach</strong></p>
<p>We will try to build intuition for this approach using the following observations.</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-30-214245.png">
<p>Here, we can observe a pattern , while calculating this nCr for current element, we can use previous value instead repetedly finding that calculation</p>
<p>Current element = prevElement * (rowNumber - colIndex) / colIndex</p>
<ul>
    <li>First, we will print the 1st element i.e. 1 manually.</li>
    <li>After that, we will use a loop(say i) that runs from 1 to n-1. It will print the rest of the elements.</li>
    <li>Inside the loop, we will use the above-said formula to print the element. We will multiply the previous answer by (n-i) and then divide it by i itself.</li>
    <li>Thus, the entire row will be printed.</li>
</ul>

```python
def optimized(n):
    for row in range(1,n+1):
        temp=[1]
        final=1
        for col in range(1,row):
            final*=(row-col)
            final//=col
            temp.append(final)
        print(*temp,sep=" ")
        
n=int(input())
optimized(n)
```

<p>TC : O(n*n)</p>
<p>SC : O(1)</p>


<h2>Find the Majority Element that occurs more than N/2 times</h2>
<p>Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.</p>
<p><strong>Example : </strong></p>
<p><strong>Input : </strong></p>
<p>N = 3, nums[] = {3,2,3}</p>
<p><strong>Output : </strong></p>
<p>3</p>
<p><strong>Explanation : </strong></p>
<p>When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>Bruteforce approach : </strong></p>
<p>In this approach, we will find count each element in given array and we will check if any element count is greater than length of array(n)/2. Then it will be our answer</p>

```python
def bruteForce(n,arr):
    count={}
    for i in range(n):
        if(arr[i] in count):
            count[arr[i]]+=1
        else:
            count[arr[i]]=1

    for i,v in count.items():
        if(v>(n//2)):
            return i
    return -1
```

<p>Time Complexity: O(N*logN) + O(N), where N = size of the given array.</p>
<p>Reason: We are using a map data structure. Insertion in the map takes logN time. And we are doing it for N elements. So, it results in the first term O(N*logN). The second O(N) is for checking which element occurs more than floor(N/2) times. If we use unordered_map instead, the first term will be O(N) for the best and average case and for the worst case, it will be O(N2).</p>
<p>Space Complexity: O(N) as we are using a map data structure.</p>

<p><strong>Optimized approach : </strong></p>
<p>This approach is based on Boyer-Moore Majority Voting Algorithm, let's discuss the algorithm</p>
<p>This algorithm works on the fact that if an element occurs more than N/2 times, it means that the remaining elements other than this would definitely be less than N/2. So let us check the proceeding of the algorithm.</p>
<p>First, choose a candidate from the given set of elements if it is the same as the candidate element, increase the votes. Otherwise, decrease the votes if votes become 0, select another new element as the new candidate.</p>
<p>When the elements are the same as the candidate element, votes are incremented whereas when some other element is found (not equal to the candidate element), we decreased the count. This actually means that we are decreasing the priority of winning ability of the selected candidate, since we know that if the candidate is in majority it occurs more than N/2 times and the remaining elements are less than N/2.</p>
<p>We keep decreasing the votes since we found some different element(s) than the candidate element. When votes become 0, this actually means that there are the equal  number of votes for different elements, which should not be the case for the element to be the majority element.</p>
<p>So the candidate element cannot be the majority and hence we choose the present element as the candidate and continue the same till all the elements get finished.</p>
<p>The final candidate would be our majority element. We check using the 2nd traversal to see whether its count is greater than N/2. If it is true, we consider it as the majority element.</p>
<p><strong>Steps to solve problem</strong></p>
<ul>
    <li>We will replace votes with count in above problem, and candidate as current element</li>
    <li>Initialize 2 variables: Count –  for tracking the count of element, current – for which element we are counting</li>
    <li>Traverse through the given array.</li>
    <ul>
        <li>If Count is 0 then store the current element of the array as current.</li>
        <li>If the current element and Element are the same increase the Count by 1.</li>
        <li>If they are different decrease the Count by 1.</li>
    </ul>
    <li>The integer present in Element should be the result we are expecting </li>
    <li>In, final we can check if current element count greater than n//2 if required</li>
</ul>

```python
def optimized(n,arr):
    count=0
    current=0
    for i in range(n):
        if(count==0):
            current=arr[i]
            count=1
        elif(current==arr[i]):
            count+=1
        else:
            count-=1
    final=0
    for i in range(n):
        if(arr[i]==current):
            final+=1
    if(final>(n//2)):
        return current
    return -1
```

<p>Time Complexity: O(N) + O(N), where N = size of the given array.</p>
<p>Reason: The first O(N) is to calculate the count and find the expected majority element. The second one is to check if the expected element is the majority one or not.</p>
<p>Note: If the question states that the array must contain a majority element, in that case, we do not need the second check. Then the time complexity will boil down to O(N).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<h2>next_permutation : find next lexicographically greater permutation</h2>
<p>Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.</p>
<p>If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).</p>
<p><strong>Example : </strong></p>
<p><strong>Input : </strong></p>
<p>Arr[] = {1,3,2}</p>
<p><strong>Output : </strong></p>
<p>Arr[] = {2,1,3}</p>
<p>All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.</p>
<p><strong>Input : </strong></p>
<p>Arr[] = {3,2,1}</p>
<p><strong>Output : </strong></p>
<p>Arr[] = {1,2,3}</p>
<p>As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the topmost permutation.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>Bruteforce Approach : </strong></p>
<p>In This approach, sort given array and find all possible permutations</p>
<p>Then find the given array in list, then we will print next element to its index</p>
<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/NewPermutation.gif">

<ul>
    <li>Define a recursive function that takes three parameters: the list, the starting index, and the ending index.</li>
    <li>If the starting index equals the ending index, print or store the permutation.</li>
    <li>Otherwise, for each index from the starting index to the ending index:</li>
    <ul>
        <li>Swap the current index with the starting index.</li>
        <li>Recursively call the function with the next starting index.</li>
        <li>Swap back to backtrack and restore the original list for the next iteration.</li>
    </ul>
</ul>

```python
def permute(arr,left,right):
    global temp
    if(left==right):
        temp.append(tuple(arr.copy()))
        return
    for i in range(left,right):
        arr[left],arr[i]=arr[i],arr[left]
        permute(arr,left+1,right)
        arr[left],arr[i]=arr[i],arr[left]
arr=list(map(int,input().split()))
n=len(arr)
temp=[]
permute(sorted(arr),0,n)
ind=temp.index(tuple(arr))
print(temp[(ind+1)%n])
```

<p>For finding, all possible permutations, it is taking N!xN. N represents the number of elements present in the input array. Also for searching input arrays from all possible permutations will take N!. Therefore, it has a Time complexity of O(N!xN).</p>
<p>Space Complexity : Since we are not using any extra spaces except stack spaces for recursion calls. So, it has a space complexity of O(1).</p>

<p><strong>Optimized Approach : </strong></p>
<p>In this approach, since we need to find next increasing subsequence, first we need find small suffix which can make next increasing sequence.</p>
<p>To Find That Suffix</p>
<ul>    
    <li>Start from the end of the list and move left to find the first place where a number is smaller than the number right after it. This spot is called the "dip".</li>
    <li>Example: In the list [1, 2, 3], the dip is at 2 because 2 is smaller than 3.</li>
</ul>
<ul>
    <li>Again, start from the end and find the smallest number that is bigger than the dip.</li>
    <li>Example: The smallest number bigger than 2 in [1, 2, 3] is 3.</li>
</ul>
<ul>
    <li>Swap the dip with the number you found.</li>
    <li>Example: Swap 2 and 3 to get [1, 3, 2].</li>
</ul>
<ul>
    <li>Finally, reverse the part of the list that comes after the original dip position. This puts it in the smallest possible order.</li>
    <li>Example: The part after 1 and 3 in [1, 3, 2] is just 2, so no change is needed.</li>
</ul>

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220908060940/Nextpermutation.png">

```python
def optimized(arr,n):
    ind=-1
    for i in range(n-2,-1,-1):
        if(arr[i]<arr[i+1]):
            ind=i
            break
    if(ind==-1):
        return arr[::-1]
    temp=arr[ind]
    for i in range(n-1,ind,-1):
        if(arr[i]>arr[ind]):
            arr[i],arr[ind]=arr[ind],arr[i]
            break
    arr[ind+1:]=reversed(arr[ind+1:])
    return arr
    
            
arr=list(map(int,input().split()))
n=len(arr)
print(optimized(arr,n))
```

<p>Time Complexity: O(3N), where N = size of the given array</p>
<p>Finding the break-point, finding the next greater element, and reversal at the end takes O(N) for each, where N is the number of elements in the input array. This sums up to 3*O(N) which is approximately O(3N).</p>
<p>Space Complexity: Since no extra storage is required. Thus, its space complexity is O(1).</p>


<h2>Set Matrix Zero</h2>
<p>Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.</p>
<p><strong>Examples : </strong></p>
<p>Input :  matrix=[[1,1,1],[1,0,1],[1,1,1]]</p>
<p>Output :  [[1,0,1],[0,0,0],[1,0,1]]</p>
<p>Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.</p>

<p>Input :  matrix=[[1,1,1],[1,0,1],[1,1,1]]</p>
<p>Output :  [[1,0,1],[0,0,0],[1,0,1]]</p>
<p>Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>Bruteforce Approach</strong></p> 
<p>In this approach, we will loop through each element of give matrix</p>
<p>if any element equals to zero, we will mark that entire row and column with -1 whose values not equal to 0</p>
<p>After that, we will loop though again with given matrix and update -1 elements value with zero</p>
<p>Final matrix will be our answer</p>

```python
def bruteForce(n,m,matrix):
    def markRow(row):
        nonlocal matrix
        for i in range(m):
            if(matrix[row][i]!=0):
                matrix[row][i]=-1
    def markCol(col):
        nonlocal matrix
        for i in range(n):
            if(matrix[i][col]!=0):
                matrix[i][col]=-1
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==0):
                markRow(i)
                markCol(j)
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==-1):
                matrix[i][j]=0
    return matrix

n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(bruteForce(n,m,copy.deepcopy(matrix)))
```

<p><strong>Time Complexity</strong>: O((N*M)*(N + M)) + O(N*M), where N = no. of rows in the matrix and M = no. of columns in the matrix.</p>
<p>Reason: Firstly, we are traversing the matrix to find the cells with the value 0. It takes O(N*M). Now, whenever we find any such cell we mark that row and column with -1. This process takes O(N+M). So, combining this the whole process, finding and marking, takes O((N*M)*(N + M)).</p>
<p>Another O(N*M) is taken to mark all the cells with -1 as 0 finally.</p>
<p><strong>Space Complexity</strong>: O(1) as we are not using any extra space.</p>

<p><strong>Better Approach</strong></p>
<p>In this approach, instead of marking entire row and entire column everytime when element equals to zero</p>
<p>We can create two arrays of size row and column</p>
<p>row array is used track if any of that row contains zero</p>
<p>column array is used track if any of that column contains zero</p>
<ul>
    <li>First, we will declare two arrays: a row array of size N and a col array of size M and both are initialized with 0.</li>
    <li>Then, we will use two loops(nested loops) to traverse all the cells of the matrix.</li>
    <li>If any cell (i,j) contains the value 0, we will mark ith index of row array i.e. row[i] and jth index of col array col[j] as 1. It signifies that all the elements in the ith row and jth column will be 0 in the final matrix.</li>
    <li>We will perform step 3 for every cell containing 0.</li>
    <li>Finally, we will again traverse the entire matrix and we will put 0 into all the cells (i, j) for which either row[i] or col[j] is marked as 1.</li>
    <li>Thus we will get our final matrix.</li>
</ul>

```python
def better(n,m,matrix):
    row=[0]*n
    col=[0]*m
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==0):
                row[i]=1
                col[j]=1
    for i in range(n):
        for j in range(m):
            if(row[i] or col[j]):
                matrix[i][j]=0
    return matrix

n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(better(n,m,copy.deepcopy(matrix)))
```

<p><strong>Time Complexity</strong>: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.</p>
<p>Reason: We are traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.</p>
<p><strong>Space Complexity</strong>: O(N) + O(M), where N = no. of rows in the matrix and M = no. of columns in the matrix.</p>
<p>Reason: O(N) is for using the row array and O(M) is for using the col array.</p>

<p><strong>Optimized Approach : </strong></p>
<p>In the previous approach, the time complexity is minimal as the traversal of a matrix takes at least O(N*M)(where N = row and M = column). In this approach, we can just improve the space complexity.</p>
<p>So, instead of using two extra matrices row and col, we will use the 1st row and 1st column of the given matrix to keep a track of the cells that need to be marked with 0.</p>
<p>But here comes a problem. If we try to use the 1st row and 1st column to serve the purpose, the cell matrix[0][0] is taken twice. To solve this problem we will take an extra variable col0 initialized with 1</p>
<p> Now the entire 1st row of the matrix will serve the purpose of the row array. And the 1st column from (0,1) to (0,m-1) with the col0 variable will serve the purpose of the col array.</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-04-001419.png">
<p>If any cell in the 0th row contains 0, we will mark matrix[0][0] as 0 and if any cell in the 0th column contains 0, we will mark the col0 variable as 0.</p>
<ul>
    <li>First, we will traverse the matrix and mark the proper cells of 1st row and 1st column with 0 accordingly. The marking will be like this: if cell(i, j) contains 0, we will mark the i-th row i.e. matrix[i][0] with 0 and we will mark j-th column i.e. matrix[0][j] with 0.</li>
    <li>If i is 0, we will mark matrix[0][0] with 0 but if j is 0, we will mark the col0 variable with 0 instead of marking matrix[0][0] again.</li>
    <li>After step 1 is completed, we will modify the cells from (1,1) to (n-1, m-1) using the values from the 1st row, 1st column, and col0 variable.</li>
    <li>We will not modify the 1st row and 1st column of the matrix here as the modification of the rest of the matrix(i.e. From (1,1) to (n-1, m-1)) is dependent on that row and column.</li>
    <li>Finally, we will change the 1st row and column using the values from matrix[0][0] and col0 variable. Here also we will change the row first and then the column.</li>
    <li>If matrix[0][0] = 0, we will change all the elements from the cell (0,1) to (0, m-1), to 0.</li>
    <li> If col0 = 0, we will change all the elements from the cell (0,0) to (n-1, 0), to 0.</li>
</ul>

```python
def optimized(n,m,matrix):
    c0=1
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==0):
                matrix[i][0]=0

                if(j!=0):
                    matrix[0][j]=0
                else:
                    c0=0
    for i in range(1,n):
        for j in range(1,m):
            if(matrix[i][0]==0 or matrix[0][j]==0):
                matrix[i][j]=0

    if(matrix[0][0]==0):
        for j in range(m):
            matrix[0][j]=0
    if(c0==0):
        for i in range(n):
            matrix[i][0]=0

    return matrix

n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(optimized(n,m,copy.deepcopy(matrix)))
```

<p><strong>Time Complexity</strong>: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.</p>
<p>Reason: In this approach, we are also traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<h2>Find the elements that appears more than N/3 times in the array</h2>
<p>Given an array of N integers. Find the elements that appear more than N/3 times in the array. If no such element exists, return an empty vector.</p>
<p><strong>Example : </strong></p>
<p>Input : N = 5, array[] = {1,2,2,3,2}</p>
<p>Output : 2</p>
<p>Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.</p>
<p>Input : N = 6, array[] = {11,33,33,11,33,11}</p>
<p>11 33</p>
<p>Here we can see that the Count(11) = 3 and Count(33) = 3. Therefore, the count of both 11 and 33 is greater than N/3 times. Hence, 11 and 33 is the answer.</p>

<p><strong>Solution : </strong></p>
<p>This problem can be solved in several approaches.</p>
<p><strong>Bruteforce Approach : </strong></p>
<p>In this approach, we will find count of each element in given array and check if its count greater than n/3, then add it into final answer</p>
<p>then return final answer</p>

```python
def bruteForce(n,arr):
    count={}
    final=[]
    for i in range(n):
        if arr[i] in count:
            count[arr[i]]+=1
        else:
            count[arr[i]]=1

        if(count[arr[i]] > n//3 and arr[i] not in final):
            final.append(arr[i])

    return sorted(final)

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```

<p><strong>Time Complexity</strong> : O(N*logN), where N = size of the given array</p>
<p>Reason: We are using a map data structure. Insertion in the map takes logN time. And we are doing it for N elements. So, it results in the first term O(N*logN).
If we use unordered_map instead, the first term will be O(N) for the best and average case and for the worst case, it will be O(N2).</p>
<p><strong>Space Complexity</strong>: O(N) as we are using a map data structure. We are also using a list that stores a maximum of 2 elements. That space used is so small that it can be considered constant.</p>


<p>Optimized Approach : </p>
<p>We know, that elements whose count greater than n/3 will always be atmost 2.</p>
<p>By using Boyer Moore’s Voting Algorithm. we can solve this problem</p>
<ul>
    <li>Initialize 4 variables:</li>
    <ul>
        <li>cnt1 & cnt2 –  for tracking the counts of elements</li>
        <li>el1 & el2 – for storing the majority of elements.</li>
    </ul>
    <li>el1 & el2 – for storing the majority of elements.</li>
    <ul>
        <li>If cnt1 is 0 and the current element is not el2 then store the current element of the array as el1 along with increasing the cnt1 value by 1.</li>
        <li>If cnt2 is 0 and the current element is not el1 then store the current element of the array as el2 along with increasing the cnt2 value by 1.</li>
        <li>If the current element and el1 are the same increase the cnt1 by 1.</li>
        <li>If the current element and el2 are the same increase the cnt2 by 1.</li>
        <li>Other than all the above cases: decrease cnt1 and cnt2 by 1.</li>
        <li>The integers present in el1 & el2 should be the result we are expecting. So, using another loop, we will manually check their counts if they are greater than the floor(N/3).</li>
    </ul>
</ul>
<p>: If the array contains the majority of elements, their occurrence must be greater than the floor(N/3). Now, we can say that the count of minority elements and majority elements is equal up to a certain point in the array. So when we traverse through the array we try to keep track of the counts of elements and the elements themselves for which we are tracking the counts. </p>
<p>After traversing the whole array, we will check the elements stored in the variables. Then we need to check if the stored elements are the majority elements or not by manually checking their counts.</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-20-224857.png">
<p>Edge Case: Why we are adding extra checks like el2 != v[i] and el1 != v[i] in the first if statements? Let’s understand it using an example:
Assume the given array is: {2, 1, 1, 3, 1, 4, 5, 6}. Now apply the algorithm without the checks:</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-20-225002.png">
<p>We can clearly notice that in iteration 5, el1 and el2 both are set to 1 as cnt1 becomes 0 in iteration 4. But this is incorrect. So, to avoid this edge case, we are checking if the current element is already included in our elements, and if it is, we will not again include it in another variable.</p>

```python
def optimized(n,arr):
    cnt1,cnt2=0,0
    ele1,ele2=None,None
    for i in range(n):
        current=arr[i]
        if(cnt1==0 and current!=ele2):
            cnt1+=1
            ele1=current
        elif(cnt2==0 and current!=ele1):
            cnt2+=1
            ele2=current
        elif(ele1==current):
            cnt1+=1
        elif(ele2==current):
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    c1,c2=0,0
    for i in range(n):
        if(ele1==arr[i]):
            c1+=1
        if(ele2==arr[i]):
            c2+=1
    final=[]
    if(c1>(n//3)):
        final.append(ele1)
    if(c2>(n//3)):
        final.append(ele2)
    return sorted(final)

arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```

<p><strong>Time Complexity</strong>: O(N) + O(N), where N = size of the given array.</p>
<p>Reason: The first O(N) is to calculate the counts and find the expected majority elements. The second one is to check if the calculated elements are the majority ones or not.</p>
<p><strong>Space Complexity</strong>: O(1) as we are only using a list that stores a maximum of 2 elements. The space used is so small that it can be considered constant.</p>

<h2>Merge overlapping sub-intervals</h2>
<p>Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.</p>
<p><strong>Example</strong></p>
<p>Input: intervals = [[1,3],[2,6],[8,10],[15,18]]</p>
<p>Output: [[1,6],[8,10],[15,18]]</p>
<p>Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].</p>
<p>Input: intervals = [[1,4],[4,5]]</p>
<p>Output: [[1,5]]</p>
<p>Explanation: Intervals [1,4] and [4,5] are considered overlapping.</p>

<p><strong>Explanation : </strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>BruteForce Approach</strong></p>
<p>First, we have to sort the given intervals, so that we can easily merge intervals, all possible overlapped intervals will be consecutive each other</p>
<p>In this approach, we will pick an interval in given array and loop through rest of intervals and we will merge all possible intervals with current interval and we can add that resulted merged interval in ans array</p>
<p>We will repeat above process for every interaval and finally we can get our ans</p>
<p>How can we merger two intervals ? . We will compare the current interval’s start with the end of the selected interval. If the start is smaller or equal to the end, we can conclude the current interval can be a part of the selected interval. So, we will update the selected interval’s end with the maximum(current interval’s end, selected interval’s end) in the answer list(not in the original array).</p>
<p>How can we confirm two intervals can not be merged? We will compare the current interval’s start with the end of the selected interval. If the start is greater than the end, we can conclude the current interval cannot be a part of the selected interval.</p>
<p>The intuition of this approach is pretty straightforward. We are just grouping close intervals by sorting the given array. After that, we merge an interval with the other by checking if one can be a part of the other interval. For this checking, we are first selecting a particular interval using a loop and then we are comparing the rest of the intervals using another loop.</p>

```python
def bruteforce(n,arr):
    ans=[]
    arr.sort()
    for i in range(n):
        start,end=arr[i]
        if(ans and start <= ans[-1][1]):
            continue
        for j in range(i+1,n):
            if(arr[j][0]<=end):
                end=max(end,arr[j][1])
            else:
                break
        ans.append([start,end])
    return ans

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
print(bruteforce(n,arr))
```

<p>Time Complexity: O(N*logN) + O(2*N), where N = the size of the given array.</p>
<p>Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are using 2 loops i and j. But while using loop i, we skip all the intervals that are merged with loop j. So, we can conclude that every interval is roughly visited twice(roughly, once for checking or skipping and once for merging). So, the time complexity will be 2*N instead of N2.</p>
<p>Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array, we are not using any extra space.</p>

<p><strong>Optimized approach </strong></p>
<p>In this approach, instead of checking current interval with all other inrtervals at all the time, we will check with ans array and merge current element with last interval in ans array</p>
<ul>
    <li>First, we will group the closer intervals by sorting the given array of intervals(if it is not already sorted).</li>
    <li>After that, we will start traversing the array using a loop(say i) and insert the first element into our answer list(as the answer list is empty).</li> 
    <li>Now, while traversing we will face two different cases:</li>
    <ul>
        <li><strong>Case 1: If the current interval can be merged with the last inserted interval of the answer list:</strong></li>
        <li>In this case, we will update the end of the last inserted interval with the maximum(current interval’s end, last inserted interval’s end) and continue moving afterward. </li>
        <li><strong>Case 2: If the current interval cannot be merged with the last inserted interval of the answer list:</strong></li>
        <li>In this case, we will insert the current interval in the answer array as it is. And after this insertion, the last inserted interval of the answer list will obviously be updated to the current interval.</li>
    </ul>
    <li>Thus the answer list will be updated with the merged intervals and finally, we will return the answer list.</li>
</ul>
<img src="Thus the answer list will be updated with the merged intervals and finally, we will return the answer list.">

```python
def optimized(n,arr):
    ans=[]
    arr.sort()
    for i in range(n):
        start,end=arr[i]
        if(not ans or start>ans[-1][1]):
            ans.append([start,end])
        else:
            ans[-1][1]=max(ans[-1][1],end)
    return ans

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
print(optimized(n,arr))
```

<p>Time Complexity: O(N*logN) + O(N), where N = the size of the given array.</p>
<p>Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are just using a single loop that runs for N times. So, the time complexity will be O(N).</p>
<p>Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array, we are not using any extra space.</p>

<h2>Merge two Sorted Arrays Without Extra Space</h2>
<p>Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.</p>
<p><strong>Example</strong></p>
<p>Input : n = 4, arr1[] = [1 4 8 10] m = 5, arr2[] = [2 3 9]</p>
<p>Output : arr1[] = [1 2 3 4] arr2[] = [8 9 10]</p>
<p>After merging the two non-decreasing arrays, we get, 1,2,3,4,8,9,10.</p>
<p>Input : n = 4, arr1[] = [1 3 5 7] m = 5, arr2[] = [0 2 6 8 9]</p>
<p>Output : arr1[] = [0 1 2 3] arr2[] = [5 6 7 8 9]</p>
<p>After merging the two non-decreasing arrays, we get, 0 1 2 3 5 6 7 8 9.</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>BruteForce Approach </strong></p>
<p>In this approach, we can use merge sort algorithm, so that we get sorted array</p>

```python
def bruteForce(n,m,arr1,arr2):
    arr=[0]*(n+m)
    index=0
    i,j=0,0
    while (i<n and j<m) :
        if(arr1[i]<=arr2[j]):
            arr[index]=arr1[i]
            i+=1
            index+=1
        else:
            arr[index]=arr2[j]
            j+=1
            index+=1

    while i<n:
        arr[index]=arr1[i]
        i+=1
        index+=1

    while j<m:
        arr[index]=arr2[j]
        j+=1
        index+=1
    return arr

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n,m=len(arr1),len(arr2)
print(bruteForce(n,m,arr1,arr2))
```

<p>Time Complexity: O(n+m) + O(n+m), where n and m are the sizes of the given arrays.</p>
<p>Reason: O(n+m) is for copying the elements from arr1[] and arr2[] to arr3[]. And another O(n+m) is for filling back the two given arrays from arr3[].</p>
<p>Space Complexity: O(n+m) as we use an extra array of size n+m.</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, since we have two sorted array, after merging two arrays, first array should contain smaller elements and second array will contain larger elements</p>
<p>So, we will try to compare elements,. Using the 2 pointers, we will swap the bigger elements of arr1[] with the smaller elements of arr2[] until the minimum of arr2[] becomes greater or equal to the maximum of arr1[].</p>
<ul>
    <li>We will declare two pointers i.e. left and right. The left pointer will point to the last index of the arr1[](i.e. Basically the maximum element of the array). The right pointer will point to the first index of the arr2[](i.e. Basically the minimum element of the array).</li>
    <li>Now, the left pointer will move toward index 0 and the right pointer will move towards the index m-1. While moving the two pointers we will face 2 different cases like the following:</li>
    <ul>
        <li>If arr1[left] > arr2[right]: In this case, we will swap the elements and move the pointers to the next positions.</li>
        <li>If arr1[left] <= arr2[right]: In this case, we will stop moving the pointers as arr1[] and arr2[] are containing correct elements.</li>
    </ul>
    <li>Thus, after step 2, arr1[] will contain all smaller elements and arr2[] will contain all bigger elements. Finally, we will sort the two arrays.</li>
</ul>
<img src="https://static.takeuforward.org/wp/uploads/2023/05/Screenshot-2023-05-07-203827.png">

```python
def optimized(n,m,arr1,arr2):
    i,j=n-1,0
    while i>=0 and j<m:
        if(arr1[i]>arr2[j]):
            arr1[i],arr2[j]=arr2[j],arr1[i]
            i-=1
            j+=1
        else:
            break
    arr1.sort()
    arr2.sort()
    return arr1+arr2

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n,m=len(arr1),len(arr2)
print(optimized(n,m,arr1,arr2))
```

<p>Time Complexity: O(min(n, m)) + O(n*logn) + O(m*logm), where n and m are the sizes of the given arrays.</p>
<p>Reason: O(min(n, m)) is for swapping the array elements. And O(n*logn) and O(m*logm) are for sorting the two arrays.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Second Optimized Approach</strong></p>
<p>In this approach, we can use shell sort(gap approach)</p>
<p>Assume the two arrays as a single continuous array</p>
<ul>
    <li>Initialize the Gap: Start with the gap equal to the combined length of both arrays divided by 2.</li>
    <li>Compare and Swap: For each gap, compare elements that are gap distance apart and swap them if they are out of order.</li>
    <li>Reduce the Gap: Halve the gap and repeat until the gap becomes 0.</li>
</ul>

<ul>
    <li>First, assume the two arrays as a single array and calculate the gap value i.e. ceil((size of arr1[] + size of arr2[]) / 2).</li>
    <li>We will perform the following operations for each gap until the value of the gap becomes 0</li>
    <ul>
        <li>Place two pointers in their correct position like the left pointer at index 0 and the right pointer at index (left+gap).</li>
        <li>Again we will run a loop until the right pointer reaches the end i.e. (n+m). Inside the loop, there will be 3 different cases:</li>
        <ul>
            <li>If the left pointer is inside arr1[] and the right pointer is in arr2[]: We will compare arr1[left] and arr2[right-n] and swap them if arr1[left] > arr2[right-n].</li>
            <li>If both the pointers are in arr2[]: We will compare arr1[left-n] and arr2[right-n] and swap them if arr1[left-n] > arr2[right-n].</li>
            <li>If both the pointers are in arr1[]: We will compare arr1[left] and arr2[right] and swap them if arr1[left] > arr2[right].</li>
        </ul>
        <li>After the right pointer reaches the end, we will decrease the value of the gap and it will become ceil(current gap / 2). </li>
    </ul>
    <li>Finally, after performing all the operations, we will get the merged sorted array.</li>
</ul>

```python
def optimized2(n,m,arr1,arr2):
    length=n+m
    gap=math.ceil(length/2)
    while(gap>0):
        left=0
        right=left+gap
        while right<length:
            if(left<n and right>=n):
                swap(arr1,arr2,left,right-n)
            elif(left>=n and right>=n):
                swap(arr2,arr2,left-n,right-n)
            else:
                swap(arr1,arr1,left,right)
            left+=1
            right+=1
        if(gap==1):
            break
        gap=math.ceil(gap/2)
    return arr1+arr2


arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n,m=len(arr1),len(arr2)
print(optimized2(n,m,arr1,arr2))
```

<p>Time Complexity: O((n+m)*log(n+m)), where n and m are the sizes of the given arrays.</p>
<p>Reason: The gap is ranging from n+m to 1 and every time the gap gets divided by 2. So, the time complexity of the outer loop will be O(log(n+m)). Now, for each value of the gap, the inner loop can at most run for (n+m) times. So, the time complexity of the inner loop will be O(n+m). So, the overall time complexity will be O((n+m)*log(n+m)).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>


<h2>Longest Consecutive Sequence in an Array</h2>
<p>You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.</p>
<p><strong>Example</strong></p>
<p>Input :  [100, 200, 1, 3, 2, 4]</p>
<p>Output : 4</p>
<p>The longest consecutive subsequence is 1, 2, 3, and 4.</p>
<p>Input :  [3, 8, 5, 7, 6]</p>
<p>Output : 4</p>
<p>The longest consecutive subsequence is 5, 6, 7, and 8.</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>
<p><strong>Bruteforce Approach</strong></p>
<p>In this approach, we will loop through given array, for each element we will try to find its consecutive elements x,x+1,x+2..and so on. we wil track the count of possible sequence for each element</p>
<p>finally we will get the the largest count among all possiblities, that will be our answer</p>
<ul>
    <li>To begin, we will utilize a loop to iterate through each element one by one.</li>
    <li>Next, for every element x, we will try to find the consecutive elements like x+1, x+2, x+3, and so on</li>
    <ul>
        <li>Within a loop, our objective is to locate the next consecutive element x+1.</li>
        <ul>
            <li>If this element is found, we increment x by 1 and continue the search for x+2. </li>
            <li>Furthermore, we increment the length of the current sequence (cnt) by 1. </li>
        </ul>
    </ul>
    <li>If a specific consecutive element, for example, x+i, is not found, we will halt the search for subsequent consecutive elements such as x+i+1, x+i+2, and so on. Instead, we will take into account the length of the current sequence (cnt).</li>
</ul>
<p>Among all the lengths we get for all the given array elements, the maximum one will be the answer.</p>

```python
def bruteForce(n,arr):
    longest=1

    for i in range(n):
        current=arr[i]
        cnt=1
        while True:
            if((current+1) in arr):
                cnt+=1
                current=current+1
            else:
                break
        longest=max(longest,cnt)
    return longest

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```
<p>Time Complexity: O(N2), N = size of the given array.</p>
<p>Reason: We are using nested loops each running for approximately N times.</p>
<p>Space Complexity: O(1), as we are not using any extra space to solve this problem.</p>

<p><strong>Better Approach</strong></p>
<p>In this approach, we will sort the given array, so that all possbile consecutive elements are adjcent with each other</p>
<p>So, after sorting, we will start iterating into list.we will track last element and current element in loop</p>
<p>if last element + 1 is our current element, then we will increase the current count of sequence and will update the last element with current</p>
<p>if not matches, then we will reset the count, will update the last element with current</p>

<p>But there is a case, if there are duplicate elements, we can't consider in sequnce, so, we will continue loop when last element equals to current, count remains same</p>

<p>Out of all possible count, we can track largest to get our final answer</p>

```python
def better(n,arr):
    arr.sort()
    last=float('-inf')
    longest=1
    cnt=0
    for i in range(n):
        if(arr[i]==last):
            continue
        if(arr[i]-1 ==last):
            cnt+=1
            last=arr[i]
            longest=max(longest,cnt)
        else:
            cnt=1
            last=arr[i]
    return longest
arr=list(map(int,input().split()))
n=len(arr)
print(better(n,arr))
```

<p>Time Complexity: O(NlogN) + O(N), N = size of the given array.</p>
<p>Reason: O(NlogN) for sorting the array. To find the longest sequence, we are using a loop that results in O(N).</p>
<p>Space Complexity: O(1), as we are not using any extra space to solve this problem.</p>

<p><strong>Optimal Approach</strong></p>
<p>In this approach, We will adopt a similar approach to the brute-force method but with optimizations in the search process. Instead of searching sequences for every array element as in the brute-force approach, we will focus solely on finding sequences only for those numbers that can be the starting numbers of the sequences. This targeted approach narrows down our search and improves efficiency.</p>
<p>We will do this with the help of the Set data structure.</p>
<p><strong>How to identify if a number can be the starting number for a sequence:</strong></p>
<ul>
    <li>First, we will put all the array elements into the set data structure.</li>
    <li>If a number, num, is a starting number, ideally, num-1 should not exist. So, for every element, x, in the set, we will check if x-1 exists inside the set.</li>
    <ul>
        <li>If x-1 exists: This means x cannot be a starting number and we will move on to the next element in the set.</li>
        <li>If x-1 does not exist: This means x is a starting number of a sequence. So, for number, x, we will start finding the consecutive elements.</li>
    </ul>
    <li>Instead of using linear search, we will use the set data structure itself to search for the elements x+1, x+2, x+3, and so on.</li>
</ul>

<p>Here, we will find all possible starting points and then find the consecutive sequence for it, that will reduce complexity, so that we will not find consecutive sequnce that already used</p>


```python
def optimized(n,arr):
    temp=set(arr)
    longest=1
    for i in range(n):
        current=arr[i]
        if(current-1 not in temp):
            cnt=1
            while current+1 in temp:
                current+=1
                cnt+=1
            longest=max(longest,cnt)
    return longest
arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```

<p>Time Complexity: O(N) + O(2*N) ~ O(3*N), where N = size of the array.</p>
<p>Reason: O(N) for putting all the elements into the set data structure. After that for every starting element, we are finding the consecutive elements. Though we are using nested loops, the set will be traversed at most twice in the worst case. So, the time complexity is O(2*N) instead of O(N2).</p>
<p>Space Complexity: O(N), as we are using the set data structure to solve this problem.</p>
<p>Note: The time complexity is computed under the assumption that we are using unordered_set and it is taking O(1) for the set operations. </p>
<ul>
    <li>If we consider the worst case the set operations will take O(N) in that case and the total time complexity will be approximately O(N2).</li>
    <li>And if we use the set instead of unordered_set, the time complexity for the set operations will be O(logN) and the total time complexity will be O(NlogN).</li>
</ul>

<h2>Longest Subarray with given Sum K(Positives)/(Negatives)</h2>
<p>Given an array and a sum k, we need to print the length of the longest subarray that sums to k.</p>
<p><strong>Examples</strong></p>
<p>Input :  N = 3, k = 5, array[] = {2,3,5}</p>
<p>Output : 2</p>
<p>Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.</p>
<p>Input : N = 5, k = 10, array[] = {2,3,5,1,9}</p>
<p>Output: 3</p>
<p>Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.</p>

<p><strong>Solution</strong></p>
<p>This problem can be solve several approaches</p>
<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we can find out all possible subarrays and find its sum, if any sum equals to given k, then we can take that subarray length. we can take out maximum of all possible lengths will be our answer</p>
<ul>
    <li>First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = size of the array).</li>
    <li>Inside the loop, we will run another loop(say j) that will signify the ending index of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).</li>
    <li>After that for each subarray starting from index i and ending at index j (i.e. arr[i….j]), we will run another loop to calculate the sum of all the elements(of that particular subarray).</li>
    <li>If the sum is equal to k, we will consider its length i.e. (j-i+1). Among all such subarrays, we will consider the maximum length by comparing all the lengths.</li>
</ul>

```python
def bruteForce(n,arr,k):
    largest=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for l in range(i,j+1):
                sum+=arr[l]
            if(sum==k):
                length=j-i+1
                largest=max(largest,length)
    return largest
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
```

<p>Time Complexity: O(N3) approx., where N = size of the array.</p>
<p>Reason: We are using three nested loops, each running approximately N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Better Approach</strong></p>
<p>In this approach, we will just modify the previous approach, where we are trying to find out sum for each possible subarray everytime</p>
<p>If we carefully observe, we can notice that to get the sum of the current subarray we just need to add the current element(i.e. arr[j]) to the sum of the previous subarray i.e. arr[i….j-1].</p>
<p>Assume previous subarray = arr[i……j-1]</p>
<p>current subarray = arr[i…..j]</p>
<p>Sum of arr[i….j] = (sum of arr[i….j-1]) + arr[j]</p>
<p>This is how we can remove the third loop and while moving the j pointer, we can calculate the sum. this can reduce our complexity</p>

<ul>
    <li>First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = array size).</li>
    <li>Inside the loop, we will run another loop(say j) that will signify the ending index as well as the current element of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).</li>
    <li>Inside loop j, we will add the current element to the sum of the previous subarray i.e. sum = sum + arr[j]. </li>
    <li>If the sum is equal to k, we will consider its length i.e. (j-i+1). Among all such subarrays with sum k, we will consider the one with the maximum length by comparing all the lengths.</li>
</ul>

```python
def better(n,arr,k):
    largest=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum==k):
                length=j-i+1
                largest=max(largest,length)
    return largest

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(better(n,arr,k))
```

<p>Time Complexity: O(N2) approx., where N = size of the array.</p>
<p>Reason: We are using two nested loops, each running approximately N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Optimized approach</strong></p>
<p>In this approach, instead of generating all subsequences everytime. we can use prefix sum to find of k sum existed for current element included and as last element</p>
<p>Here, the prefix sum of a subarray ending at index i, simply means the sum of all the elements of that subarray.</p>
<p>Assume, the prefix sum of a subarray ending at index i is x. In that subarray, we will search for another subarray ending at index i, whose sum equals k</p>
<p>Here, we need to observe that if there exists another subarray ending at index i with sum k, then the prefix sum of the rest of the subarray will be x-k. The below image will clarify the concept:</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-13-004939.png">
<p>Now, for a subarray ending at index i with the prefix sum x, if we remove the part with the prefix sum x-k, we will be left with the part whose sum is equal to k. And that is what we want.</p>
<p>That is why, instead of searching the subarrays with sum k, we will keep track of the prefix sum of the subarrays generated at every index using a map data structure.</p>
<p>In the map, we will store every prefix sum calculated, with its index in a <key, value> pair. Now, at index i, we just need to check the map data structure to get the index i.e. preSumMap[x-k] where the subarrays with the prefix sum x-k occur. Then we will simply subtract the index i.e. preSumMap[x-k] from the current index i to get the length of the subarray i.e. len = i -preSumMap[x-k].</p>

<ul>
    <li>First, we will declare a map to store the prefix sums and the indices</li>
    <li>Then we will run a loop(say i) from index 0 to n-1(n = size of the array).</li>
    <li>For each index i, we will do the following</li>
    <ul>
        <li>We will add the current element i.e. a[i] to the prefix sum.</li>
        <li>If the sum is equal to k, we should consider the length of the current subarray i.e. i+1. We will compare this length with the existing length and consider the maximum one.</li>
        <li>We will calculate the prefix sum i.e. x-k, of the remaining subarray.</li>
        <li>If that sum of the remaining part i.e. x-k exists in the map, we will calculate the length i.e. i-preSumMap[x-k], and consider the maximum one comparing it with the existing length we have achieved until now.</li>
        <li>If the sum, we got after step 3.1, does not exist in the map we will add that with the current index into the map. We are checking the map before insertion because we want the index to be as minimum as possible and so we will consider the earliest index where the sum x-k has occurred. [Detailed discussion in the edge case section]</li>
    </ul>
</ul>

<p><strong>Edge Case</strong></p>
<p>If there are zeros and negative values present in given array, then prefix sum will have same sum at different places.</p>
<p>So,since we are trying to find out maximum length, we have ti consider the first prefix as considerable</p>
<p>so, we will add prefix sum only once, since we are coming from starting position, we will add its first occurance</p>
<p>Inorder to overcome its second occurance, we will check if it is already existed or not, if its there, we won't add it again</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-13-005443.png">
<p>In steps 2 and 3 the element at index i is 0. So, in those steps, the prefix sum remains the same but the index is getting updated in the map. Now, when index i reaches the end, it calculates the length i.e. i-preSumMap[rem] = 3-2 = 1. Here it is considering only the subarray [3] which is incorrect as the longest subarray we can get is [0, 0, 3] and hence the length should be 3.</p>
<p>Now, to avoid this edge case i.e. to maximize the calculated length, we need to observe the formula we are using to calculate the length i.e. len = i - preSumMap[rem].</p>
<p>Now, if we minimize the term preSumMap[rem] (i.e. the index where the subarray with sum x-k ends), we will get the maximum length. That is why we will consider only the first or the leftmost index where the subarray with sum x-k ends. After that, we will not update that particular index even if we get a similar subarray ending at a later index.</p>
<p>So, we will check the map before inserting the prefix sum. If it already exists in the map, we will not update it but if it is not present, we will insert it for the first time.</p>

```python
def optimized1(n,arr,k):
    prefix={}
    largest=0
    sum=0
    for i in range(n):
        sum+=arr[i]
        if(sum==k):
            largest=max(largest,i+1)
        rem=sum-k
        if(rem in prefix):
            length=i-prefix[rem]
            largest=max(largest,length)
        if sum not in prefix:
            prefix[sum]=i
    return largest

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(optimized1(n,arr,k))
```

<p>Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.</p>
<p>Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N)(though in the worst case, unordered_map takes O(N) to find an element and the time complexity becomes O(N2)) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array.</p>

<p>Space Complexity: O(N) as we are using a map data structure.</p>


<p><strong>Optimal Approach 2 (only for positive values)</strong></p>
<p>In this, we can use two pointer approach</p>
<p>We can use two pointers left and right, intially we will place them at 0 position, we will try to move right pointer forward direction and we will add elements to sum as we are moving forward</p>
<p>When sum equals to k, then subarray from left to right might be our answer, so we can find length and track its length</p>
<p>When sum crosses k, that means we have to reduce elements, so we will move left pointer forward and reduce the sum by left elements</p>
<p>As, above process continues, we can have multiple subarrays whose sum equals to k, among all possible lengths, we will take the largest as our answer</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-13-012512.png">
<ul>
    <li>First, we will take two pointers: left and right, initially pointing to the index 0.</li>
    <li>The sum is set to a[0] i.e. the first element initially.</li>
    <li>Now we will run a while loop until the right pointer crosses the last index i.e. n-1.</li>
    <li>Inside the loop, we will do the following:</li>
    <ul>
        <li>We will use another while loop and it will run until the sum is lesser or equal to k.</li>
        <ul>
            <li>Inside this second loop, from the sum, we will subtract the element that is pointed by the left pointer and increase the left pointer by 1.</li>
        </ul>
        <li>After this loop gets completed, we will check if the sum is equal to k. If it is, we will compare the length of the current subarray i.e. (right-left+1) with the existing one and consider the maximum one.</li>
        <li>Then we will move forward the right pointer by 1. If the right pointer is pointing to a valid index(< n) after the increment, we will add the element i.e. a[right] to the sum.</li>
    </ul>
    <li>Finally, we will return the maximum length.</li>
</ul>

```python
def optimized2(n,arr,k):
    largest=0
    left,right=0,0
    sum=arr[0]
    while right<n:

        while (left<=right and sum>k):
            sum-=arr[left]
            left-=1

        if(sum==k):
            length=right-left+1
            largest=max(largest,length)

        right+=1
        if(right<n):
            sum+=arr[right]
    return largest
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(optimized2(n,arr,k))  
```

<p>Time Complexity: O(2*N), where N = size of the given array.</p>
<p>Reason: The outer while loop i.e. the right pointer can move up to index n-1(the last index). Now, the inner while loop i.e. the left pointer can move up to the right pointer at most. So, every time the inner loop does not run for n times rather it can run for n times in total. So, the time complexity will be O(2*N) instead of O(N2).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>


<h2>Count Subarray sum Equals K</h2>
<p>Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.</p>
<p>A subarray is a contiguous non-empty sequence of elements within an array.</p>
<p><strong>Examples</strong></p>
<p>Input :  N = 4, array[] = {3, 1, 2, 4}, k = 6</p>
<p>Output : 2</p>
<p>Explanation :  The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].</p>
<p>Input :  N = 3, array[] = {1,2,3}, k = 3</p>
<p>Output : 2</p>
<p>Explanation : The subarrays that sum up to 3 are [1, 2], and [3].</p>

<p><strong>Solution</strong></p>
<p>This problem can solved in several approaches</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we can all possible subarrays and find sum for each subarray, then if sum equals to k, then imcrease count</p>
<p>In this way, we can get the final answer</p>

```python
def bruteForce(n,arr,k):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            s=0
            for l in range(i,j+1):
                s+=arr[l]
            if(s==k):
                cnt+=1
    return cnt
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
```

<p>Time Complexity: O(N3), where N = size of the array.</p>
<p>Reason: We are using three nested loops here. Though all are not running for exactly N times, the time complexity will be approximately O(N3).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Better Approach</strong></p>
<p>In this approach, we will modify the existing approach eliminate the 3rd inner loop to find sum for each subarray</p>
<p>If we carefully observe, we can notice that to get the sum of the current subarray we just need to add the current element(i.e. arr[j]) to the sum of the previous subarray i.e. arr[i….j-1].</p>
<p>Assume previous subarray = arr[i……j-1]</p>
<p>current subarray = arr[i…..j]</p>
<p>Sum of arr[i….j] = (sum of arr[i….j-1]) + arr[j]</p>
<p>This is how we can remove the third loop and while moving the j pointer, we can calculate the sum. this can reduce our complexity</p>

```python
def better(n,arr,k):
    cnt=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            if(s==k):
                cnt+=1
    return cnt
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(better(n,arr,k))
```

<p>Time Complexity: O(N2), where N = size of the array.</p>
<p>Reason: We are using two nested loops here. As each of them is running for exactly N times, the time complexity will be approximately O(N2).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Optimized approach</strong></p>
<p>In this approach, we will use the concept of prefix sum</p>
<p>Here, the prefix sum of a subarray ending at index i, simply means the sum of all the elements of that subarray.</p>
<p>Assume, the prefix sum of a subarray ending at index i is x. In that subarray, we will search for another subarray ending at index i, whose sum equals k</p>
<p>Here, we need to observe that if there exists another subarray ending at index i with sum k, then the prefix sum of the rest of the subarray will be x-k. The below image will clarify the concept:</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/04/Screenshot-2023-04-13-004939.png">
<p>Now, for a subarray ending at index i with the prefix sum x, if we remove the part with the prefix sum x-k, we will be left with the part whose sum is equal to k. And that is what we want.</p>

<p>Now, there may exist multiple subarrays with the prefix sum x-k. So, the number of subarrays with sum k that we can generate from the entire subarray ending at index i, is exactly equal to the number of subarrays with the prefix sum x-k, that we can remove from the entire subarray.</p>
<p>n the map, we will store every prefix sum calculated, with its occurrence in a <key, value> pair. Now, at index i, we just need to check the map data structure to get the number of times that the subarrays with the prefix sum x-k occur. Then we will simply add that number to our answer.</p>
<p>We will apply the above process for all possible indices of the given array. The possible values of the index i can be from 0 to n-1(where n = size of the array).</p>

<ul>
    <li>First, we will declare a map to store the prefix sums and their counts.</li>
    <li>Then, we will set the value of 0 as 1 on the map.</li>
    <li>Then we will run a loop(say i) from index 0 to n-1(n = size of the array).</li>
    <li>For each index i, we will do the following:</li>
    <ul>
        <li>We will add the current element i.e. arr[i] to the prefix sum.</li>
        <li>We will calculate the prefix sum i.e. x-k, for which we need the occurrence.</li>
        <li>We will add the occurrence of the prefix sum x-k i.e. mpp[x-k] to our answer.</li>
        <li>Then we will store the current prefix sum in the map increasing its occurrence by 1.</li>
    </ul>
</ul>

<p><strong>Why do we need to set the value of 0?</strong></p>
<p>Let’s understand this using an example. Assume the given array is [3, -3, 1, 1, 1] and k is 3</p>
<p>Now, for index 0, we get the total prefix sum as 3, and k is also 3. So, the prefix sum of the remove-part should be x-k = 3-3 = 0. Now, if the value is not previously set for the key 0 in the map, we will not count that subarray and it will not add to final answer.</p>
<p>This will mean that we have not found any subarray with sum 3 till now. But this should not be the case as index 0 itself is a subarray with sum k i.e. 3.</p>
<p>This will mean that we have not found any subarray with sum 3 till now. But this should not be the case as index 0 itself is a subarray with sum k i.e. 3.</p>

```python
def optimized(n,arr,k):
    prefixCnt={0:1}
    s=0
    cnt=0
    for i in range(n):
        s+=arr[i]
        rem=s-k
        if rem in prefixCnt:
            cnt+=prefixCnt[rem]
        if s in prefixCnt:
            prefixCnt[s]+=1
        else:
            prefixCnt[s]=1

    return cnt

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(optimized(n,arr,k))
```

<p>Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.</p>
<p>Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array.</p>
<p>Space Complexity: O(N) as we are using a map data structure.</p>


<h2>Count the number of subarrays with given xor K</h2>
<p>Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.</p>
<p><strong>Examples</strong></p>
<p>Input :  A = [4, 2, 2, 6, 4] , k = 6</p>
<p>Output : 4</p>
<p>Explanation :  The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]</p>

<p>Input :  A = [5, 6, 7, 8, 9], k = 5</p>
<p>Output : 2</p>
<p>Explanation :  The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]</p>

<p><strong>Solution</strong></p>
<p>This problem completely similar to previous problem "Count Subarray sum Equals K"</p>
<p>In this problem, we have to find xor value instead of sum</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we will find all possible sub arrays with given array and find its xor value</p>
<p>if any xor value equals to given k value, we will track count of it</p>

```python
def bruteForce(n,arr,k):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            xr=0
            for l in range(i,j+1):
                xr^=arr[l]
            if(xr==k):
                cnt+=1
    return cnt

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
```

<p>Time Complexity: O(N3) approx., where N = size of the array.</p>
<p>Reason: We are using three nested loops, each running approximately N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Better Approach</strong></p>
<p>This approach, slight modification to previous appoach, to remove the nested 3rd loop</p>
<p>If we carefully observe, we can notice that to get the XOR of the current subarray we just need to XOR the current element(i.e. arr[j]) to the XOR of the previous subarray i.e. arr[i….j-1].</p>
<p>Assume previous subarray = arr[i……j-1]</p>
<p>current subarray = arr[i…..j]</p>
<p>XOR of arr[i….j] = (XOR of arr[i….j-1]) ^ arr[j]</p>
<p>This is how we can remove the third loop and while moving j pointer, we can calculate the XOR.</p>

```python
def better(n,arr,k):
    cnt=0
    for i in range(n):
        xr=0
        for j in range(i,n):
            xr^=arr[j]
            if(xr==k):
                cnt+=1
    return cnt

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(better(n,arr,k))
```

<p>Time Complexity: O(N2), where N = size of the array.</p>
<p>Reason: We are using two nested loops here. As each of them is running for N times, the time complexity will be approximately O(N2).</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>Optimized approach</strong></p>
<p>In this approach, we are going to use the concept of the prefix XOR to solve this problem.</p>
<p>Here, the prefix XOR of a subarray ending at index i, simply means the XOR of all the elements of that subarray.</p>
<p>Assume, the prefix XOR of a subarray ending at index i is xr. In that subarray, we will search for another subarray ending at index i, whose XOR is equal to k. Here, we need to observe that if there exists another subarray ending at index i, with XOR k, then the prefix XOR of the rest of the subarray will be xr^k. The below image will clarify the concept</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/05/Screenshot-2023-05-02-011455.png">
<p>Now, for a subarray ending at index i with the prefix XOR xr, if we remove the part with the prefix XOR xr^k, we will be left with the part whose XOR is equal to k. And that is what we want.</p>
<p>Now, for a subarray ending at index i with the prefix XOR xr, if we remove the part with the prefix XOR xr^k, we will be left with the part whose XOR is equal to k. And that is what we want.</p>
<p>So, for a subarray ending at index i, instead of counting the subarrays with XOR k, we can count the subarrays with the prefix XOR xr^k present in it.</p>
<p>That is why, instead of searching the subarrays with XOR k, we will keep the occurrence of the prefix XOR of the subarrays using a map data structure. </p>
<p>In the map, we will store every prefix XOR calculated, with its occurrence in a <key, value> pair. Now, at index i, we just need to check the map data structure to get the number of times that the subarrays with the prefix XOR xr^k occur. Then we will simply add that number to our count.</p>
<p>We will apply the above process for all possible indices of the given array. The possible values of the index i can be from 0 to n-1(where n = size of the array).</p>

<ul>
    <li>First, we will declare a map to store the prefix XORs and their counts.</li>
    <li>Then, we will set the value of 0 as 1 on the map.</li>
    <li>Then we will run a loop(say i) from index 0 to n-1(n = size of the array).</li>
    <li>For each index i, we will do the following:</li>
    <ul>
        <li>We will XOR the current element i.e. arr[i] to the existing prefix XOR.</li>
        <li>Then we will calculate the prefix XOR i.e. xr^k, for which we need the occurrence.</li>
        <li>We will add the occurrence of the prefix XOR xr^k i.e. mpp[xr^k] to our answer.</li>
        <li>Then we will store the current prefix XOR, xr in the map increasing its occurrence by 1.</li>
    </ul>
</ul>
<p><strong>Why do we need to set the value of 0 beforehand?</strong></p>
<p>Question: Why do we need to set the value of 0 beforehand?
Let’s understand this using an example. Assume the given array is [3, 3, 1, 1, 1] and k is 3. Now, for index 0, we get the total prefix XOR as 3, and k is also 3. So, the prefix XOR xr^k will be = 3^3 = 0. Now, if the value is not previously set for the key 0 in the map, we will get the default value 0 and we will add 0 to our answer. This will mean that we have not found any subarray with XOR 3 till now. But this should not be the case as index 0 itself is a subarray with XOR k i.e. 3.</p>
<p>So, in order to avoid this situation we need to set the value of 0 as 1 on the map beforehand.</p>

```python
def optimized(n,arr,k):
    prefixCnt={0:1}
    xr=0
    cnt=0
    for i in range(n):
        xr^=arr[i]
        x=xr^k
        if x in prefixCnt:
            cnt+=prefixCnt[x]
        if xr in prefixCnt:
            prefixCnt[xr]+=1
        else:
            prefixCnt[xr]=1
    return cnt

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(optimized(n,arr,k))
```

<p>Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the arra</p>
<p>Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array. Point to remember for unordered_map in the worst case, the searching time increases to O(N), and hence the overall time complexity increases to O(N2). </p>
<p>Space Complexity: O(N) as we are using a map data structure.</p>


<h2>3 Sum : Find triplets that add up to a zero</h2>
<p> Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.</p>
<p><strong>Examples</strong></p>
<p>input :  nums = [-1,0,1,2,-1,-4]</p>
<p>output :  [[-1,-1,2],[-1,0,1]]</p>
<p>explanation : Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k</p>
<p>input :  nums=[-1,0,1,0]</p>
<p>output : Output: [[-1,0,1],[-1,1,0]]</p>
<p>explanation : Out of all possible unique triplets possible, [-1,0,1] and [-1,1,0] satisfy the condition of summing up to zero with i!=j!=k</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>

<p><strong>BruteForce Approach</strong></p>
<p>In the question, it is clearly stated that for each case the picked indices i.e. i, j, and k must be distinct. This means [arr[1], arr[1], arr[2]] is not a valid triplet and also remember [arr[1], arr[0], arr[2]] and [arr[0], arr[1], arr[2]] will be considered the same.</p>
<p>In this approach, we will find out all possible triplets whose sum equals to zero and we will sort each triplet and store it in a set, so duplicate unique triplets will not occur anymore</p>
<ul>
    <li>Initialize an empty set ans: This will store unique triplets that sum to zero.</li>
    <li>Triple nested loops: These loops iterate over all possible triplets (i, j, k) in the array.</li>
    <li>Check if the sum of the triplet is zero: If the sum of arr[i], arr[j], and arr[k] is zero, proceed.</li>
    <li>Sort and add the triplet to the set: Convert the triplet to a sorted tuple and add it to the set ans to ensure uniqueness.</li>
    <li>Return the result as a list: Convert the set ans to a list and return it.</li>
</ul>

```python
def bruteForce(n, arr):
    ans = set()
    # Iterate over all possible triplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if the triplet sums to zero
                if (arr[i] + arr[j] + arr[k]) == 0:
                    # Sort the triplet and add it to the set
                    temp = sorted([arr[i], arr[j], arr[k]])
                    ans.add(tuple(temp))
    # Convert the set to a list and return it
    return list(ans)

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```

<p>Time Complexity: O(N3 * log(no. of unique triplets)), where N = size of the array.</p>
<p>Reason: Here, we are mainly using 3 nested loops. And inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.</p>
<p>Space Complexity: O(2 * no. of the unique triplets) as we are using a set data structure and a list to store the triplets.</p>
<p><strong>Better Approach</strong></p>
<p>In the previous approach, we utilized 3 loops, but now our goal is to reduce it to 2 loops. To achieve this, we need to find a way to calculate arr[k] since we intend to eliminate the third loop (k loop). To calculate arr[k], we can derive a formula as follows</p>
<p>Since loop one will give arr[i] and loop two will give arr[j], then 3rd values of triplet will be target-(arr[i]+arr[j]), here target is 0, hence third value will be -(arr[i]+arr[j])</p>
<p>We will just apply two sum problem optimized approach here to find out third value</p>
<p>So, we will first calculate arr[i] and arr[j] using 2 loops and for the third one i.e. arr[k] we will not use another loop and instead we will look up the value 0-(arr[i]+arr[j]+arr[k]) in the set data structure. Thus we can remove the third loop from the algorithm.</p>

<ul>
    <li>Initialize an empty set ans: This set will store unique triplets that sum to zero.</li>
    <li>Outer loop: Iterate over each element in the array. For each element, initialize an empty hash set s.</li>
    <li>Inner loop: Iterate over the elements following the current element in the outer loop.</li>
    <ul>
        <li>Calculate the required third element that, together with the current two elements, sums to zero.</li>
        <li>If this third element is already in the set s, it means a valid triplet has been found.</li>
        <li>Sort the triplet and add it to the set ans as a tuple to ensure uniqueness.</li>
        <li>Add the current element to the set s for future checks.</li>
    </ul>
</ul>

```python
def better(n, arr):
    ans = set()
    # Iterate over the array
    for i in range(n):
        s = set()
        # Iterate over the rest of the array starting from the next element
        for j in range(i + 1, n):
            third = -(arr[i] + arr[j])
            # Check if the third element is in the set
            if third in s:
                temp = sorted([arr[i], arr[j], third])
                ans.add(tuple(temp))  # Add the sorted triplet as a tuple to the set
            s.add(arr[j])  # Add the current element to the set
    return list(ans)  # Convert the set to a list and return it

arr=list(map(int,input().split()))
n=len(arr)
print(better(n,arr))
```

<p>Time Complexity: O(N2*log(M)), where N = size of the array, M = no. of elements in the set.</p>
<p>Reason: Here, we are mainly using 2 nested loops, and inside the loops there are some operations on the set data structure which take log(M) time complexity.</p>
<p>Space Complexity: O(2 * no. of the unique triplets) + O(N) as we are using a set data structure and a list to store the triplets and extra O(N) for storing the array elements in another set.</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, we will use two pointer approach to solve the problem</p>
<p>In this approach, we intend to get rid of two things i.e. the HashSet we were using for the look-up operation and the set data structure used to store the unique triplets.</p>
<p>So, We will first sort the array. Then, we will fix a pointer i, and the rest 2 pointers j and k will be moving. </p>
<p>Now, we need to first understand what the HashSet and the set were doing to make our algorithm work without them. So, the set data structure was basically storing the unique triplets in sorted order and the HashSet was used to search for the third element.</p>
<p>That is why, we will first sort the entire array, and then to get the unique triplets, we will simply skip the duplicate numbers while moving the pointers.</p>
<p><strong>How to Skip Duplicate Elements</strong></p>
<p>As the entire array is sorted, the duplicate numbers will be in consecutive places. So, while moving a pointer, we will check the current element and the adjacent element. Until they become different, we will move the pointer by 1 place. We will follow this process for all 3 pointers. Thus, we can easily skip the duplicate elements while moving the pointers.</p>
<p>Now, we can also remove the HashSet as we have two moving pointers i.e. j and k that will find the appropriate value of arr[j] and arr[k]. So, we do not need that HashSet anymore for the look-up operations.</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/07/Screenshot-2023-07-27-001839.png">

<ol>
    <li>Sorting the Array: The array is sorted first. This helps in easily avoiding duplicates and using the two-pointer technique.</li>
    <li>Outer Loop: The outer loop iterates through the array with index i. For each element arr[i], it considers it as the first element of the triplet.</li>
    <li>Skip Duplicates: To avoid duplicate triplets, if the current element is the same as the previous one, the loop continues to the next iteration.</li>
    <li>Two-pointer Technique: Two pointers, j and k, are initialized. j starts just after i and k starts at the end of the array. The goal is to find two numbers such that their sum with arr[i] is zero.</li>
    <ul>
        <li>Move Pointers: Depending on the sum of arr[i], arr[j], and arr[k], move the pointers to find a triplet that sums to zero:</li>
        <ul>
            <li>If the sum is less than zero, increment j.</li>
            <li>If the sum is greater than zero, decrement k.</li>
            <li>If the sum is zero, add the triplet to the set ans and move both pointers inward while skipping duplicates.</li>
        </ul>
    </ul>
    <li>Skip Duplicate Elements: After finding a triplet, both pointers are moved inward while skipping duplicate elements to avoid counting the same triplet multiple times.</li>
    <li>Return Unique Triplets: Finally, the set ans containing unique triplets is returned.</li>
</ol>

<p>We can remove set and don't need to sort it, since array is sorted already</p>

```python
def optimized(n,arr):
    ans=[]
    arr.sort()
    for i in range(n):
        if(i!=0 and arr[i]==arr[i-1]):
            continue
        j,k=i+1,n-1
        while(j<k):
            sum=arr[i]+arr[j]+arr[k]
            if(sum<0):
                j+=1
            elif(sum>0):
                k-=1
            else:
                temp=[arr[i],arr[j],arr[k]]
                ans.append(temp)
                j+=1
                k-=1
                while(j<k and arr[j]==arr[j-1]):
                    j+=1
                while(k>j and arr[k]==arr[k+1]):
                    k-=1
    return ans

arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```
<p>Time Complexity: O(NlogN)+O(N2), where N = size of the array.</p>
<p>Reason: The pointer i, is running for approximately N times. And both the pointers j and k combined can run for approximately N times including the operation of skipping duplicates. So the total time complexity will be O(N2). </p>
<p>Space Complexity: O(no. of quadruplets), This space is only used to store the answer. We are not using any extra space to solve this problem. So, from that perspective, space complexity can be written as O(1).</p>



<h2>4 Sum - Find Quads that add up to a target value</h2>
<p>Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.</p>
<p><strong>Examples</strong></p>
<p>input :  arr[] = [1,0,-1,0,-2,2], target = 0</p>
<p>output :  [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]</p>
<p>explanation :  We have to find unique quadruplets from the array such that the sum of those elements is equal to the target sum given that is 0. The result obtained is such that the sum of the quadruplets yields 0.</p>
<p>input : arr[] = [4,3,3,4,4,2,1,2,1,1], target = 9</p>
<p>output : [[1,1,3,4],[1,2,2,4],[1,2,3,3]]</p>
<p>explanation :  The sum of all the quadruplets is equal to the target i.e. 9.</p>

<p><strong>Solution</strong></p>
<p>This problem, is completely similar to the previous problem</p>

<p><strong>BruteForce Approach</strong></p>
<p>In the question, it is clearly stated that for each case the picked indices i.e. i, j, k and l must be distinct. This means [arr[1], arr[1], arr[2], arr[3]] is not a valid triplet and also remember [arr[1], arr[0], arr[2], arr[3]] and [arr[0], arr[1], arr[2], arr[4]] will be considered the same.</p>
<p>In this approach, we will find out all possible quadruplets whose sum equals to target and we will sort each quadruplets and store it in a set, so duplicate unique quadruplets will not occur anymore</p>
<ul>
    <li>Initialize an empty set ans: This will store unique quadruplets that sum to target.</li>
    <li>four nested loops: These loops iterate over all possible triplets (i, j, k, l) in the array.</li>
    <li>Check if the sum of the triplet is zero: If the sum of arr[i], arr[j], and arr[k] is zero, proceed.</li>
    <li>Sort and add the quadruplets to the set: Convert the quadruplets to a sorted tuple and add it to the set ans to ensure uniqueness.</li>
    <li>Return the result as a list: Convert the set ans to a list and return it.</li>
</ul>

```python
def bruteForce(n, arr, target):
    ans = set()
    # Iterate over all possible quadruplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    sum = arr[i] + arr[j] + arr[k] + arr[l]
                    # Check if the quadruplet sums to the target
                    if sum == target:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        temp.sort()  # Sort the quadruplet
                        ans.add(tuple(temp))  # Add the sorted tuple to the set
    return ans  # Return the set of unique quadruplets
arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(bruteForce(n,arr,target))
```

<p>Time Complexity: O(N4), where N = size of the array.</p>
<p>Reason: Here, we are mainly using 4 nested loops. But we not considering the time complexity of sorting as we are just sorting 4 elements every time.</p>
<p>Space Complexity: O(2 * no. of the quadruplets) as we are using a set data structure and a list to store the quads.</p>

<p><strong>Better Approach</strong></p>
<p>In the previous approach, we utilized 4 loops, but now our goal is to reduce it to 3 loops. To achieve this, we need to find a way to calculate arr[l] since we intend to eliminate the fourth loop (l loop). To calculate arr[l], we can derive a formula as follows</p>
<p>Since loop one will give arr[i] and loop two will give arr[j] and loop three will give arr[k], then 4th values of quadruplets will be target-(arr[i]+arr[j]+arr[k]), hence third value will be target-(arr[i]+arr[j])</p>
<p>We will just apply two sum problem optimized approach here to find out fourth value</p>
<p>So, we will first calculate arr[i],arr[j] and arr[k] using 3 loops and for the fourth one i.e. arr[l] we will not use another loop and instead we will look up the value target-(arr[i]+arr[j]+arr[k]) in the set data structure. Thus we can remove the fourth loop from the algorithm.</p>

<ul>
    <li>Initialize an Empty Set ans: This set will store unique quadruplets that sum to the target value.</li>
    <li>Outer Loop: Iterate over each element in the array with index i.</li>
    <li>Second Loop: For each element arr[i], iterate over the elements after it with index j.</li>
    <li>HashSet s: A HashSet s is used to store elements that have been seen so far between indices j and k. This helps in quickly checking if the required fourth element exists.</li>
    <li>Check for Fourth Element: For each pair (i, j), and each element k after j, the function calculates the required fourth element (fourth = target - (arr[i] + arr[j] + arr[k])). If fourth is found in the HashSet s, it means a valid quadruplet is found.</li>
    <li>Store Unique Quadruplets: The quadruplet [arr[i], arr[j], arr[k], fourth] is sorted and added to the set ans to ensure uniqueness.</li>
    <li>Add Current Element to HashSet: The current element arr[k] is added to the HashSet s for future checks.</li>
    <li>Return the Result as a Set: Finally, the set ans containing unique quadruplets is returned directly.</li>
</ul>

```python
def better(n, arr, target):
    ans = set()
    # Iterate over all pairs (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            s = set()
            # Iterate over all elements after j
            for k in range(j + 1, n):
                fourth = target - (arr[i] + arr[j] + arr[k])
                # Check if the fourth element is in the set
                if fourth in s:
                    temp = sorted([arr[i], arr[j], arr[k], fourth])
                    ans.add(tuple(temp))  # Add the sorted quadruplet as a tuple to the set
                s.add(arr[k])  # Add the current element to the set
    return ans  # Return the set of unique quadruplets


arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(better(n,arr,target))
```

<p>Time Complexity: O(N3*log(M)), where N = size of the array, M = no. of elements in the set.</p>
<p>RReason: Here, we are mainly using 3 nested loops, and inside the loops there are some operations on the set data structure which take log(M) time complexity.</p>
<p>Space Complexity: O(2 * no. of the quadruplets)+O(N)</p>
<p>Reason: we are using a set data structure and a list to store the quads. This results in the first term. And the second space is taken by the set data structure we are using to store the array elements. At most, the set can contain approximately all the array elements and so the space complexity is O(N).</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, we are using two pointer approach similar to previous problem</p>

<ol>
    <li>Sorting the Array: The array is sorted first. This helps in easily avoiding duplicates and using the two-pointer technique.</li>
    <li>Outer Loop: The outer loop iterates through the array with index i. For each element arr[i], it considers it as the first element of the quadruplet.</li>
    <ul>
        <li>Skip Duplicates: To avoid duplicate quadruplets, if the current element is the same as the previous one, the loop continues to the next iteration.</li>
    </ul>
    <li>Second Loop: For each element arr[i], the inner loop iterates over the elements after it with index j.</li>
    <ul>
        <li>Skip Duplicates: Similarly, to avoid duplicate quadruplets, if the current element is the same as the previous one, the loop continues to the next iteration.</li>
    </ul>
    <li>Two-pointer Technique: Two pointers, k and l, are initialized. k starts just after j and l starts at the end of the array. The goal is to find two numbers such that their sum with arr[i] and arr[j] equals the target value.</li>
    <ul>
        <li>Move Pointers: Depending on the sum of arr[i], arr[j], arr[k], and arr[l], move the pointers to find a quadruplet that sums to the target:</li>
        <ul>
            <li>If the sum is less than the target, increment k.</li>
            <li>If the sum is greater than the target, decrement l.</li>
            <li>If the sum is equal to the target, add the quadruplet to the list ans and move both pointers inward while skipping duplicates.</li>
        </ul>
    </ul>
    <li>Skip Duplicate Elements: After finding a quadruplet, both pointers are moved inward while skipping duplicate elements to avoid counting the same quadruplet multiple times.</li>
    <li>Return Unique Quadruplets: Finally, the list ans containing unique quadruplets is returned.</li>
</ol>

```python
def optimized(n, arr, target):
    ans = []
    arr.sort()  # Sort the array to use the two-pointer technique
    for i in range(n):
        # Skip duplicate elements to avoid duplicate quadruplets
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, n):
            # Skip duplicate elements to avoid duplicate quadruplets
            if j != i + 1 and arr[j] == arr[j - 1]:
                continue
            k, l = j + 1, n - 1  # Initialize two pointers
            while k < l:
                sum = arr[i] + arr[j] + arr[k] + arr[l]
                if sum < target:
                    k += 1  # Move the left pointer to the right
                elif sum > target:
                    l -= 1  # Move the right pointer to the left
                else:
                    temp = [arr[i], arr[j], arr[k], arr[l]]  # Quadruplet found
                    ans.append(tuple(temp))
                    k += 1
                    l -= 1
                    # Skip duplicate elements to avoid duplicate quadruplets
                    while k < l and arr[k] == arr[k - 1]:
                        k += 1
                    while l > k and arr[l] == arr[l + 1]:
                        l -= 1
    return ans  # Return the list of unique quadruplets
arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(optimized(n,arr,target))

```


<p>Time Complexity: O(N3)+O(nlogn), where N = size of the array.</p>
<p>Reason: Each of the pointers i and j, is running for approximately N times. And both the pointers k and l combined can run for approximately N times including the operation of skipping duplicates. So the total time complexity will be O(N3) and arr is sorted once , for that o(nLogn). </p>
<p>Space Complexity: O(no. of quadruplets), This space is only used to store the answer. We are not using any extra space to solve this problem. So, from that perspective, space complexity can be written as O(1).</p>


<h2>Find the repeating and missing numbers</h2>
<p>You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.</p>
<p><strong>Examples : </strong></p>
<p>input : array[] = {3,1,2,5,3}</p>
<p>output : {3,4}</p>
<p>A = 3 , B = 4 Since 3 is appearing twice and 4 is missing</p>
<p>input : array[] = {3,1,2,5,4,6,7,5}</p>
<p>output : {5,8}</p>
<p>A = 5 , B = 8 Since 5 is appearing twice and 8 is missing</p>

<p><strong>Solution</strong></p>
<p>this problem can be solved in several approaches</p>
<p><strong>bruteForce(n, arr):</strong></p>
<ul>
  <li><p><strong>Set Up:</strong> Start with no missing or repeating numbers (<code>missing</code> and <code>repeating</code> are <code>None</code>).</p></li>
  <li><p><strong>Check Each Number:</strong> For each number from 1 to <code>n</code>:
    <ul>
      <li><p>Count how many times this number is in the list.</p></li>
      <li><p>If it's not there, it's the missing number.</p></li>
      <li><p>If it's there twice, it's the repeating number.</p></li>
      <li><p>Stop if you've found both numbers.</p></li>
    </ul>
  </p></li>
  <li><p><strong>Return Result:</strong> Return the repeating and missing numbers.</p></li>
</ul>
<p><strong>Simple Idea:</strong> Look for each number in the list. The one that's missing is the missing number, and the one that appears twice is the repeating number.</p>

```python
def bruteForce(n,arr):
    missing,repeating=None,None
    for i in range(1,n+1):
        cnt=0
        for j in range(n):
            if(arr[j]==i):
                cnt+=1
        if(cnt==0):
            missing=i
        if(cnt==2):
            repeating=i
        if(missing and repeating):
            break
    return [repeating,missing

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```

<p>Time Complexity: O(N2), where N = size of the given array.</p>
<p>Reason: Here, we are using nested loops to count occurrences of every element between 1 to N.</p>
<p>Space Complexity: O(1) as we are not using any extra space.</p>

<p><strong>better(n, arr):</strong></p>
<ul>
  <li><p><strong>Set Up:</strong> Use a dictionary to count appearances of each number. Start with no missing or repeating numbers.</p></li>
  <li><p><strong>Count Appearances:</strong> Go through each number in the list:
    <ul>
      <li><p>If the number is already in the dictionary, it appears twice (so it's the repeating number).</p></li>
      <li><p>If not, add it to the dictionary.</p></li>
    </ul>
  </p></li>
  <li><p><strong>Find Missing:</strong> Check each number from 1 to <code>n</code>:
    <ul>
      <li><p>If a number isn't in the dictionary, it's the missing number.</p></li>
    </ul>
  </p></li>
  <li><p><strong>Return Result:</strong> Return the repeating and missing numbers.</p></li>
</ul>
<p><strong>Simple Idea:</strong> Use a dictionary to count how many times each number appears. The one that appears twice is the repeating number. Then, find the number that isn't in the dictionary (the missing number).</p>



```python
def better(n,arr):
    count={}
    missing,repeating=None,None
    for i in range(n):
        if arr[i] in count:
            count[arr[i]]+=1
        else:
            count[arr[i]]=1
        if(count[arr[i]]==2):
            repeating=arr[i]
    for i in range(1,n+1):
        if i not in count:
            missing=i
            break
    return [repeating,missing]
```

<p>Time Complexity: O(2N), where N = the size of the given array.</p>
<p>Reason: We are using two loops each running for N times. So, the time complexity will be O(2N).</p>
<p>Space Complexity: O(N) as we are using a hash array to solve this problem.</p>

<p><strong>optimized(n, arr):</strong></p>
<ul>
  <li><p><strong>Calculate Expected Sums:</strong> Calculate what the sum of numbers from 1 to <code>n</code> should be.</p></li>
  <li><p><strong>Calculate Actual Sums:</strong> Calculate the actual sum of the numbers in the list.</p></li>
  <li><p><strong>Find Differences:</strong> Find the difference between the actual and expected sums. This helps identify the missing and repeating numbers.</p></li>
  <li><p><strong>Solve for Missing and Repeating:</strong> Use simple math to find the missing and repeating numbers from these differences.</p></li>
  <li><p><strong>Return Result:</strong> Return the repeating and missing numbers.</p></li>
</ul>
<p><strong>Simple Idea:</strong> Use math to compare what the sum of numbers should be and what it actually is. This helps figure out the missing and repeating numbers.</p>

<p>1. Calculate Expected Sum of First <code>n</code> Natural Numbers (<code>s1n</code>):</p>
<ul>
  <li><p><code>s1n = \frac{n \times (n + 1)}{2}</code></p></li>
</ul>

<p>2. Calculate Expected Sum of Squares of First <code>n</code> Natural Numbers (<code>s2n</code>):</p>
<ul>
  <li><p><code>s2n = \frac{n \times (n + 1) \times (2n + 1)}{6}</code></p></li>
</ul>

<p>3. Calculate Actual Sum of Array Elements (<code>s1</code>):</p>
<ul>
  <li><p><code>s1 = \sum_{i=0}^{n-1} arr[i]</code></p></li>
</ul>

<p>4. Calculate Actual Sum of Squares of Array Elements (<code>s2</code>):</p>
<ul>
  <li><p><code>s2 = \sum_{i=0}^{n-1} arr[i]^2</code></p></li>
</ul>

<p>5. Calculate <code>val1</code> (Difference in Sums):</p>
<ul>
  <li><p><code>val1 = s1 - s1n</code></p></li>
</ul>

<p>6. Calculate <code>val2</code> (Difference in Sum of Squares):</p>
<ul>
  <li><p><code>val2 = s2 - s2n</code></p></li>
</ul>

<p>7. Solve for <code>x</code> (Repeating Number) and <code>y</code> (Missing Number):</p>
<ul>
  <li><p><code>val2 = (x^2 - y^2) = (x - y) \times (x + y)</code></p></li>
  <li><p><code>x + y = \frac{val2}{val1}</code></p></li>
  <li><p><code>x = \frac{val1 + \frac{val2}{val1}}{2}</code></p></li>
  <li><p><code>y = x - val1</code></p></li>
</ul>


```python
def optimized(n,arr):
    s1n=(n*(n+1))//2
    s2n=((n*(n+1))*(2*n+1))//6
    s1,s2=0,0
    for i in range(n):
        s1+=arr[i]
        s2+=(arr[i]*arr[i])
    val1=s1-s1n # (x-y)
    val2=s2-s2n # (x^2-y^2) 
    val2=val2//val1 # (x+y)
    x=(val1+val2)//2
    y=x-val1
    return [x,y]
arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```

<p>Time Complexity: O(N), where N = the size of the given array.</p>
<p>Reason: We are using only one loop running for N times. So, the time complexity will be O(N).</p>
<p>Space Complexity: O(1) as we are not using any extra space to solve this problem.</p>


<h2>Maximum Product Subarray in an Array</h2>
<p>Given an array that contains both negative and positive integers, find the maximum product subarray.</p>
<p><strong>Examples</strong></p>
<p>Input : Nums = [1,2,3,4,5,0]</p>
<p>Output : 120</p>
<p>Explanation : In the given array, we can see 1×2×3×4×5 gives maximum product value.</p>
<p>Input : Nums = [1,2,-3,0,-4,-5]</p>
<p>Output : 20</p>
<p>Explanation :  In the given array, we can see (-4)×(-5) gives maximum product value.</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approches</p>

<p><strong>Bruteforce</strong></p>
<p>In this approach, we will find all possible subarrays and calculate product for each subarray</p>
<p>among all products, we will track maximum , that will be our answer</p>

```python
def bruteForce(n,arr):
    maxi=float('-inf')
    for i in range(n):
        for j in range(i,n):
            temp=1
            for k in range(i,j+1):
                temp*=arr[k]
            maxi=max(maxi,temp)
    return maxi
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```

<p>Time Complexity: O(N3)</p>
<p>Reason: We are using 3 nested loops for finding all possible subarrays and their product.</p>
<p>Space Complexity: O(1)</p>
<p>Reason: No extra data structure was used</p>

<p><strong>Better Approach</strong></p>
<p>In this approach, we will just modify existing approach</p>
<p>For finding product of subarrays, we are looping through each subarray evrytime, instead of that, get previous subarray product and multiply with current element will give current prduct of subarray</p>


```python
def better(n,arr):
    maxi=float('-inf')
    for i in range(n):
        temp=1
        for j in range(i,n):
            temp*=arr[j]
            maxi=max(maxi,temp)
    return maxi

arr=list(map(int,input().split()))
n=len(arr)
print(better(n,arr))
```

<p>Time Complexity: O(N2)</p>
<p>Reason: We are using two nested loops</p>
<p>Space Complexity: O(1)</p>
<p>Reason: No extra data structures are used for computation</p>

<p><strong>Optimized Approach</strong></p>
<p>We will optimize the solution through some observations.</p>
<ul>
    <li><strong>If the given array only contains positive numbers</strong>: If this is the case, we can confidently say that the maximum product subarray will be the entire array itself.</li>
    <li><strong>If the given also array contains an even number of negative numbers</strong>: As we know, an even number of negative numbers always results in a positive number. So, also, in this case, the answer will be the entire array itself.</li>
    <li><strong>If the given array also contains an odd number of negative numbers</strong>: Now, an odd number of negative numbers when multiplied result in a negative number. Removal of 1 negative number out of the odd number of negative numbers will leave us with an even number of negatives. Hence the idea is to remove 1 negative number from the result. Now we need to decide which 1 negative number to remove such that the remaining subarray yields the maximum product.</li>
</ul>
<p>For example, the given array is: {3, 2, -1, 4, -6, 3, -2, 6}</p>
<p>We will try to remove each possible negative number and check in which case the subarray yields the maximum product.</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/08/Screenshot-2023-08-05-174139.png">
<ul>
    <li>Upon observation, we notice that each chosen negative number divides the array into two parts.</li>
    <li>The answer will either be the prefix or the suffix of that negative number.</li>
    <li>To find the answer, we will check all possible prefix subarrays (starting from index 0) and all possible suffix subarrays (starting from index n-1).</li>
    <li>The maximum product obtained from these prefix and suffix subarrays will be our final answer.</li>
    <li>If the array contains 0’s as well: We should never consider 0’s in our answer(as considering 0 will always result in 0) and we want to obtain the maximum possible product. So, we will divide the given array based on the location of the 0’s and apply the logic of case 3 for each subarray.</li>
    <li>For example, the given array is: {-2, 3, 4, -1, 0, -2, 3, 1, 4, 0, 4, 6, -1, 4}.</li>
    <ul>
        <li>In this case, we will divide the array into 3 different subarrays based on the 0’s locations. So, the subarrays will be {-2, 3, 4, -1}, {-2, 3, 1, 4}, and {4, 6, -1, 4}.</li>
        <li>In these 3 subarrays, we will apply the logic discussed in case 3. We will get 3 different answers for 3 different subarrays.</li>
        <li>The maximum one among those 3 answers will be the final answer.</li>
    </ul>
</ul>
<p>Summary: In real-life problems, we will not separate out the cases as we did in the observations. Instead, we can directly apply the logic discussed in the 4th observation to any given subarray, and it will automatically handle all the other cases.</p>

<ul>
    <li>We will first declare 2 variables i.e. ‘pre’(stores the product of the prefix subarray) and ‘suff’(stores the product of the suffix subarray). They both will be initialized with 1(as we want to store the product).</li>
    <li>Now, we will use a loop(say i) that will run from 0 to n-1.</li>
    <li>We have to check 2 cases to handle the presence of 0:</li>
    <ul>
        <li>If pre = 0: This means the previous element was 0. So, we will consider the current element as a part of the new subarray. So, we will set ‘pre’ to 1.</li>
        <li>If suff = 0: This means the previous element was 0 in the suffix. So, we will consider the current element as a part of the new suffix subarray. So, we will set ‘suff’ to 1.</li>
    </ul>
    <li>Next, we will multiply the elements from the starting index with ‘pre’ and the elements from the end with ‘suff’. To incorporate both cases inside a single loop, we will do the following:</li>
    <ul>
        <li>We will multiply arr[i] with ‘pre’ i.e. pre *= arr[i].</li>
        <li>We will multiply arr[n-i-1] with ‘suff’ i.e. suff *= arr[n-i-1].</li>
    </ul>
    <li>After each iteration, we will consider the maximum among the previous answer, ‘pre’ and ‘suff’ i.e. max(previous_answer, pre, suff).</li>
    <li>Finally, we will return the maximum product.</li>
</ul>

```python
def optimized(n,arr):
    prefix,suffix,maxi=1,1,float('-inf')
    for i in range(n):
        if(prefix==0):
            prefix=1
        if(suffix==0):
            suffix=1
        prefix=prefix*(arr[i])
        suffix=suffix*(arr[n-i-1])
        maxi=max(maxi,max(prefix,suffix))
    return maxi

arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```

<p>Time Complexity: O(N), N = size of the given array.</p>
<p>Reason: We are using a single loop that runs for N times.</p>
<p>Space Complexity: O(1) as No extra data structures are used for computation.</p>

<p><strong>Optimized Approach 2</strong></p>
<p>In this approach, we will find the maximum product subarray by keeping track of the maximum and minimum products ending at each position in the array</p>
<p>The reason for keeping both the maximum and minimum is that multiplying two negative numbers can produce a positive number, which can be a new maximum.</p>
<p>The key insight is that the product of a subarray can be greatly affected by negative numbers. A single negative number can turn a large positive product into a large negative one, and vice versa.</p>
<p>Therefore, at each step, we need to keep track of both the maximum and minimum products that can end at the current position because a negative number can flip the roles of maximum and minimum when multiplied.</p>
<p>If the current element is zero, any product involving it will be zero. We reset our running products to 1 because any subarray starting from the next element needs to start fresh.</p>

<ul>
    <li>currMin and currMax are initialized to 1. These will store the minimum and maximum products ending at the current position.</li>
    <li>ans is initialized to the maximum value in the array, which handles the case where all elements might be negative or zero.</li>
    <li>For each element arr[i], if the element is zero, reset currMin and currMax to 1 because a product involving zero will reset the product sequence.</li>
    <li>Use a temporary variable temp to store the current value of currMin before updating it. This is necessary because currMin will be updated and its old value is needed to compute currMax.</li>
    <li>currMin is updated to the minimum value among currMax * arr[i], currMin * arr[i], and arr[i]. This considers the case where multiplying by a negative number could change the sign and thus change the minimum to maximum.</li>
    <li>currMax is updated to the maximum value among currMax * arr[i], temp * arr[i], and arr[i].</li>
    <li>ans is updated to the maximum value between ans and currMax. This ensures ans always holds the highest product found so far.</li>
    <li>Finally, the function returns ans, which is the maximum product subarray.</li>
</ul>

```python
def optimized2(n, arr):
    currMin, currMax = 1, 1  # Initialize current min and max products
    ans = max(arr)  # Initialize the answer with the maximum element in the array

    for i in range(n):
        if arr[i] == 0:  # If the current element is zero
            currMin, currMax = 1, 1  # Reset current min and max products
            continue
        
        temp = currMin  # Store the current min value temporarily
        # Update currMin to the minimum product ending at the current position
        currMin = min(currMax * arr[i], currMin * arr[i], arr[i])
        # Update currMax to the maximum product ending at the current position
        currMax = max(currMax * arr[i], temp * arr[i], arr[i])
        # Update the answer to be the maximum value found so far
        ans = max(ans, currMax)
    
    return ans  # Return the maximum product subarray
arr=list(map(int,input().split()))
n=len(arr)
print(optimized2(n,arr))
```

<p>Time Complexity: O(N)</p>
<p>Reason: A single iteration is used.</p>
<p>Space Complexity: O(1)</p>
<p>Reason: No extra data structure is used for computation</p>

<h2>Count inversions in an array</h2>
<p>Given an array of N integers, count the inversion of the array.</p>
<p>What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].</p>

<p><strong>Examples</strong></p>
<p>Input : N = 5, array[] = {1,2,3,4,5}</p>
<p>Output : 0</p>
<p>Explanation : we have a sorted array and the sorted array has 0 inversions as for i < j you will never find a pair such that A[j] < A[i]. More clear example: 2 has index 1 and 5 has index 4 now 1 < 5 but 2 < 5 so this is not an inversion.</p>

<p>Input : N = 5, array[] = {5,4,3,2,1}</p>
<p>Output : 10</p>
<p>Explanation : we have a reverse sorted array and we will get the maximum inversions as for i < j we will always find a pair such that A[j] < A[i]. Example: 5 has index 0 and 3 has index 2 now (5,3) pair is inversion as 0 < 2 and 5 > 3 which will satisfy out conditions and for reverse sorted array we will get maximum inversions and that is (n)*(n-1) / 2.For above given array there is 4 + 3 + 2 + 1 = 10 inversions.</p>

<p>Input : N = 5, array[] = {5,3,2,1,4}</p>
<p>Output : 7</p>
<p>Explanation : There are 7 pairs (5,1), (5,3), (5,2), (5,4),(3,2), (3,1), (2,1) and we have left 2 pairs (2,4) and (1,4) as both are not satisfy our condition. </p>

<p><strong>Example</strong></p>
<p>This problem can be solved in several approaches</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this problem, we have to find count of pairs, (a[i],a[j]) such that a[i]>a[j] where i < j </p>
<p>For example, for the given array: [5,3,2,1,4], (5, 3) will be a valid pair as 5 > 3 and index 0 < index 1. But (1, 4) cannot be valid pair.</p>
<p>In this approach, we run a loop through given array and for each element we can loop through remianing elements next to it, check if any element is there greater then current element, then increase count</p>
<p>Then final count will be our answer</p>

<ol>
    <li><strong>Initialization:</strong></li>
    <ul>
        <li>cnt is initialized to 0 to keep track of the number of inversions.</li>
    </ul>
    <li><strong>Two Nested Loops:</strong></li>
    <ul>
        <li>The outer loop (with index i) iterates through each element of the array.</li>
        <li>The inner loop (with index j) iterates through each element that comes after the element at index i.</li>
        <li>For each pair (i, j), the function checks if arr[i] > arr[j]. If this condition is true, it means there's an inversion, and cnt is incremented by 1.</li>
    </ul>
    <li><strong>Return the Count:</strong></li>
    <ul>
        <li>The function returns the total count of inversions found in the array.</li>
    </ul>
</ol>

```python
def bruteForce(n, arr):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                cnt += 1
    return cnt
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```

<p>Time Complexity: O(N2), where N = size of the given array.</p>
<p>Reason: We are using nested loops here and those two loops roughly run for N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space to solve this problem.</p>

<p><strong>Optimized Approach</strong></p>
<p>In this approach, we will try divide the array into two parts and compare both to calculate possible pairs by sorting each part</p>
<p>Assume two sorted arrays are given i.e. a1[] = {2, 3, 5, 6} and a2[] = {2, 2, 4, 4, 8}. Now, we have to count the pairs i.e. a1[i] and a2[j] such that a1[i] > a2[j].</p>
<p>In order to solve this, we will keep two pointers i and j, where i will point to the first index of a1[] and j will point to the first index of a2[]. Now in each iteration, we will do the following:</p>
<ul>
    <li>If a1[i] <= a2[j]: These two elements cannot be a pair and so we will move the pointer i to the next position. This case is illustrated below:</li>
    <img src="https://static.takeuforward.org/wp/uploads/2023/06/Screenshot-2023-06-08-002847.png">
    <li>Why we moved the i pointer: We know, that the given arrays are sorted. So, all the elements after the pointer j, should be greater than a2[j]. Now, as a1[i] is smaller or equal to a2[j], it is obvious that a1[i] will be smaller or equal to all the elements after a2[j]. We need a bigger value of a1[i] to make a pair and so we move the i pointer to the next position i.e. next bigger value.</li>
    <li>If a1[i] > a2[j]: These two elements can be a pair and so we will update the count of pairs. Now, here, we should observe that as a1[i] is greater than a2[j], all the elements after a1[i] will also be greater than a2[j] and so, those elements will also make pair with a2[j]. So, the number of pairs added will be n1-i (where n1 = size of a1[ ]). Now, we will move the j pointer to the next position. This case is also illustrated below:</li>
    <img src="https://static.takeuforward.org/wp/uploads/2023/06/Screenshot-2023-06-08-004326.png">
</ul>
<p>The above process will continue until at least one of the pointers reaches the end.</p>
<p>Until now, we have figured out how to count the number of pairs in one go if two sorted arrays are given. But in our actual question, only a single unsorted array is given. So, how to break it into two sorted halves so that we can apply the above observation? </p>
<p>We can think of the merge sort algorithm that works in a similar way we want. In the merge sort algorithm, at every step, we divide the given array into two halves and then sort them, and while doing that we can actually count the number of pairs.</p>
<p>Basically, we will use the merge sort algorithm to use the observation in the correct way.</p>
<p>The steps are basically the same as they are in the case of the merge sort algorithm. The change will be just a one-line addition inside the merge() function. Inside the merge(), we need to add the number of pairs to the count when a[left] > a[right].</p>

<p>The steps of the merge() function were the following:</p>
<ul>
    <li>In the merge function, we will use a temp array to store the elements of the two sorted arrays after merging. Here, the range of the left array is low to mid and the range for the right half is mid+1 to high.</li>
    <li>Now we will take two pointers left and right, where left starts from low and right starts from mid+1</li>
    <li>Using a while loop( while(left <= mid && right <= high)), we will select two elements, one from each half, and will consider the smallest one among the two. Then, we will insert the smallest element in the temp array. </li>
    <li>After that, the left-out elements in both halves will be copied as it is into the temp array.</li>
    <li>Now, we will just transfer the elements of the temp array to the range low to high in the original array.</li>
</ul>

<p><strong>Modifications in merge() and mergeSort(): </strong></p>
<ul>
    <li>n order to count the number of pairs, we will keep a count variable, cnt, initialized to 0 beforehand inside the merge().</li>
    <li>While comparing a[left] and a[right] in the 3rd step of merge(), if a[left] > a[right], we will simply add this line:
    cnt += mid-left+1 (mid+1 = size of the left half)</li>
    <li>Now, we will return this cnt from merge() to mergeSort(). </li>
    <li>Inside mergeSort(), we will keep another counter variable that will store the final answer. With this cnt, we will add the answer returned from mergeSort() of the left half, mergeSort() of the right half, and merge().</li>
    <li>Finally, we will return this cnt, as our answer from mergeSort().</li>
</ul>


```python
import math
def merge(arr,low,mid,high):
    left=low
    right=mid+1
    temp=[]
    cnt=0
    while(left<=mid and right<=high):
        if(arr[left] <= arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            cnt+=(mid-left+1)
            right+=1

    while(left<=mid):
        temp.append(arr[left])
        left+=1

    while(right<=high):
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return cnt

def mergeSort(arr,low,high):
    cnt=0
    if(low>=high):
        return cnt
    mid=math.floor((low+high)/2)
    cnt+=mergeSort(arr,low,mid)
    cnt+=mergeSort(arr,mid+1,high)
    cnt+=merge(arr,low,mid,high)
    return cnt

def optimized(n,arr):
    low,high=0,n-1
    return mergeSort(arr,low,high)


arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
```

<p>Time Complexity: O(N*logN), where N = size of the given array</p>
<p>Reason: We are not changing the merge sort algorithm except by adding a variable to it. So, the time complexity is as same as the merge sort.</p>
<p>Space Complexity: O(N), as in the merge sort We use a temporary array to store elements in sorted order.</p>

<h2>Count Reverse Pairs</h2>
<p>Given an array of numbers, you need to return the count of reverse pairs. Reverse Pairs are those pairs where i< j and arr[i]>2*arr[j].</p>
<p><strong>Examples</strong></p>
<p>Input :  N = 5, array[] = {1,3,2,3,1)</p>
<p>Output : 2</p>
<p>Explanation :  The pairs are (3, 1) and (3, 1) as from both the pairs the condition arr[i] > 2*arr[j] is satisfied.</p>

<p>Input :  N = 4, array[] = {3,2,1,4}</p>
<p>Output : 1</p>
<p>Explanation : There is only 1 pair  ( 3 , 1 ) that satisfy the condition arr[i] > 2*arr[j]</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>


<p><strong>BruteForce Approach</strong></p>
<p>In this problem, we have to find count of pairs, (a[i],a[j]) such that a[i]>2*a[j] where i < j </p>
<p>For example, for the given array: [5,3,2,1,4], (5, 2) will be a valid pair as 5 > 4 and index 0 < index 1. But (1, 4) cannot be valid pair.</p>
<p>In this approach, we run a loop through given array and for each element we can loop through remianing elements next to it, check if any element satisfies  element<2*current_element, then increase count</p>
<p>Then final count will be our answer</p>

<ol>
    <li><strong>Initialization:</strong></li>
    <ul>
        <li>cnt is initialized to 0 to keep track of the number of inversions.</li>
    </ul>
    <li><strong>Two Nested Loops:</strong></li>
    <ul>
        <li>The outer loop (with index i) iterates through each element of the array.</li>
        <li>The inner loop (with index j) iterates through each element that comes after the element at index i.</li>
        <li>For each pair (i, j), the function checks if arr[i] > 2*arr[j]. If this condition is true, it means there's an inversion, and cnt is incremented by 1.</li>
    </ul>
    <li><strong>Return the Count:</strong></li>
    <ul>
        <li>The function returns the total count of inversions found in the array.</li>
    </ul>
</ol>

```python
def bruteForce(n, arr):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > 2*arr[j]:
                cnt += 1
    return cnt
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```

<p>Time Complexity: O(N2), where N = size of the given array.</p>
<p>Reason: We are using nested loops here and those two loops roughly run for N times.</p>
<p>Space Complexity: O(1) as we are not using any extra space to solve this problem.</p>

<p><strong>Optimized approach</strong></p>
<p>In order to solve this problem we will use the merge sort algorithm like we used in the problem count inversion with a slight modification of the merge() function. But in this case, the same logic will not work. In order to understand this, we need to deep dive into the merge() function.</p>
<p>The merge function works by comparing two elements from two halves i.e. arr[left] and arr[right]. Now, the condition in the question was arr[i] > arr[j]. That is why we merged the logic. While comparing the elements, we counted the number of pairs.</p>
<p>But in this case, the condition is arr[i] > 2*arr[j]. And, we cannot change the condition of comparing the elements in the merge() function. If we change the condition, the merge() function will fail to merge the elements. So, we need to check this condition and count the number of pairs separately.</p>
<p>Here, our approach will be to check, for every element in the sorted left half(sorted), how many elements in the right half(also sorted) can make a pair. Let’s try to understand, using the following example:</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/06/Screenshot-2023-06-10-221649.png">
<p>For the first element of the left half i.e. 6, we will start checking from index 0 of the right half i.e. arr2[]. Now, we can clearly see that the first two elements of arr2[] can make a pair with arr1[0] i.e. 6.</p>
<img src="https://static.takeuforward.org/wp/uploads/2023/06/Screenshot-2023-06-10-221824.png">
<p>For the next element i.e. arr1[1], we will start checking from index 2(0-based indexing) i.e. where we stopped for the previous element. </p>
<p>Note: This process will work because arr1[1] will always be greater than arr1[0] which concludes if arr2[0] and arr2[1] are making a pair with arr1[0], they will obviously make pairs with a number greater than arr1[0] i.e. arr1[1].</p>
<p>Thus before the merge step in the merge sort algorithm, we will calculate the total number of pairs each time.</p>
<p><strong>Approach</strong></p>
<p>The steps are basically the same as they are in the case of the merge sort algorithm. The change will be just in the mergeSort() function:</p>
<ul>
    <li>In order to count the number of pairs, we will keep a count variable, cnt, initialized to 0 beforehand inside the mergeSort().</li>
    <li>We will add the numbers returned by the previous mergeSort() calls.</li>
    <li>Before the merge step, we will count the number of pairs using a function, named countPairs().</li>
    <li>We need to remember that the left half starts from low and ends at mid, and the right half starts from mid+1 and ends at high.</li>
</ul>
<p>The steps of the countPairs() function will be as follows:</p>
<ul>
    <li>We will declare a variable, cnt, initialized with 0.</li>
    <li>We will run a loop from low to mid, to select an element at a time from the left half.</li>
    <li>Inside that loop, we will use another loop to check how many elements from the right half can make a pair.</li>
    <li>Lastly, we will add the total number of elements i.e. (right-(mid+1)) (where right = current index), to the cnt and return it.</li>
</ul>

```python
import math
def merge(arr,low,mid,high):
    left=low
    right=mid+1
    temp=[]
    while(left<=mid and right<=high):
        if(arr[left] <= arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while(left<=mid):
        temp.append(arr[left])
        left+=1

    while(right<=high):
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i]=temp[i-low]
def countPairs(arr,low,mid,high):
    cnt=0
    right=mid+1
    for i in range(low,mid+1):
        while (right<=high and (arr[i] > (2*arr[right]))):
            right+=1
        cnt+=(right-(mid+1))
    return cnt

def mergeSort(arr,low,high):
    cnt=0
    if(low>=high):
        return cnt
    mid=math.floor((low+high)/2)
    cnt+=mergeSort(arr,low,mid)
    cnt+=mergeSort(arr,mid+1,high)
    cnt+=countPairs(arr,low,mid,high)
    merge(arr,low,mid,high)
    return cnt

def optimized(n,arr):
    low,high=0,n-1
    return mergeSort(arr,low,high)


arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))

```

<p>Time Complexity: O(2N*logN), where N = size of the given array.</p>
<p>Reason: Inside the mergeSort() we call merge() and countPairs() except mergeSort() itself. Now, inside the function countPairs(), though we are running a nested loop, we are actually iterating the left half once and the right half once in total. That is why, the time complexity is O(N). And the merge() function also takes O(N). The mergeSort() takes O(logN) time complexity. Therefore, the overall time complexity will be O(logN * (N+N)) = O(2N*logN).</p>
<p>Space Complexity: O(N), as in the merge sort We use a temporary array to store elements in sorted order.</p>