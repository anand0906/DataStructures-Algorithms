class MinStack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        return len(self.stack)==0

    def top(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack Is Empty")
        return self.stack[-1][0]

    def getMin(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack Is Empty")
        return self.stack[-1][1]

    def push(self,data):
        if self.isEmpty():
            mini=data
            self.stack.append((data,mini))
        else:
            mini=self.getMin()
            mini=min(mini,data)
            self.stack.append((data,mini))

    def pop(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack Is Empty")
        return self.stack.pop()

    def size(self):
        return len(self.stack)

class MinStack:
    def __init__(self):
        self.stack=[]
        self.min=None

    def isEmpty(self):
        return len(self.stack)==0

    def top(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack Is Empty")
        if(self.stack[-1]<self.min):
            return self.min
        return self.stack[-1]

    def getMin(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack Is Empty")
        return self.min

    def push(self,data):
        if self.isEmpty():
            self.min=data
            self.stack.append(data)
        else:
            if(data>=self.min):
                self.stack.append(data)
            else:
                temp=2*data-self.min
                self.stack.append(temp)
                self.min=data

    def pop(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack Is Empty")
        y=self.stack.pop()
        if(y>self.min):
            return y
        else:
            temp=2*self.min-y
            self.min=temp
            return self.min

    def size(self):
        return len(self.stack)

stack=MinStack2()
stack.push(2)
stack.push(1)
print(stack.getMin())
stack.push(0)
print(stack.getMin())
print(stack.stack)
