# Title: 감소하는 수
# Link: https://www.acmicpc.net/problem/1038
import itertools
import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def add_to_one(d_number):
    if d_number == 9876543210:
        return -1
    r_str = []
    d_str = list(reversed(str(d_number)))
    carry = 0
    num = '1' + '0'*(len(d_str)-1)
    for i, d in enumerate(d_str):
        if i+1 == len(d_str):
            r = int(d) + int(num[i]) + carry
            if r >= 10:
                r_str.append(str(len(r_str)))
                r_str.append(str(len(r_str)))
            else:
                r_str.append(str(r))
        else:
            r = int(d) + int(num[i]) + carry
            if r < int(d_str[i+1]):
                r_str.append(str(r))
                carry = 0
            else:
                carry = 1
                if len(r_str) == 0:
                    r_str.append('0')
                else:
                    r_str.append(str(int(r_str[-1])+1))
    return int(''.join(reversed(r_str)))


def get_nth_number(N):
    d_number = 0
    for _ in range(N):
        d_number = add_to_one(d_number)
        if d_number == -1:
            return -1

    return d_number


def get_nth_decreasing_numbers(N):
    decreasing_numbers = []
    for n in range(1, 11):
        decreasing_numbers += sorted(map(lambda l: int(''.join(l)), itertools.combinations('9876543210', n)))
        if len(decreasing_numbers) > N:
            return decreasing_numbers[N]
    return -1


if __name__ == '__main__':
    N = read_single_int()
    # print(get_nth_number(N))
    print(get_nth_decreasing_numbers(N))