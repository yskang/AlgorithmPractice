# Title: 2018년을 뒤돌아 보며
# Link: https://www.acmicpc.net/problem/16674

import sys

sys.setrecursionlimit(10 ** 6)


read_list_str = lambda: list(sys.stdin.readline().strip())


def solution(n: list):
    two = n.count('2')
    zero = n.count('0')
    one = n.count('1')
    eight = n.count('8')

    if two + zero + one + eight == len(n):
        if not(two > 0 and zero > 0 and one > 0 and eight > 0):
            return 1
        if not(two == zero == one == eight):
            return 2
        else:
            return 8
    else:
        return 0
    


def main():
    n = read_list_str()
    print(solution(n))


if __name__ == '__main__':
    main()