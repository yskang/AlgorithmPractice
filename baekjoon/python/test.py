<<<<<<< HEAD
from sys import stdin

dir = [
    (0,1), (0, -1), (-1, 0), (1, 0)
]

v, e = map(int, stdin.readline().split())

board = [set() for _ in range(v)]
degs = [0 for _ in range(v)]

for _ in range(e):
    a, b = map(lambda x: int(x)-1, stdin.readline().split())
    degs[a] += 1
    degs[b] += 1

    board[a].add(b)
    board[b].add(a)

visits = set()

def dfs(idx):
    nodes = 1
    odds = degs[idx] % 2
    for nxt in board[idx]:
        if nxt in visits:
            continue
        
        visits.add(nxt)
        u,o =  dfs(nxt)
        nodes += u
        odds += o
    return nodes, odds

g = []
for idx in range(v):
    if idx in visits:
        continue
    visits.add(idx)
    g.append(dfs(idx))
# print(g)

newg, onecnt = [], 0

for nodes, odd in g:
    if nodes == 1:
        onecnt += 1
        continue
    newg.append((nodes, odd))

if onecnt >= 2:
    newg.append((2, 2))
elif onecnt == 1:
    newg.append((1, 0))


ans, eo  = len(g) - 1, [newg[0][0] - newg[0][1], newg[0][1]]

for nodes, odd in newg[1:]:
    be, bo = eo
    even = nodes - odd

    ae = even + be
    ao = odd + bo

    if ao >= 2:
        eo = [ae + 2, ao -2]
    else:
        eo = [ae - 2, ao+2]

# print(eo, ans)

if eo[1] > 2:
    ans += (eo[1]-2) // 2

print(ans)
=======
void solve() {  
   int v, e;  
   cin >> v >> e;  
   vvi edges(v);  
   vi deg(v);  
   for (int i = 0, a, b; i < e; i++) {  
      cin >> a >> b, a--, b--;  
      edges[a].pb(b), edges[b].pb(a);  
      deg[a]++;  
      deg[b]++;  
   }  
   vi vis(v);  
   int component = 0, ans = 0;  
   for (int i = 0; i < v; i++) {  
      if (vis[i]) continue;  
      component++;  
      vi group;  
      queue<int> q;  
      q.push(i);  
      vis[i] = 1;  
      while (sz(q)) {  
         int cur = q.front();  
         q.pop();  
         group.pb(cur);  
         for (int to: edges[cur]) {  
            if (!vis[to]) {  
               vis[to] = 1;  
               q.push(to);  
            }  
         }  
      }  
      int odd = 0;  
      for (int j: group) if (deg[j] % 2)odd++;  
      if (odd > 2) {  
         odd -= 2;  
         ans += odd / 2;  
      }  
   }  
   cout << ans + max(0, component - 1);  
}
>>>>>>> b1598dd0ae5d4f8b3adc13b93a8f30f48deccce8
