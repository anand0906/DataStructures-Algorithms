<h1>Queue</h1>
<p>A Queue is a linear data structure that follows <strong>First in First Out (FIFO)</strong> principle</p>
<p>This means the first element added to the queue will be the first one to be removed</p>
<p>Queues are used in scenarios where ordering and processing in the order of arrival are important, such as in print job management, CPU scheduling, and breadth-first search algorithms in graphs.</p>
<h3>FIFO Principle</h3>
<p>A Queue is like a line waiting to purchase tickets, where the first person in line is the first person served. (i.e. First come first serve).</p>
<p>Position of the entry in a queue ready to be served, that is, the first entry that will be removed from the queue, is called the front of the queue(sometimes, head of the queue), similarly, the position of the last entry in the queue, that is, the one most recently added, is called the rear (or the tail) of the queue. See the below figure.</p>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220805131014/fifo.png">
<h3>Key Characteristics</h3>
<ul>
	<li><strong>FIFO</strong> : The first element enqueued (inserted) is the first one to be dequeued (removed).</li>
	<li><strong>Operations</strong></li>
	<ul>
		<li><strong>Enqueue : </strong>Addition of an element to the queue</li>
		<li><strong>Dequeue : </strong>Removal of an element from the queue</li>
		<li><strong>Front : </strong>Get the front element from the queue</li>
		<li><strong>Rear : </strong>Get the rear element from the queue</li>
	</ul>
</ul>
<h3>Applications</h3>
<p>Queue is used when things don’t have to be processed immediately, but have to be processed in First In First Out order. </p>
<p><strong>Useful Applications of Queue</strong></p>
<ul>
	<li>When a resource is shared among multiple consumers. Examples include CPU scheduling, Disk Scheduling.</li>
	<li>When data is transferred asynchronously (data not necessarily received at the same rate as sent) between two processes. Examples include IO Buffers, pipes, etc. </li>
</ul>
<h4>Applications of Queue in Operating Systems</h4>
<ul>
    <li>
        <strong>Semaphores</strong>
        <p>Semaphores are synchronization primitives used to control access to shared resources by multiple processes. They can be implemented using queues in the following ways:</p>
        <ul>
            <li><strong>Queue of Waiting Processes:</strong> When a process wants to access a shared resource and the semaphore value indicates that the resource is currently unavailable, the process is placed in a queue. This queue is known as the semaphore queue or wait queue. The semaphore maintains this queue to manage processes waiting for the resource to become available.</li>
            <li><strong>Implementation Detail:</strong> The queue here ensures that processes are given access in a controlled manner (such as FIFO) when the resource becomes available.</li>
        </ul>
    </li>
    <li>
        <strong>FCFS (First-Come, First-Served) Scheduling</strong>
        <p>FCFS Scheduling is one of the simplest CPU scheduling algorithms. In this method:</p>
        <ul>
            <li><strong>FIFO Queue:</strong> Processes are managed in a First-Come, First-Served order. The processes that arrive first are placed in a FIFO queue. The CPU scheduler then picks processes from this queue in the same order they arrived.</li>
            <li><strong>Example:</strong> If processes P1, P2, and P3 arrive in that order, P1 will be executed first, followed by P2, and then P3. This order is maintained using a FIFO queue, ensuring fairness based on arrival time.</li>
        </ul>
    </li> 
    <li>
        <strong>Spooling in Printers</strong>
        <p>Spooling (Simultaneous Peripheral Operations On-Line) involves managing the order and execution of tasks related to input/output operations. In the context of printers:</p>
        <ul>
            <li><strong>Print Queue:</strong> Spooling uses a queue to manage print jobs. When multiple print jobs are sent to the printer, they are placed in a print queue. The printer then processes these jobs one by one in the order they were received.</li>
            <li><strong>Benefits:</strong> This queue allows the CPU to continue processing other tasks while print jobs are handled by the printer in the background, thereby improving efficiency and resource utilization.</li>
        </ul>
    </li>
    <li>
        <strong>Buffer for Devices (e.g., Keyboard)</strong>
        <p>Buffers are used to temporarily store data while it is being transferred between different components or devices. For devices like keyboards:</p>
        <ul>
            <li><strong>Input Buffer:</strong> When a user types on a keyboard, the keystrokes are placed in an input buffer. This buffer is essentially a queue where keystrokes are stored until they are processed by the system or application.</li>
            <li><strong>Handling Input:</strong> The input buffer allows the operating system to handle input at its own pace, ensuring that keystrokes are not lost and are processed in the correct order.</li>
        </ul>
    </li>
