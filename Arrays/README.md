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
