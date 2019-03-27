# Title: 배열과 연산
# Link: https://www.acmicpc.net/problem/15932

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_words = lambda: sys.stdin.readline().strip().split(' ')


def solution(n: int, q: int, m: int, commands: list, y: int):
    results = []
    for i in y:
        results.append([i, 0])
    
    while commands:
        command = commands.pop()
        if len(command) == 1:
            for result in results:
                result[1] += result[0]
        else:
            s, e = int(command[1]), int(command[2])
            for result in results:
                if s <= result[0] <= e:
                    result[0] = e-(result[0]-s)

    return '\n'.join(map(lambda r: str(r[1]), results))


def main():
    n, q, m = read_list_int()
    commands = []
    for _ in range(q):
        commands.append(read_list_words())
    y = read_list_int()

    print(solution(n, q, m, commands, y))


if __name__ == '__main__':
    main()