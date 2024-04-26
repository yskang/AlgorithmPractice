#include<bits/stdc++.h>
using namespace std;

int v, e;
vector<vector<int> > graph;
set<int> odds, evens;
map<int, vector<int> > groups;
priority_queue<pair<int, int> > group_info;
int ans = 0;

struct UnionFind {
    vector<int> parent;
    vector<int> rank;
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }
    int find(int u) {
        if (u == parent[u]) return u;
        return parent[u] = find(parent[u]);
    }
    void merge(int u, int v) {
        u = find(u);
        v = find(v);
        if (u == v) return;
        if (rank[u] > rank[v]) swap(u, v);
        parent[u] = v;
        if (rank[u] == rank[v]) rank[v]++;
    }
};

UnionFind uf = UnionFind(1);

void solution()
{
    for (int i = 1; i <= v; i++)
    {
        int g = uf.find(i);
        groups[g].push_back(i);

        if (graph[i].size() % 2 == 1)
        {
            odds.insert(i);
        }
        else
        {
            evens.insert(i);
        }
    }

    for (const pair<int, vector<int> >& group : groups)
    {
        int odd_num = 0, even_num = 0;
        set<int> temp_list;
        temp_list.insert(group.first);
        for (auto it = group.second.begin(); it != group.second.end(); ++it)
        {
            int node = *it;
            temp_list.insert(node);
        }
        for (int node : temp_list) {
            if (odds.find(node) != odds.end()) 
            {
                odd_num++;
            } else {
                even_num++;
            }
        }
        group_info.push(make_pair(odd_num, even_num));
    }

    while (group_info.size() > 1)
    {
        pair<int, int> a = group_info.top();
        group_info.pop();
        pair<int, int> b = group_info.top();
        group_info.pop();

        int merged_odd = 0, merged_even = 0;

        if (a.first > 0 && b.first > 0)
        {
            merged_odd = a.first + b.first - 2;
            merged_even = a.second + b.second -2;
        }
        else if (a.first > 0 && b.first == 0)
        {
            merged_odd = a.first;
            merged_even = a.second + b.second;
        }
        else if (a.first == 0 && b.first == 0)
        {
            merged_odd = 2;
            merged_even = a.second + b.second - 2;
        }
        else 
        {
            merged_odd = b.first;
            merged_even = a.second + b.second;
        }
        ans++;
        group_info.push(make_pair(merged_odd, merged_even));
    }

    pair<int, int> last = group_info.top();

    if (last.first == 0 || last.first == 2)
    {
        cout << ans << '\n';
    }
    else
    {
        cout << ans + int((last.first - 2) / 2) << '\n';
    }
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> v >> e;
    graph.resize(v+1);
    uf = UnionFind(v+1);
    for (int i = 0; i < e; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
        uf.merge(a, b);
    }
    solution();
    return 0;
}
