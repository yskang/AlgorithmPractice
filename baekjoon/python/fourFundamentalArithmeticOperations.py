# Four Fundamental Arithmetic Operations
# https://www.acmicpc.net/problem/10869

import sys

# testData = [
#     '1 2'
# ]

# testData.reverse()
# rl = lambda: testData.pop()
rl = lambda: input()

line = rl()
a = int(line.split(' ')[0])
b = int(line.split(' ')[1])

print(a+b)
print(a-b)
print(a*b)
print(divmod(a,b)[0])
print(divmod(a,b)[1])
