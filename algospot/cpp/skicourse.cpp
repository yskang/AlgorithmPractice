#include <stdio.h>
#include <vector>
using namespace std;
#define MAX_N 1001

vector<int> G[MAX_N],R[MAX_N];
int T,N,M,D[MAX_N],Q[MAX_N],C[MAX_N],K[MAX_N];

int main()
{
	int i,x,y;

	scanf ("%d",&T); while (T--){
		scanf ("%d %d",&N,&M);
		for (i=0;i<N;i++) G[i].clear(),R[i].clear(),K[i]=0,D[i]=0x7fffffff;
		for (i=0;i<M;i++){
			scanf ("%d %d",&x,&y); x--; y--;
			G[x].push_back(y);
			R[y].push_back(x);
		}

		int head = -1, tail = -1;
		Q[++head] = 0; D[0] = 0; C[0] = 1;
		while (tail < head){
			x = Q[++tail];
			for (i=0;i<G[x].size();i++){
				y = G[x][i];
				if (D[y] > D[x] + 1){
					Q[++head] = y; D[y] = D[x] + 1; C[y] = 1;
				}
			}
		}

		head = tail = -1;
		Q[++head] = N-1; K[N-1] = 1;
		while (tail < head){
			x = Q[++tail];
			for (i=0;i<R[x].size();i++){
				y = R[x][i];
				if (!K[y] && D[y] < D[x]){
					Q[++head] = y; K[y] = 1;
				}
			}
		}

		for (i=0;i<N;i++) if (K[i]) printf ("%d ",i+1); printf ("\n");
	}

	return 0;
}
