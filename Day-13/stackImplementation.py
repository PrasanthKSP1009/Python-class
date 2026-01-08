class Stack:
    def __init__(self):
        self.stack = []
    def push(self,val):
        if len(self.stack) == 5:
            return "Stack Overflow"
        else:
            self.stack.append(val)
            return ("Pushed Element", val)
    def pop(self):
        if not self.stack:
            return "Stack Underflow"
        else:
            return self.stack.pop()
    def top (self):
        if not self.stack:
            return "Stack Underflow"
        else:
            return self.stack[-1]
    def peek (self):
        if not self.stack:
            return "Stack Underflow"
        else:
            return self.stack[-1]
stackObj = Stack()
print(stackObj.top())
ele = [5,10,15,20,25,30]
for i in ele:
    print(stackObj.push(i))
    print(stackObj.stack)