# Title: Odd Even Linked List
# Link: https://www.acmicpc.net/problem/list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def odd_evenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head


def solution():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    return sol.odd_evenList(head)


def main():
    print(solution())


if __name__ == '__main__':
    main()