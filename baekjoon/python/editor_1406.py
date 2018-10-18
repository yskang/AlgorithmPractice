# Title: 에디터
# Link: https://www.acmicpc.net/problem/1406

import sys
import collections

sys.setrecursionlimit(10 ** 6)

read_list_str = lambda: list(sys.stdin.readline().strip())
read_single_int = lambda: int(sys.stdin.readline().strip())
read_splited_str = lambda: sys.stdin.readline().strip().split(' ')


def solution(contents: list, commands: list):
    left, right = contents, collections.deque([])
    for command in commands:
        if command[0] == 'L' and left != []:
            right.appendleft(left.pop())
        elif command[0] == 'D' and len(right) != 0:
            left.append(right.popleft())
        elif command[0] == 'B' and left != []:
            left.pop()
        elif command[0] == 'P':
            left.append(command[1])

    return ''.join(left + list(right))


def main():
    contents = read_list_str()
    n = read_single_int()
    commands = []
    for _ in range(n):
        commands.append(read_splited_str())
    print(solution(contents, commands))


if __name__ == '__main__':
    main()