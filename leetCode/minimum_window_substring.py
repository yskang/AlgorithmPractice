import collections


class Solution():
    def minWindow(self, s, t):
        distance = len(s)
        min_pair = (0, -1)
        pairs = list(filter(lambda x: x[1] in t, enumerate(s, 0)))
        dicts = {k: t.count(k) for k in t}
        spare_char = list(dicts.keys())

        start, end = 0, 0
        while end <= len(pairs) and start <= len(pairs):
            while spare_char:
                if end >= len(pairs):
                    return s[min_pair[0]:min_pair[1] + 1]
                dicts[pairs[end][1]] -= 1
                if dicts[pairs[end][1]] <= 0:
                    if spare_char.count(pairs[end][1]) > 0:
                        spare_char.remove(pairs[end][1])
                end += 1

            while not spare_char:
                dicts[pairs[start][1]] += 1
                if dicts[pairs[start][1]] > 0:
                    spare_char.append(pairs[start][1])
                start += 1

            if distance > (pairs[end-1][0] - pairs[start-1][0]):
                distance = pairs[end-1][0] - pairs[start-1][0]
                min_pair = (pairs[start-1][0], pairs[end-1][0])

        return s[min_pair[0]:min_pair[1] + 1]

    def stephnatic(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]


if __name__ == '__main__':
    sol = Solution()
    # print(sol.minWindow("ab", "a"))
    # print(sol.minWindow("a", "b"))
    # print(sol.minWindow("a", "aa"))
    # print(sol.minWindow("bba", "ba"))
    # print(sol.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))
    print(sol.minWindow("ADDBECODEBANC", "ABC"))
    # print(sol.stephnatic("ab", "a"))
