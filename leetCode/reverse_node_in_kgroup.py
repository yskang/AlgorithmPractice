# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 1:
            return head
        ans = None
        last = None
        current = head
        while current.next:
            front, end = self.reverse_k(current, k)
            if not front and not end:
                break
            last = front
            current = end.next
        return ans
            


def main():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    sol = Solution()
    sol.reverseKGroup(node_1, 2)


if __name__ == "__main__":
    main()