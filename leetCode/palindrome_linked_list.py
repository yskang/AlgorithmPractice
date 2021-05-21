# Title: Palindrome Linked List
# Link: https://leetcode.com/problems/palindrome-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, ns: list):
        self.ns = ns
        self.head = ListNode(ns[0])
        self.head.next = None
        self.pointer = self.head
        
        for n in ns[1:]:
            self.node = ListNode(n)
            self.node.next = None
            self.pointer.next = self.node
            self.pointer = self.node

    def get_head(self):
        return self.head


class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        buffer = []
        node = head
        while node.next:
            buffer.append(node.val)
            node = node.next
        buffer.append(node.val)
        
        for i, val in enumerate(buffer):
            if val != buffer[-(i+1)]:
                return False
        return True
    
    def is_palindrome_two(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev




def problem():
    linked_list = LinkedList([1, 2, 3, 4, 5])
    head = linked_list.get_head()
    node = head
    while node.next:
        node = node.next

    solution = Solution()
    return solution.is_palindrome_two(head)


def main():
    print(problem())


if __name__ == '__main__':
    main()