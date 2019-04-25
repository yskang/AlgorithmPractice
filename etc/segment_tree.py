class Segment_Tree:
    '''
    A Class used to get partial sum of an array and update data
    ...
    Attributes
    ----------
    array : list
        a list which to make a segment tree

    Methods
    -------
    init(tree, start, end, node)
        make segment tree from the array. don't call this method directly.
    sum(left, right, node=1, start=0, end=-1)
        return the partial sum of the array.
    update(index, diff, node=1, start=0, end=-1)
        update the value of the index of array as +diff.
    '''

    def __init__(self, array):
        '''
        Parameters
        ----------
        array : list
            the array that you want to make tree
        '''
        self.array = array
        self.tree = [0 for _ in range(len(self.array) * 4)]
        self.init(self.tree, 0, len(self.array)-1, 1)
        self.last_index = len(array)-1

    def init(self, tree, start, end, node):
        '''
        Don't Call This Method Directly
        '''        
        if start == end:
            tree[node] = self.array[start]
            return tree[node]
        mid = (start + end) // 2
        tree[node] = self.init(tree, start, mid, node * 2) + self.init(tree, mid + 1, end, node * 2 + 1)
        return tree[node]

    def sum(self, left, right, node=1, start=0, end=-1):
        '''
        Parameters
        ----------
        left : int
            start index of the part [left, left+1, left+2 .. right-2, right-1, right]
        right : int
            end index of the part [left, left+1, left+2 .. right-2, right-1, right]
        '''
        if end == -1:
            end = self.last_index
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        return self.sum(left, right, node*2, start, (start+end)//2) + self.sum(left, right, node*2+1, (start+end)//2+1, end)

    def update(self, index, diff, node=1, start=0, end=-1):
        '''
        Parameters
        ----------
        index: int
            the index of array. which you want to update value
        diff: int
            the amount of value which you wnat to add. if you want to make 4 to 10, put diff to 6
        '''

        if end == -1:
            end = self.last_index
        if not(start <= index <= end):
            return
        self.tree[node] += diff
        if start != end:
            self.update(index, diff, node*2, start, (start+end)//2)
            self.update(index, diff, node*2+1, (start+end)//2+1, end)


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
    # tree = [0 for _ in range(len(a) * 4)]
    # tree2 = [0 for _ in range(len(a) * 4)]
    # init_segment_sum(a, tree, 0, 11)
    # print('a: {}'.format(a))
    # print('segment tree(sum): {}'.format(tree))
    # print('partial sum of (3~9): {}'.format(segment_sum(tree, 1, 0, 11, 3, 9)))
    # print('update a[3] to 8')
    # update(tree, 1, 0, 11, 3, 1)
    # print('segment tree(sum): {}'.format(tree))
    # print('partial sum of (3~9): {}'.format(segment_sum(tree, 1, 0, 11, 3, 9)))

    segment = Segment_Tree(a)
    print(segment.sum(3, 9))
    segment.update(3, 1)
    print(segment.sum(3, 9))
