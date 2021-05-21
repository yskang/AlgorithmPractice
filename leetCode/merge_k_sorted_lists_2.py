# Title: Merge k Sorted Lists
# Link: https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem:
    def merge_k_lists(self, lists: List) -> ListNode:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        l = len(lists) // 2
        return self.merge_two_lists(self.merge_k_lists(lists[:l]), self.merge_k_lists(lists[l:]))
  
    def merge_two_lists(self, l1: list, l2: list) -> ListNode:
        if not l1 or l2 and l1.val > l2.val:
            l1, l2 = l2, l1
        if l1:
            l1.next = self.merge_two_lists(l1.next, l2)
        return l1


def solution():
    lists = []
    problem = Problem()
    return problem.merge_k_lists(lists)


def main():
    print(solution())


if __name__ == '__main__':
    main()