# Get Prime Numbers
# https://www.acmicpc.net/problem/1929

import sys
 
rl = lambda:sys.stdin.readline()
 
[start, end] = list(map(int, rl().split(' ')))
 
target = list(range(2, end+1))
s = 2
 
if target == [2]:
    print(2)
    exit()
 
while True:
    target = list(filter(lambda x: x % s != 0, target))
 
    if target == []:
        break
 
    target.append(s)
     
    s = target[0]
 
    if s >= end**(0.5):
        break
 
target.sort()
 
print('\n'.join(list(map(str, filter(lambda x: x >= start, target)))))