</ul>
<h4>Applications of Queue in Networks</h4>
<ul>
    <li>
        <strong>Queues in Routers/Switches</strong>
        <p>In networking devices such as routers and switches, queues are essential for managing network traffic. Here’s how they are used:</p>
        <ul>
            <li><strong>Traffic Management:</strong> Routers and switches use queues to manage the flow of packets. When packets arrive faster than they can be processed or forwarded, they are placed in a queue. This helps in handling bursts of traffic and ensures that packets are processed in the order they arrive.</li>
            <li><strong>Buffering:</strong> Queues act as buffers to hold packets temporarily. This buffering helps in smooth data transmission and prevents packet loss during network congestion.</li>
            <li><strong>Quality of Service (QoS):</strong> Queues are used to implement Quality of Service policies, prioritizing certain types of traffic over others. For example, voice traffic might be given higher priority over regular data traffic to ensure clear and uninterrupted communication.</li>
        </ul>
    </li>
    <li>
        <strong>Mail Queues</strong>
        <p>Mail queues are used in email systems to manage the delivery of email messages. Here’s how they function:</p>
        <ul>
            <li><strong>Outgoing Mail Queue:</strong> When an email is sent, it is placed in an outgoing mail queue. This queue holds the email until it can be delivered to the recipient’s mail server. The email server processes these queued messages sequentially to ensure proper delivery.</li>
            <li><strong>Incoming Mail Queue:</strong> Similarly, incoming emails are placed in an incoming mail queue when they arrive at a mail server. These emails are then processed and delivered to the recipients’ mailboxes. This queue helps manage email delivery and handle large volumes of incoming messages efficiently.</li>
            <li><strong>Retry Mechanism:</strong> If an email cannot be delivered immediately (e.g., due to a temporary issue with the recipient’s server), it remains in the queue and is retried at intervals. This ensures that emails are eventually delivered even if initial attempts fail.</li>
        </ul>
    </li>
</ul>
<h4>Other Applications</h4>
<ol>
	<li>Applied as waiting lists for a single shared resource like CPU, Disk, and Printer.</li>
	<li>Applied as buffers on MP3 players and portable CD players.</li>
	<li>Applied on Operating system to handle the interruption.</li>
	<li>Applied to add song at the end or to play from the front.</li>
	<li>Applied on WhatsApp when we send messages to our friends and they don’t have an internet connection then these messages are queued on the server of WhatsApp.</li>
</ol>


<h2>Queue Implmentation Using List</h2>

```python
class Queue:

    def __init__(self):
        self.queue=[]

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if(self.isEmpty()):
            raise IndexError("Queue is Empty !")
        return self.queue.pop(0)

    def getFront(self):
        if(self.isEmpty()):
            raise IndexError("Queue is Empty !")
        return self.queue[-1]

    def getRear(self):
        if(self.isEmpty()):
            raise IndexError("Queue is Empty !")
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.size()==0

queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.size())
```

<h2>Queue Implmentation Using Arrays Fixed Size</h2>

<p>Let's go through each function in your <strong>Queue</strong> class and explain it in simple terms:</p>

<p><strong>__init__(self, capacity)</strong></p>
<p>This is the constructor method that initializes the queue. It sets up the queue with a fixed capacity and initializes the necessary variables:</p>
<ul>
  <li><strong>self.capacity</strong> stores the maximum number of items the queue can hold.</li>
  <li><strong>self.queue</strong> creates a list of the specified capacity filled with zeroes.</li>
  <li><strong>self.size</strong> keeps track of the current number of elements in the queue.</li>
  <li><strong>self.front</strong> and <strong>self.rear</strong> are set to -1, indicating that the queue is initially empty.</li>
</ul>

<p><strong>enqueue(self, data)</strong></p>
<p>This method adds a new item (<strong>data</strong>) to the rear of the queue:</p>
<ul>
  <li>It first checks if the queue is full by comparing <strong>self.rear</strong> to <strong>self.capacity - 1</strong>. If it's full, it raises an <strong>IndexError</strong>.</li>
  <li>If the queue is initially empty (<strong>self.rear == -1</strong>), it sets both <strong>self.rear</strong> and <strong>self.front</strong> to 0.</li>
  <li>Otherwise, it increments <strong>self.rear</strong> to the next position.</li>
  <li>It then assigns the <strong>data</strong> to the <strong>self.queue</strong> at the <strong>self.rear</strong> position and increments <strong>self.size</strong>.</li>
