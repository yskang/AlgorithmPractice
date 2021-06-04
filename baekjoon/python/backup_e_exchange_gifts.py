# Title: 선물 교환
# Link: https://www.acmicpc.net/problem/gifts

import sys
from collections import defaultdict
from typing import DefaultDict, List

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, graph: DefaultDict, edges: DefaultDict):
    # 1. 그래프에서 홀수 노드들을 가상의 노드와 연결 시킨다.
    dummy_node = n+1
    graph[dummy_node] = set()
    for node in range(1, n+1):
        if len(graph[node]) % 2 == 1:
            graph[dummy_node].add(node)
            graph[node].add(dummy_node)

    # 2. 임의의 한 노드에서 시작하여, 오일러 경로를 구한다.
    # 3. 모든 노드의 엣지가 없으면 다음단계, 그렇지 않으면 다시 2단계

    path = []
    while True:
        start = None
        for node in graph:
            if graph[node]:
                start = node
                break
        else:
            break
        path += get_path(graph, start)

    # 4. 경로를 따라, 선물 문자열을 만들고, 출력한다.
    gift_string = ['0' for _ in range(m)]
    
    x = path[0]
    for y in path[1:]:
        edge = (x, y)
        if edge in edges:
            gift_string[edges[edge]] = '1'
        x = y

    return ''.join(gift_string)
    

def get_path(graph: DefaultDict, start: int) -> List:
    ans = []
    st = [start]

    while st:
        v = st[-1]
        if not graph[v]:
            ans.append(v)
            st.pop()
        else:
            u = graph[v].pop()
            graph[u].discard(v)
            st.append(u)
    return ans


def main():
    t = read_single_int()
    for _ in range(t):
        edges = defaultdict(lambda: None)
        graph = defaultdict(lambda: set())
        n, m = read_list_int()
        for i in range(m):
            x, y = read_list_int()
            graph[x].add(y)
            graph[y].add(x)
            edges[(x, y)] = i
        print(solution(n, m, graph, edges))


if __name__ == '__main__':
    main()