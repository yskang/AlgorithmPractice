# Title: 줄 세우기
# Link: https://www.acmicpc.net/problem/2252
import sys
import queue
import heapq

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_line(students, indegrees, N):
    line = []
    qu = queue.Queue()
    for number in range(1, N+1):
        if indegrees[number] == 0:
            # heapq.heappush(qu, number)
            qu.put(number)

    while qu.qsize() > 0:
        # zero_indegree = heapq.heappop(qu)
        zero_indegree = qu.get()
        line.append(zero_indegree)
        for number in students[zero_indegree]:
            indegrees[number] -= 1
            if indegrees[number] == 0:
                # heapq.heappush(qu, number)
                qu.put(number)

    return ' '.join(map(str, line))


if __name__ == '__main__':
    N, M = read_list_int()
    students = [[] for _ in range(N+1)]
    indegrees = [0 for _ in range(N+1)]

    for _ in range(M):
        a, b = read_list_int()
        students[a].append(b)
        indegrees[b] += 1
    print(get_line(students, indegrees, N))