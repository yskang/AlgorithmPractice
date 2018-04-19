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

    def solution(self, heights):
        if not heights:
            return 0
        heights.append(0)
        max_area = 0
        stacked_index = [0]

        for current_index in range(1, len(heights)):
            if heights[stacked_index[-1]] < heights[current_index]:
                stacked_index.append(current_index)
            else:
                while True:
                    saved_index = stacked_index.pop()
                    height = heights[saved_index]
                    width = current_index if not stacked_index else current_index - stacked_index[-1] - 1
                    area = height * width
                    max_area = area if max_area < area else max_area
                    if stacked_index == [] or heights[stacked_index[-1]] < heights[current_index]:
                        stacked_index.append(current_index)
                        break

        return max_area


if __name__ == "__main__":
    sol = Solution()
    print(sol.solution([2, 1, 5, 6, 2, 3]))
    print(sol.solution([1]))
    print(sol.solution([2, 1, 2]))
    print(sol.largestRectangleArea([2, 1, 2]))



