# Title: 두개의 손
# Link: https://www.acmicpc.net/problem/16675

import sys


sys.setrecursionlimit(10 ** 6)

read_list_str = lambda: list(sys.stdin.readline().strip().split(' '))

draw = 0
win_a = 1
win_b = 2

def is_win(a, b):
    if a == b:
        return draw
    if a == 'S':
        if b == 'R':
            return win_b
        elif b == 'P':
            return win_a
    if a == 'R':
        if b == 'P':
            return win_b
        elif b == 'S':
            return win_a
    if a == 'P':
        if b == 'S':
            return win_b
        elif b == 'R':
            return win_a
   

def solution(m1, m2, t1, t2):
    if is_win(m1, t1) == win_a and is_win(m1, t2) == win_a:
        return 'MS'
    if is_win(m2, t1) == win_a and is_win(m2, t2) == win_a:
        return 'MS'
    if is_win(t1, m1) == win_a and is_win(t1, m2) == win_a:
        return 'TK'
    if is_win(t2, m1) == win_a and is_win(t2, m2) == win_a:
        return 'TK'
    return '?'



def main():
    m1, m2, t1, t2 = read_list_str()
    print(solution(m1, m2, t1, t2))


if __name__ == '__main__':
    main()