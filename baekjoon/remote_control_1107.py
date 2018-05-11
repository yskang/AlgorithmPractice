# Title: 리모컨
# Link: https://www.acmicpc.net/problem/1107

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def is_number_ok(num, brokens):
    ok = True
    for n_str in str(num):
        ok = ok & brokens[int(n_str)]
    return ok


def minimum_ok_number(broken_table):
    for i, v in enumerate(broken_table):
        if v:
            return i


def maximum_of_number(broken_table):
    for i in range(9, -1, -1):
        if broken_table[i]:
            return i


def get_up_number(target, broken_table):
    index = -1
    for i, n_str in enumerate(str(target)):
        if not broken_table[int(n_str)]:
            index = i
            break
    if index == -1:
        return target
    else:
        front = int(str(target)[:index+1])
        while not is_number_ok(front, broken_table):
            front += 1
        return int(str(front) + str(minimum_ok_number(broken_table)) * (len(str(target))-index-1))


def get_down_number(target, broken_table):
    index = -1
    for i, n_str in enumerate(str(target)):
        if not broken_table[int(n_str)]:
            index = i
            break
    if index == -1:
        return target
    else:
        front = int(str(target)[:index+1])
        while not is_number_ok(front, broken_table):
            front -= 1
            if front == -1:
                if len(str(target)) - index - 1 >= 1:
                    index += 1
                    front = int(str(target)[:index+1])
                else:
                    return -1
        return int(str(front) + str(maximum_of_number(broken_table)) * (len(str(target))-index-1))


def get_press_times(N, broken_buttons):
    broken_table = [x not in broken_buttons for x in range(10)]
    is_zero_work = broken_table[0]
    updown_from_100 = abs(100 - N)
    number_from_0 = N + 1

    if len(broken_buttons) == 0:
        return min(updown_from_100, number_from_0, len(str(N)))
    elif is_zero_work and len(broken_buttons) == 9:
        return min(updown_from_100, number_from_0)
    elif len(broken_buttons) == 10:
        return updown_from_100
    else:
        up_number = get_up_number(N, broken_table)
        up_press = len(str(up_number)) + up_number - N

        down_number = get_down_number(N, broken_table)
        if down_number != -1:
            down_press = len(str(down_number)) + N - down_number
        else:
            down_press = 999999999

        return min(up_press, down_press, updown_from_100)


if __name__ == '__main__':
    N = read_single_int()
    M = read_single_int()
    broken_buttons = []
    if M != 0:
        broken_buttons = read_list_int()
    print(get_press_times(N, broken_buttons))
