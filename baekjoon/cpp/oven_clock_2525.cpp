#include<bits/stdc++.h>

using namespace std;

void solution(int a, int b, int c) {
    int h = (int) ((b + c) / 60);
    int m = (b + c) % 60;
    int hour = (a + h) % 24;
    cout << hour << " " << m << endl;
}


int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int a, b, c;
    cin >> a >> b >> c;

    solution(a, b, c);
    
    return 0;
}