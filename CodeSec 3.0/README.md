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
<a href="https://github.com/dev-singh-kanyal/JusPay/blob/main/Hackathon_Que_Notes.md">Click Here</a>
<a href="https://quanticdev.com/algorithms/trees/lockable-tree/">Click Here</a>
<a href="https://leetcode.com/discuss/interview-question/1279262/juspay-tree-of-space-locking-and-unlocking-n-ary-tree">Click Here</a>