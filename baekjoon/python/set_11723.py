# Title: 집합
# Link: https://www.acmicpc.net/problem/11723

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_words = lambda: sys.stdin.readline().strip().split()


def main():
    m = read_single_int()
    s = 0
    base = pow(2, 20)-1
    for _ in range(m):
        op = read_list_words()
        
        if op[0] == 'add':
            s |= (1 << (int(op[1])-1))
        elif op[0] == 'remove':
            s &= (base ^ (1 << (int(op[1])-1)))
        elif op[0] == 'check':
            if s & (1 << (int(op[1])-1)):
                print(1)
            else:
                print(0)
        elif op[0] == 'toggle':
            s ^= (1 << (int(op[1])-1))
        elif op[0] == 'all':
            s = base
        elif op[0] == 'empty':
            s = 0


if __name__ == '__main__':
    main()