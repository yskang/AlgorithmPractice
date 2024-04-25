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