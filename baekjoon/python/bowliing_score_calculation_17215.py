# Title: 볼링 점수 계산
# Link: https://www.acmicpc.net/problem/17215

import sys


sys.setrecursionlimit(10 ** 6)


read_single_str = lambda: sys.stdin.readline().strip()


def solution(throws: list):
    score = 0
    frame = 1
    chance = 1
    rest = 10
    throws.reverse()
    while throws:
        pins = throws.pop()

        if pins.isdigit():
            if frame <= 10:
                score += int(pins)

            if chance == 2:
                chance = 1
                frame += 1
                rest = 10
            else:
                chance += 1
                rest -= int(pins)

        elif pins == '-':
            if chance == 2:
                chance = 1
                frame += 1
                rest = 10
            else:
                chance += 1

        elif pins == 'S':
            if frame <= 10:
                score += 10
                r = 10
                for i in range(-1, -3, -1):
                    t = throws[i]
                    if t.isdigit():
                        score += int(t)
                        r -= int(t)
                    elif t == 'S':
                        score += 10
                    elif t == 'P':
                        score += r
            frame += 1
            chance = 1
            rest = 10

        elif pins == 'P':
            if frame <= 10:
                score += rest
                t = throws[-1]
                if t.isdigit():
                    score += int(t)
                elif t == 'S':
                    score += 10
            frame += 1
            chance = 1
            rest = 10

    return score


def main():
    throws = read_single_str()
    print(solution(list(throws)))


if __name__ == '__main__':
    main()