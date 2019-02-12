# Title: 캐빈 베이컨의 6단계 법칙
# Link: https://www.acmicpc.net/problem/1389

import sys
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, friends_of: list):
    min_user = -1
    min_score = 9999999999
    frind_map = defaultdict(lambda: -1)

    for user in range(1, n+1):
        sum_score = 0
        for goal in range(1, n+1):
            if user == goal:
                continue
            if frind_map[(goal, user)] != -1:
                sum_score += frind_map[(goal, user)]
                continue
            score_map = [0 for _ in range(n+1)]
            queue = deque()
            queue.append((user, 0))
            is_find = False
            while not is_find:
                u, t = queue.popleft()
                for friend in friends_of[u]:
                    if score_map[friend] == 0:
                        score_map[friend] = t+1
                        queue.append((friend, t+1))
                        if friend == goal:
                            is_find = True
                            sum_score += (t+1)
                            frind_map[(user, goal)] = t+1
                            break
        if sum_score < min_score:
            min_score = sum_score
            min_user = user
    return min_user


def main():
    n, m = read_list_int()
    friends_of = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = read_list_int()
        friends_of[a].append(b)
        friends_of[b].append(a)
    print(solution(n, m, friends_of))


if __name__ == '__main__':
    main()