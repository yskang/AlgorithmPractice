# Sort Numbers - 3
# https://www.acmicpc.net/problem/10989

import sys
 
rl = lambda:sys.stdin.readline()
 
nums = [(x, 0) for x in range(10001)]
numOfNums = int(rl())
 
for i in range(1, numOfNums + 1):
    index = int(rl())
    nums[index] = (index, nums[index][1] + 1)
 
print('\n'.join(['\n'.join([str(index) for x in range(value)]) for (index, value) in nums if value != 0]))
