# Sort Numbers
# https://www.acmicpc.net/problem/2750

numOfNums = int(input())

nums = []
for i in range(numOfNums):
    nums.append(int(input()))
nums.sort()
print('\n'.join(list(map(str, nums))))
