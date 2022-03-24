# Title: Interactive Sorting
# Link: https://practice.contest.atcoder.jp/tasks/practice_2

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_str = lambda: sys.stdin.readline().strip()


def merge(firsts: list, seconds: list):
    ans = []
    idx_first, idx_second = 0, 0
    while True:
        print('? {} {}'.format(firsts[idx_first], seconds[idx_second]))
        sys.stdout.flush()
        a = read_single_str()
        if a == '<':
            ans.append(firsts[idx_first])
            idx_first += 1
        else:
            ans.append(seconds[idx_second])
            idx_second += 1
        if idx_first == len(firsts):
            ans += seconds[idx_second:]
            break
        elif idx_second == len(seconds):
            ans += firsts[idx_first:]
            break
    return ans


def merge_sort(ns: list, n: int):
    if n == 0:
        return []
    elif n == 1:
        return ns
    h = n//2
    return merge(merge_sort(ns[:h], h), merge_sort(ns[h:], n-h))


def query(a: str, b: str):
    print('? {} {}'.format(a, b))
    sys.stdout.flush()
    return True if read_single_str() == '<' else False


def special_case(ns: list):
    twos_1 = []
    twos_2 = []
    if query('A', 'B'):
        twos_1 = ['A', 'B']
    else:
        twos_1 = ['B', 'A']
    
    if query('C', 'D'):
        twos_2 = ['C', 'D']
    else:
        twos_2 = ['D', 'C']
    
    last = ''
    threes = []
    if query(twos_1[1], twos_2[1]):
        threes = [twos_1[0], twos_1[1], twos_2[1]]
        last = twos_2[0]
    else:
        threes = [twos_2[0], twos_2[1], twos_1[1]]
        last = twos_1[0]
    
    fours = []
    if query(threes[1], 'E'):
        if query(threes[2], 'E'):
            fours = [threes[0], threes[1], threes[2], 'E']
        else:
            fours = [threes[0], threes[1], 'E', threes[2]]
    else:
        if query('E', threes[0]):
            fours = ['E', threes[0], threes[1], threes[2]]
        else:
            fours = [threes[0], 'E', threes[1], threes[2]]
    
    fives = []
    if query(fours[1], last):
        if query(fours[2], last):
            fives = [fours[0], fours[1], fours[2], last, fours[3]]
        else:
            fives = [fours[0], fours[1], last, fours[2], fours[3]]
    else:
        if query(last, fours[0]):
            fives = [last, fours[0], fours[1], fours[2], fours[3]]
        else:
            fives = [fours[0], last, fours[1], fours[2], fours[3]]

    return fives


def solution(n: int, q: int):
    ns = [chr(i) for i in range(ord('A'), ord('A')+n)]
    
    if n == 5 and q == 7:
        ns = special_case(ns)
    else:
        ns = merge_sort(ns, n)

    print('! {}'.format(''.join(ns)))
    sys.stdout.flush()


def main():
    n, q = read_list_int()
    solution(n, q)


if __name__ == '__main__':
    main()
