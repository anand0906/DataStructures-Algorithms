<h1>Stack</h1>
<p>A stack is a linear data structure that follows the <strong>Last In, First Out (LIFO) principle</strong>.</p>
<p>This means that the last element added to the stack will be the first one to be removed.</p>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240606180735/Stack-representation-in-Data-Structures-(1).webp">
<h2>Characteristics of a Stack</h2>
<ul>
	<li><strong>LIFO :</strong> The most recently added element is the first to be removed.</li>
	<li><strong>Oprations :</strong></li>
	<ul>
		<li><strong>PUSH :</strong>Add an element to the top of the stack.</li>
		<li><strong>POP :</strong>Remove the element from the top of the stack.</li>
		<li><strong>PEEK/TOP :</strong>View the top element without removing it.</li>
		<li><strong>ISEMPTY :</strong>Check if the stack is empty.</li>
		<li><strong>SIZE :</strong>Get the number of elements in the stack.</li>
	</ul>
</ul>
<h2>Applications</h2>
<p>Stacks are used in various applications, such as:</p>
<ul>
	<li><strong>Function Call Management :</strong>When a function is called in a program, the current context is pushed onto the call stack. When the function returns, the context is popped from the stack and execution resumes at the previous location.</li>
	<li><strong>Expression Evaluation :</strong>Stacks are used to evaluate expressions and handle parentheses.</li>
	<li><strong>Undo Mechanisms :</strong>Many applications use stacks to implement undo functionality.</li>
	<li><strong>Backtracking Algorithms :</strong>Algorithms like depth-first search (DFS) use stacks to remember their state.</li>
	<li><strong>Browser Tabs :</strong>Some web browsers manage open tabs using a stack. The most recently opened tab is the first one to be closed when you close tabs one by one.</li>
	<li><strong>Browser History :</strong>Web browsers use a stack to keep track of the pages you've visited. The last page you visited is at the top of the stack, and when you click the back button, you go to the previous page, effectively popping the current page off the stack.</li>
</ul>
<h2>Understaning Stacks Practically</h2>
<p>There are many real-life examples of a stack. </p>
<ul>
	<li>Consider the simple example of plates stacked over one another in a canteen. The plate which is at the top is the first one to be removed, i.e. the plate which has been placed at the bottommost position remains in the stack for the longest period of time. So, it can be simply seen to follow the LIFO/FILO order.</li>
	<li>When you pile books on a desk, the last book you place on the pile is the first one you take off when you need it.</li>
	<li>When you perform an action in a text editor (like typing or deleting text), it gets pushed onto an undo stack. If you press the undo button, the last action performed is the first one to be undone.</li>
</ul>
<h2>Types Of Stack</h2>
<ul>
	<li><strong>Fixed Size Stack :</strong>As the name suggests, a fixed size stack has a fixed size and cannot grow or shrink dynamically. If the stack is full and an attempt is made to add an element to it, an overflow error occurs. If the stack is empty and an attempt is made to remove an element from it, an underflow error occurs.</li>
	<li><strong>Dynamic Size Stack :</strong>A dynamic size stack can grow or shrink dynamically. When the stack is full, it automatically increases its size to accommodate the new element, and when the stack is empty, it decreases its size. This type of stack is implemented using a linked list, as it allows for easy resizing of the stack.</li>
</ul>
<h2>Operation Of Stack</h2>
<h3>Push</h3>
<p>Adds an item to the stack. If the stack is full, then it is said to be an Overflow condition.</p>
<p><strong>Algorithm For Push</strong></p>
<pre>
	begin
	 if stack is full
	    return
	 endif
	else  
	 increment top
	 stack[top] assign value
	end else
	end procedure	
</pre>
<h3>Pop</h3>
<p>Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.</p>
<p><strong>Algorithm For Pop</strong></p>
<pre>
	begin
	 if stack is empty
	    return -1
	 endif
	 else
	  store value of stack[top]
	  decrement top
	  return value
	 end else
	end procedure	
</pre>
<h3>Peek/Top</h3>
<p>Returns the top element of the stack.</p>
<p><strong>Algorithm For Top</strong></p>
<pre>
	begin 
  		return stack[top]
	end procedure
</pre>
<h3>isEmpty</h3>
<p>Returns true if the stack is empty, else false.</p>
<p><strong>Algorithm For isEmpty</strong></p>
<pre>
	begin
	 if top < 1
	    return true
	 else
	    return false
	end procedure
</pre>

<h2>Implementation Of Stack</h2>
<p>There are two ways to implement a stack</p>
<ul>
	<li>Using Array</li>
	<li>Using Linked List</li>
</ul>

<h3>Implementation of Stack Using Array</h3>
<p>In Python, you can use a list to implement a stack. The list methods append() and pop() make it straightforward to implement stack operations.</p>

```python
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("StackUnderFlow : Stack is Empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("StackUnderFlow : Stack is Empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

# Example usage:
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)  # Output: [1, 2, 3]
print(s.pop())  # Output: 3
print(s.peek())  # Output: 2
print(s.size())  # Output: 2
print(s)  # Output: [1, 2]
```

<p><strong>Advantages</strong></p>
<ul>
	<li>Easy to implement.</li>
	<li>Memory is saved as pointers are not involved.</li>
</ul>
<p><strong>Disadvantages</strong></p>
<ul>
	<li>The total size of the stack must be defined beforehand.</li>
	<li>It is not dynamic i.e., it doesn’t grow and shrink depending on needs at runtime. [But in case of dynamic sized arrays like vector in C++, list in Python, ArrayList in Java, stacks can grow and shrink with array implementation as well].</li>
</ul>

<h3>Implementation of stack using linked list</h3>

```python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:

    def __init__(self):
        self.head=None
        self.count=0

    def isEmpty(self):
        return self.head==None

    def push(self,data):
        if(self.head==None):
            self.head=Node(data)
            self.count+=1
        else:
            node=Node(data)
            node.next=self.head
            self.head=node
            self.count+=1

    def pop(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack is Empty")
        else:
            node=self.head
            self.head=node.next
            node.next=None
            self.count-=1
            return node.data
        
    def peek(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack is Empty")
        else:
            return self.head.data

    def size(self):
        return self.count

    def display(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<-")
                temp=temp.next
            print()

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Size Of Stack :",stack.size())
print("Peek Of Stack :",stack.peek())
stack.pop()
stack.display()
stack.pop()
stack.push(100)
stack.display()
stack.pop()
stack.display()
```

<p><strong>Advantages</strong></p>
<ul>
	<li>The linked list implementation of a stack can grow and shrink according to the needs at runtime.</li>
	<li>It is used in many virtual machines like JVM.</li>
</ul>
<p><strong>Disadvantages</strong></p>
<ul>
	<li>Requires extra memory due to the involvement of pointers.</li>
	<li>Random accessing is not possible in stack.</li>
</ul>

<h2>Design A Min Stack</h2>
<p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>
<p>Implement the MinStack class:</p>
<ul>
    <li>MinStack() initializes the stack object.</li>
    <li>void push(int val) pushes the element val onto the stack.</li>
    <li>void pop() removes the element on the top of the stack.</li>
    <li>int top() gets the top element of the stack.</li>
    <li>int getMin() retrieves the minimum element in the stack</li>
</ul>
<p>You must implement a solution with O(1) time complexity for each function.</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in two approaches</p>
<p>In this problem, we have to develop a stack data structure that supports retrieving the minimum element in constant time, along with the standard stack operations like push, pop, and top.</p>


<p><strong>Approach-1 (Uses Extra Space)</strong></p>
<p>By storing the current minimum value along with each element in the stack, we ensure that we can always retrieve the minimum value in constant time, even after popping elements from the stack. This approach efficiently maintains the minimum value without requiring additional complex operations.</p>
<ul>
    <li><strong>Stack with Tuples:</strong>
        <ul>
            <li>We use a stack where each element is a tuple <code>(value, current_minimum)</code>.</li>
            <li>The <code>value</code> is the actual value pushed onto the stack.</li>
            <li>The <code>current_minimum</code> is the minimum value in the stack up to that point.</li>
        </ul>
    </li>
    <li><strong>Pushing Elements:</strong>
        <ul>
            <li>When you push a new element onto the stack, you need to update the minimum value.</li>
            <li>If the stack is empty, the current minimum is the new element itself.</li>
            <li>If the stack is not empty, the current minimum is the smaller value between the new element and the current minimum from the top of the stack.</li>
        </ul>
    </li>
    <li><strong>Popping Elements:</strong>
        <ul>
            <li>When you pop an element from the stack, you remove the top element (both the value and the current minimum).</li>
            <li>The previous element in the stack will have the correct current minimum for the remaining stack.</li>
        </ul>
    </li>
    <li><strong>Getting the Top Element:</strong>
        <ul>
            <li>The <code>top</code> method returns the value of the top element in the stack.</li>
        </ul>
    </li>
    <li><strong>Getting the Minimum Element:</strong>
        <ul>
            <li>The <code>getMin</code> method returns the current minimum, which is stored as the second value in the top element of the stack.</li>
        </ul>
    </li>
</ul>

```python
class MinStack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def top(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        return self.stack[-1][0]

    def getMin(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        return self.stack[-1][1]

    def push(self, data):
        if self.isEmpty():
            mini = data
        else:
            mini = min(data, self.getMin())
        self.stack.append((data, mini))

    def pop(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        return self.stack.pop()[0]

    def size(self):
        return len(self.stack)

# Example usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Returns -3
min_stack.pop()
print(min_stack.top())     # Returns 0
print(min_stack.getMin())  # Returns -2
print(min_stack.size())    # Returns 2
```

<p><strong>Approach-2 (Efficient)</strong></p>
<p>1. <strong>Stack and Minimum:</strong></p>
<ul>
    <li>We use a single stack to store elements.</li>
    <li>We keep track of the current minimum value in a separate variable called <strong>min</strong>.</li>
</ul>
<p>2. <strong>Pushing Elements:</strong></p>
<ul>
    <li>When pushing an element, if it’s greater than or equal to the current minimum, it is pushed directly onto the stack.</li>
    <li>If the element is smaller than the current minimum, we push a transformed value (<strong>2*data - min</strong>) onto the stack and update the minimum to this new element. This transformation helps us track the minimum correctly.</li>
</ul>
<p>3. <strong>Popping Elements:</strong></p>
<ul>
    <li>When popping an element, if the popped value is greater than or equal to the current minimum, we simply pop it.</li>
    <li>If the popped value is less than the current minimum, we retrieve the original minimum value by reversing the transformation and update the minimum.</li>
</ul>
<p>4. <strong>Getting the Top Element:</strong></p>
<ul>
    <li>To get the top element, if the top value is less than the current minimum, it means the current minimum is the top element.</li>
