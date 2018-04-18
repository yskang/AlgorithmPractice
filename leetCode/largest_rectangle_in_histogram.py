class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        heights.append(0)
        width = len(heights)
        ans = 0

        stack = [-1]

        for i in range(width):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                ans = max(ans, h * w)
            stack.append(i)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))


