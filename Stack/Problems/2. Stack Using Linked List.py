class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:

    def __init__(self):
        self.head=None
        self.count=0

    def isEmpty(self):
        return self.head==None

    def push(self,data):
        if(self.head==None):
            self.head=Node(data)
            self.count+=1
        else:
            node=Node(data)
            node.next=self.head
            self.head=node
            self.count+=1

    def pop(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack is Empty")
        else:
            node=self.head
            self.head=node.next
            node.next=None
            self.count-=1
            return node.data
        
    def peek(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack is Empty")
        else:
            return self.head.data

    def size(self):
        return self.count

    def display(self):
        if(self.isEmpty()):
            raise IndexError("StackUnderFlow : Stack is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<-")
                temp=temp.next
            print()

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Size Of Stack :",stack.size())
print("Peek Of Stack :",stack.peek())
stack.pop()
stack.display()
stack.pop()
stack.push(100)
stack.display()
stack.pop()
stack.display()

