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