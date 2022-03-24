# Title: 기타줄
# Link: https://www.acmicpc.net/problem/1049

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, packages: list, singles: list):
    min_package = min(packages)
    min_single = min(singles)
    p, r = divmod(n, 6)
    a = (p * min_package) if p*min_package < 6*p*min_single else (6*p*min_single)
    b = (r * min_single) if r*min_single < min_package else min_package
    return a+b


def main():
    n, m = read_list_int()
    packages = []
    singles = []
    for _ in range(m):
        package, single = read_list_int()
        packages.append(package)
        singles.append(single)
    print(solution(n, m, packages, singles))


if __name__ == '__main__':
    main()