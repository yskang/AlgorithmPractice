import sys
from collections import deque
from types import SimpleNamespace

args = sys.argv

in_lines = None
with open(args[1], 'r') as f:
    in_lines = deque(map(lambda x: x.strip(), f.readlines()))
out_lines = None
with open(args[2], 'r') as f:
    out_lines = deque(map(lambda x:x.strip(), f.readlines()))

line = in_lines.popleft()
n, m = map(int, line.split())
ns = []
ms = []
for _ in range(n):
    line = in_lines.popleft()
    a, h = map(int, line.split())
    ns.append(SimpleNamespace(attack=a, health=h))

for _ in range(m):
    line = in_lines.popleft()
    a, h = map(int, line.split())
    ms.append(SimpleNamespace(attack=a, health=h))

o = out_lines.popleft()
if o == '-1' or o == '0':
    print(True)
else:
    while out_lines:
        line = out_lines.popleft()
        if line.startswith('attack'):
            _, a, t = line.split()
            a = int(a)
            t = int(t)

            if ns[a-1].health <= 0:
                print(False)
                break

            ms[t-1].health -= ns[a-1].attack
            ns[a-1].health -= ms[t-1].attack
        elif line.startswith('use'):
            while True:
                dead = False
                for x in ns:
                    x.health -= 1
                    if x.health == 0:
                        dead = True
                for x in ms:
                    x.health -= 1
                    if x.health == 0:
                        dead = True
                if not dead:
                    break

    for x in ms:
        if x.health > 0:
            print(False)

    print(True)
