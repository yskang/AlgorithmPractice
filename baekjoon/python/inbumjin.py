import sys
from collections import deque

sys.setrecursionlimit(10**6)
def read_input(): return sys.stdin.readline().strip()


VISIT, BLACK = 0, 1


def topological(graph):
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = VISIT
        for k in graph.get(node, []):
            sk = state.get(k, None)
            if sk == VISIT or sk == BLACK:
                continue
            elif sk == None:
                enter.discard(k)
                dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter:
        n = enter.pop()
        if state.get(n, None) == None:
            dfs(n)
    return order


if __name__ == '__main__':
    first_line = read_input()
    n, m = first_line.split(' ')
    # make a graph with adjacency list
    g = dict()
    for _ in range(int(m)):
        line = read_input()
        a, b = list(map(int, line.split(' ')))
        if g.get(a, None):
            g[a] = g[a].append(b)
        else:
            g[a] = [b]

    answer = ' '.join(map(str, list(topological(g))))
    print(answer)

