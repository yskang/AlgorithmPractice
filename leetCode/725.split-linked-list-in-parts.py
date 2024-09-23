#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#
from typing import List, Optional


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = self.get_size(head)
        print(size)
        return []

    def get_size(self, head: Optional[ListNode]) -> int:
        size = 0
        while head:
            size += 1
            head = head.next
        return size


# @lc code=end
def main():
    sol = Solution()
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    head = [1,2,3]
    k = 5
    print(sol.splitListToParts(head, k))
    
    
if __name__ == '__main__':
    main()