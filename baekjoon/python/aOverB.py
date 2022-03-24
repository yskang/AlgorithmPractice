# A/B
# https://www.acmicpc.net/problem/1008

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
result = a/b
print('%0.9f' %result)
