#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int size, sum = 0;
    cin >> size;

    vector<int> l(size, 1);
    
    for (int i : l) {
        for (int j : l) {
            sum += l[j];
        }
    }

    cout << sum << endl;
}