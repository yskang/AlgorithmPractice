#include<bits/stdc++.h>
using namespace std;

struct CostNode {
    int cost;
    int node;
};

vector<int> djikstra(int start, vector<vector<pair<int, int> > > graph) {
    vector<int> dist(graph.size(), INT_MAX);
    vector<int> path(graph.size(), -1);
    
    dist[start] = 0;
    priority_queue<CostNode> pq;
    pq.push(CostNode(0, start));
    while (!pq.empty()) {
        int cost = pq.top().first;
        int node = pq.top().second;
        pq.pop();
        if (dist[node] < cost) {
            continue;
        }
        for (auto edge : graph[node]) {
            int next_node = edge.first;
            int next_cost = edge.second;
            int new_cost = cost + next_cost;
            if (new_cost < dist[next_node]) {
                dist[next_node] = new_cost;
                pq.push({new_cost, next_node});
                path[next_node] = node;
            }
            else if (new_cost == dist[next_node]) {
                path[next_node] = max(node, path[next_node]);
            }
        }
    }
    return path;
}

void solution(int n, int m, int k, vector<int> ramens, vector<vector<pair<int, int>>> graph, vector<int> start_positions) {
    ramens.insert(ramens.begin(), 0);
    vector<int> path;
    path = djikstra(1, graph);
    for (int i = 0; i < start_positions.size(); i++) {
        int start = start_positions[i];
        if (start == 1) {
            if (ramens[start] > 0) {
                ramens[start] -= 1;
                cout << start << endl;
                continue;
            }
            else {
                cout << -1 << endl;
                continue;
            }
        }
        if (path[start] == -1) {
            cout << -1 << endl;
            continue;
        }
        int current = start;
        while (true) {
            if (current == -1) {
                cout << -1 << endl;
                break;
            }
            if (ramens[current] > 0) {
                ramens[current] -= 1;
                cout << current << endl;
                break;
            }
            if (current == 1) {
                cout << -1 << endl;
                break;
            }
            current = path[current];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> ramens(n+1);
    vector<vector<pair<int, int>>> graph(n+1);
    vector<int> start_positions(k);
    for (int i = 1; i < n+1; i++) {
        cin >> ramens[i];
    }
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }
    for (int i = 0; i < k; i++) {
        cin >> start_positions[i];
    }
    solution(n, m, k, ramens, graph, start_positions);
    return 0;
}






void solution(int n, int m, int k, vector<int> ramens, vector<vector<pair<int, int> > > graph, vector<int> start_positions)
{
    ramens.insert(ramens.begin(), 0);
    vector<int> path;
    path = djikstra(1, graph);
    for (int i = 0; i < start_positions.size(); i++)
    {
        int start = start_positions[i];
        if (start == 1)
        {
            if (ramens[start] > 0)
            {
                ramens[start] -= 1;
                cout << start << endl;
                continue;
            }
            else
            {
                cout << -1 << endl;
                continue;
            }
        }
        if (path[start] == -1)
        {
            cout << -1 << endl;
            continue;
        }
        int current = start;
        while (true)
        {
            if (current == -1)
            {
                cout << -1 << endl;
                break;
            }
            if (ramens[current] > 0)
            {
                ramens[current] -= 1;
                cout << current << endl;
                break;
            }
            if (current == 1)
            {
                cout << -1 << endl;
                break;
            }
            current = path[current];
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n, m, k;
    cin >> n >> m >> k;

    vector<int> ramens(n+1);
    vector<vector<pair<int, int> > > graph(n+1);
    vector<int> start_positions(k);

    for (int i = 1; i < n+1; i++)
    {
        cin >> ramens[i];
    }

    for (int i = 0; i < m; i++) 
    {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back(pair<int, int>(b, c));
        graph[b].push_back(pair<int, int>(a, c));
    }

    for (int i = 0; i < k; i++)
    {
        cin >> start_positions[i];
    }

    solution(n, m, k, ramens, graph, start_positions);
    return 0;
}
