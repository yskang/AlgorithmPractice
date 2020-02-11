#include <iostream>
using namespace std;

int main() {
    int n, a;
    int minNum = 1000000, maxNum = -1000000;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> a;
        minNum = min(minNum, a);
        maxNum = max(maxNum, a);
    }

    cout << minNum << " " << maxNum;
}