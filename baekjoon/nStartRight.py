n = int(input())
output = []
for i in range(n):
    for k in range(n-i-1):
        output.append(' ')
    for j in range(i+1):
        output.append('*')
    print(''.join(output))
    output[:] = []
