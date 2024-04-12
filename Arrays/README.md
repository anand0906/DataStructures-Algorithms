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
        elif(arr[i]<second_smallest and second_smallest!=smallest):
            second_smallest=arr[i]

        if(arr[i]>largest):
            second_largest=largest
            largest=arr[i]
        elif(arr[i]>second_largest and second_largest!=largest):
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