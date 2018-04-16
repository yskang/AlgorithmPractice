class Solution(object):
    def countSmaller(self, nums):
        smallers = []
        enumerated_nums = list(enumerate(nums))
        sorted_pair = sorted(list(enumerate(nums)), key=lambda x: x[1])
        index_of_pair = {}

        for i in range(len(sorted_pair)):
            index_of_pair[sorted_pair[i]] = i

        # print(enumerated_nums)
        # print(sorted_pair)
        # print(index_of_pair)

        for p in enumerated_nums:
            # print("for ", p)
            smallers.append(index_of_pair[p])
            # print("append ", index_of_pair[p], " index of pair", p)
            #
            # print("reduce indexes over me")
            for k in range(index_of_pair[p]+1, len(sorted_pair)):
                index_of_pair[sorted_pair[k]] -= 1
            #     print("for ", k)
            #     print(index_of_pair)
            #
            # print("remove ", smallers[-1], "th element")
            # print("sorted:", sorted_pair)
            sorted_pair = sorted_pair[:smallers[-1]] + sorted_pair[smallers[-1]+1:]
            # print("sorted:", sorted_pair)

        return smallers


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSmaller([5, 2, 6, 1, 2, 5]))
    print(sol.countSmaller([-1, -1]))
