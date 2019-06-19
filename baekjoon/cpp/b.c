#include <stdio.h>
//#include <algorithm>

//using namespace std;

#define INF (1<<29)

typedef long long lli;

lli hp, att, ehp, eatt;
lli chp[100001], catt[121];

int f(int buf, int c) {
	lli h = chp[c] - 3 * eatt*buf;
	lli a = catt[buf];
	if (h <= 0) return INF;
	lli hh = ehp - eatt*c;
	if (hh <= 0) return buf + c;
	lli need = ((hh + a - 1) / a - 1);
	if (need*eatt >= h) return INF;
	return need + 1 + buf + c;
}
  
int main() {
	scanf("%lld %lld %lld %lld", &hp, &att, &ehp, &eatt);
	chp[0] = hp; catt[0] = att;
	for (int i = 1; i <= 120; i++) {
		catt[i] = catt[i - 1] + catt[i - 1] / 5;
		if (catt[i] >= INF) catt[i] = INF;
	}
	for (int i = 1; i <= 100000; i++) {
		chp[i] = chp[i - 1] + chp[i - 1] / 10;
		if (chp[i] >= INF) chp[i] = INF;
	}
	int res = (1 << 29);
    int c_c , b_c, a_c;
	for (int i = 0; i <= 120; i++) {
		for (int j = 0; j <= 100000; j++) {
			int w = f(i, j);
			if (w < res)  { 
                b_c = i ;//b
                c_c = j;//c
                a_c = w - i - j;//a
                res = w;
            }
		}
	}
	printf("%d : B : %d C : %d A : %d\n", res, b_c, c_c, a_c);
	return 0;
}