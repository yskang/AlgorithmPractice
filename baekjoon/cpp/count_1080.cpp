#include<bits/stdc++.h>

using namespace std;

vector<int> numbers = vector<int>(201, 0);

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        numbers[a+100]++;
    }
    int v;
    cin >> v;
    cout << numbers[v+100] << endl;
    return 0;
}