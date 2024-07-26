class Node:

    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None


class LRUCache:

    def __init__(self,capacity):
        self.capacity=capacity
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.map={}
        self.head.next=self.tail
        self.tail.prev=self.head

    def put(self,key,val):
        if key in self.map:
            self.delete(self.map[key])
        if(len(self.map)==self.capacity):
            self.delete(self.tail.prev)
        self.insertBegin(Node(key,val))

    def get(self,key):
        if key not in self.map:
            return -1
        val=self.map[key].val
        self.delete(self.map[key])
        self.insertBegin(Node(key,val))
        return self.map[key].val

    def insertBegin(self,node):
        self.map[node.key]=node
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

    def delete(self,node):
        del self.map[node.key]
        node.prev.next=node.next
        node.next.prev=node.prev
        node.next=None
        node.prev=None
        
