import sys
 
rl = lambda:sys.stdin.readline().strip().replace('\n', '').replace('\r', '')
 
class Stack:
    def __init__(self):
        self.stack = []
     
    def push(self, d):
        self.stack.append(d)
     
    def pop(self):
        if self.size() == 0:
            return -1
        return self.stack.pop()
     
    def size(self):
        return len(self.stack)
     
    def empty(self):
        if self.size() == 0:
            return 1
        return 0
     
    def top(self):
        if self.size() == 0:
            return -1
        return self.stack[self.size()-1]
 
stack = Stack()
 
numOfCommand = int(rl())
 
for c in range(numOfCommand):
    command = rl().split(' ')
    if command[0] == 'push':
        stack.push(command[1])
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'top':
        print(stack.top())
    else:
        print('error')