</ul>

<p><strong>dequeue(self)</strong></p>
<p>This method removes an item from the front of the queue and returns it:</p>
<ul>
  <li>It first checks if the queue is empty by checking if <strong>self.front</strong> is -1. If it's empty, it raises an <strong>IndexError</strong>.</li>
  <li>It retrieves the item at the <strong>self.front</strong> position and stores it in the <strong>popped</strong> variable.</li>
  <li>If there is only one item left (<strong>self.size == 1</strong>), it resets <strong>self.front</strong> and <strong>self.rear</strong> to -1.</li>
  <li>Otherwise, it increments <strong>self.front</strong> to the next position.</li>
  <li>It decrements <strong>self.size</strong> and returns the <strong>popped</strong> item.</li>
</ul>

<p><strong>getRear(self)</strong></p>
<p>This method returns the item at the rear of the queue without removing it:</p>
<ul>
  <li>It checks if the queue is empty (<strong>self.rear == -1</strong>). If it's empty, it raises an <strong>IndexError</strong>.</li>
  <li>Otherwise, it returns the item at the <strong>self.rear</strong> position.</li>
</ul>

<p><strong>getFront(self)</strong></p>
<p>This method returns the item at the front of the queue without removing it:</p>
<ul>
  <li>It checks if the queue is empty (<strong>self.front == -1</strong>). If it's empty, it raises an <strong>IndexError</strong>.</li>
  <li>Otherwise, it returns the item at the <strong>self.front</strong> position.</li>
</ul>

<p><strong>getSize(self)</strong></p>
<p>This method returns the current number of items in the queue:</p>
<ul>
  <li>It simply returns the value of <strong>self.size</strong>.</li>
</ul>

<p><strong>isEmpty(self)</strong></p>
<p>This method checks if the queue is empty:</p>
<ul>
  <li>It returns <strong>True</strong> if <strong>self.size</strong> is 0, otherwise it returns <strong>False</strong>.</li>
</ul>

<p><strong>Example Usage</strong></p>
<p>Here is how the class is used:</p>
<ol>
  <li>queue = <strong>Queue(10)</strong>  # Creates a queue with capacity 10</li>
  <li>queue.<strong>enqueue(1)</strong>  # Adds 1 to the queue</li>
  <li>queue.<strong>enqueue(2)</strong>  # Adds 2 to the queue</li>
  <li>queue.<strong>enqueue(3)</strong>  # Adds 3 to the queue</li>
  <li>print(queue.queue)  # Prints the queue: [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]</li>
  <li>print(queue.dequeue())  # Removes and prints the front item: 1</li>
  <li>print(queue.dequeue())  # Removes and prints the front item: 2</li>
  <li>print(queue.dequeue())  # Removes and prints the front item: 3</li>
  <li>print(queue.getSize())  # Prints the size of the queue: 0</li>
</ol>


```python
class Queue:

    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[0]*capacity
        self.size=0
        self.front=-1
        self.rear=-1

    def enqueue(self,data):
        if(self.rear==(self.capacity-1)):
            raise IndexError("Queue is Full !")
        if(self.rear==-1):
            self.rear=0
            self.front=0
        else:
            self.rear+=1
        self.queue[self.rear]=data
        self.size+=1

    def dequeue(self):
        if(self.front==-1):
            raise IndexError("Queue is Empty !")
        popped=self.queue[self.front]
        if(self.size==1):
            self.rear=-1
            self.front=-1
        else:
            self.front+=1
        self.size-=1
        return popped

    def getRear(self):
        if(self.rear==-1):
            raise IndexError("Queue is Empty !")
        return self.queue[self.rear]

    def getFront(self):
        if(self.front==-1):
            raise IndexError("Queue is Empty !")
        return self.queue[self.front]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size==0

queue=Queue(10)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.getSize())
```


<h2>Queue Using Linked List</h2>

<p>Your implementation of the <strong>Queue</strong> class using a linked list is efficient and well-structured. Let's explain each part of the code:</p>

<p><strong>Class Node</strong></p>
<p>This class represents a node in the linked list. Each node contains some data and a reference to the next node in the list.</p>
<ul>
  <li><strong>self.data</strong> stores the data of the node.</li>
  <li><strong>self.next</strong> is a reference to the next node, initially set to None.</li>
</ul>

