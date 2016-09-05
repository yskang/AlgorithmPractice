import sys

# testData = [
#     '5 8 4'
# ]

# testData.reverse()
# rl = lambda: testData.pop()
rl = lambda: input()

line = rl()
a = int(line.split(' ')[0])
b = int(line.split(' ')[1])
c = int(line.split(' ')[2])

print((a+b)%c)
print((a%c + b%c)%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)
