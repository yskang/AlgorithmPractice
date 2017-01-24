class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[len(self.data) - 1]

    def empty(self):
        return len(self.data) == 0

    def print(self):
        print(self.data)

stack = Stack()
stack.push('a')
stack.print()
stack.push('b')
stack.print()
stack.push('c')
stack.print()
print(stack.pop())
stack.print()
