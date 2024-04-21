#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;

int n, m, k;
vector<int>vec[100010];
bool dele[100010];
int ind[100010];
int ans = 0;
bool is_can;

//delete path count, exist path

pair<int, int> back(int now, bool flag) {
	if (now == n) {
		return make_pair(0, flag);
	}

	int ret_exist = 0;
	int ret_value = 0;
	int to_value = 1234567890;

	for (int i = 0; i < vec[now].size(); i++) {
		auto k = back(vec[now][i], flag ^ 1);
		if (k.second) {
			if (to_value > k.first) {
				to_value = k.first;
				if (ret_exist)ret_value++;
				ret_exist = 1;
			}
			else {
				if (to_value == 0 && k.first == 0) {
				}
				else
					ret_value++;
			}
		}
		else
			ret_value++;
	}
	return make_pair(ret_value + to_value, ret_exist);
}



int main() {
	scanf("%d %d %k", &n, &m, &k);
	for (int i = 1; i <= m; i++) {
		int u, v;
		scanf("%d %d", &u, &v);
		vec[u].push_back(v);
		ind[v]++;
	}

	int mini = 1234567890;

	for (int i = 1; i <= n; i++) {
		if (!ind[i]) {
			auto k = back(i, 1);
			if (k.second)mini = min(mini, k.first);
		}
	}

	printf("%d\n", mini == 1234567890 ? -1 : mini);

	return 0;

}