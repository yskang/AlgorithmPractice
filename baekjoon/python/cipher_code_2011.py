# Title: 암호코드
# Link: https://www.acmicpc.net/problem/2011

import sys
import random


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


DIV = 1000000

def is_valid(first: str, second=None):
    if second==None:
        first = int(first)
        if 1 <= first <= 26:
            return True
        return False
    else:
        if first == '0':
            return False
        elif 1 <= int(first+second) <= 26:
            return True
        else:
            return False


def count(code: str, i: int, cache: list, is_valid_pw: list):
    if not is_valid_pw[0]:
        return 0
    if i < 0:
        return 0
    if cache[i] != -1:
        return cache[i]
    if i == 0:
        cache[i] = 1
        return 1
    elif i == 1:
        if int(code[:2]) == 10 or int(code[:2]) == 20:
            return 1
        elif 10 < int(code[:2]) <= 26:
            cache[i] = 2
            return 2
        if int(code[1]) == 0 and int(code[0]) >= 3:
            is_valid_pw[0] = False
            return 0
        cache[i] = 1
        return 1

    ans = 0
    # first_valid = is_valid(code[i-1])
    second_valid = is_valid(code[i])
    two_valid = is_valid(code[i-1], code[i])

    if not second_valid:
        if int(code[i-1]) >= 3 or int(code[i-1]) == 0:
            is_valid_pw[0] = False
            return 0

    if second_valid and two_valid:
        ans = count(code, i-1, cache, is_valid_pw) + count(code, i-2, cache, is_valid_pw)
    elif not second_valid and two_valid:
        ans = count(code, i-2, cache, is_valid_pw)
    elif second_valid and not two_valid:
        ans = count(code, i-1, cache, is_valid_pw)

    cache[i] = ans
    return ans


def solution(code: str):
    if code[0] == '0':
        return 0
    is_valid_pw = [True]
    cache = [-1 for _ in range(len(code)+1)]
    ans = count(code, len(code)-1, cache, is_valid_pw)

    if not is_valid_pw[0]:
        return 0

    return ans % DIV


def main():
    code = read_single_str()
    print(solution(code))


if __name__ == '__main__':
    main()
