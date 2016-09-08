testData = [
'5',
'5',
'2',
'3',
'4',
'1'
]

testData.reverse()

rl = lambda: testData.pop()
# rl = lambda: input()

numOfNums = int(rl())

nums = []
nums.append(int(rl()))
for i in range(numOfNums-1):
    num = int(rl())
    for j in range(len(nums)):
        if num < nums[j]:
            nums.insert(j, num)
            break 

nums.reverse()
for num in nums:
    print(num)