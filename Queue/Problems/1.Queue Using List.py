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
