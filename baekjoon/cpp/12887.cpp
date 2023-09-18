#include <iostream>
#include <math.h>
#include <string.h>
using namespace std;
 
#define m 10007
typedef long long ll;
 
ll n;
ll origin[4][4] = 
{ 
{2,1,1,0},
{1,2,0,1},
{1,0,2,1},
{0,1,1,2} };
 
ll mat[30][4][4];
 
int main() {
    memcpy(mat[0], origin, sizeof(origin));
 
    cin >> n;
    ll tmp[4][4];
    int d = 1;
    while ((ll(1) << d) <= n) {
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                ll t = 0;
                for (int k = 0; k < 4; ++k) {
                    t = (t + (mat[d - 1][i][k] * mat[d - 1][k][j]) % m) % m;
                }
                tmp[i][j] = t;
            }
        }
 
        memcpy(mat[d++], tmp, sizeof(tmp));
    }
 
    int dd = 0;
    int arr[4] = { 1,0,0,0 };
    while ((ll(1) << dd) <= n) {
        int tmp[4];
        if (n & (ll(1) << dd)) {
            for (int i = 0; i < 4; ++i) {
                tmp[i] = 0;
                for (int j = 0; j < 4; ++j)
                    tmp[i] = (tmp[i] + (mat[dd][i][j] * arr[j]) % m) % m;
            }
 
            memcpy(arr, tmp, sizeof(tmp));
        }
        dd++;
    }
 
    cout << arr[0] % m;
}
