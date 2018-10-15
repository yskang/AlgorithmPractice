# Title: A+B=3
# Link: https://www.acmicpc.net/problem/10950

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

def calculate(a: int, b: int):
    return a+b


def main():
    T = read_single_int()
    
    for _ in range(T):
        A, B = read_list_int()
        print(calculate(A, B))


if __name__ == '__main__':
    main()