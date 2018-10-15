# Sort Numbers 2
# https://www.acmicpc.net/problem/2751

import sys
rl = lambda: sys.stdin.readline().replace('\n', '')
 
numOfNums = int(rl())
temp = int(rl())
nums = {temp}
 
for i in range(numOfNums-1):
    nums.add(int(rl()))
 
x = sorted(nums)
 
print('\n'.join(map(str, x)))
