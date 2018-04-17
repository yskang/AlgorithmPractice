import bisect


class Solution(object):
    def first_solution(self, nums, k):
        if not nums:
            return []
        result = []

        for i in range(0, len(nums) - k + 1):
            result.append(max(nums[i:i + k]))

        return result

    def second_solution(self, nums, k):
        if not nums:
            return []

        windowed = sorted(nums[0:k])
        result = [windowed[-1]]

        for i in range(0, len(nums) - k):
            windowed.remove(nums[i])
            j = bisect.bisect_left(windowed, nums[i + k])
            windowed = windowed[:j] + [nums[i + k]] + windowed[j:]
            result.append(windowed[-1])

        return result

    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []

        current_max = max(nums[0:k])
        result = [current_max]

        for i in range(0, len(nums)-k):
            if current_max == nums[i]:
                current_max = max(nums[i+1:i+1+k])
            else:
                if current_max < nums[i+k]:
                    current_max = nums[i+k]
            result.append(current_max)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([], 0))
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
