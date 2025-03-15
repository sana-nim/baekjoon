import sys
from collections import deque

input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.empty():
            return -1
        return self.queue.popleft()

    def size(self):
        return len(self.queue)

    def empty(self):
        if not self.queue:
            return 1
        else:
            return 0

    def front(self):
        if self.empty():
            return -1
        return self.queue[0]

    def back(self):
        if self.empty():
            return -1
        return self.queue[-1]

n = int(input().strip())
q = Queue()

for i in range(n):
    cmd = input().strip().split()

    if cmd[0] == 'push':
        q.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(q.pop())
    elif cmd[0] == 'size':
        print(q.size())
    elif cmd[0] == 'empty':
        print(q.empty())
    elif cmd[0] == 'front':
        print(q.front())
    elif cmd[0] == 'back':
        print(q.back())
