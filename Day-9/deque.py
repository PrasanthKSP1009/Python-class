from collections import deque

dq = deque()

dq.append(10)
print(dq)
dq.appendleft(5)
print(dq)
dq.insert(1,7.5)
print(dq)
dq.rotate(2)
print(dq)