</ul>
<p>5. <strong>Getting the Minimum Element:</strong></p>
<ul>
    <li>The <strong>getMin</strong> method simply returns the current minimum value.</li>
</ul>
<p><strong>Example</strong></p>
<p>Let’s see an example:</p>
<ol>
    <li><strong>Push -2:</strong></li>
    <ul>
        <li>Stack: <code>[-2]</code></li>
        <li>Minimum: <code>-2</code></li>
    </ul>
    <li><strong>Push 0:</strong></li>
    <ul>
        <li>Stack: <code>[-2, 0]</code></li>
        <li>Minimum: <code>-2</code></li>
    </ul>
    <li><strong>Push -3:</strong></li>
    <ul>
        <li>Stack: <code>[-2, 0, -4]</code> (transformed value <code>2*(-3) - (-2) = -4</code>)</li>
        <li>Minimum: <code>-3</code></li>
    </ul>
    <li><strong>Get Min:</strong></li>
    <ul>
        <li>Minimum: <code>-3</code></li>
    </ul>
    <li><strong>Pop:</strong></li>
    <ul>
        <li>Stack: <code>[-2, 0]</code></li>
        <li>Minimum: <code>-2</code></li>
    </ul>
    <li><strong>Top:</strong></li>
    <ul>
        <li>Top: <code>0</code></li>
    </ul>
    <li><strong>Get Min:</strong></li>
    <ul>
        <li>Minimum: <code>-2</code></li>
    </ul>
</ol>


```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def isEmpty(self):
        return len(self.stack) == 0

    def top(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        if self.stack[-1] < self.min:
            return self.min
        return self.stack[-1]

    def getMin(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        return self.min

    def push(self, data):
        if self.isEmpty():
            self.min = data
            self.stack.append(data)
        else:
            if data >= self.min:
                self.stack.append(data)
            else:
                temp = 2 * data - self.min
                self.stack.append(temp)
                self.min = data

    def pop(self):
        if self.isEmpty():
            raise IndexError("StackUnderFlow: Stack Is Empty")
        y = self.stack.pop()
        if y > self.min:
            return y
        else:
            temp = 2 * self.min - y
            self.min = temp
            return self.min

    def size(self):
        return len(self.stack)

# Example usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Returns -3
min_stack.pop()
print(min_stack.top())     # Returns 0
print(min_stack.getMin())  # Returns -2
print(min_stack.size())    # Returns 2

```

<p>Let's break down the mathematical reasoning behind the transformation used in the <strong>MinStack</strong> to ensure it maintains the minimum element efficiently.</p>

<p><strong>Intuition and Proof</strong></p>

<ul>
    <li><strong>Pushing an Element</strong>
        <ul>
            <li><strong>Condition: x < minEle</strong></li>
            <li>Given that the new element <strong>x</strong> is less than the current minimum <strong>minEle</strong>, we push the value <strong>2x - minEle</strong> onto the stack.</li>
            <li>This transformed value will always be less than <strong>x</strong>.</li>
            <li><strong>Proof: 2x - minEle < x</strong></li>
            <li>Starting from the condition <strong>x < minEle</strong>, subtract <strong>minEle</strong> from both sides:
                <ul>
                    <li>x - minEle < 0</li>
                </ul>
            </li>
            <li>Add <strong>x</strong> to both sides:
                <ul>
                    <li>x - minEle + x < x</li>
                </ul>
            </li>
            <li>Simplify the left side:
                <ul>
                    <li>2x - minEle < x</li>
                </ul>
            </li>
            <li>This inequality shows that <strong>2x - minEle</strong> is always less than <strong>x</strong>, confirming that the transformation keeps the value lower than the new element, which helps in identifying when to update the minimum during popping.</li>
        </ul>
    </li>
</ul>

<ul>
    <li><strong>Popping an Element</strong>
        <ul>
            <li>When popping an element, we check if the top of the stack is less than the current minimum element (<strong>minEle</strong>). If it is, it indicates that the element was transformed during insertion, and we need to update the minimum value.</li>
            <li><strong>Retrieving the Previous Minimum</strong></li>
            <li>Let <strong>y</strong> be the popped value.</li>
            <li>If <strong>y < minEle</strong>, it means <strong>y</strong> was transformed and pushed as <strong>2x - prevMinEle</strong>, where <strong>prevMinEle</strong> was the minimum before <strong>x</strong> was pushed.</li>
            <li>The value of <strong>x</strong> was then set as the new <strong>minEle</strong>.</li>
            <li><strong>Proof: Updating minEle</strong></li>
            <li>From the transformation:
                <ul>
                    <li>y = 2x - prevMinEle</li>
                </ul>
            </li>
            <li>Since <strong>minEle = x</strong> (the value of <strong>x</strong> was set as the new minimum when it was pushed):
                <ul>
                    <li>minEle = x</li>
                </ul>
            </li>
            <li>To find the previous minimum, use the current minimum (<strong>minEle</strong>) and the popped value (<strong>y</strong>):
                <ul>
                    <li>newMinEle = 2 × minEle - y</li>
                </ul>
            </li>
            <li>Substitute <strong>y</strong> with <strong>2x - prevMinEle</strong>:
                <ul>
                    <li>newMinEle = 2 × x - (2x - prevMinEle)</li>
                </ul>
            </li>
            <li>Simplify:
                <ul>
                    <li>newMinEle = 2x - 2x + prevMinEle</li>
                    <li>newMinEle = prevMinEle</li>
                </ul>
            </li>
            <li>This ensures that when an element is popped and is less than the current minimum, the minimum value is correctly updated to the previous minimum.</li>
        </ul>
    </li>
</ul>

<p><strong>Summary</strong></p>

<ul>
    <li>When pushing a value <strong>x</strong> less than the current minimum (<strong>minEle</strong>), the value <strong>2x - minEle</strong> is pushed, and the minimum is updated to <strong>x</strong>.</li>
    <li>When popping a value <strong>y</strong> less than the current minimum, the previous minimum is recalculated using:
        <ul>
            <li>newMinEle = 2 × minEle - y</li>
        </ul>
    </li>
</ul>

<p>This approach ensures the stack can keep track of the minimum element efficiently while using a single stack.</p>


<h2>Check For Balenced Parentheses</h2>
<p>Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.</p>
<p>An input string is valid if:</p>
<ol>    
    <li>Open brackets must be closed by the same type of brackets.</li>
    <li>Open brackets must be closed in the correct order.</li>
    <li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

<p><strong>Example Cases</strong></p>
<ul>
    <li><strong>Balanced String</strong>:
        <ul>
            <li>Input: <strong>n = 6</strong>, <strong>s = "({[]})"</strong></li>
            <li>Output: <strong>True</strong></li>
            <li>Explanation: Every opening parenthesis has a corresponding closing parenthesis in the correct order.</li>
        </ul>
    </li>
    <li><strong>Unbalanced String</strong>:
        <ul>
            <li>Input: <strong>n = 6</strong>, <strong>s = "({[})"</strong></li>
            <li>Output: <strong>False</strong></li>
            <li>Explanation: The closing parenthesis <strong>}</strong> does not match the last opened <strong>{</strong>.</li>
        </ul>
    </li>
    <li><strong>Unbalanced String (Unmatched Closing)</strong>:
        <ul>
            <li>Input: <strong>n = 2</strong>, <strong>s = ")("</strong></li>
            <li>Output: <strong>False</strong></li>
            <li>Explanation: There is a closing parenthesis <strong>)</strong> without a matching opening parenthesis.</li>
        </ul>
    </li>
</ul>

<p><strong>Solution</strong></p>
<ul>
    <li><strong>Initialize Stack</strong>: A stack is used to keep track of the opening parentheses.</li>
    <li><strong>Dictionary for Matching</strong>: A dictionary <strong>temp</strong> is used to map each opening parenthesis to its corresponding closing parenthesis.</li>
    <li><strong>Iterate through the String</strong>: The function iterates through each character in the string <strong>s</strong>.</li>
    <li><strong>Push Opening Parentheses</strong>: If the character is an opening parenthesis (<strong>(</strong>, <strong>{</strong>, <strong>[</strong>), it is pushed onto the stack.</li>
    <li><strong>Check Closing Parentheses</strong>: If the character is a closing parenthesis (<strong>)</strong>, <strong>}</strong>, <strong>]</strong>):
        <ul>
            <li>If the stack is empty, it means there is no corresponding opening parenthesis, and the string is not balanced.</li>
            <li>Otherwise, check if the top of the stack matches the current closing parenthesis using the dictionary <strong>temp</strong>. If it matches, pop the stack. If not, the string is not balanced.</li>
        </ul>
    </li>
    <li><strong>Final Check</strong>: After processing all characters, if the stack is not empty, it means there are unmatched opening parentheses left.</li>
    <li><strong>Return Result</strong>: The function returns <strong>True</strong> if all parentheses are balanced, otherwise <strong>False</strong>.</li>
</ul>

```python
def solve(n, s):
    stack = []
    temp = {"(": ")", "[": "]", "{": "}"}
    for i in range(n):
        if s[i] in "({[":
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            if temp[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    return True
s=input()
n=len(s)
print(solve(n,s))
```

<h2>Expression Conversions</h2>
<p><strong>Infix, Prefix, and Postfix Notations</strong></p>
    
<p><strong>Infix Notation</strong></p>
<p><strong>Definition</strong>: In infix notation, operators are written between the operands they act on. This is the most common notation used in arithmetic and in many programming languages.</p>
<p><strong>Example</strong>:</p>
<ul>
    <li>A + B</li>
    <li>(A + B) * C</li>
    <li>A + (B * C)</li>
</ul>
<p><strong>Uses</strong>:</p>
<ul>
    <li>Easily understandable and readable by humans.</li>
    <li>Directly used in many programming languages and calculators.</li>
    <li>Requires precedence rules and parentheses to determine the order of operations.</li>
</ul>
<p><strong>Evaluation</strong>:</p>
<p>The expression A + B * C is evaluated as A + (B * C) because multiplication has higher precedence than addition.</p>

<p><strong>Prefix Notation (Polish Notation)</strong></p>
<p><strong>Definition</strong>: In prefix notation, operators are written before their operands. There is no need for parentheses as the order of operations is unambiguous.</p>
<p><strong>Example</strong>:</p>
<ul>
    <li>+ A B</li>
    <li>* + A B C (which is equivalent to (A + B) * C)</li>
    <li>+ A * B C (which is equivalent to A + (B * C))</li>
</ul>
<p><strong>Uses</strong>:</p>
<ul>
    <li>Simplifies the process of parsing expressions.</li>
    <li>Useful in functional programming and certain types of compilers.</li>
    <li>Eliminates the need for precedence rules and parentheses.</li>
