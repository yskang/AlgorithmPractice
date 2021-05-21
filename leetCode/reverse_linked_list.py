# Title: Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Problem:
    def reverse_list(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
            return prev

    def reverse_list_recursion(self, head: ListNode) -> ListNode:
        return self._reverse(head)
    
    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)



def solution():
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    node = head.next
    node.next = ListNode(val=3)ㅖ
   
    problem = Problem()
    return problem.reverse_list(head)


def main():
    print(solution())


if __name__ == '__main__':
    main()