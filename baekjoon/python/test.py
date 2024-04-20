import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write

direction = {
    "A": (0,1,2,3),
    "B": (),
    "C": ((0, 2),(1, 3)),
    "D": ((1, 3),(0, 2))
}

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

revDir = (2, 3, 0, 1)

def solve():
    n, m = map(int, input().split())
    graph = [list(input()) for i in range(n)]
    visited = [[[[False for i in range(128)] for i in range(128)] for i in range(m)] for i in range(n)]

    q = deque()
    q.append((0, 0, 0, 0, 0))
    visited[0][0][0][0] = True

    while q:
        cx, cy, curr, rState, cState = q.popleft()

        if cx == n - 1 and cy == m - 1:
            return curr

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            revD = revDir[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[cx][cy] == 'B':
                continue
            elif graph[cx][cy] == 'A':
                pass
            else:
                check = ((rState & (1 << cx) != 0) + (cState & (1 << cy) != 0)) % 2
                checkArr = direction[graph[cx][cy]][check]
                if i not in checkArr:
                    continue

            if graph[nx][ny] == 'B':
                continue
            elif graph[nx][ny] == 'A':
                pass
            else:
                check = ((rState & (1 << nx) != 0) + (cState & (1 << ny) != 0)) % 2
                checkArr = direction[graph[nx][ny]][check]
                if revD not in checkArr:
                    continue

            if visited[nx][ny][rState][cState]:
                continue

            visited[nx][ny][rState][cState] = True 
            q.append((nx, ny, curr + 1, rState, cState))

        
        rState ^= (1 << cx) 
        cState ^= (1 << cy)

        if visited[cx][cy][rState][cState]:
            continue
        
        visited[cx][cy][rState][cState] = True
        q.append((cx, cy, curr + 1, rState, cState))

    return -1 
        
if __name__ == "__main__":
    print(solve())