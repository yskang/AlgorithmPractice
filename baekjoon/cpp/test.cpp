#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;

struct dsu {
    vi root;
    
    dsu(int n) {
        root.resize(n);
        for (int i = 0; i < n; i++) root[i] = i;
    }

    int find(int i) {
        if (i != root[i]) root[i] = find(root[i]);
        return root[i];
    }

    bool merge(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        root[a] = b;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, m; cin >> n >> m;
    vvi graph(n+1);
    dsu uf(n+1);
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
        uf.merge(u, v);
    }

    vi isodd(n+1);
    int oddall = 0;
    for (int i = 1; i <= n; i++) {
        if (graph[i].size() & 1) {
            isodd[uf.find(i)] = 1;
            oddall++;
        }
    }

    set<int> odd, even;
    for (int i = 1; i <= n; i++) {
        if (isodd[uf.find(i)]) odd.insert(uf.find(i));
        else even.insert(uf.find(i));
    }

    int rst = 0;
    while (odd.size() + even.size() > 1) {
        if (odd.size() == 0) {
            int a = *even.begin(); even.erase(even.begin());
            int b = *even.begin(); even.erase(even.begin());
            uf.merge(a, b);
            oddall += 2;
            rst++;
            odd.insert(uf.find(a));
        }
        else {
            if (odd.size() > 1) {
                int a = *odd.begin(); odd.erase(odd.begin());
                int b = *odd.begin(); odd.erase(odd.begin());
                uf.merge(a, b);
                oddall -= 2;
                rst++;
                odd.insert(uf.find(a));
            }
            else {
                int a = *odd.begin(); odd.erase(odd.begin());
                int b = *even.begin(); even.erase(even.begin());
                uf.merge(a, b);
                rst++;
                odd.insert(uf.find(a));
            }
        }
    }

    if (oddall > 2) rst += (oddall - 2) / 2;
    cout << rst << endl;
}