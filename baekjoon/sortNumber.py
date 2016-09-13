# Sort Numbers
# https://www.acmicpc.net/problem/2750

import sys

testData = [
'12',
'1',
'100',
'-3',
'4',
'0',
'1000000',
'-9',
'8',
'7',
'6',
'-5',
'-1000000'
]

def quickSort(xs):
    if len(xs) <= 1:
        return xs

    pivot = xs[len(xs)-1]

    less = []
    more = []
    equal = []

    for x in xs:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            more.append(x)
        else:
            equal.append(x)

    return quickSort(less) + equal + quickSort(more)

def mergeSort(xs):
    if len(xs) <= 1:
        return xs

    mid = len(xs) // 2
    lefts = mergeSort(xs[:mid])
    rights = mergeSort(xs[mid:])

    result = []
    l = 0
    r = 0

    while l < len(lefts) and r < len(rights):
        if lefts[l] < rights[r]:
            result.append(lefts[l])
            l += 1
        else:
            result.append(rights[r])
            r += 1
    
    result += lefts[l:]
    result += rights[r:]
    return result


testData.reverse()
rl = lambda: testData.pop()

# rl = lambda: sys.sdein.readline()

numOfNums = int(rl())
temp = int(rl())
nums = {temp}

for i in range(numOfNums-1):
    nums.add(int(rl()))

x = sorted(nums)

print('\n'.join(map(str, x)))
