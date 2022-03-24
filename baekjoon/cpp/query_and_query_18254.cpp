#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void updateBIT(int BITree[], int n, int index, int val)
{
    index = index + 1;
    while (index <= n)
    {
        BITree[index] ^= val;
        index += index & (-index);
    }
}

int *constructBITree(int arr[], int n)
{
    int *BITree = new int [n+1];
    for (int i = 1; i <= n; i++)
    {
        BITree[i] = 0;
    }

    for (int i = 0; i < n; i++)
    {
        updateBIT(BITree, n, i, arr[i]);
    }
    
    return BITree;
}

int getSum(int BITree[], int index)
{
    int sum = 0;
    index = index + 1;
    
    while (index > 0)
    {
        sum ^= BITree[index];
        index -= index & (-index);
    }

    return sum;
}

void update(int BITree[], int l, int r, int n, int val)
{
    updateBIT(BITree, n, l, val);
    updateBIT(BITree, n, r+1, val);
}

struct updatedata
{
    int l, r, x;
};

struct query
{
    int kind, a, b, c;
};

int n, m, q;
vector<updatedata> updates;
vector<query> queries;
int a_list[100011];
int prefix_xors[100011];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    cin >> m;
    cin >> q;

    for (int i = 0; i < n; i++)
    {
        cin >> a_list[i];
    }

    int a, b, c, d;

    for (int i = 0; i < m; i++)
    {
        cin >> a;
        cin >> b;
        cin >> c;
        updates.push_back({a, b, c});
    }

    for (int i = 0; i < q; i++)
    {
        cin >> a;
        if (a == 1)
        {
            cin >> b;
            cin >> c;
            cin >> d;
            queries.push_back({a, b, c, d});
        } 
        else 
        {
            cin >> b;
            cin >> c;
            queries.push_back({a, b, c, d});
        }
    }

    prefix_xors[0] = 0;

    for (int i = 0; i < n; i++)
    {
        prefix_xors[i+1] = prefix_xors[i]^a_list[i];
    }

    int arr[n];
    fill_n(arr, n, 0);
    int *bit_tree = constructBITree(arr, n);

    int ql, qr, res;

    int ans[q];
    fill_n(ans, q, -1);
    int ans_idx = 0;
    for (int i = 0; i < q; i++)
    {
        if (queries[i].kind == 1)
        {
            update(bit_tree, queries[i].a-1, queries[i].b-1, n, queries[i].c);
        }
        else
        {
            ql = queries[i].a;
            qr = queries[i].b;
            res = prefix_xors[qr] ^ prefix_xors[ql-1];
            for (int j = 0; j < m; j++)
            {
                if ((updates[j].r < ql) or (qr < updates[j].l))
                {
                    continue;
                }
                if ((min(updates[j].r, qr) - max(updates[j].l, ql) + 1)%2 == 1)
                {
                    res ^= getSum(bit_tree, j) ^ updates[j].x;
                }
            }
            ans[ans_idx] = res;
            ans_idx++;
        }
    }

    for (int i = 0; i < ans_idx; i++)
    {
        cout << ans[i] << "\n";
    }

    return 0;
}