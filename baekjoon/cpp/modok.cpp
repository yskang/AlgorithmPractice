#include <iostream>
using namespace std;

int myMin;
int opoMin;
bool win = false;

typedef struct {
	int power;
	int vital;
	bool isDead;
	bool isAttacked;
}minions;

//pair<int, int> player;//100점
//minions player;


void copyMin(minions copy[8], minions origin[8], int num) {
	int i;
	for (i = 1; i <= num; i++) {
		copy[i].isAttacked = origin[i].isAttacked;
		copy[i].isDead = origin[i].isDead;
		copy[i].power = origin[i].power;
		copy[i].vital = origin[i].vital;
	}
}

//미니언 공격
void attack(minions& p, minions& o) {
	p.isAttacked = true;

	p.vital -= o.power;
	if (p.vital <= 0)
		p.isDead = true;

	o.vital -= p.power;
	if (o.vital <= 0)
		o.isDead = true;
}

//모독 사용
void defile(minions player[8], minions opponent[8]) {
	int i;
	bool isDead = true;

	//모독 메카니즘
	while (isDead) {
		isDead = false;
		for (i = 1; i <= myMin; i++) {
			if (!player[i].isDead) {
				player[i].vital -= 1;
				if (player[i].vital == 0) {
					isDead = true;
					player[i].isDead = true;
				}
			}
		}

		for (i = 1; i <= opoMin; i++) {
			if (!opponent[i].isDead) {
				opponent[i].vital -= 1;
				if (opponent[i].vital == 0) {
					isDead = true;
					opponent[i].isDead = true;
				}
			}
		}
	}
}

void calculate(int order[8], int cnt) {
	int i;
	
	for (i = 0; i < cnt; i++) {
		if (order[i] == -1) {
			cout << "use modok" << endl;
		}
		else {
			cout << "attack " << order[i] / 10 << " " << order[i] % 10 << endl;
		}
	}
}

void myTurn(minions player[8], minions opponent[8],int order[8], int cnt, bool defileUsed) {//order: 공격 및 모독 사용 기록, cnt: order 수 늘리기
	int i, j;
	minions tmpPlayer[8];
	minions tmpOppo[8];


	//확인
	/*for (i = 0; i < cnt; i++)
		cout << order[i] << ' ';
	cout << endl;

	for (i = 1; i <= myMin; i++) {
		cout << "Player " << i << ": [" << player[i].power << ", " << player[i].vital << ']' << endl;
	}
	cout << endl;

	for (i = 1; i <= opoMin; i++) {
		cout << "Opponent " << i << ": [" << opponent[i].power << ", " << opponent[i].vital << ']' << endl;
	}

	cout << " ==================================================== " << endl;*/
	

	if (win)//하나라도 성공시 끝내기
		return;

	if (opoMin == 0) {//만약 적 미니언 없을 시 0회로 걍 성공
		cout << 0 << endl;
		return;
	}
	else if (myMin == 0) {//만약 내 미니언이 없을 시 모독 사용으로 바로 정리되는지 확인
		defile(player, opponent);
		for (i = 1; i <= opoMin; i++) {
			if (!opponent[i].isDead)
				return;

			if (i == opoMin) {
				win = true;
				cout << 1 << endl;
				cout << "use modok" << endl;
				return;
			}
		}
	}

	//적 몰살 성공 확인
	for (i = 1; i <= opoMin; i++) {
		if (!opponent[i].isDead)
			break;
		
		if (i == opoMin) {//성공 조건
			win = true;
			cout << cnt << endl;
			calculate(order, cnt);
			return;
		}
	}

	


	//모독 사용, 내 하수인 모두 사망 또는 공격 다한 후 적 하수인 살아있음 실패
	for (i = 1; i <= myMin; i++) {
		if (!player[i].isDead || !player[i].isAttacked || defileUsed == false)
			break;

		if (i == myMin) {
			for (j = 1; j <= opoMin; j++) {
				if (!opponent[j].isDead) {
					return;
				}
			}
		}
	}

	

	
	copyMin(tmpPlayer, player, myMin);
	copyMin(tmpOppo, opponent, opoMin);
	

	for (i = 1; i <= myMin; i++) {
		if (!defileUsed) {//모독 사용하지 않았을 시
		//모독 사용
			defile(player, opponent);
			order[cnt] = -1;
			myTurn(player, opponent, order, cnt + 1, true);

			//백트래킹
			copyMin(player, tmpPlayer, myMin);
			copyMin(opponent, tmpOppo, opoMin);
			order[cnt] = 0;
		}

		if (!player[i].isAttacked && !player[i].isDead) {//공격하지 않고 죽지도 않았으면 player 미니언이 공격 가능
			//cout << "Here" << endl;
			for (j = 1; j <= opoMin; j++) {
				if (!opponent[j].isDead) {//적이 죽지 않았다면 공격 가능
					//공격
					attack(player[i], opponent[j]);
					order[cnt] = i * 10 + j;
					myTurn(player, opponent, order, cnt + 1, defileUsed);

					//백트래킹
					copyMin(player, tmpPlayer, myMin);
					copyMin(opponent, tmpOppo, opoMin);
					order[cnt] = 0;
				}
			}
		}
	}

	return;
}

int main() {
	
	int i;
	int order[8];
	minions player[8];
	minions opponent[8];

	cin >> myMin >> opoMin;

	for (i = 1; i <= myMin; i++) {
		cin >> player[i].power >> player[i].vital;
		player[i].isDead = false;
		player[i].isAttacked = false;
	}

	for (i = 1; i <= opoMin; i++) {
		cin >> opponent[i].power >> opponent[i].vital;
		opponent[i].isDead = false;
	}

	myTurn(player, opponent, order, 0, false);//dfs

	if (!win && opoMin != 0) {
		cout << -1 << endl;
	}

	return 0;
}
