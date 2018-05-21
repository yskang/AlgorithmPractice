def init_segment_sum(array, tree, node, start, end):
    if start == end:
        tree[node] = array[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init_segment_sum(array, tree, node * 2, start, mid) + init_segment_sum(array, tree, node * 2 + 1,
                                                                                        mid + 1, end)
    return tree[node]


def sum(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return sum(tree, node*2, start, (start+end)//2, left, right) + sum(tree, node*2+1, (start+end)//2+1, end, left, right)


# init segment tree of an array from index start to end.
# return index of minimum value of array in range from start to end.
def init_segment_min(array, tree, node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    mid = (start + end) // 2
    left = init_segment_min(array, tree, node * 2, start, mid)
    right = init_segment_min(array, tree, node * 2 + 1, mid + 1, end)
    if array[left] < array[right]:
        tree[node] = left
    else:
        tree[node] = right
    return tree[node]


def find_min(array, tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    left_index = find_min(array, tree, node*2, start, (start+end)//2, left, right)
    right_index = find_min(array, tree, node*2+1, (start+end)//2+1, end, left, right)
    if left_index == -1 and right_index == -1:
        return -1
    elif left_index == -1:
        return right_index
    elif right_index == -1:
        return left_index
    else:
        if array[left_index] < array[right_index]:
            return left_index
        return right_index


if __name__ == '__main__':
    a = [3, 5, 6, 7, 2, 9, 4, 5, 2, 8, 1, 5]
    tree = [0 for _ in range(len(a) * 4)]
    tree2 = [0 for _ in range(len(a) * 4)]
    init_segment_sum(a, tree, 1, 0, 11)
    init_segment_min(a, tree2, 1, 0, 11)
    print(tree)
    print(tree2)
    print(sum(tree, 1, 0, 11, 3, 9))
    print(find_min(a, tree2, 1, 0, 11, 0, 9))
