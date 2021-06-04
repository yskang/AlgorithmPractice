# Title: 선물 교환
# Link: https://www.acmicpc.net/problem/gifts

import sys
from collections import defaultdict
from typing import DefaultDict, List
import json

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class GraphVisualizer:
    def __init__(self):
        self.json = {
                        "kind": {"graph": True},
                        "nodes": [],
                        "edges": [],
                    }
    
    def add_node(self, id, label):
        self.json['nodes'].append({'id': id, 'label': label})

    def add_edge(self, source, destination, color='red'):
        self.json['edges'].append({'from': source, 'to': destination, 'color': color})

    def get_graph(self):
        return json.dumps(self.json)


def graph_visualization():
    formatted = {
        "kind": {"graph": True},
        "nodes": [],
        "edges": [],
    }
    return json.dumps(formatted)


def solution(n: int, m: int, graph: DefaultDict, edges: DefaultDict) -> str:
    # 그래프에서 홀수노드를을 가상노드에 연결한다.
    graph[0]
    for node in graph:
        if len(graph[node]) % 2 == 1:
            graph[0].add(node)
            graph[node].add(0)
    # 그래프에 더이상 엣지가 남아있지 않을 때까지
    # 오일러 경로를 구한ek.
    path = []
    while True:
        for node in graph:
            if graph[node]:
                path += get_path(graph, node)
                break
        else:
            break

    # 경로를 따라 선물 문자열을 완성하여 출력
    gift_string = ['0' for _ in range(m)]

    x = path[0]
    for y in path[1:]:
        edge = (x, y)
        if edge in edges:
            gift_string[edges[edge]] = '1'
        x = y

    return ''.join(gift_string)


def get_path(graph: DefaultDict, start: int) -> List[int]:
    ans = []
    st = [start]
    while st:
        v = st[-1]
        if not graph[v]:
            ans.append(st.pop())    
        else:
            u = graph[v].pop()
            graph[u].discard(v)
            st.append(u)
    return ans


def main():
    t = read_single_int()
    for _ in range(t):
        gv = GraphVisualizer()
        graph = defaultdict(lambda: set())
        edges = defaultdict(lambda: None)
        n, m = read_list_int()
        for i in range(m):
            x, y = read_list_int()
            graph[x].add(y)
            graph[y].add(x)
            edges[(x, y)] = i
            gv.add_node(str(x), str(x))
            gv.add_node(str(y), str(y))
            gv.add_edge(str(x), str(y))
            gv.add_edge(str(y), str(x))
            gr = gv.get_graph()
            print('')
        print(solution(n, m, graph, edges))


if __name__ == '__main__':
    main()