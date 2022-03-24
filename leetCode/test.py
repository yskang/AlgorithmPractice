class ListNode(object):
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def set_hash(self, h):
        self.v_hash = h

    def get_hash_2(self):
        self.lowest_dot()
        self.next = self.


class Solution(object):
    def reverseList(self, head):

        next_node = head
        while next_node:
            before = next_node
            next_node = next_node.next
            if next_node == None:
                head = before
        return head


def print_ans(h):
    v = N
    while h:
        print(h, v, h.v_hash)
        v -= 1
        h = h.next
    return True

def verify_ans_reverse(h):
    v = N
    while h:
        if v != h.v_hash: return False
        v -= 1
        h = h.next
    return True

N = int(input())

head = None

for i in range(N):
    head = ListNode(i, head)

h = head
hash = 1

while h:
    h.set_hash(hash)
    hash += 1
    h = h.next


d = Solution().reverseList(head)

if verify_ans_reverse(d):
    print("passed!")
else:
    print("failed!")
    print_ans(d)

