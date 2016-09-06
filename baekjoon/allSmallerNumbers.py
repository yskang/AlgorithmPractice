[numOfInput, n] = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))
outs = []
for num in nums:
    if num < n:
        outs.append(str(num))
print(' '.join(outs))