<p><strong>Class Queue</strong></p>
<p>This class implements the queue using linked list nodes.</p>
<ul>
  <li><strong>self.size</strong> keeps track of the number of elements in the queue.</li>
  <li><strong>self.rear</strong> points to the last node in the queue.</li>
  <li><strong>self.front</strong> points to the first node in the queue.</li>
</ul>

<p><strong>Method enqueue(self, data)</strong></p>
<p>This method adds a new item (<strong>data</strong>) to the rear of the queue.</p>
<ul>
  <li>If the queue is empty (<strong>self.rear is None</strong>), it creates a new node and sets both <strong>self.front</strong> and <strong>self.rear</strong> to this node.</li>
  <li>Otherwise, it creates a new node, sets the <strong>next</strong> pointer of the current <strong>self.rear</strong> to this new node, and then updates <strong>self.rear</strong> to the new node.</li>
  <li>It increments <strong>self.size</strong> by 1.</li>
</ul>

<p><strong>Method dequeue(self)</strong></p>
<p>This method removes an item from the front of the queue and returns its data.</p>
<ul>
  <li>If the queue is empty (<strong>self.front is None</strong>), it raises an <strong>IndexError</strong>.</li>
  <li>Otherwise, it stores the current <strong>self.front</strong> in a temporary variable <strong>temp</strong>, updates <strong>self.front</strong> to the next node, and if the queue becomes empty, it also sets <strong>self.rear</strong> to None.</li>
  <li>It decrements <strong>self.size</strong> by 1 and returns the data of the dequeued node.</li>
</ul>

<p><strong>Method isEmpty(self)</strong></p>
<p>This method checks if the queue is empty.</p>
<ul>
  <li>It returns <strong>True</strong> if <strong>self.rear</strong> is None, indicating the queue is empty. Otherwise, it returns <strong>False</strong>.</li>
</ul>

<p><strong>Method getSize(self)</strong></p>
<p>This method returns the current number of items in the queue.</p>
<ul>
  <li>It simply returns the value of <strong>self.size</strong>.</li>
</ul>

```python
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:

    def __init__(self):
        self.size=0
        self.rear=None
        self.front=None

    def enqueue(self,data):
        if(self.rear==None):
            node=Node(data)
            self.front=node
            self.rear=node
        else:
            node=Node(data)
            self.rear.next=node
            self.rear=node
        self.size+=1

    def dequeue(self):
        if(self.front==None):
            raise IndexError("Queue is empty !")
        else:
            temp=self.front
            self.front=self.front.next
            if(self.front==None):
                self.rear=None
            self.size-=1
            return temp.data

    def isEmpty(self):
        return self.rear==None

    def getSize(self):
        return self.size
            

```


<h2>Queue Using Stack</h2>
<p>It can be impleneted in two approaches</p>

<p><strong>Intuition Behind Both Approaches</strong></p>

<p><strong>First Implementation</strong><br>
<strong>Enqueue Operation: O(n), Dequeue Operation: O(1)</strong></p>

<p><strong>Idea</strong>: Ensure elements are always in the correct order for dequeueing.</p>

<ul>
  <li><strong>Enqueue</strong>: To add a new element, first move all elements from <strong>stack1</strong> to <strong>stack2</strong>. This reverses the order of elements. Then, add the new element to <strong>stack1</strong>. Finally, move all elements back from <strong>stack2</strong> to <strong>stack1</strong>. This maintains the correct order for the queue.
    <ul>
      <li><strong>Why?</strong>: This ensures that the new element is always at the correct position in <strong>stack1</strong> for subsequent dequeue operations.</li>
    </ul>
  </li>
  <li><strong>Dequeue</strong>: Simply pop from <strong>stack1</strong>. The front of the queue is always at the top of <strong>stack1</strong>.
    <ul>
      <li><strong>Why?</strong>: Since elements are maintained in the correct order during enqueue, we can directly remove the front element from <strong>stack1</strong>.</li>
    </ul>
  </li>
</ul>

<p><strong>Second Implementation</strong><br>
<strong>Enqueue Operation: O(1), Dequeue Operation: O(n)</strong></p>

<p><strong>Idea</strong>: Separate stacks for enqueueing and dequeueing.</p>

