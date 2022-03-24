import sys


def count_zero_one(n):
    dp = [(1, 0), (0, 1)]
    for i in range(2, n + 1):
        dp.append((dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]))
    return dp

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    dp = count_zero_one(40)
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        print("{} {}".format(dp[n][0], dp[n][1]))
