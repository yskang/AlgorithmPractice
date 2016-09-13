# Stack Sequence
# https://www.acmicpc.net/problem/1874

import sys
rl = lambda:sys.stdin.readline().replace('\n', '').replace('\r', '').strip()
 
numOfSequence = int(rl())
ins = []
for j in range(numOfSequence):
    ins.append(int(rl()))
 
ins.reverse()
rd = lambda: ins.pop()
 
i = 1
count = 1
result = []
 
result.append('+')
 
stack = []
stack.append(i)
 
elem = int(rd())
 
 
while True:
    if stack != [] and stack[len(stack) - 1] == elem:
        k = stack.pop()
        result.append('-')
        if count == numOfSequence:
            break
        elem = int(rd())
        count = count + 1
 
    else:
        i = i + 1
        stack.append(i)
        result.append('+')
        if i > numOfSequence:
            result[:] = []
            result.append('NO')
            break
 
print('\n'.join(result))
