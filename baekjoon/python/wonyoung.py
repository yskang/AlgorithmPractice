import sys

A, B, N = map(int, sys.stdin.readline().split())

gifts = []
step = {'B':A,'R':B}
ready = {'B':0, 'R':0}

for i in range(0, N):
    line = sys.stdin.readline().split()
    t = int(line[0])
    color = line[1]
    n = int(line[2])
    t = max(t, ready[color])
    if step[color] == 0:
        gifts.extend([(t, color)] * n)
    else:
        gifts.extend(map(lambda n: (n, color), range(t, t+step[color]*n, step[color])))
    ready[color] = t + step[color] * n

gifts.sort()

bs = []
rs = []
idx = 1
for _, c in gifts:
    if c == 'B':
        bs.append(idx)
    else:
        rs.append(idx)
    idx = idx + 1
print(len(bs))
print(" ".join(map(str, bs)))
print(len(rs))
print(" ".join(map(str, rs)))