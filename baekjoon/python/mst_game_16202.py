import sys
import collections
import heapq

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

INF = 99999999999999

class Graph:
    def __init__(self):
        self.weight = collections.defaultdict(lambda:collections.defaultdict(lambda:None))

    def add_node(self, node_a: int, node_b: int, weight: int):
        self.weight[node_a][node_b] = weight
        self.weight[node_b][node_a] = weight


def prim(g: Graph, n: int):
    pq = []
    checked = collections.defaultdict(lambda: False)
    keys = collections.defaultdict(lambda:INF)
    parents = collections.defaultdict(lambda:None)
    heapq.heappush(pq, (0, 1)) #(key, node)

    while pq:
        key, node = heapq.heappop(pq)
        checked[node] = True
        for child in g.weight[node]:
            weight = g.weight[node][child]
            if not checked[child] and weight < keys[child]:
                keys[child] = weight
                parents[child] = node
                heapq.heappush(pq, (weight, child))

    cost = 0
    min_start, min_end, min_cost = 0, 0, INF

    for start in parents:
        temp = g.weight[start][parents[start]]
        if temp < min_cost:
            min_cost = temp
            min_start = start
            min_end = parents[start]
        cost += temp

    return cost, True if len(parents) == n-1 else False, (min_start, min_end)


def solution_prim(g: Graph, num_node: int, num_edge: int, k: int):
    ans = [0 for _ in range(k)]
    for i in range(k):
        cost, valid, (start, end) = prim(g, num_node)
        if valid:
            ans[i] = cost
            del(g.weight[start][end])
            del(g.weight[end][start])
        else:
            break
    return ' '.join(map(str, ans))


def find(x: int, parents: list):
    if x == parents[x]:
        return x
    p = find(parents[x], parents)
    parents[x] = p
    return p


def union(x: int, y: int, parents: list):
    x = find(x, parents)
    y = find(y, parents)
    if x != y:
        parents[y] = x


def kruskal(edges: list, parents: list, num_node: int):
    cost = 0
    i = 0
    while num_node-1 > 0:
        if i >= len(edges):
            return 0, False
        c, s, e = edges[i]
        if find(s, parents) != find(e, parents):
            cost += c
            union(s, e, parents)
            num_node -= 1
        i+=1
    return cost, True


def solution_kruskal(edges: list, num_node: int, k: int):
    ans = [0 for _ in range(k)]
    for i in range(k):
        parents = [i for i in range(num_node+1)]
        cost, valid = kruskal(edges[i+1:], parents, num_node)
        ans[i] = cost
        if not valid:
            break
    
    return ' '.join(map(str, ans))


def main():
    n, m, k = read_list_int()
    # g = Graph()
    edges = [(-1, -1)]
    for i in range(m):
        a, b = read_list_int()
        # g.add_node(a, b, i+1)
        edges.append((i+1, a, b))
    # print(solution_prim(g, n, m, k))
    print(solution_kruskal(edges, n, k))

if __name__ == '__main__':
    main()