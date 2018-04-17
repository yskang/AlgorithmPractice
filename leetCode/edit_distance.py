class Solution(object):

    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        if m == 0 or n == 0:
            return n if m == 0 else m

        d = [[0]*(m+1) for y in range(n+1)]

        for i in range(1, m+1):
            d[0][i] = i

        for j in range(1, n+1):
            d[j][0] = j

        for j in range(1, n+1):
            for i in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    cost = 0
                else:
                    cost = 1
                d[j][i] = min(d[j][i-1]+1, d[j-1][i]+1, d[j-1][i-1]+cost)

        return d[n][m]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("horse", "ros"))
    print(sol.minDistance("intention", "execution"))