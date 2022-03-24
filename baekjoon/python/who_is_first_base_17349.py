# Title: 1루수가 누구야
# Link: https://www.acmicpc.net/problem/17349

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(ans: list):
    res = []
    for i in range(9):
        h = i+1
        temp = []
        for f in range(9):
            is_false = False
            for k, (tf, num) in enumerate(ans):
                if k == f:
                    tf = tf^1
                if h == num and tf == 1:
                    continue
                elif h != num and tf == 0:
                    continue
                else:
                    temp.append(False)
                    is_false = True
                    break
            if not is_false:
                temp.append(True)

        res.append(temp)

    first = -1
    true_count = 0
    for j, row in enumerate(res):
        for i, r in enumerate(row):
            if r:
                true_count += 1
                first = j+1

    
    if true_count == 1:
        return first
    else:
        return -1


def main():
    ans = []
    for _ in range(9):
        ans.append(read_list_int())
    print(solution(ans))


if __name__ == '__main__':
    main()