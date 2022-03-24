# Title: 숫자 야구
# Link: https://www.acmicpc.net/problem/2503

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def check(case: str, ans: []):
    guess = str(ans[0])
    strike, ball = 0, 0
    for i in range(3):
        if case[i] == guess[i]:
            strike += 1
    if guess[0] == case[1] or guess[0] == case[2]:
        ball += 1
    if guess[1] == case[0] or guess[1] == case[2]:
        ball += 1
    if guess[2] == case[0] or guess[2] == case[1]:
        ball += 1

    if strike == int(ans[1]) and ball == int(ans[2]):
        return True
    return False


def solution(n: int, answers: list):
    res = 0
    for number in range(0, 1000):
        case = str(number)
        if len(set(case)) != 3 or case.find('0') != -1:
            continue
        for ans in answers:
            if not check(case, ans):
                break
        else:
            res += 1
    return res


def main():
    n = read_single_int()
    answers = []
    for _ in range(n):
        answers.append(read_list_int())
    print(solution(n, answers))


if __name__ == '__main__':
    main()