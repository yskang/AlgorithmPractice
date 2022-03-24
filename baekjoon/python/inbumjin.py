import sys
from collections import deque


def read_input(): return sys.stdin.readline().strip()


GRAY, BLACK = 0, 1


def topological(graph):
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, []):
            sk = state.get(k, None)
            if sk == GRAY:
                raise ValueError("cycle")
            if sk == BLACK:
                continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while len(enter) > 0:
        dfs(enter.pop())

    return order


if __name__ == '__main__':
    first_line = read_input()
    n, m = first_line.split()
    # make a graph with adjacency list
    if n == '1':
        print(1)
    else:
        g = dict()
        for _ in range(int(m)):
            line = read_input()
            a, b = line.split()
            if g.get(a):
                g[a].append(b)
            else:
                g[a] = [b]

        answer = ' '.join(topological(g))
        print(answer)

