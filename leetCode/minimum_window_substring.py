class Solution():
    def __init__(self):
        self.i = -1

    def to_tuple(self, s):
        self.i += 1
        return s, self.i

    def minWindow(self, s, t):
        self.i = -1
        distance = len(s)
        min_pair = (0, -1)
        pairs = list(filter(lambda x: t.count(x[0]) > 0, map(self.to_tuple, s)))

        t_dic = {k: t.count(k) for k in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"}
        dicts = {}
        for k in t_dic:
            if t_dic[k] != 0:
                dicts[k] = t_dic[k]
        print(pairs)
        print(dicts)

        if not pairs:
            return ""

        end = 0
        dicts[pairs[0][0]] -= 1
        count = 0
        for k in dicts:
            if dicts[k] <= 0:
                count += 1
        if count == len(dicts):
            print("ok! [{}, {}]".format(0, end))

            d = pairs[end][1] - pairs[0][1]
            if d < distance:
                distance = d
                min_pair = (pairs[0][1], pairs[end][1])
                print("new distance {}. min pair: ({}, {})".format(distance, pairs[0][1], pairs[end][1]))

        for end in range(1, len(pairs)):
            dicts[pairs[end][0]] -= 1
            count = 0
            for k in dicts:
                if dicts[k] <= 0:
                    count += 1
            if count == len(dicts):
                print("ok! [{}, {}]".format(0, end))

                d = pairs[end][1] - pairs[0][1]
                if d < distance:
                    distance = d
                    min_pair = (pairs[0][1], pairs[end][1])
                    print("new distance {}. min pair: ({}, {})".format(distance, pairs[0][1], pairs[end][1]))

                break
        print("end: {}".format(end))

        for start in range(1, len(pairs)):
            dicts[pairs[start-1][0]] += 1

            count = 0
            for k in dicts:
                if dicts[k] <= 0:
                    count += 1
            if count == len(dicts):
                print("ok! [{}, {}]".format(start, end))

                d = pairs[end][1] - pairs[start][1]
                if d < distance:
                    distance = d
                    min_pair = (pairs[start][1], pairs[end][1])
                    print("new distance {}. min pair: ({}, {})".format(distance, pairs[start][1], pairs[end][1]))

                continue
            else:
                while end+1 < len(pairs):
                    end += 1
                    dicts[pairs[end][0]] -= 1

                    count = 0
                    for k in dicts:
                        if dicts[k] <= 0:
                            count += 1
                    if count == len(dicts):
                        print("ok! [{}, {}]".format(start, end))

                        d = pairs[end][1] - pairs[start][1]
                        if d < distance:
                            distance = d
                            min_pair = (pairs[start][1], pairs[end][1])
                            print("new distance {}. min pair: ({}, {})".format(distance, pairs[start][1], pairs[end][1]))

                        break

        return s[min_pair[0]:min_pair[1]+1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow("ab", "a"))
    # print(sol.minWindow("a", "b"))
    # print(sol.minWindow("a", "aa"))
    # print(sol.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))
    # print(sol.minWindow("ADDBECODEBANC", "ABC"))
