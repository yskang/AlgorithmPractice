#include<bits/stdc++.h>
using namespace std;


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

    int ans = 0;


    cout << n << " " << m << " " << k << endl;
    for (int i = 1; i < n+1; i++)
    {
        cout << ramens[i] << " ";
    }
    cout << endl;
    for (int i = 1; i < n+1; i++)
    {
        cout << i << ": ";
        for (int j = 0; j < graph[i].size(); j++)
        {
            cout << graph[i][j].first << " " << graph[i][j].second << " ";
            cout << endl;
        }
        cout << endl;
    }
    for (int i = 0; i < k; i++)
    {
        cout << start_positions[i] << " ";
    }
}
