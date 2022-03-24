# Print Star - 3
# https://www.acmicpc.net/problem/2440

n = int(input())
output = []
for i in range(n, 0, -1):
    for j in range(i):
        output.append('*')
    print(''.join(output))
    output[:] = []
