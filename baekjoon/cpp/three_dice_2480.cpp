#include<bits/stdc++.h>

using namespace std;


void solution(int a, int b, int c) {
    int prise = 0;
    if ( a != b && b != c && c != a) {
        prise = max(a, max(b, c)) * 100;
    } else if ( a == b && b == c && a == c) {
        prise = 10000 + a * 1000;
    } else {
        if (a == b) {
            prise = 1000 + a * 100;
        } else if (b == c) {
            prise = 1000 + b * 100;
        } else {
            prise = 1000 + c * 100;
        }
    }
    cout << prise << endl;
}


int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    int a, b, c;
    cin >> a >> b >> c;

    solution(a, b, c);
    
    return 0;
}