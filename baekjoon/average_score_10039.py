# https://www.acmicpc.net/problem/10039
import sys


def get_average_score(scores):
    return sum(list(map(lambda x: 40 if x < 40 else x, scores)))/5


if __name__ == "__main__":
    scores = []
    for i in range(5):
        scores.append(int(sys.stdin.readline().strip()))

    print(int(get_average_score(scores)))

