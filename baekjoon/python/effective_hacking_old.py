import sys
import random
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def dfs_old(nodes, node, visited, count):
    if visited[node]:
        return
    visited[node] = True
    count[0] += 1
    for child in nodes[node]:
        dfs_old(nodes, child, visited, count)


def maximum_node_old(nodes, candidates, N):
    max_computer = 0
    max_nodes = []
    max_visits = []

    for node, valid in enumerate(candidates[1:], 1):
        if valid:
            count = [0]
            visited = [False] * (N + 1)

            dfs_old(nodes, node, visited, count)

            if count[0] > max_computer:
                max_computer = count[0]
                max_nodes = [node]
                max_visits = [visited]
            elif count[0] == max_computer:
                max_nodes.append(node)
                max_visits.append(visited)

    anothers = [False for _ in range(N+1)]
    for visited_log in max_visits:
        for node, visit in enumerate(visited_log[1:], 1):
            anothers[node] |= visit

    for node, visit in enumerate(anothers[1:], 1):
        if not visit:
            count = [0]
            visited = [False] * (N + 1)

            dfs_old(nodes, node, visited, count)

            if count[0] > max_computer:
                max_computer = count[0]
                max_nodes = [node]
                max_visits = [visited]
            elif count[0] == max_computer:
                max_nodes.append(node)
                max_visits.append(visited)

    return ' '.join(list(map(str, sorted(max_nodes))))




def dfs(n: int, visited: list):
    if visited[n]:
        return
    visited[n] = True

    for ch in graph[n]:
        dfs(ch, visited)
    
    stack.append(n)


def dfs_r(n: int, visited: list, scc: list):
    if visited[n]:
        return
    visited[n] = True

    for ch in r_graph[n]:
        dfs_r(ch, visited, scc)

    scc.append(n)


def maximum_node(N: int):
    candis = [True for _ in range(N+1)]
    map_table = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    for node in range(1, N+1):
        dfs(node, visited)

    visited = [False for _ in range(N+1)]
    for node in reversed(stack):
        temp = []
        dfs_r(node, visited, temp)
        sorted_temp = sorted(temp)

        if temp:
            # print(temp, end= ', ')
            for t in temp:
                map_table[t] = sorted_temp
            for t in sorted_temp[1:]:
                candis[t] = False
    # print()

    for a, b in inputs:
        a = map_table[a][0]
        b = map_table[b][0]
        if a != b:
            mod_graph[b].add(a)
            candis[a] = False

    # inputs = []

    # print(mod_graph)
    # print(map_table)
    # print(candis)

    child_nums = defaultdict(lambda: [])
    for node, trusted in enumerate(candis[1:], 1):
        if trusted:
            visited = [False for _ in range(N+1)]
            count = [0]
            get_num_child(node, map_table, visited, count)
            child_nums[count[0]].append(node)

    # print(child_nums)
    max_nodes = set(child_nums[sorted(child_nums.keys(), reverse=True)[0]])
    results = set()
    for node in max_nodes:
        results.update(map_table[node])
    
    return ' '.join(map(str, sorted(results)))


def get_num_child(node: int, map_table: list, visited: list, count: list):
    if visited[node]:
        return

    visited[node] = True

    for child in mod_graph[node]:
        get_num_child(map_table[child][0], map_table, visited, count)

    count[0] += len(map_table[node])
    return



if __name__ == '__main__':
    while True:
        N, M = random.randint(1, 10000), random.randint(1, 100000)

        ns = [i for i in range(1, N+1)]
        random.shuffle(ns)

        nodes = [[] for _ in range(N + 1)]
        candidates = [True for _ in range(N + 1)]

        graph = [set() for _ in range(N+1)]
        r_graph = [set() for _ in range(N+1)]
        mod_graph = [set() for _ in range(N+1)]
        stack = []
        inputs = []

        saved_nodes = []

        for _ in range(M):
            a = random.randint(1, N)
            b = random.randint(1, N)
            saved_nodes.append((a, b))
            # a, b = read_list_int()
            nodes[b].append(a)
            candidates[a] = False

            graph[b].add(a)
            r_graph[a].add(b)
            inputs.append((a, b))

        old_result = maximum_node_old(nodes, candidates, N)
        new_result = maximum_node(N)

        print(new_result)
        print(old_result)
        if old_result != new_result:
            print('Wrong result!!')
            print('N: {}, M: {}'.format(N, M))
            print(saved_nodes)
            break