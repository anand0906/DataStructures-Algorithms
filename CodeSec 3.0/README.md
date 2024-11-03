<h1>Hackathon</h1>

<p><strong>Note</strong></p>
<ul>
	<li>Given tree is fully balenced (Each node have 0 or m nodes)</li>
	<li>Output should be True If operation success, otherwise False</li>
	<li>Expected Time Complexity : </li>
	<ul>
		<li>Time Complexity : </li>
		<ul>
			<li>Lock/Unlock : O(log<sub>m</sub>n)</li>
			<li>Upgrade : (number of Locked descendents) * O(log<sub>m</sub>n)</li>
		</ul>
	</ul>
</ul>

<p><strong>Lock</strong></p>
<ul>
	<li>Node can't be locked if it is alread locked, Return False</li>
	<li>Node can't be locked if it has any locked nodes (By any userid) in its ancestors, Return False</li>
	<li>Node can't be locked if it has any locked nodes (By any userid) in its descendents, Return False</li>
	<li></li>
	<li>Lock The Given Node By UserId UID, Return True If it is Successfully Locked</li>
</ul>

<p><strong>Unlock</strong></p>
<ul>
	<li>If node is not locked , Return False</li>
	<li>If node is locked by other UID, Return False</li>
	<li>Otherwise, Unlock the node and Return True</li>
</ul>

<p><strong>Upgrade</strong></p>
<ul>
	<li>Upgrade not possible , if given node is already locked, Return False</li>
	<li>Upgrade not possible , if any ancestor of node already locked, Return False</li>
	<li>Upgrade not possible , if it has no locked Descendent, Return False</li>
	<li>Upgrade not possible , if any descendent locked with different used id / more than one userid </li>
	<li>Otherwise, unlock all locked descendents and lock given node , Return True</li>
</ul>


<p><strong>References</strong></p>
<a href="https://www.thejoboverflow.com/p/p703/">Click Here For Question</a>
<a href="https://github.com/dev-singh-kanyal/JusPay/blob/main/Hackathon_Que_Notes.md">Click Here</a>
<a href="https://quanticdev.com/algorithms/trees/lockable-tree/">Click Here</a>
<a href="https://leetcode.com/discuss/interview-question/1279262/juspay-tree-of-space-locking-and-unlocking-n-ary-tree">Click Here</a>
<a href="https://www.algostreak.com/post/locking-unlocking-of-n-ary-tree">Click Here</a>


<p><strong>The problem of locking and unlocking nodes in an N-ary tree</strong> has strong relevance to databases, particularly in the context of indexing and concurrency control. Let’s dive into how this algorithm applies to database systems:</p>

<ol>
    <li>
        <strong>Tree-Like Structure in Databases (Indexing)</strong>
        <ul>
            <li><strong>Indexing</strong>: In relational databases, tree structures (like B-Trees or B+ Trees) are often used to organize and optimize the lookup of data, making it faster to access rows in a table. These tree structures act as indexes, where each node might represent a key (e.g., a row ID or primary key).</li>
            <li><strong>Locking a Portion of the Index</strong>: When running transactions, you may need to "lock" portions of the index to ensure consistency. For instance, if a transaction updates or reads a certain range of keys, locking prevents other operations from modifying those keys until the transaction is complete. Our lock/unlock/upgrade scheme for tree nodes in this problem is very similar to how databases control access to portions of an index.</li>
        </ul>
    </li>  
    <li>
        <strong>Concurrency Control in Databases</strong>
        <ul>
            <li><strong>Multiple Granularity Locking (MGL)</strong>: Databases employ MGL to handle locks at various levels of the hierarchy (e.g., table, page, row). In the N-ary tree problem, we see a similar concept, where a node cannot be locked if its ancestor or any of its descendants are locked, essentially requiring a hierarchical check.</li>
            <li><strong>Shared vs. Exclusive Locks</strong>: In databases, a "shared" lock allows multiple transactions to read without modification, while an "exclusive" lock prevents other transactions from accessing the resource at all. Though our example does not explicitly define shared or exclusive locks, the concept could be expanded to include such details. For instance, ancestors could have "shared" locks while individual nodes require "exclusive" locks.</li>
        </ul>
    </li>
    <li>
        <strong>Single-Threaded vs. Multi-Threaded Locking (Locks vs. Latches)</strong>
        <ul>
            <li><strong>Locks</strong>: In single-threaded systems (like JavaScript's single-threaded model), locks prevent multiple asynchronous tasks from accessing a resource inconsistently. Even though there's only one thread, asynchronous operations (like HTTP requests) can create race conditions that locks help prevent. For example, while one task is waiting for data, another task might try to access the same resource.</li>
            <li><strong>Latches</strong>: In multi-threaded databases, latches (mutexes or other thread-safe mechanisms) are used to control access to shared resources across threads. In a database with multiple threads, you would need latches to ensure the tree is accessed safely without conflicts.</li>
        </ul>
    </li>
    <li>
        <strong>Tree Traversal and Locking Granularity</strong>
        <ul>
            <li>When applying locking to nodes in a tree, only specific paths need to be locked: the target node’s ancestors (up to the root) and its descendants. Siblings do not affect lockability directly, meaning the algorithm can release any mutexes associated with sibling nodes.</li>
            <li>This fine-grained locking improves efficiency, allowing transactions to operate on different branches of the tree concurrently, as long as they don’t interfere with each other’s ancestors or descendants. This is analogous to shared and exclusive locks in a database, where locks are acquired only on parts of the hierarchy that directly impact the transaction.</li>
        </ul>
    </li>
    <li>
        <strong>Thread-Safety Enhancements Using Mutexes</strong>
        <ul>
            <li><strong>Read-Write Mutexes</strong>: You might start with a write lock at the node level, then switch to read locks on certain ancestors or descendants as needed.</li>
            <li><strong>Releasing Unnecessary Locks</strong>: Releasing locks on siblings and focusing only on ancestors and descendants minimizes lock contention. This kind of selective locking is critical in databases to maximize concurrent access while maintaining data consistency.</li>
        </ul>
    </li>
    <li>
        <strong>Testing and Robustness in Locking Algorithms</strong>
        <ul>
            <li><strong>Concurrent Locking Attempts</strong>: Verifying that concurrent requests for locking the same subtree fail if any conflicts arise.</li>
            <li><strong>Independent Locking of Siblings</strong>: Ensuring that siblings can be locked/unlocked independently, which is essential for efficient parallel processing in databases.</li>
            <li><strong>Upgrade Locks</strong>: Checking that locks can be upgraded appropriately and that all descendants are unlocked as expected.</li>
        </ul>
    </li>
</ol>

<p>This N-ary tree locking problem thus serves as an excellent conceptual model for understanding how hierarchical locking mechanisms work in databases. The principles we covered apply to real-world indexing and concurrency management, highlighting the importance of efficient locking mechanisms in database performance and consistency.</p>

