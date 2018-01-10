# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersect(selfself, head):
        tortois = head
        hare = head

        while hare is not None and hare.next is not None:
            tortois = tortois.next
            hare = hare.next.next
            if tortois is hare:
                return tortois
        return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        prt1 = head
        prt2 = intersect
        while prt1 != prt2:
            prt1 = prt1.next
            prt2 = prt2.next

        return prt1


sol = Solution()
sol.detectCycle(None)