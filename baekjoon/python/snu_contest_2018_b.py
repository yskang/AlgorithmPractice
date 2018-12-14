# Title: 시그널
# Link: https://www.acmicpc.net/problem/16113

import sys

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_single_str = lambda: sys.stdin.readline().strip()

zero = '######...######'
one = '#####'
two = '#.####.#.####.#'
three = '#.#.##.#.######'
four = '###....#..#####'
five = '###.##.#.##.###'
six = '######.#.##.###'
seven = '#....#....#####'
eight = '######.#.######'
nine = '###.##.#.######'

def solution(n: int, s: str):
    w = n // 5

    signal = ''
    for start in range(w):
        for offset in range(5):
            signal += s[start + offset * w]

    signal = signal.replace(zero, '0')
    signal = signal.replace(two, '2')
    signal = signal.replace(three, '3')
    signal = signal.replace(four, '4')
    signal = signal.replace(five, '5')
    signal = signal.replace(six, '6')
    signal = signal.replace(seven, '7')
    signal = signal.replace(eight, '8')
    signal = signal.replace(nine, '9')
    signal = signal.replace(one, '1')
    signal = signal.replace('.', '')
    return signal


def main():
    n = read_single_int()
    s = read_single_str()
    print(solution(n, s))


if __name__ == '__main__':
    main()

