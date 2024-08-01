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
            
