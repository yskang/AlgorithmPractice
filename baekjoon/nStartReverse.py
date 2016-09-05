n = int(input())
output = []
for i in range(n, 0, -1):
    for j in range(i):
        output.append('*')
    print(''.join(output))
    output[:] = []
