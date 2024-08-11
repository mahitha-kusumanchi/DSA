class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def isEmpty(self):
        return len(self.items)==0
    def pop(self):
        if self.isEmpty()==True:
            return "List is empty"
        return (self.items).pop()
    def peek(self):
        if self.isEmpty() == True:
            return "List is empty"
        return (self.items)[-1]
    def size(self):
        return len(self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.items)
print(stack.pop())
print(stack.items)
print(stack.peek())
