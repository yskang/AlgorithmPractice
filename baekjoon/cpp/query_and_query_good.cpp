#include <bits/stdc++.h>
#define x first
#define y second
using namespace std;

struct asdf{
	int s, e, x;
};

struct asdff{
	int s, e, x, i;
};

typedef pair<int, int> p;

int n, m, q;
int arr[101010];
p mq[101010]; //mquery
int prefix[101010];
int buckres[101010];
int ans[101010];
vector<asdf> qry;
vector<asdff> sweep[101010];

int tree[1 << 18];
int tmp[1 << 18];

void push(int node, int s, int e){
	if(!tmp[node]) return;
	if(s ^ e){
		tmp[node << 1] ^= 1;
		tmp[node << 1 | 1] ^= 1;
	}else{
		tree[node] ^= 1;
	}
	tmp[node] = 0;
}

void update(int l, int r, int node = 1, int s = 0, int e = (1<<17)-1){
	push(node, s, e);
	if(r < s || e < l) return;
	if(l <= s && e <= r){
		tmp[node]++;
		push(node, s, e);
		return;
	}
	int m = s + e >> 1;
	update(l, r, node << 1, s, m);
	update(l, r, node << 1 | 1, m+1, e);
	tree[node] = tree[node << 1] ^ tree[node << 1 | 1];
}

int query(int l, int r, int node = 1, int s = 0, int e = (1<<17)-1){
	push(node, s, e);
	if(r < s || e < l) return 0;
	if(l <= s && e <= r) return tree[node];
	int m = s + e >> 1;
	return query(l, r, node << 1, s, m) ^ query(l, r, node << 1 | 1, m+1, e);
}

void solve_bucket(){
	if(qry.empty()) return;
	qry.clear();
	for(int i=n; i>=1; i--) arr[i] ^= arr[i-1];
	for(int i=1; i<=m; i++){
		prefix[i] ^= prefix[i-1];
		buckres[mq[i].x] ^= prefix[i];
		buckres[mq[i].y] ^= prefix[i];
	}
	memset(prefix, 0, sizeof prefix);
	for(int i=1; i<=n; i++){
		buckres[i] ^= buckres[i-1];
		arr[i] ^= buckres[i];
		arr[i] ^= arr[i-1];
	}
	memset(buckres, 0, sizeof buckres);
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	mt19937 seed(chrono::high_resolution_clock::now().time_since_epoch().count());
	uniform_int_distribution<int> rd(100, 150);
	int bucket = rd(seed);
	cin >> n >> m >> q;
	for(int i=1; i<=n; i++) cin >> arr[i];
	for(int i=1; i<=m; i++){
		cin >> mq[i].x >> mq[i].y; mq[i].y++;
		int v; cin >> v;
		prefix[mq[i].x] ^= v;
		prefix[mq[i].y] ^= v;
	}
	for(int i=1; i<=n; i++){
		prefix[i] ^= prefix[i-1];
		arr[i] ^= prefix[i];
		arr[i] ^= arr[i-1];
	}
	memset(prefix, 0, sizeof prefix);
	memset(ans, -1, sizeof ans);
	int pv = 0;
	while(q--){
		int op, s, e, x; cin >> op >> s >> e;
		if(op == 1){
			cin >> x;
			prefix[s] ^= x; prefix[e+1] ^= x;
			qry.push_back({s-1, e, x});
		}else{
			ans[++pv] = arr[e] ^ arr[s-1];
			for(auto i : qry){
				sweep[i.s].push_back({s, e, i.x, pv});
				sweep[i.e].push_back({s, e, i.x, pv});
			}
		}
		if(--bucket == 0){
			solve_bucket();
			bucket = rd(seed);
		}
	}
	for(int i=0; i<=m; i++){
		mq[i].y--;
		update(mq[i].x, mq[i].y);
		for(auto t : sweep[i]) ans[t.i] ^= query(t.s, t.e) * t.x;
	}
	for(int i=1; i<=pv; i++) cout << ans[i] << "\n";
}