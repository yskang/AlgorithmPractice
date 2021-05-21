# Title: Swap Nodes in Pairs
# Link: https://leetcode.com/problems/swap-nodes-in-pairs

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Problem:
    def swap_pairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next    


def solution():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    problem = Problem()
    return problem.swap_pairs(head)


def main():
    print(solution())


if __name__ == '__main__':
    main()