</ul>
<p><strong>Evaluation</strong>:</p>
<p>The expression * + A B C is evaluated as:</p>
<ol>
    <li>Evaluate + A B</li>
    <li>Then, multiply the result by C</li>
</ol>

<p><strong>Postfix Notation (Reverse Polish Notation)</strong></p>
<p><strong>Definition</strong>: In postfix notation, operators are written after their operands. Like prefix notation, there is no need for parentheses because the order of operations is clear.</p>
<p><strong>Example</strong>:</p>
<ul>
    <li>A B +</li>
    <li>A B C + * (which is equivalent to A * (B + C))</li>
    <li>A B C * + (which is equivalent to A + (B * C))</li>
</ul>
<p><strong>Uses</strong>:</p>
<ul>
    <li>Particularly useful in stack-based and postfix calculators.</li>
    <li>Simplifies the process of evaluating expressions in computer programs.</li>
    <li>Eliminates the need for precedence rules and parentheses.</li>
</ul>
<p><strong>Evaluation</strong>:</p>
<p>The expression A B C * + is evaluated as:</p>
<ol>
    <li>Evaluate B C *</li>
    <li>Then, add the result to A</li>
</ol>

<p><strong>Conversion Between Notations</strong></p>
<ol>
    <li><strong>Infix to Prefix</strong>:
        <ul>
            <li>A + B becomes + A B</li>
            <li>(A + B) * C becomes * + A B C</li>
        </ul>
    </li>
    <li><strong>Infix to Postfix</strong>:
        <ul>
            <li>A + B becomes A B +</li>
            <li>(A + B) * C becomes A B + C *</li>
        </ul>
    </li>
    <li><strong>Prefix to Postfix</strong>:
        <ul>
            <li>+ A B becomes A B +</li>
            <li>* + A B C becomes A B + C *</li>
        </ul>
    </li>
</ol>

<p><strong>Practical Uses</strong></p>
<ul>
    <li><strong>Compilers</strong>: Prefix and postfix notations are used in the intermediate stages of compilation for expression evaluation.</li>
    <li><strong>Calculators</strong>: Postfix notation is used in many calculators and stack-based programming languages because it is easier to evaluate using stacks.</li>
    <li><strong>Expression Parsing</strong>: Prefix and postfix notations simplify parsing algorithms, eliminating the need for parentheses and operator precedence handling.</li>
</ul>

<p><strong>Example Comparisons</strong></p>
<p><strong>Infix</strong>: (3 + 4) * 5</p>
<ul>
    <li><strong>Prefix</strong>: * + 3 4 5</li>
    <li><strong>Postfix</strong>: 3 4 + 5 *</li>
</ul>
<p><strong>Infix</strong>: A + (B * C)</p>
<ul>
    <li><strong>Prefix</strong>: + A * B C</li>
    <li><strong>Postfix</strong>: A B C * +</li>
</ul>

<p>By understanding and using these notations, you can simplify the process of expression evaluation, especially in the context of computer science and programming.</p>

