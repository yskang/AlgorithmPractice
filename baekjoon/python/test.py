import sys
input = sys.stdin.readline
import heapq
INF = int(1e10)
#################################################
n, m, k = map(int, input().split())

market = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == b:
        continue

    graph[a].append([b, c])
    graph[b].append([a, c])

visit = []
heapq.heappush(visit, [0, 1, 0])

distance = [[INF, 0, 0] for _ in range(n+1)]
# visited = [False for _ in range(n+1)]
# visited[1] = True
distance[1][0] = 0


while visit:
    cost, node, root = heapq.heappop(visit)
    if market[node] > 0:
        root = node

    for next_node, dis in graph[node]:
        if dis + cost < distance[next_node][0]:
            distance[next_node][0] = dis + cost
            distance[next_node][1] = node
            distance[next_node][2] = root
            heapq.heappush(visit, [dis+cost, next_node, root])

        elif dis + cost == distance[next_node][0]:
            if distance[next_node][1] < node:
                distance[next_node][1] = node
                distance[next_node][2] = root

        # if visited[next_node]:
        #     continue
        #
        # visited[next_node] = True
check = [True for _ in range(n+1)]
for _ in range(k):
    n = int(input())
    now_mart = n
    path = [now_mart]
    if distance[now_mart][0] == INF or not check:
        print(-1)
        continue

    while True:
        if now_mart == 0 or not check:
            for node in path:
                check[node] = False
            print(-1)
            break

        if market[now_mart] > 0:
            market[now_mart] -= 1
            print(now_mart)
            break

        now_mart = distance[now_mart][2]
        distance[n][2] = now_mart
        path.append(now_mart)