<ul>
  <li><strong>Enqueue</strong>: Simply push the new element onto <strong>stack1</strong>. No reordering is necessary at this stage.
    <ul>
      <li><strong>Why?</strong>: Adding to the end of the queue is straightforward and does not require reordering elements already in the queue.</li>
    </ul>
  </li>
  <li><strong>Dequeue</strong>: When removing an element, check <strong>stack2</strong> first. If <strong>stack2</strong> is empty, move all elements from <strong>stack1</strong> to <strong>stack2</strong>. This reverses their order, making the oldest element (front of the queue) the top of <strong>stack2</strong>. Then, pop from <strong>stack2</strong>.
    <ul>
      <li><strong>Why?</strong>: By transferring elements from <strong>stack1</strong> to <strong>stack2</strong>, the oldest element moves to the top of <strong>stack2</strong>, ready for dequeueing. This ensures we always remove the correct element.</li>
    </ul>
  </li>
</ul>

<p><strong>Summary</strong></p>
<ol>
  <li><strong>First Implementation</strong>: Prioritizes fast dequeue operations by maintaining order during enqueue. This results in an <strong>O(n)</strong> enqueue time but <strong>O(1)</strong> dequeue time.</li>
  <li><strong>Second Implementation</strong>: Prioritizes fast enqueue operations by pushing directly to <strong>stack1</strong>. This results in an <strong>O(1)</strong> enqueue time but <strong>O(n)</strong> dequeue time when <strong>stack2</strong> is empty.</li>
</ol>

```python
class Queue: # TC : O(n) (Enqueue) SC : O(2n)
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue(self,data):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(data)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if not self.stack1:
            raise IndexError("Queue is Empty !")
        return self.stack1.pop()

    def front(self):
        if not self.stack1:
            raise IndexError("Queue is Empty !")
        return self.stack1[-1]

    def rear(self):
        if not self.stack1:
            raise IndexError("Queue is Empty !")
        return self.stack1[0]

    def size(self):
        return len(self.stack1)

    def isEmpty(self):
        return self.size()==0


class Queue: # TC : O(n) (dequeue & front) SC : O(2n)
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue(self,data):
        self.stack1.append(data)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty !")
        if(not self.stack2):
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def front(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty !")
        if(not self.stack2):
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def rear(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty !")
        if(self.stack1):
            return self.stack1[-1]
        return self.stack2[0]

    def size(self):
        return len(self.stack1)+len(self.stack2)

    def isEmpty(self):
        return self.size()==0


```


<h2>Stack Using Queue</h2>

<p>The <strong>MyStack</strong> class uses a single queue to implement stack operations. The main idea is to maintain the order of elements such that the most recently added element is always at the front of the queue.</p>

<p><strong>Class MyStack</strong></p>
<p>This class provides methods to perform stack operations using a queue.</p>

<ul>
  <li><strong>__init__(self)</strong>: Initializes an empty queue.</li>
  <li><strong>push(self, data)</strong>: Adds an element to the stack.
    <ul>
      <li>First, get the current size of the queue.</li>
      <li>Then, add the new element to the queue.</li>
      <li>Move all previously added elements to the back of the queue to maintain the stack order.</li>
    </ul>
  </li>
  <li><strong>pop(self)</strong>: Removes the top element from the stack.
    <ul>
      <li>Check if the stack (queue) is empty.</li>
      <li>If not, remove and return the front element of the queue, which represents the top of the stack.</li>
    </ul>
  </li>
  <li><strong>top(self)</strong>: Returns the top element of the stack without removing it.
    <ul>
      <li>Check if the stack (queue) is empty.</li>
      <li>If not, return the front element of the queue.</li>
    </ul>
  </li>
  <li><strong>size(self)</strong>: Returns the number of elements in the stack.
    <ul>
      <li>Simply return the size of the queue.</li>
    </ul>
  </li>
  <li><strong>empty(self)</strong>: Checks if the stack is empty.
    <ul>
      <li>Return <strong>True</strong> if the size of the queue is 0, otherwise return <strong>False</strong>.</li>
    </ul>
  </li>
</ul>

```python
from queue import Queue

class MyStack:

    def __init__(self):
        self.queue=Queue()

    def push(self,data):
        n=self.queue.qsize()
        self.queue.put(data)
        for i in range(n):
            temp=self.queue.get()
            self.queue.put(temp)

    def pop(self):
        if(self.empty()):
            raise IndexError("Stack is empty")
        return self.queue.get()

    def top(self):
        if(self.empty()):
            raise IndexError("Stack is empty")
        return self.queue.queue[0]

    def size(self):
        return self.queue.qsize()

    def empty(self):
        return self.size()==0
        

```