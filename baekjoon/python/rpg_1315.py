# Title: RPG
# Link: https://www.acmicpc.net/problem/1315

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
max_size = 1001

class Quest:
    def __init__(self):
        self.strengths = []
        self.intelligents = []
        self.points = []
        self.completed = []
    
    def add_quest(self, s: int, i: int, p: int):
        self.strengths.append(s)
        self.intelligents.append(i)
        self.points.append(p)
        self.completed.append(False)
        


def maximum_quest(stren: int, inteli: int, n: int, quests: Quest, dp: list):
    if dp[stren][inteli] != -1:
        return dp[stren][inteli]

    points = 0
    completions = []
    count = 0
    for i in range(n):
        if quests.strengths[i] <= stren or quests.intelligents[i] <= inteli:
            if not quests.completed[i]:
                points += quests.points[i]
                quests.completed[i] = True
                completions.append(i)    
            count += 1
    
    max_quest = count

    if points != 0:
        for s in range(stren, min(1000, stren+points+1)):
            i = min(1000, inteli + points - (s - stren))
            max_quest = max(max_quest, maximum_quest(s, i, n, quests, dp))

    for i in completions:
        quests.completed[i] = False

    dp[stren][inteli] = max_quest
    return max_quest


def solution(n: int, quests: Quest):
    dp = [[-1 for _ in range(1001)] for _ in range(1001)]
    return maximum_quest(1, 1, n, quests, dp)


def main():
    q = Quest()
    n = read_single_int()
    for _ in range(n):
        q.add_quest(*read_list_int())
    print(solution(n, q))


if __name__ == '__main__':
    main()