n = int(input())
output = []
for i in range(n, 0, -1):
    for k in range(n-i):
        output.append(' ')
    for j in range(i):
        output.append('*')
    print(''.join(output))
    output[:] = []

