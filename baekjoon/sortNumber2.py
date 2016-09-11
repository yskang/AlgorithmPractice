import sys


testData = [
'10',
'5',
'2',
'3',
'1',
'4',
'2',
'3',
'5',
'1',
'10000',
'9'
]

# testData.reverse()
rl = lambda: testData.pop()
rls = lambda: '\n'.join(testData)

# rl = lambda:sys.stdin.readline().replace('\n', '')
# rls = lambda:sys.stdin.readlines()

nums = [(x, 0) for x in range(10001)]
ins = rls().split('\n')
numOfNums = int(ins[0])

for i in range(1, numOfNums + 1):
    index = int(ins[i])
    nums[index] = (index, nums[index][1] + 1)

print(''.join(['\n'.join([str(index) for x in range(value)])+'\n' for (index, value) in nums if value != 0]))



