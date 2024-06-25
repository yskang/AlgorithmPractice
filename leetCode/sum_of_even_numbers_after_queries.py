# Title: sum of even numbers after queries

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = 0
        sums = []

        for num in nums:
            if num % 2 == 0:
                ans += num

        for val, index in queries:
            is_even_num = nums[index] % 2 == 0
            is_even_val = val % 2 == 0
            if is_even_num and is_even_val:
                ans += val
            elif is_even_num and not is_even_val:
                ans -= nums[index]
            elif not is_even_num and not is_even_val:
                ans += nums[index] + val
            nums[index] += val
            sums.append(ans)
        return sums
