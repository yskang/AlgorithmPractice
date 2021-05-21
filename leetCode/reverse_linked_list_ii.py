# Title: Reverse Linked List II
# Link: https://leetcode.com/problems/reverse-linked-list-ii/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem:
    def reverse_between(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        part = None
        n = n - m
        head_end, tail_head = None, None
        m -= 1

        while m:
            m -= 1
            head_end = cur
            cur = cur.next
        part = cur

        while n:
            n -= 1
            cur = cur.next
        tail_head = cur.next
        cur.next = None

        part = self._rev(part, tail_head)

        if head_end:
            head_end.next = part
            return head
        return part

    def _rev(self, head: ListNode, taile: ListNode) -> ListNode:
        cur, rev = head, taile
        while cur.next:
            cur, rev, rev.next = cur.next, cur, rev
        cur, rev, rev.next = cur.next, cur, rev

        return rev


def solution():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    m = 1
    n = 4
    problem = Problem()
    return problem.reverse_between(head, m, n)


def main():
    print(solution())


if __name__ == '__main__':
    main()