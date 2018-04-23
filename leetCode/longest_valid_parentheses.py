class Solution():
    def longestValidParentheses(self, s):
        valid_ps = []
        numbered_ps = enumerate(s, 0)
        stack = []

        for (i, p) in numbered_ps:
            if p == '(':
                stack.append((i, p))
            else:
                if stack:
                    popped = stack.pop()
                    valid_ps.append((popped[0], i))

        if not valid_ps:
            return 0

        print(stack)
        print(valid_ps)

        valid_ps = sorted(valid_ps, key=lambda x: x[0])
        print(valid_ps)

        start = valid_ps[0][0]
        end = valid_ps[0][1]
        max_range = [end - start + 1]
        current_max = max_range[-1]

        for p in valid_ps[1:]:
            if p[0] - end == 1:
                end = p[1]
                max_range[-1] += (p[1] - p[0] + 1)
                current_max = max(current_max, max_range[-1])
            elif p[0] - end > 1:
                start = p[0]
                end = p[1]
                max_range.append(end - start + 1)
                current_max = max(current_max, max_range[-1])

        return current_max


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses("(()()(())(("))