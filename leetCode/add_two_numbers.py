# Title: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem:
    def add_two_numbers(self, l1, l2):
        addends = l1, l2
        dummy = end = ListNode(0)
        carry = 0
        while addends or carry:
            carry += sum(a.val for a in addends)
            addends = [a.next for a in addends if a.next]
            end.next = end = ListNode(carry % 10)
            carry //= 10
        return dummy.next

    def add_two_numbers_2(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n // 10)
            return node
        return tolist(toint(l1) + toint(l2))

    def add_two_numbers_3(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        n = toint(l1) + toint(l2)
        first = last = ListNode(n % 10)
        while n > 9:
            n //= 10
            last.next = last = ListNode(n % 10)
        return first



def solution():
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(9, ListNode(7, ListNode(5)))

    problem = Problem()
    return problem.add_two_numbers(l1, l2)


def main():
    print(solution())


if __name__ == '__main__':
    main()