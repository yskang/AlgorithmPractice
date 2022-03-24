# Title: 나이순 정렬
# Link: https://www.acmicpc.net/problem/10814

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_str = lambda: list(sys.stdin.readline().strip())


def solution(persons: list):
    return sorted(persons, key=lambda p: int(p[0]))


def main():
    N = read_single_int()
    persons = []
    for _ in range(N):
        age, name = sys.stdin.readline().strip().split(' ')
        persons.append((age, name))
    print('\n'.join(map(lambda p: '{} {}'.format(p[0], p[1]), solution(persons))))


if __name__ == '__main__':
    main()