<h3>Infix To PostFix</h3>
<ul>
    <li><strong>Initialize Stack and Result</strong>:
        <ul>
            <li><strong>stack</strong> is used to keep track of operators.</li>
            <li><strong>ans</strong> is a string that will hold the resulting postfix expression.</li>
        </ul>
    </li>
    <li><strong>Order of Operations</strong>:
        <ul>
            <li>A dictionary <strong>order</strong> is used to define the precedence of operators. Higher values indicate higher precedence.</li>
        </ul>
    </li>
    <li><strong>Iterate Through the Expression</strong>:
        <ul>
            <li>For each character in the input string <strong>s</strong>:</li>
            <ul>
                <li><strong>If the character is an operand</strong> (alphanumeric), append it directly to <strong>ans</strong>.</li>
                <li><strong>If the character is (</strong> (opening parenthesis), push it onto the stack.</li>
                <li><strong>If the character is )</strong> (closing parenthesis), pop from the stack and append to <strong>ans</strong> until ( is encountered.</li>
                <li><strong>If the character is an operator</strong>:
                    <ul>
                        <li>Pop from the stack and append to <strong>ans</strong> while the precedence of the current operator is less than or equal to the precedence of the operator at the top of the stack.</li>
                        <li>Push the current operator onto the stack.</li>
                    </ul>
                </li>
            </ul>
        </ul>
    </li>
    <li><strong>Append Remaining Operators</strong>:
        <ul>
            <li>After the input string has been fully processed, pop any remaining operators from the stack and append them to <strong>ans</strong>.</li>
        </ul>
    </li>
</ul>

<p><strong>Example</strong></p>
<ul>
    <li><strong>Input</strong>: n = 7, s = "A+B*C"</li>
    <li><strong>Output</strong>: "ABC*+"</li>
</ul>

<p><strong>Detailed Steps for Example</strong></p>
<ul>
    <li><strong>Initialization</strong>:
        <ul>
            <li>stack = []</li>
            <li>ans = ""</li>
        </ul>
    </li>
    <li><strong>Processing Each Character</strong>:
        <ul>
            <li>s[0] = 'A' (operand): Append to ans → ans = "A"</li>
            <li>s[1] = '+' (operator): Push onto stack → stack = ['+']</li>
            <li>s[2] = 'B' (operand): Append to ans → ans = "AB"</li>
            <li>s[3] = '*' (operator): Push onto stack (higher precedence) → stack = ['+', '*']</li>
            <li>s[4] = 'C' (operand): Append to ans → ans = "ABC"</li>
        </ul>
    </li>
    <li><strong>Final Stack Emptying</strong>:
        <ul>
            <li>Pop '*' from stack and append to ans → ans = "ABC*"</li>
            <li>Pop '+' from stack and append to ans → ans = "ABC*+"</li>
        </ul>
    </li>
    <li><strong>Return Result</strong>:
        <ul>
            <li>The final postfix expression is "ABC*+".</li>
        </ul>
    </li>
</ul>


```python
def solve(n,s):
    stack=[]
    ans=""
    order={"(":0,")":0,"+":1,"-":1,"*":2,"/":2,"^":3}
    for i in range(n):
        if(s[i].isalnum()):
            ans+=s[i]
        elif(s[i] == "("):
            stack.append(s[i])
        elif(s[i] == ")"):
            while stack and stack[-1]!="(":
                ans+=stack.pop()
            stack.pop()
        else:
            while stack and (order[s[i]]<=order[stack[-1]]):
                ans+=stack.pop()
            stack.append(s[i])
    while stack:
        ans+=stack.pop()
    return ans

s=input()
n=len(s)
print(solve(n,s))
```

<p><strong>Time Complexity : O(n)</strong>Each character in the input string is processed exactly once, and stack operations are O(1) on average</p>
<p><strong>Space Complexity : O(n)</strong> We need O(n) space for the result string and O(n) space for the stack.</p>


<h3>Infix To Prefix</h3>
<p><strong>Steps to Convert Infix to Prefix</strong></p>

<ul>
    <li><strong>Reverse the Infix Expression</strong>: Reverse the input string.</li>
    <li><strong>Replace Parentheses</strong>: Swap the opening and closing parentheses.</li>
    <li><strong>Apply Infix to Postfix Conversion</strong>: Convert the modified infix expression to postfix.</li>
    <li><strong>Reverse the Postfix Expression</strong>: Reverse the resulting postfix expression to get the prefix expression.</li>
</ul>

<p><strong>Explanation of Each Step</strong></p>

<ul>
    <li><strong>Reverse the Infix Expression</strong>:
        <ul>
            <li>Reversing the string ensures that operators are processed in the correct order for prefix notation.</li>
            <li>For example, the infix expression <strong>A + B * C</strong> becomes <strong>C * B + A</strong>.</li>
        </ul>
    </li>
    <li><strong>Replace Parentheses</strong>:
        <ul>
            <li>Swapping the parentheses adjusts their positions due to the reversal.</li>
            <li>For example, <strong>)</strong> becomes <strong>(</strong> and <strong>(</strong> becomes <strong>)</strong>.</li>
        </ul>
    </li>
    <li><strong>Apply Infix to Postfix Conversion</strong>:
        <ul>
            <li>This step uses the Shunting Yard algorithm to convert the modified infix expression to postfix.</li>
        </ul>
    </li>
    <li><strong>Reverse the Postfix Expression</strong>:
        <ul>
            <li>Reversing the postfix expression gives the final prefix expression.</li>
        </ul>
    </li>
</ul>

<p><strong>Example</strong></p>

<ul>
    <li><strong>Input</strong>: A + B * C</li>
    <li><strong>Reverse</strong>: C * B + A</li>
    <li><strong>Replace Parentheses</strong>: Not applicable here since there are no parentheses.</li>
    <li><strong>Infix to Postfix</strong>: Convert C * B + A to CB*A+</li>
    <li><strong>Reverse Postfix</strong>: +A*BC</li>
</ul>

<p><strong>Handling ^ Operator</strong></p>
<p>The exponentiation operator <strong>^</strong> is handled differently in the infix to postfix conversion due to its higher precedence and right-to-left associativity.</p>
<p><strong>Higher Precedence</strong></p>
<ul>
    <li><strong>^</strong> has a higher precedence than <strong>*</strong>, <strong>+</strong>, and <strong>-</strong>. Therefore, when <strong>^</strong> is encountered, it needs to stay on the stack until a lower precedence operator or an operand is encountered.</li>
</ul>
<p><strong>Right-to-Left Associativity</strong></p>
<ul>
    <li>Unlike other operators which are left-to-right associative, <strong>^</strong> is right-to-left associative. This means that for expressions like <strong>A ^ B ^ C</strong>, the expression is evaluated as <strong>A ^ (B ^ C)</strong>.</li>
</ul>

```python
def solve(n,s):
    s=s[::-1]
    temp=list(s)
    for i in range(n):
        if(temp[i]=="("):
            temp[i]=")"
        elif(temp[i]==")"):
            temp[i]="("
    s="".join(temp)
    stack=[]
    ans=""
    order={"(":0,")":0,"+":1,"-":1,"*":2,"/":2,"^":3}
    for i in range(n):
        if(s[i].isalnum()):
            ans+=s[i]
        elif(s[i] == "("):
            stack.append(s[i])
        elif(s[i] == ")"):
            while stack and stack[-1]!="(":
                ans+=stack.pop()
            stack.pop()
        else:
            if(s[i]=="^"):
                while stack and (order[s[i]]<=order[stack[-1]]):
                    ans+=stack.pop()
            else:
                while stack and (order[s[i]]<order[stack[-1]]):
                    ans+=stack.pop()
            stack.append(s[i])
    while stack:
        ans+=stack.pop()
    return ans[::-1]

s=input()
n=len(s)
print(solve(n,s))
```

<ul>
    <li><strong>Time Complexity</strong>: O(n) – Each character is processed a constant number of times.</li>
    <li><strong>Space Complexity</strong>: O(n) – Space is used for the reversed string, stack, and result.</li>
</ul>

<h3>Postfix to Infix</h3>
<p><strong>Steps to Convert Postfix to Infix</strong></p>

<ul>
    <li><strong>Initialize an empty stack.</strong></li>
    <li><strong>Iterate through each character in the postfix expression.</strong>
        <ul>
            <li>If the character is an operand, push it onto the stack.</li>
            <li>If the character is an operator, pop two elements from the stack, create a new string with the operator between the two operands, and push this new string back onto the stack.</li>
        </ul>
    </li>
    <li><strong>The final element in the stack is the infix expression.</strong></li>
</ul>

<p><strong>Example</strong></p>

<ul>
    <li><strong>Input (Postfix Expression)</strong>: <code>ab+c*</code></li>
    <li><strong>Output (Infix Expression)</strong>: <code>((a+b)*c)</code></li>
</ul>

<p><strong>Explanation of the Example</strong></p>

<ul>
    <li>Read <strong>'a'</strong>: Operand, push onto stack: <code>['a']</code></li>
    <li>Read <strong>'b'</strong>: Operand, push onto stack: <code>['a', 'b']</code></li>
    <li>Read <strong>'+'</strong>: Operator, pop 'b' and 'a', form <code>(a+b)</code>, push back onto stack: <code>['(a+b)']</code></li>
    <li>Read <strong>'c'</strong>: Operand, push onto stack: <code>['(a+b)', 'c']</code></li>
    <li>Read <strong>'*'</strong>: Operator, pop 'c' and '(a+b)', form <code>((a+b)*c)</code>, push back onto stack: <code>['((a+b)*c)']</code></li>
</ul>

<p><strong>Code</strong></p>

```python
def solve(n, s):
    stack = []
    for i in range(n):
        if s[i].isalnum():
            stack.append(s[i])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new = f"({op2+s[i]+op1})"
            stack.append(new)
    return stack[-1]

s = input()
n = len(s)
print(solve(n, s))
```

<p><strong>Complexity Analysis</strong></p>
<p><strong>Time Complexity</strong></p>
<ul>
    <li>Each character in the string is processed once, so the time complexity is <strong>O(n)</strong>.</li>
</ul>
<p><strong>Space Complexity</strong></p>
<ul>
    <li>The stack can hold up to <strong>O(n)</strong> elements in the worst case, so the space complexity is <strong>O(n)</strong>.</li>
</ul>

<br>    
<br>    


<h3>Prefix To Infix</h3>
<p><strong>Steps to Convert Postfix to Infix</strong></p>

<ul>
    <li><strong>Initialize an empty stack.</strong></li>
    <li><strong>Iterate through each character in the postfix expression from right to left.</strong>
        <ul>
            <li>If the character is an operand, push it onto the stack.</li>
            <li>If the character is an operator, pop two elements from the stack, create a new string with the operator between the two operands, and push this new string back onto the stack.</li>
        </ul>
    </li>
    <li><strong>The final element in the stack is the infix expression.</strong></li>
</ul>

<p><strong>Example</strong></p>

<ul>
    <li><strong>Input (Postfix Expression)</strong>: <code>ab+c*</code></li>
    <li><strong>Output (Infix Expression)</strong>: <code>((a+b)*c)</code></li>
</ul>

<p><strong>Explanation of the Example</strong></p>

<ul>
    <li>Read <strong>'c'</strong>: Operand, push onto stack: <code>['c']</code></li>
    <li>Read <strong>'*'</strong>: Operator, pop 'c' and 'b', form <code>(b*c)</code>, push back onto stack: <code>['(b*c)']</code></li>
    <li>Read <strong>'+'</strong>: Operator, pop '(b*c)' and 'a', form <code>(a+(b*c))</code>, push back onto stack: <code>['(a+(b*c))']</code></li>
    <li>Read <strong>'b'</strong>: Operand, push onto stack: <code>['b', '(a+(b*c))']</code></li>
    <li>Read <strong>'a'</strong>: Operand, push onto stack: <code>['a', 'b', '(a+(b*c))']</code></li>
</ul>

<p><strong>Code</strong></p>

```python
def solve(n, s):
    stack = []
    for i in range(n - 1, -1, -1):
        if s[i].isalnum():
            stack.append(s[i])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new = f"({op1+s[i]+op2})"
            stack.append(new)
    return stack[-1]

s = input()
n = len(s)
print(solve(n, s))
```

<p><strong>Complexity Analysis</strong></p>
<p><strong>Time Complexity</strong></p>
<ul>
    <li>Each character in the string is processed once, so the time complexity is <strong>O(n)</strong>.</li>
</ul>
<p><strong>Space Complexity</strong></p>
<ul>
    <li>The stack can hold up to <strong>O(n)</strong> elements in the worst case, so the space complexity is <strong>O(n)</strong>.</li>
</ul>

<br>
<br>

<h3>Postfix To Prefix</h3>
<p><strong>Steps to Convert Postfix to Infix</strong></p>

<ul>
    <li><strong>Initialize an empty stack.</strong></li>
    <li><strong>Iterate through each character in the postfix expression.</strong>
        <ul>
            <li>If the character is an operand (a letter or digit), push it onto the stack.</li>
            <li>If the character is an operator, pop the top two operands from the stack. 
                <ul>
                    <li>The first operand popped is <strong>op1</strong>, and the second operand popped is <strong>op2</strong>.</li>
                    <li>Create a new infix expression by placing the operator between <strong>op2</strong> and <strong>op1</strong>, and enclose it in parentheses.</li>
                    <li>Push this new infix expression back onto the stack.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>The final element in the stack is the complete infix expression.</strong></li>
</ul>

<p><strong>Example</strong></p>

<ul>
    <li><strong>Input (Postfix Expression)</strong>: <code>ab+c*</code></li>
    <li><strong>Output (Infix Expression)</strong>: <code>((a+b)*c)</code></li>
</ul>

<p><strong>Explanation of the Example</strong></p>

<ul>
    <li>Read <strong>'a'</strong>: Operand, push onto stack: <code>['a']</code></li>
    <li>Read <strong>'b'</strong>: Operand, push onto stack: <code>['a', 'b']</code></li>
    <li>Read <strong>'+'</strong>: Operator, pop 'b' and 'a', form <code>(a+b)</code>, push back onto stack: <code>['(a+b)']</code></li>
    <li>Read <strong>'*'</strong>: Operator, pop '(a+b)' and 'c', form <code>((a+b)*c)</code>, push back onto stack: <code>['((a+b)*c)']</code></li>
</ul>

<p><strong>Code</strong></p>

<pre>
<code>
def solve(n, s):
    stack = []
    for i in range(n):
        if s[i].isalnum():
            stack.append(s[i])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new = "({}{}{})".format(op2, s[i], op1)
            stack.append(new)
    return stack[-1]

s = input()
n = len(s)
print(solve(n, s))
</code>
</pre>

<p><strong>Complexity Analysis</strong></p>

<p><strong>Time Complexity</strong></p>

<ul>
    <li>Each character in the string is processed once, so the time complexity is <strong>O(n)</strong>.</li>
</ul>

<p><strong>Space Complexity</strong></p>

<ul>
    <li>The stack can hold up to <strong>O(n)</strong> elements in the worst case, so the space complexity is <strong>O(n)</strong>.</li>
</ul>


<h3>Prefix To Postfix</h3>
<p>This function converts a postfix expression to its corresponding prefix expression by processing the postfix expression from right to left.</p>

<p><strong>Steps to Convert Postfix to Prefix</strong></p>

<ul>
    <li><strong>Initialize an empty stack.</strong></li>
    <li><strong>Iterate through each character in the postfix expression from right to left.</strong>
        <ul>
            <li>If the character is an operand (a letter or digit), push it onto the stack.</li>
            <li>If the character is an operator, pop the top two operands from the stack. 
                <ul>
                    <li>The first operand popped is <strong>op1</strong>, and the second operand popped is <strong>op2</strong>.</li>
                    <li>Create a new prefix expression by placing the operator before <strong>op1</strong> and <strong>op2</strong>, resulting in <strong>op1+op2+operator</strong>.</li>
                    <li>Push this new prefix expression back onto the stack.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>The final element in the stack is the complete prefix expression.</strong></li>
</ul>

<p><strong>Example</strong></p>

<ul>
    <li><strong>Input (Postfix Expression)</strong>: <code>ab+c*</code></li>
    <li><strong>Output (Prefix Expression)</strong>: <code>*+abc</code></li>
</ul>

<p><strong>Explanation of the Example</strong></p>

<ul>
    <li>Read <strong>'c'</strong>: Operand, push onto stack: <code>['c']</code></li>
    <li>Read <strong>'+'</strong>: Operator, pop 'c' and 'b', form <code>+bc</code>, push back onto stack: <code>['+bc']</code></li>
    <li>Read <strong>'a'</strong>: Operand, push onto stack: <code>['a', '+bc']</code></li>
    <li>Read <strong>'*'</strong>: Operator, pop '+bc' and 'a', form <code>*+abc</code>, push back onto stack: <code>['*+abc']</code></li>
</ul>

<p><strong>Code</strong></p>

```python
def solve(n, s):
    stack = []
    for i in range(n - 1, -1, -1):
        if s[i].isalnum():
            stack.append(s[i])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new = op1 + op2 + s[i]
            stack.append(new)
    return stack[-1]

s = input()
n = len(s)
print(solve(n, s))
```

<p><strong>Complexity Analysis</strong></p>
<p><strong>Time Complexity</strong></p>
<ul>
    <li>Each character in the string is processed once, so the time complexity is <strong>O(n)</strong>.</li>
</ul>
<p><strong>Space Complexity</strong></p>
<ul>
    <li>The stack can hold up to <strong>O(n)</strong> elements in the worst case, so the space complexity is <strong>O(n)</strong>.</li>
</ul>



<p>The stack stores all possible greater elements for the elements processed so far. This helps efficiently find the next greater element for each item in the array.</p>

<p><strong>Purpose of the Stack:</strong></p>
<ul>
    <li>The stack keeps track of elements that might be the next greater element for the elements to the left of the current element in the array.</li>
</ul>

<p><strong>Processing Each Element:</strong></p>
<ol>
    <li><strong>From Right to Left:</strong> By processing the array from right to left, the stack can be used to efficiently find the next greater element.</li>
    <li><strong>Pop Operation:</strong>
        <ul>
            <li><strong>Removing Smaller Elements:</strong> For each element, while the stack is not empty and the top of the stack is less than or equal to the current element, pop elements from the stack. This ensures that only elements greater than the current element remain in the stack.</li>
        </ul>
    </li>
    <li><strong>Determining the Next Greater Element:</strong>
        <ul>
            <li><strong>Top of the Stack:</strong> If the stack is not empty after popping, the top element of the stack is the next greater element for the current element.</li>
            <li><strong>Stack is Empty:</strong> If the stack is empty, there is no greater element for the current element, so <strong>-1</strong> is appended to the result list <strong>ans</strong>.</li>
        </ul>
    </li>
    <li><strong>Push Operation:</strong>
        <ul>
            <li><strong>Adding Current Element:</strong> After processing the current element, push it onto the stack. This prepares it to potentially be the next greater element for the elements to the left.</li>
        </ul>
    </li>
</ol>

<p><strong>Example Walkthrough:</strong></p>
<p>Let's take an example array <strong>[4, 5, 2, 10, 8]</strong> to see how the stack stores possible greater elements and how it is updated:</p>

<ol>
    <li><strong>Initialization:</strong>
        <ul>
            <li><strong>ans = []</strong></li>
            <li><strong>stack = []</strong></li>
        </ul>
    </li>
    <li><strong>Process elements from right to left:</strong>
        <ul>
            <li><strong>Element 8 (at index 4):</strong>
                <ul>
                    <li>Append <strong>-1</strong> to <strong>ans</strong> because there is no next element.</li>
                    <li>Push <strong>8</strong> onto the stack.</li>
                    <li><strong>ans = [-1]</strong></li>
                    <li><strong>stack = [8]</strong></li>
                </ul>
            </li>
            <li><strong>Element 10 (at index 3):</strong>
                <ul>
                    <li>Pop <strong>8</strong> from the stack because <strong>8 <= 10</strong>.</li>
                    <li>Append <strong>-1</strong> to <strong>ans</strong> because the stack is now empty.</li>
                    <li>Push <strong>10</strong> onto the stack.</li>
                    <li><strong>ans = [-1, -1]</strong></li>
                    <li><strong>stack = [10]</strong></li>
                </ul>
            </li>
            <li><strong>Element 2 (at index 2):</strong>
                <ul>
                    <li>No elements in the stack are less than or equal to <strong>2</strong>, so no popping occurs.</li>
                    <li>Append <strong>10</strong> to <strong>ans</strong> because the top of the stack is <strong>10</strong>.</li>
                    <li>Push <strong>2</strong> onto the stack.</li>
                    <li><strong>ans = [-1, -1, 10]</strong></li>
                    <li><strong>stack = [10, 2]</strong></li>
                </ul>
            </li>
            <li><strong>Element 5 (at index 1):</strong>
                <ul>
                    <li>Pop <strong>2</strong> from the stack because <strong>2 <= 5</strong>.</li>
                    <li>Append <strong>10</strong> to <strong>ans</strong> because the top of the stack is <strong>10</strong>.</li>
                    <li>Push <strong>5</strong> onto the stack.</li>
                    <li><strong>ans = [-1, -1, 10, 10]</strong></li>
                    <li><strong>stack = [10, 5]</strong></li>
                </ul>
            </li>
            <li><strong>Element 4 (at index 0):</strong>
                <ul>
                    <li>No elements in the stack are less than or equal to <strong>4</strong>, so no popping occurs.</li>
                    <li>Append <strong>5</strong> to <strong>ans</strong> because the top of the stack is <strong>5</strong>.</li>
                    <li>Push <strong>4</strong> onto the stack.</li>
                    <li><strong>ans = [-1, -1, 10, 10, 5]</strong></li>
                    <li><strong>stack = [10, 5, 4]</strong></li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>Reverse the ans List:</strong> Reverse <strong>ans</strong> to match the original left-to-right order of the array.</li>
    <li><strong>Final result:</strong> <strong>[5, 10, 10, -1, -1]</strong></li>
</ol>



```python
def optimized(n, arr):
    ans = []  # Initialize an empty list to store the answers
    stack = []  # Initialize an empty stack
    
    for i in range(n-1, -1, -1):  # Traverse the array from right to left
        while stack and arr[i] >= stack[-1]:  # Pop elements from stack while they are less than or equal to current element
            stack.pop()
        
        if stack:  # If the stack is not empty, the top element is the next greater element
            ans.append(stack[-1])
        else:  # If the stack is empty, there is no next greater element
            ans.append(-1)
        
        stack.append(arr[i])  # Push the current element onto the stack
    
    return ans[::-1]  # Reverse the answer list before returning

arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```

<p><strong>Summary</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> <strong>O(n)</strong> due to the traversal and stack operations.</li>
    <li><strong>Space Complexity:</strong> <strong>O(n)</strong> due to the stack and output list <strong>ans</strong>.</li>
</ul>


<h3>Next Smaller Elements</h3>
<p>For each element in the array, find the first smaller element that comes after it. If no such element exists, the result is -1.</p>
<p>Here, it follows same approach as previous, just condition while popping element from stack will change</p>
<p>It will pop only when curren element less than stack top element</p>

```python
def next_smaller(n, arr):
    ans = []
    stack = []
    for i in range(n-1, -1, -1):
        while stack and  arr[i] <= stack[-1] :
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    return ans[::-1]
```

<h3>Previous Smaller Element</h3>
<p>For each element in the array, find the first smaller element that comes before it. If no such element exists, the result is -1.</p>
<p>Here, we will loop from left to right, since we need to track left elements that will be used as answers for right elements</p>

```python
def previous_smaller(n, arr):
    ans = []
    stack = []
    for i in range(n):
        while stack and arr[i] <= stack[-1]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    return ans
```

<h3>Previous Greater Element</h3>
<p>For each element in the array, find the first greater element that comes before it. If no such element exists, the result is -1.</p>
<p>Here We Finding Greater Elements</p>

```python
def previous_greater(n, arr):
    ans = []
    stack = []
    for i in range(n):
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    return ans

```
<br>
<br>

<h2>Next Greater Element : Circular</h2>
<p>Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.</p>
<p>The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.</p>

<p><strong>Examples</strong></p>
<p><strong>Input :</strong>nums = [1,2,1]</p>
<p><strong>Output :</strong>[2,-1,2]</p>
<p><strong>Explanation :</strong>he first 1's next greater number is 2; The number 2 can't find next greater number. The second 1's next greater number needs to search circularly, which is also 2.</p>
<p><strong>Input :</strong>nums = [1,2,3,4,3]</p>
<p><strong>Output :</strong>[2,3,4,-1,4]</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>

<p><strong>BruteForce Approach</strong></p>
<p>Here, For Each Element, we compare with remaining n-1 elements to find greater element</p>
<p>In a circular array, we treat the array as if it loops around. For each element, we look for the next element that is greater than it by checking all subsequent elements, including wrapping around to the start of the array if necessary. If no such element is found, we return <strong>-1</strong>.</p>

<p><strong>Code Explanation</strong></p>
<p>The function <strong>bruteForce</strong> goes through each element of the array and finds the next greater element using a nested loop. Here’s a step-by-step breakdown of the code:</p>

<ul>
    <li><strong>Initialization</strong>:
        <ul>
            <li>Create an empty list <strong>ans</strong> to store the results.</li>
        </ul>
    </li>
    <li><strong>Outer Loop</strong>:
        <ul>
            <li>Iterate through each element of the array using the index <strong>i</strong>.</li>
        </ul>
    </li>
    <li><strong>Inner Loop</strong>:
        <ul>
            <li>For each element at index <strong>i</strong>, check all subsequent elements up to the next <strong>(n-1)</strong> elements.</li>
            <li>Use the modulo operation <strong>(j % n)</strong> to wrap around the array when the end is reached.</li>
        </ul>
    </li>
    <li><strong>Condition</strong>:
        <ul>
            <li>If a greater element is found, append it to the result list <strong>ans</strong> and break out of the inner loop.</li>
            <li>If no greater element is found after checking <strong>(n-1)</strong> elements, append <strong>-1</strong> to the result list <strong>ans</strong>.</li>
        </ul>
    </li>
    <li><strong>Return the Result</strong>:
        <ul>
            <li>Return the result list <strong>ans</strong>.</li>
        </ul>
    </li>
</ul>

```python
def bruteForce(n, arr):
    ans = []
    for i in range(n):
        flag = True
        for j in range(i + 1, n + i):
            if arr[j % n] > arr[i]:
                ans.append(arr[j % n])
                flag = False
                break
        if flag:
            ans.append(-1)
    return ans
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
```

<p><strong>Example Walkthrough</strong></p>

<p>Consider the array <strong>[4, 5, 2, 10, 8]</strong>:</p>

<ol>
    <li><strong>Initialization</strong>:
        <ul>
            <li><strong>ans = []</strong></li>
        </ul>
    </li>
    <li><strong>Process each element</strong>:
        <ul>
            <li><strong>Element 4</strong> (at index 0):
                <ul>
                    <li>Check elements: 5, 2, 10, 8, (4 - wraps around)</li>
                    <li>Next greater element is 5.</li>
                    <li><strong>ans = [5]</strong></li>
                </ul>
            </li>
            <li><strong>Element 5</strong> (at index 1):
                <ul>
                    <li>Check elements: 2, 10, 8, 4, (5 - wraps around)</li>
                    <li>Next greater element is 10.</li>
                    <li><strong>ans = [5, 10]</strong></li>
                </ul>
            </li>
            <li><strong>Element 2</strong> (at index 2):
                <ul>
                    <li>Check elements: 10, 8, 4, 5, (2 - wraps around)</li>
                    <li>Next greater element is 10.</li>
                    <li><strong>ans = [5, 10, 10]</strong></li>
                </ul>
            </li>
            <li><strong>Element 10</strong> (at index 3):
                <ul>
                    <li>Check elements: 8, 4, 5, 2, (10 - wraps around)</li>
                    <li>No greater element found, so append -1.</li>
                    <li><strong>ans = [5, 10, 10, -1]</strong></li>
                </ul>
            </li>
            <li><strong>Element 8</strong> (at index 4):
                <ul>
                    <li>Check elements: 4, 5, 2, 10, (8 - wraps around)</li>
                    <li>Next greater element is 10.</li>
                    <li><strong>ans = [5, 10, 10, -1, 10]</strong></li>
                </ul>
            </li>
        </ul>
    </li>
</ol>

<p><strong>Summary</strong></p>
<ul>
    <li><strong>Time Complexity</strong>: O(n^2) due to the nested loops.</li>
    <li><strong>Space Complexity</strong>: O(n) for the result list ans.</li>
</ul>

<p><strong>Efficient Approach</strong></p>

<p><strong>Intuition in Simple Words</strong></p>
<p>In a circular array, imagine the array is connected end-to-end. For each element, we want to find the next greater element, even if it means wrapping around to the beginning of the array.</p>
<p>To do this efficiently:</p>
<ul>
    <li><strong>Use a Stack</strong>: Think of the stack as a tool to keep track of elements that might be the next greater element for upcoming elements.</li>
    <li><strong>Process from End to Start</strong>: By going backwards, we can ensure that we have already considered all potential next greater elements for each element as we encounter it.</li>
    <li><strong>Wrap Around</strong>: By looping through the array twice, we simulate the circular nature without explicitly handling it separately.</li>
</ul>

<p><strong>Step-by-Step Process</strong></p>
<ol>
    <li><strong>Initialize</strong>:
        <ul>
            <li>Start with an empty stack and an empty result list.</li>
        </ul>
    </li>
    <li><strong>Loop Through Elements Backwards Twice</strong>:
        <ul>
            <li>This means we effectively handle the circular part without extra complexity.</li>
        </ul>
    </li>
    <li><strong>For Each Element</strong>:
        <ul>
            <li><strong>Pop Elements from the Stack</strong>: Remove elements from the stack that are less than or equal to the current element because they can't be the next greater element.</li>
            <li><strong>Add to Result</strong>: If we are in the first pass (i.e., actual elements in the array), append the top element of the stack to the result as it is the next greater element. If the stack is empty, append <strong>-1</strong> (no greater element found).</li>
            <li><strong>Push Current Element</strong>: Push the current element onto the stack as it might be the next greater element for upcoming elements.</li>
        </ul>
    </li>
    <li><strong>Reverse the Result</strong>:
        <ul>
            <li>Since we collected results in reverse order, reverse <strong>ans</strong> before returning.</li>
        </ul>
    </li>
</ol>

```python
def optimized(n, arr):
    ans = []
    stack = []
    for j in range(2 * n - 1, -1, -1):
        i = j % n
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        if j < n:
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
        stack.append(arr[i])
    ans = ans[::-1]
    return ans
arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```

<p><strong>Example Walkthrough</strong></p>

<p>Consider the array <strong>[4, 5, 2, 10, 8]</strong>:</p>

<ol>
    <li><strong>Initialization</strong>:
        <ul>
            <li><strong>ans = []</strong></li>
            <li><strong>stack = []</strong></li>
        </ul>
    </li>
    <li><strong>Process each element (in reverse order)</strong>:
        <ul>
            <li><strong>Element 8</strong> (at index 4):
                <ul>
                    <li>Check: Stack is empty.</li>
                    <li>Push <strong>8</strong> onto stack.</li>
                    <li><strong>stack = [8]</strong></li>
                </ul>
            </li>
            <li><strong>Element 10</strong> (at index 3):
                <ul>
                    <li>Check: 8 is less than 10, pop 8.</li>
                    <li>Push <strong>10</strong> onto stack.</li>
                    <li><strong>stack = [10]</strong></li>
                </ul>
            </li>
            <li><strong>Element 2</strong> (at index 2):
                <ul>
                    <li>Check: Stack is not empty, 10 is greater.</li>
                    <li>Append <strong>10</strong> to <strong>ans</strong>.</li>
                    <li>Push <strong>2</strong> onto stack.</li>
                    <li><strong>ans = [10]</strong></li>
                    <li><strong>stack = [10, 2]</strong></li>
                </ul>
            </li>
            <li><strong>Element 5</strong> (at index 1):
                <ul>
                    <li>Check: 2 is less than 5, pop 2.</li>
                    <li>Stack is not empty, 10 is greater.</li>
                    <li>Append <strong>10</strong> to <strong>ans</strong>.</li>
                    <li>Push <strong>5</strong> onto stack.</li>
                    <li><strong>ans = [10, 10]</strong></li>
                    <li><strong>stack = [10, 5]</strong></li>
                </ul>
            </li>
            <li><strong>Element 4</strong> (at index 0):
                <ul>
                    <li>Check: Stack is not empty, 5 is greater.</li>
                    <li>Append <strong>5</strong> to <strong>ans</strong>.</li>
                    <li>Push <strong>4</strong> onto stack.</li>
                    <li><strong>ans = [10, 10, 5]</strong></li>
                    <li><strong>stack = [10, 5, 4]</strong></li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>Reverse the Result</strong>:
        <ul>
            <li><strong>ans = [5, 10, 10, -1, 10]</strong> (after reversing)</li>
        </ul>
    </li>
</ol>

<p><strong>Summary</strong></p>
<ul>
    <li><strong>Time Complexity</strong>: O(n) because each element is pushed and popped from the stack at most once.</li>
    <li><strong>Space Complexity</strong>: O(n) for the stack and result list <strong>ans</strong>.</li>
</ul>

<p><strong>Next Smaller Element in Circular Array</strong></p>

<p><strong>Intuition</strong></p>
<p>In a circular array, we treat the array as if it loops around. For each element, we look for the next smaller element. We use a stack to keep track of potential next smaller elements efficiently.</p>

<p><strong>Code</strong></p>

```python
def next_smaller(n, arr):
    ans = []
    stack = []
    for j in range(2 * n - 1, -1, -1):
        i = j % n
        while stack and arr[i] <= stack[-1]:
            stack.pop()
        if j < n:
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
        stack.append(arr[i])
    ans = ans[::-1]
    return ans
```

<p><strong>Previous Smaller Element in Circular Array</strong></p>

<p><strong>Intuition</strong></p>
<p>For each element in the circular array, we look for the previous element that is smaller than it. We use a stack to keep track of potential previous smaller elements efficiently.</p>

<p><strong>Code</strong></p>

```python
def previous_smaller(n, arr):
    ans = [-1] * n
    stack = []
    for j in range(n):
        i = j % n
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            ans[i] = arr[stack[-1]]
        stack.append(i)
    return ans
```

<p><strong>Previous Greater Element in Circular Array</strong></p>

<p><strong>Intuition</strong></p>
<p>For each element in the circular array, we look for the previous element that is greater than it. We use a stack to keep track of potential previous greater elements efficiently.</p>

<p><strong>Code</strong></p>

```python
def previous_greater(n, arr):
    ans = [-1] * n
    stack = []
    for j in range(n):
        i = j % n
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            ans[i] = arr[stack[-1]]
        stack.append(i)
    return ans
```


<br>
<br>

<h2>Sum Of Subarray Minimums</h2>
<p>Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.</p>

<p><strong>Examples</strong></p>
<p><strong>Input:</strong>arr = [3,1,2,4] </p>
<p><strong>Output:</strong>17</p>
<p><strong>Explanation:</strong>Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.Sum is 17.</p>
<p><strong>Input:</strong>arr = [11,81,94,43,3] </p>
<p><strong>Output:</strong>444</p>

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>

<p><strong>BruteForce Approach</strong></p>
<p>In this approach, we will find out all possible subarrays for given array, and for each subarrays we will find minimum value</p>
<p>The sum of all minimum values will be our answer</p>

```python
def bruteforce(n,arr):
    sum=0
    for i in range(n):
        for j in range(i,n):
            mini=float('inf')
            for k in range(i,j+1):
                mini=min(mini,arr[k])
            sum+=mini
    return sum
arr=list(map(int,input().split()))
n=len(arr)
print(bruteforce(n,arr))
```

<p><strong>Time Complexity :</strong> O(n^3), since we have 3 nested loops</p>
<p><strong>Space Complexity :</strong>O(1), we are not using any extra space</p>

<p><strong>Better Approach</strong></p>
<p>We will just modify the above approach, to eliminate 3rd inner loop</p>

```python
def better(n,arr):
    sum=0
    for i in range(n):
        mini=float('inf')
        for j in range(i,n):
            mini=min(mini,arr[j])
            sum+=mini
    return sum
arr=list(map(int,input().split()))
n=len(arr)
print(bruteforce(n,arr))
```
<p><strong>Time Complexity :</strong> O(n^2), since we have 2 nested loops</p>
<p><strong>Space Complexity :</strong>O(1), we are not using any extra space</p>

<p><strong>Efficient Approach</strong></p>
<p>In this approach, We will loop through given array, for each element, we will find how many subarrays will have current element as minimum cuurent, then we will multiply current element with number of possible subbarrays, then will add that to final sum</p>
<p>Each number in the array can be the smallest number in several subarrays. We need to figure out how many times each number is the smallest in different subarrays and then sum up these contributions.</p>
<p>To find out how many subarrays have a specific element as the smallest element, follow these simple steps:</p>
<ul>
    <li><strong>Identify Boundaries:</strong></li>
    <ul>
        <li>For each element in the array, figure out:
            <ul>
                <li><strong>How far to the left</strong> you can go while this element is still the smallest.</li>
                <li><strong>How far to the right</strong> you can go while this element is still the smallest.</li>
            </ul>
        </li>
    </ul>
</ul>

<ul>
    <li><strong>Calculate the Lengths:</strong></li>
    <ul>
        <li><strong>Left Length:</strong> How many subarrays start from this element and extend to the left boundary.</li>
        <li><strong>Right Length:</strong> How many subarrays end at this element and extend to the right boundary.</li>
    </ul>
</ul>

<p><strong>Example</strong></p>
<p>Let's use an array <strong>[3, 1, 2, 4]</strong> and find out how many subarrays have the element <strong>2</strong> (at index 2) as the smallest.</p>

<ul>
    <li><strong>Find the Boundaries for 2:</strong></li>
    <ul>
        <li><strong>Left Boundary:</strong>
            <p>Look to the left of <strong>2</strong> to see how far you can extend while <strong>2</strong> is still the smallest.</p>
            <p>The nearest smaller number to the left of <strong>2</strong> is <strong>1</strong> (at index 1).</p>
            <p>So, <strong>2</strong> can extend left to the position right after <strong>1</strong> (i.e., index 2 can start from index 1 and extend to index 2).</p>
        </li>
        <li><strong>Right Boundary:</strong>
            <p>Look to the right of <strong>2</strong> to see how far you can extend while <strong>2</strong> is still the smallest.</p>
            <p>The nearest smaller number to the right of <strong>2</strong> is <strong>4</strong> (at index 3).</p>
            <p>So, <strong>2</strong> can extend right up to index 3 (i.e., index 2 can end at index 3).</p>
        </li>
    </ul>
</ul>

<ul>
    <li><strong>Calculate the Lengths:</strong></li>
    <ul>
        <li><strong>Left Length:</strong>
            <p>From index <strong>2</strong>, you can extend to the start of the array (index <strong>1</strong>).</p>
            <p>So, <strong>Left Length</strong> = <strong>2 - 1</strong> = <strong>1</strong></p>
        </li>
        <li><strong>Right Length:</strong>
            <p>From index <strong>2</strong>, you can extend up to index <strong>3</strong>.</p>
            <p>So, <strong>Right Length</strong> = <strong>3 - 2</strong> = <strong>1</strong></p>
        </li>
    </ul>
</ul>

<p><strong>Count Subarrays:</strong></p>
<p><strong>Number of Subarrays with 2 as the Minimum:</strong></p>
<p>The total number of subarrays where <strong>2</strong> is the smallest is <strong>Left Length * Right Length</strong>.</p>
<p>For <strong>2</strong>: <strong>1 (Left Length) * 1 (Right Length) = 1</strong></p>

<p><strong>Summary</strong></p>
<ol>
    <li>For each number, find out how far left and right you can go while keeping that number as the smallest.</li>
    <li>Multiply these two lengths to get the number of subarrays where that number is the smallest.</li>
</ol>

<p>In Order to find, previous smaller and next smaller for each element in given array, we can use algorithms discussed previously</p>

<p>The given code solves the problem of finding the sum of the minimum values of all subarrays efficiently. It consists of three main parts:</p>

<ul>
    <li><strong>Finding the Next Smaller Element:</strong> Computes the index of the next smaller element for each element in the array.</li>
    <li><strong>Finding the Previous Smaller or Equal Element:</strong> Computes the index of the previous smaller or equal element for each element in the array.</li>
    <li><strong>Calculating the Total Sum:</strong> Uses the results from the previous two functions to calculate the total sum of minimum values of all subarrays.</li>
</ul>

<p><strong>1. nextSmallerElement(n, arr)</strong></p>
<p>This function computes the index of the next smaller element for each element in the array. If there is no smaller element to the right, it returns <code>n</code> (the length of the array).</p>
<ul>
    <li><strong>Input:</strong> <code>n</code> (length of the array), <code>arr</code> (the array of integers)</li>
    <li><strong>Output:</strong> A list where each position contains the index of the next smaller element.</li>
</ul>
<p><strong>How it works:</strong></p>
<ul>
    <li>Traverse the array from right to left.</li>
    <li>Use a stack to keep track of indices of elements.</li>
    <li>For each element, pop from the stack while the stack's top element is greater than or equal to the current element.</li>
    <li>If the stack is not empty, the top of the stack is the index of the next smaller element; otherwise, use <code>n</code>.</li>
    <li>Append the current index to the stack.</li>
    <li>Reverse the result list at the end to match the original order of the array.</li>
</ul>

<p><strong>2. previousSmallerOrEqualElement(n, arr)</strong></p>
<p>This function computes the index of the previous smaller or equal element for each element in the array. If there is no such smaller or equal element to the left, it returns <code>-1</code>.</p>
<ul>
    <li><strong>Input:</strong> <code>n</code> (length of the array), <code>arr</code> (the array of integers)</li>
    <li><strong>Output:</strong> A list where each position contains the index of the previous smaller or equal element.</li>
</ul>
<p><strong>How it works:</strong></p>
<ul>
    <li>Traverse the array from left to right.</li>
    <li>Use a stack to keep track of indices of elements.</li>
    <li>For each element, pop from the stack while the stack's top element is strictly greater than the current element (since we are looking for smaller or equal elements).</li>
    <li>If the stack is not empty, the top of the stack is the index of the previous smaller or equal element; otherwise, use <code>-1</code>.</li>
    <li>Append the current index to the stack.</li>
</ul>

<p><strong>3. optimized(n, arr)</strong></p>
<p>This function calculates the sum of minimum values of all subarrays using the results from the two helper functions above.</p>
<ul>
    <li><strong>Input:</strong> <code>n</code> (length of the array), <code>arr</code> (the array of integers)</li>
    <li><strong>Output:</strong> The total sum of minimum values of all subarrays.</li>
</ul>
<p><strong>How it works:</strong></p>
<ul>
    <li>Compute the next smaller element (NSE) and previous smaller or equal element (PSE) arrays using the two helper functions.</li>
    <li>For each element in the array:
        <ul>
            <li>Calculate how many subarrays it can be the smallest in by using the difference between its index and the NSE and PSE indices.</li>
            <li>Multiply the number of such subarrays by the element's value.</li>
            <li>Sum these contributions to get the final result.</li>
        </ul>
    </li>
</ul>

<p><strong>Example Walkthrough</strong></p>
<p>Consider <code>arr = [3, 1, 2, 4]</code>.</p>
<ul>
    <li><strong>For element 3 at index 0:</strong>
        <ul>
            <li><strong>NSE:</strong> Index 1 (value 1 is the next smaller element).</li>
            <li><strong>PSE:</strong> No smaller element to the left, so index -1.</li>
            <li><strong>Right Length:</strong> <code>NSE[0] - 0 = 1</code></li>
            <li><strong>Left Length:</strong> <code>0 - PSE[0] = 0 - (-1) = 1</code></li>
            <li><strong>Contribution:</strong> <code>3 * 1 * 1 = 3</code></li>
        </ul>
    </li>
    <li><strong>For element 1 at index 1:</strong>
        <ul>
            <li><strong>NSE:</strong> Index 2 (value 2 is the next smaller element).</li>
            <li><strong>PSE:</strong> No smaller element to the left, so index -1.</li>
            <li><strong>Right Length:</strong> <code>NSE[1] - 1 = 2 - 1 = 1</code></li>
            <li><strong>Left Length:</strong> <code>1 - PSE[1] = 1 - (-1) = 2</code></li>
            <li><strong>Contribution:</strong> <code>1 * 1 * 2 = 2</code></li>
        </ul>
    </li>
    <li><strong>For element 2 at index 2:</strong>
        <ul>
            <li><strong>NSE:</strong> Index 3 (value 4 is the next smaller element).</li>
            <li><strong>PSE:</strong> Index 1 (value 1 is the previous smaller element).</li>
            <li><strong>Right Length:</strong> <code>NSE[2] - 2 = 3 - 2 = 1</code></li>
            <li><strong>Left Length:</strong> <code>2 - PSE[2] = 2 - 1 = 1</code></li>
            <li><strong>Contribution:</strong> <code>2 * 1 * 1 = 2</code></li>
        </ul>
    </li>
    <li><strong>For element 4 at index 3:</strong>
        <ul>
            <li><strong>NSE:</strong> Beyond the end of the array, so <code>n</code>.</li>
            <li><strong>PSE:</strong> Index 2 (value 2 is the previous smaller element).</li>
            <li><strong>Right Length:</strong> <code>NSE[3] - 3 = 4 - 3 = 1</code></li>
            <li><strong>Left Length:</strong> <code>3 - PSE[3] = 3 - 2 = 1</code></li>
            <li><strong>Contribution:</strong> <code>4 * 1 * 1 = 4</code></li>
        </ul>
    </li>
</ul>

<p><strong>Final Sum Calculation</strong></p>
<p>Add up all the contributions: <code>3 + 2 + 2 + 4 = 11</code>.</p>


```python
def nextSmallerElement(n,arr):
    ans=[]
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and arr[i]<=arr[stack[-1]]:
            stack.pop()
        if(stack):
            ans.append(stack[-1])
        else:
            ans.append(n)
        stack.append(i)
    return ans[::-1]

def previousSmallerOrEqualElement(n,arr):
    ans=[]
    stack=[]
    for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
            stack.pop()
        if(stack):
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(i)
    return ans

def optimized(n,arr):
    nse=nextSmallerElement(n,arr)
    pse=previousSmallerOrEqualElement(n,arr)
    sum=0
    for i in range(n):
        right=nse[i]-i
        left=i-pse[i]
        sum+=(left*right*arr[i])
    return sum

arr=list(map(int,input().split()))
n=len(arr)
print(optimized(n,arr))
```

<ul>
    <li><strong>Time Complexity</strong>O(n) for each function, and thus O(n) for the combined operations.</li>
    <li><strong>Space Complexity</strong>O(n) due to the storage required for the stack and result arrays.</li>
</ul>

<br>
<br>

<h2>Sum of Subarray Ranges</h2>
<p>You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.</p>
<p>Return the sum of all subarray ranges of nums.</p>
<p>A subarray is a contiguous non-empty sequence of elements within an array.</p>
<p><strong>Examples</strong></p>
<pre>
Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
</pre>
<pre>
Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
</pre>
<pre>
Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
</pre>

<p><strong>Solution</strong></p>

<p>The problem is to find the sum of all subarray ranges of a given integer array <code>nums</code>. The range of a subarray is the difference between the largest and smallest element in that subarray.</p>

<p><strong>BruteForce Approach</strong></p>
<p><strong>Explanation:</strong> This approach calculates the sum of ranges for all possible subarrays by explicitly iterating over all possible subarrays.</p>
<ul>
    <li>Iterate over all starting indices of subarrays.</li>
    <li>For each starting index, iterate over all ending indices.</li>
    <li>For each subarray defined by these indices, find the minimum and maximum values.</li>
    <li>Compute the range (difference between maximum and minimum) and add it to the total sum.</li>
</ul>
<p><strong>Complexity:</strong> O(n^3) due to nested loops for subarray and element comparisons.</p>

```python
def bruteforce(n, arr):
    sum = 0
    for i in range(n):
        for j in range(i, n):
            mini = float('inf')
            maxi = float('-inf')
            for k in range(i, j + 1):
                mini = min(mini, arr[k])
                maxi = max(maxi, arr[k])
            sum += (maxi - mini)
    return sum
```

<p><strong>Better Approach</strong></p>

<p><strong>Explanation:</strong> This approach improves upon the brute force approach by maintaining the minimum and maximum values while expanding the subarray.</p>
<ul>
    <li>Iterate over all starting indices of subarrays.</li>
    <li>For each starting index, initialize minimum and maximum values.</li>
    <li>Expand the subarray by extending the ending index and updating the minimum and maximum values.</li>
    <li>Compute the range and add it to the sum.</li>
</ul>

<p><strong>Complexity:</strong> O(n^2) due to nested loop for subarrays and linear update operations.</p>

```python
def better(n, arr):
    sum = 0
    for i in range(n):
        mini = float('inf')
        maxi = float('-inf')
        for j in range(i, n):
            mini = min(mini, arr[j])
            maxi = max(maxi, arr[j])
            sum += (maxi - mini)
    return sum
```

<p><strong>Optimized Approach</strong></p>
<p>In this approach, simply we will find minimum sum and maximum sum as previous problem, and the difference would be our answer</p>
<p><strong>Explanation:</strong> This approach uses monotonic stacks to efficiently calculate the contribution of each element to the total sum of ranges.</p>
<ul>
    <li>Compute the next and previous smaller or equal elements and the next and previous greater or equal elements using stacks.</li>
    <li>Calculate the contribution of each element as minimum and maximum in all possible subarrays.</li>
    <li>Subtract the total contribution of minimum values from the total contribution of maximum values to get the final result.</li>
</ul>

<p><strong>Complexity:</strong> O(n) for each of the stack-based computations, resulting in an overall O(n) complexity.</p>

```python
def nextSmallerElement(n, arr):
    ans = []
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(n)
        stack.append(i)
    return ans[::-1]

def previousSmallerOrEqualElement(n, arr):
    ans = []
    stack = []
    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(i)
    return ans

def optimizedMin(n, arr):
    nse = nextSmallerElement(n, arr)
    pse = previousSmallerOrEqualElement(n, arr)
    sum = 0
    for i in range(n):
        right = nse[i] - i
        left = i - pse[i]
        sum += (left * right * arr[i])
    return sum

def nextGreaterElement(n, arr):
    ans = []
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(n)
        stack.append(i)
    return ans[::-1]

def previousGreaterOrEqualElement(n, arr):
    ans = []
    stack = []
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(i)
    return ans

def optimizedMax(n, arr):
    nse = nextGreaterElement(n, arr)
    pse = previousGreaterOrEqualElement(n, arr)
    sum = 0
    for i in range(n):
        right = nse[i] - i
        left = i - pse[i]
        sum += (left * right * arr[i])
    return sum

def optimized(n, arr):
    return optimizedMax(n, arr) - optimizedMin(n, arr)
```

<ul>
    <li><strong>Time Complexity</strong>O(n) for each function, and thus O(n) for the combined operations.</li>
    <li><strong>Space Complexity</strong>O(n) due to the storage required for the stack and result arrays.</li>
</ul>

<br>
<br>


<h2>Asteroid Collision</h2>
<p>We are given an array asteroids of integers representing asteroids in a row.</p>
<p>For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.</p>
<p>Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.</p>

<p><strong>Examples</strong></p>
<p><strong>Input : </strong>asteroids = [5,10,-5]</p>
<p><strong>Output : </strong>[5,10]</p>
<p><strong>Explantion : </strong>The 10 and -5 collide resulting in 10. The 5 and 10 never collide.</p>
<p><strong>Input : </strong>asteroids = [8,-8]</p>
<p><strong>Output : </strong>[]</p>
<p><strong>Explantion : </strong>The 8 and -8 collide exploding each other. </p>
<p><strong>Input : </strong>asteroids = [10,2,-5]</p>
<p><strong>Output : </strong>[10]</p>
<p><strong>Explantion : </strong>The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.</p>

<p><strong>Solution</strong></p>
<p><strong>Problem Understanding:</strong></p>
<ul>
    <li><strong>Asteroid Representation:</strong>
        <ul>
            <li>Positive values represent asteroids moving to the right.</li>
            <li>Negative values represent asteroids moving to the left.</li>
            <li>Two asteroids moving in the same direction will not collide.</li>
        </ul>
    </li>
    <li><strong>Collision Rules:</strong>
        <ul>
            <li>When a right-moving asteroid (positive) meets a left-moving asteroid (negative):
                <ul>
                    <li>The larger asteroid survives, and the smaller one explodes.</li>
                    <li>If they are of equal size, both explode.</li>
                </ul>
            </li>
            <li>If both asteroids are moving in the same direction, they don’t collide.</li>
        </ul>
    </li>
</ul>

<p><strong>Solution Strategy:</strong></p>
<ul>
    <li><strong>Use a Stack:</strong> The stack will help us keep track of the asteroids that are moving to the right and haven't yet collided with any asteroids moving to the left.</li>
    <li><strong>Iterate Through Asteroids:</strong> For each asteroid, check if it collides with the top asteroid in the stack. Handle the collision based on the size of the asteroids and update the stack accordingly.</li>
</ul>

<p><strong>Detailed Steps:</strong></p>
<ol>
    <li><strong>Initialize an Empty Stack:</strong> This stack will store the asteroids moving to the right.</li>
    <li><strong>Process Each Asteroid:</strong>
        <ul>
            <li>If the current asteroid is moving to the right (positive value), push it onto the stack.</li>
            <li>If the current asteroid is moving to the left (negative value):
                <ul>
                    <li>Check collisions with the top of the stack:
                        <ul>
                            <li>Pop the stack while collisions occur (i.e., the top asteroid is moving to the right and is larger).</li>
                            <li>If the top of the stack is equal to the absolute value of the current asteroid, pop the stack (both explode).</li>
                            <li>If the stack is empty or the top of the stack is a left-moving asteroid, push the current asteroid onto the stack.</li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>Return the Final Stack:</strong> The stack will contain the state of the asteroids after all collisions.</li>
</ol>

<p><strong>Python Code Implementation:</strong></p>

```python
def asteroidCollision(asteroids):
    stack = []

    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
        else:
            while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                stack.pop()
            if stack and stack[-1] == abs(asteroid):
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(asteroid)

    return stack
arr=list(map(int,input().split()))
n=len(arr)
print(asteroidCollision(n,arr))
````

<p><strong>Example Walkthrough:</strong></p>
<ul>
    <li><strong>Example Input:</strong>
        <pre><code>asteroids = [5, 10, -5]</code></pre>
    </li>
    <li><strong>Execution Steps:</strong>
        <ul>
            <li><strong>Process 5:</strong> Positive, push onto the stack. Stack: [5]</li>
            <li><strong>Process 10:</strong> Positive, push onto the stack. Stack: [5, 10]</li>
            <li><strong>Process -5:</strong>
                <ul>
                    <li>Collision with 10:</li>
                    <li>10 is larger than 5, so 10 survives and -5 does not collide.</li>
                    <li>Stack: [5, 10] (no changes needed)</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>Final Stack:</strong> After processing all asteroids, the stack contains [5, 10], indicating that these asteroids survived.</li>
    <li><strong>Example Output:</strong>
        <pre><code>[5, 10]</code></pre>
    </li>
</ul>

<p><strong>Complexity Analysis:</strong></p>
<ul>
    <li><strong>Time Complexity:</strong> O(n), where n is the number of asteroids. Each asteroid is pushed and popped from the stack at most once.</li>
    <li><strong>Space Complexity:</strong> O(n), due to the space required for the stack in the worst case.</li>
</ul>

<br>
<br>

<h2>Remove K Digits</h2>
<p>Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num</p>
<p><strong>Examples</strong></p>
<p><strong>Input :</strong>num = "1432219", k = 3</p>
<p><strong>Output :</strong>"1219"</p>
<p><strong>Explantion :</strong>Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.</p>
<p><strong>Input :</strong>num = "10200", k = 1</p>
<p><strong>Output :</strong>"200"</p>
<p><strong>Explantion :</strong>Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.</p>
<p><strong>Input :</strong>num = "10", k = 2</p>
<p><strong>Output :</strong>"0"</p>
<p><strong>Explantion :</strong>Remove all the digits from the number and it is left with nothing which is 0.</p>

<p><strong>Solution</strong></p>
<h2>Approach:</h2>

<ol>
    <li><strong>Using a Stack:</strong>
        <p>Think of a stack as a "smart list" where you can easily add and remove elements. We’ll use this stack to build the smallest possible number step-by-step.</p>
    </li>
    <li><strong>Processing Digits:</strong>
        <ul>
            <li><strong>Check if the current digit can make the number smaller:</strong> If the digit you are currently looking at is smaller than the last digit in the stack, and you still have digits left to remove (<code>k</code>), then remove the last digit from the stack.</li>
            <li><strong>Add the current digit to the stack:</strong> After adjusting the stack, add the current digit to the stack.</li>
        </ul>
    </li>
    <li><strong>Removing Remaining Digits:</strong>
        <p>After processing all digits, if there are still digits left to remove (<code>k</code> is still greater than 0), remove digits from the end of the stack.</p>
    </li>
    <li><strong>Forming the Final Number:</strong>
        <ul>
            <li>Convert the stack to a string to form the number.</li>
            <li>Remove any leading zeros (because they don’t count in a number).</li>
            <li>If the result is empty (meaning you removed all digits), return <code>'0'</code>.</li>
        </ul>
    </li>
</ol>

<h2>Why This Works:</h2>

<ul>
    <li><strong>Removing Larger Digits First:</strong> By removing larger digits when you find a smaller digit that comes after them, you ensure the remaining digits form a smaller number.</li>
    <li><strong>Building in a Greedy Way:</strong> You’re always making the best choice locally (removing digits to make the number smaller) to achieve the smallest overall number.</li>
</ul>

<h2>Example:</h2>

<p>For the number <code>1432219</code> with <code>k = 3</code>:</p>

<ol>
    <li>Start with an empty stack.</li>
    <li>Add '1' to the stack.</li>
    <li>Add '4' to the stack.</li>
    <li>When you reach '3', '3' is smaller than '4', so remove '4' (because '3' makes the number smaller when it's before '4').</li>
    <li>Continue this process for each digit.</li>
</ol>

<p>After processing all digits and removing any leftover digits if necessary, you end up with the smallest possible number after removing <code>k</code> digits.</p>

<p>This method ensures that at each step, you’re making choices that lead to the smallest number overall.</p>


```python
def solve(n,s,k):
    stack=[]
    for i in range(n):
        while stack and int(s[i]) <int(stack[-1]) and k>0:
            stack.pop()
            k-=1
        stack.append(s[i])

    while k>0:
        k-=1
        stack.pop()
    final="".join(stack).lstrip('0')
    return final if final else '0'

s=input()
n=len(s)
k=int(input())
print(solve(n,s,k))
```

<ul>
    <li><strong>Time Complexity:</strong> O(n), where n is the number of digits traversed</li>
    <li><strong>Space Complexity:</strong> O(n), due to the space required for the stack in the worst case.</li>
</ul>


<h2>Area of largest rectangle in Histogram</h2>
<p>Given an array of integers heights representing the histogram's bar height where the width of each bar is 1  return the area of the largest rectangle in histogram.</p>
<p><strong>Examples</strong></p>
<p><strong>Input : </strong>N =6, heights[] = {2,1,5,6,2,3}</p>
<p><strong>Output : </strong>10</p>
<p><strong>Explanation : </strong></p>
<img src="https://lh3.googleusercontent.com/0HBN1kCWyRdgeNIlyx7qYR5sQM6qQaqFDTFO_0BeolTyHuWTD9xmawkqhxmrKwcBjLDcd3p73JfhNTZr0JxGtYv5fw3gDU1ccJa7JJZiO4VM32QA92VFIob1YTFaVEN3r4UVUzm3">

<p><strong>Solution</strong></p>
<p>This problem can be solved in several approaches</p>
<p></p>