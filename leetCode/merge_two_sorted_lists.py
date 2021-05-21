# Title: Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem:
    def merge_two_lists(self, l1: list, l2: list) -> ListNode:
        if l1 and l2:
            if l2.val < l1.val:
                l1, l2 = l2, l1
            l1.next = self.merge_two_lists(l1.next, l2)
        return l1 or l2

    def merge_two_lists_2(self, l1: list, l2: list) -> ListNode:
        if not l1 or l2 and l1.val > l2.val:
            l1, l2 = l2, l1
        if l1:
            l1.next = self.merge_two_lists_2(l1.next, l2)
        return l1


def solution():
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    problem = Problem()
    return problem.merge_two_lists(l1, l2)


def main():
    print(solution())


if __name__ == '__main__':
    main()