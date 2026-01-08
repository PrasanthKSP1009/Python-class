from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()
    def enqueue(self,val):
        self.q.append(val)
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return ("Element Pushed", val)
    def dequeue(self):
        return ("Popped Element is",self.q.popleft())

stack = Queue()
print(stack.enqueue(5))
print(stack.q)
print(stack.enqueue(10))
print(stack.q)
print(stack.enqueue(15))
print(stack.q)
print(stack.dequeue())
print(stack.q)