class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        lists = list(filter(lambda node: node != None, lists))

        result_node = ListNode(0)
        current_node = result_node
        sorted_list = []
        for list_node in lists:
            sorted_list.append(list_node)

        sorted_list = sorted(sorted_list, key=lambda list_node: list_node.val, reverse=True)

        while sorted_list:
            popped_node = sorted_list.pop()
            new_node = ListNode(popped_node.val)
            current_node.next = new_node
            current_node = new_node
            popped_node = popped_node.next

            if popped_node is not None:
                if not sorted_list:
                    current_node.next = popped_node
                    break
                for i in range(len(sorted_list) - 1, -1, -1):
                    if sorted_list[i].val >= popped_node.val:
                        sorted_list.insert(i + 1, popped_node)
                        break
                    if i == 0:
                        sorted_list.insert(0, popped_node)

        return result_node.next



if __name__ == '__main__':
    n_1 = ListNode(1)
    n_1_2 = ListNode(1)
    n_2 = ListNode(2)
    n_3 = ListNode(3)
    n_4 = ListNode(4)
    n_4_2 = ListNode(4)
    n_5 = ListNode(5)
    n_6 = ListNode(6)

    n_1.next = n_4
    n_4.next = n_5

    n_1_2.next = n_3
    n_3.next = n_4_2

    n_2.next = n_6

    ls = [n_6, None]

    sol = Solution()
    ans = sol.mergeKLists(ls)
    ans_vals = []

    while ans is not None:
        ans_vals.append(str(ans.val))
        ans = ans.next

    print("->".join(ans_vals))

