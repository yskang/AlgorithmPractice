#include<bits/stdc++.h>

using namespace std;

vector<pair<int, int> > numbers;

void solution(int x, int n) {
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += numbers[i].first * numbers[i].second;
    }
    if (sum == x) {
        cout << "Yes" << endl;
        return;
    }
    cout << "No" << endl;
    return;
}


int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    long long x;
    int n;
    cin >> x;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        numbers.push_back(make_pair(a, b));
    }
    solution(x, n);
    return 0;
}