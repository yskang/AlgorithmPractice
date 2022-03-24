# Title: DSLR
# Link: https://www.acmicpc.net/problem/9019

import sys
from collections import deque, defaultdict
from heapq import heappop, heappush


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
INF = 10**10

ops = ['D', 'S', 'L', 'R']


def dijkstra(reg: int, target: int):
    visited = defaultdict(lambda: False)
    distances = defaultdict(lambda: INF)
    paths = defaultdict(lambda: None)
    hq = []
    
    distances[reg] = 0
    heappush(hq, (0, reg))

    while hq:
        dist, r = heappop(hq)
        if distances[r] != dist:
            continue
        
        visited[r] = True

        childs = []
        childs.append((r * 2) % 10000)
        childs.append(9999 if r == 0 else (r-1))
        
        if r < 10:
            child_l = r * 10
            child_r = r * 1000
        elif r < 100:
            child_l = r * 10
            child_r = (r % 10) * 1000 + (r // 10)
        elif r < 1000:
            child_l = r * 10
            child_r = (r % 10) * 1000 + (r // 10)
        elif r < 10000:
            child_l = (r * 10) % 10000 + (r // 1000)
            child_r = (r // 10) + (r % 10) * 1000
        childs.append(child_l)
        childs.append(child_r)

        # t = deque(str(r).zfill(4))
        # t.rotate(-1)
        # childs.append(int(''.join(t)))
        # t.rotate(2)
        # childs.append(int(''.join(t)))

        for op, child in enumerate(childs):
            if not visited[child]:
                if dist + 1 < distances[child]:
                    distances[child] = dist+1
                    heappush(hq, (dist+1, child))
                    paths[child] = (r, ops[op])
                    if paths[target]:
                        return paths
    return paths        


def solution(a: int, b: int):
    visited = defaultdict(lambda: None)
    que = deque()
    que.append(a)
    while que:
        parent = que.popleft()
        childs = []

        childs.append((parent * 2) % 10000)
        childs.append(9999 if parent == 0 else (parent-1))
        
        # if parent < 10:
        #     child_l = parent * 10
        #     child_r = parent * 1000
        # elif parent < 100:
        #     child_l = parent * 10
        #     child_r = (parent % 10) * 1000 + (parent // 10)
        # elif parent < 1000:
        #     child_l = parent * 10
        #     child_r = (parent % 10) * 1000 + (parent // 10)
        # elif parent < 10000:
        #     child_l = (parent * 10) % 10000 + (parent // 1000)
        #     child_r = (parent // 10) + (parent % 10) * 1000

        # childs.append(child_l)
        # childs.append(child_r)

        t = deque(str(parent).zfill(4))
        t.rotate(-1)
        childs.append(int(''.join(t)))
        t.rotate(2)
        childs.append(int(''.join(t)))

        for op, child in enumerate(childs):
            if visited[child] == None:
                visited[child] = (parent, ops[op])
                if child == b:
                    
                    ans = [visited[b]]
                    while True:
                        ans.append(visited[ans[-1][0]])
                        if ans[-1] == None:
                            ans.pop()
                            break
                        if ans[-1][0] == a:
                            break
                    
                    return ''.join(map(lambda x: x[1], reversed(ans)))

                que.append(child)



def main():
    t = read_single_int()
    for _ in range(t):
        print(solution(*read_list_int()))


if __name__ == '__main__':
    main()