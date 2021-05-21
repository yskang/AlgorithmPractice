# Title: Array Partition 1
# Link: https://leetcode.com/problems/array-partition-i/


class Solution:
    def array_pair_sum(self, nums: list) -> int:
        nums = sorted(nums)
        s = 0
        for i in range(0, len(nums), 2):
            s += nums[i]
        return s


def solution():
    nums = [1,4,3,2]

    sol = Solution()
    return sol.array_pair_sum(nums)


def main():
    print(solution())


if __name__ == '__main__':
    main()