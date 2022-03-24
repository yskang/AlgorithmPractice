# Title: 회의실배정
# Link: https://www.acmicpc.net/problem/1931

import sys
from collections import defaultdict as ddict
from collections import OrderedDict as odict
import bisect
import heapq

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, meetings: list):
    count = 1
    # meetings = sorted(sorted(meetings, key=lambda m: m[0]), key=lambda m: m[1])
    meetings = sorted(meetings, key= lambda m: (m[1], m[0]))

    prev_meeting = meetings[0]
    for meeting in meetings[1:]:
        if meeting[0] >= prev_meeting[1]:
            prev_meeting = meeting
            count += 1
    
    return count


def main():
    n = read_single_int()
    meetings = []
    for _ in range(n):
        meetings.append(tuple(read_list_int()))
    print(solution(n, meetings))


if __name__ == '__main__':
    main()