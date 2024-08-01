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
    
