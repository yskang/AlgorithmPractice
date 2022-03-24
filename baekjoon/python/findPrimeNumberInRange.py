# Prime Number
# https://www.acmicpc.net/problem/2581

import sys
 
rl = lambda:sys.stdin.readline()
 
start = int(rl())
end = int(rl())
 
if start == 1:
    start = 2
 
target = list(range(2, end+1))
s = 2
 
while True:
    target = list(filter(lambda x: x % s != 0, target))
 
    if target == []:
        break
 
    if s >= start:
        target.append(s)
     
    s = target[0]
 
    if s >= start and s >= int(end/2) + 1:
        break
 
if target == []:
    print(-1)
else:
    print(sum(target))
    print(min(target))
