class Solution(object):
    def maximal_rectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        width = len(matrix[0])
        heights = [0] * (width+1)
        ans = 0

        for row in matrix:
            for i in range(width):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0

            stack = [-1]

            for i in range(width+1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximal_rectangle([["1", "0", "1", "0", "0"],
                                ["1", "0", "1", "1", "1"],
                                ["1", "1", "1", "1", "1"],
                                ["1", "0", "1", "1", "0"]]))
