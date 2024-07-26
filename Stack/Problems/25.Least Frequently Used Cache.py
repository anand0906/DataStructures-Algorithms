class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.count=1
        self.next=None
        self.prev=None

class LinkedList:

    def __init__(self):
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0


    def InsertBegin(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
        self.size+=1

    def deleteAtEnd(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self.size-=1

class LFUCache:

    def __init__(self,capacity):
        self.size=capacity
        self.keyMap={}
        self.freqMap={}
        self.currentSize=0
        self.minFreq=0


    def updateFreqencyList(self,node):
        self.keyMap.pop(node.key)
        self.freqMap[node.count].deleteAtEnd(node)
        if(node.count==self.minFreq and self.freqMap[node.count].size==0):
            self.minFreq+=1
        node.count+=1
        if(node.count in self.freqMap):
            nextHigherList=self.freqMap[node.count]
        else:
            nextHigherList=LinkedList()
        nextHigherList.InsertBegin(node)
        self.freqMap[node.count]=nextHigherList
        self.keyMap[node.key]=node

    def get(self,key):
        if key not in self.keyMap:
            return -1
        node=self.keyMap[key]
        self.updateFreqencyList(node)
        return node.val


    def put(self,key,val):
        if(self.size==0):
            return -1

        if(key in self.keyMap):
            node=self.keyMap[key]
            node.val=val
            self.updateFreqencyList(node)
        else:
            if(self.currentSize==self.size):
                minList=self.freqMap[self.minFreq]
                self.keyMap.pop(minList.tail.prev.key)
                minList.deleteAtEnd(minList.tail.prev)
                self.currentSize-=1
            self.currentSize+=1
            self.minFreq=1
            if(self.minFreq in self.freqMap):
                currentList=self.freqMap[self.minFreq]
            else:
                currentList=LinkedList()
            node=Node(key,val)
            currentList.InsertBegin(node)
            self.keyMap[key]=node
            self.freqMap[self.minFreq]=currentList
    
