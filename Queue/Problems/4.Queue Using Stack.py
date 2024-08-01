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

