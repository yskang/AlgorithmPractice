#include<bits/stdc++.h>

using namespace std;

vector<pair<int, int> > numbers;

void solution(int n) {
    while (n) {
        cout << "long ";
        n -= 4;
    }
    cout << "int" << endl;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    cin >> n;
    solution(n);
    return 0;
}