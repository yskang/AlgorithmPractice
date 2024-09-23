#
# @lc app=leetcode id=2251 lang=python3
#
# [2251] Number of Flowers in Full Bloom
#
from typing import List

class RUPQ():

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        self.bit_tree = [0] * (self.n + 1)
        self.construct_bit_tree()

    def update_bit(self, index, val):
        index = index + 1
        while (index <= self.n):
            self.bit_tree[index] += val
            index += index & (-index)

    def construct_bit_tree(self):
        for i in range(self.n):
            self.update_bit(i, self.arr[i])

    def get_sum(self, index):
        sum_values = 0
        index = index + 1
        while (index > 0):
            sum_values += self.bit_tree[index]
            index -= index & (-index)
        return sum_values

    def update(self, left, right, value):
        self.update_bit(left, value)
        self.update_bit(right + 1, -value)


# @lc code=start
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        all_index = set()
        for start, end in flowers:
            all_index.add(start)
            all_index.add(end)
        for person in people:
            all_index.add(person)
        all_index = sorted(list(all_index))
        index_map = {index: i for i, index in enumerate(all_index)}
        rupq = RUPQ([0] * len(all_index))
        for start, end in flowers:
            rupq.update(index_map[start], index_map[end], 1)
        ans = []
        for person in people:
            ans.append(rupq.get_sum(index_map[person]))
        return ans
# @lc code=end


def main():
    sol = Solution()
    ans = sol.fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2, 3, 7, 11])
    print(ans)


if __name__ == "__main__":
    main()