import bisect

class Solution(object):
    def countSmaller(self, nums):
        smallers = []
        enumerated_nums = list(enumerate(nums))
        sorted_pair = sorted(list(enumerate(nums)), key=lambda x: x[1])
        index_of_pair = {}

        for i in range(len(sorted_pair)):
            index_of_pair[sorted_pair[i]] = i

        for p in enumerated_nums:
            smallers.append(index_of_pair[p])
            for k in range(index_of_pair[p]+1, len(sorted_pair)):
                index_of_pair[sorted_pair[k]] -= 1
            sorted_pair = sorted_pair[:smallers[-1]] + sorted_pair[smallers[-1]+1:]

        return smallers

    def second_solution(self, nums):
        def sort(enum):
            half = int(len(enum) / 2)
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    def third_solution(self, nums):
        s = sorted(nums)
        c = []
        for n in nums:
            p = bisect.bisect_left(s, n)
            c.append(p)
            s.pop(p)
        return c

    def merge_sort(self, nums):
        half = int(len(nums)/2)
        if half > 0:
            left, right = self.merge_sort(nums[:half]), self.merge_sort(nums[half:])
            for i in range(len(nums))[::-1]:
                if not right or left and left[-1] > right[-1]:
                    nums[i] = left.pop()
                else:
                    nums[i] = right.pop()
        return nums



if __name__ == "__main__":
    sol = Solution()
    print(sol.countSmaller([5, 2, 6, 1, 2, 5]))
    print(sol.countSmaller([-1, -1]))
    print(sol.second_solution([-2, 2, 3, 4, 63, 3, 4, 5]))
    print(sol.merge_sort([-2, 2, 3, 4, 63, 3, 4, 5]))
