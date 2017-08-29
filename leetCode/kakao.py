def main():
    land = [[1, 2, 5, 5],
            [1, 5, 1, 5],
            [1, 2, 3, 5],
            [1, 2, 5, 5],
            [1, 5, 1, 5],
            [1, 2, 5, 5]]
    print(solution(land))

def solution(land):
    dp = [land[0]]
    for i in range(len(land)-1):
        dp.append([-1]*4)

    for i in range(len(land)-1):
        for j in range(4):
            dp[i+1][j] = max(dp[i][:j] + dp[i][j+1:]) + land[i+1][j]

    print(dp)
    return max(dp[len(land)-1])

main()