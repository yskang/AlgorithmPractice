# Title: 묘수풀이: 모독
# Link: https://www.acmicpc.net/problem/17226

import sys
from copy import deepcopy
from collections import deque, defaultdict
from types import SimpleNamespace

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def do_modok(ns: list, ms: list):
    while True:
        dead = False
        for n in ns:
            n.life -= 1
            if n.life == 0:
                dead = True
        for m in ms:
            m.life -= 1
            if m.life == 0:
                dead = True
        if not dead:
            break
    a, b = [], []
    for n in ns:
        if n.life > 0:
            a.append(n)
    for m in ms:
        if m.life > 0:
            b.append(m)
    return a, b            


def get_candis(ns: list, ms: list):
    a, b = [], []
    filtered = list(filter(lambda x: x.available , ns))
    if filtered:
        attacks = sorted(list(set(map(lambda x: x.attack, filtered))), reverse=True)
        lifes = sorted(list(set(map(lambda x: x.life, filtered))), reverse=True)
        a = list(map(lambda x: x[1] ,filter(lambda x: x[0].attack in attacks[:5] or x[0].life in lifes[:5], zip(ns, [i for i in range(len(ns))]))))

    if ms:
        lifes = sorted(list(set(map(lambda x: x.life, ms))), reverse=True)
        b = list(map(lambda x: x[1] ,filter(lambda x: x[0].life in lifes[:5], zip(ms, [i for i in range(len(ms))]))))

    return a, b


def solution(n: int, m: int, ns: list, ms: list):
    if m == 0:
        return 0
    
    queue = deque()

    queue.append((deepcopy(ns), deepcopy(ms), []))

    while queue:
        nns, mms, commands = queue.popleft()

        if not mms:
            return commands

        n_candis, m_candis = get_candis(nns, mms)

        for card in n_candis:
            for target in m_candis:
                if nns[card].available:
                    ccommands = deepcopy(commands)
                    nnns = deepcopy(nns)
                    mmms = deepcopy(mms)

                    a = nnns[card].index
                    t = mmms[target].index

                    nnns[card].life -= mmms[target].attack
                    mmms[target].life -= nnns[card].attack

                    nnns[card].available = False

                    nnns = list(filter(lambda c: c.life > 0, nnns))
                    mmms = list(filter(lambda c: c.life > 0, mmms))

                    ccommands.append('attack {} {}'.format(a, t))
                    queue.append((nnns, mmms, ccommands))

        if 'use modok' not in commands:
            nnns, mmms = do_modok(deepcopy(nns), deepcopy(mms))
            if not mmms:
                commands.append('use modok')
                return commands
            if not nnns:
                continue
            else:
                ccommands = deepcopy(commands)
                ccommands.append('use modok')
                queue.append((nnns, mmms, ccommands))

    return -1


def main():
    n, m = read_list_int()
    ns = []
    ms = []
    for i in range(n):
        a, p = read_list_int()
        ns.append(SimpleNamespace(attack= a, life= p, index= i+1, available= True))
    for i in range(m):
        a, p = read_list_int()
        ms.append(SimpleNamespace(attack= a, life= p, index= i+1))
    ans = solution(n, m, ns, ms)
    if ans == -1 or ans == 0:
        print(ans)
    else:
        print(len(ans))
        for a in ans:
            print(a)


if __name__ == '__main__':
    main()