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
        


