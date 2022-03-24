class Segment_Min_Tree:
    '''
    A Class used to get partial min of an array and update data
    ...
    Attributes
    ----------
    array : list
        a list which to make a segment tree

    Methods
    -------
    init(tree, start, end, node)
        make segment tree from the array. don't call this method directly.
    min(left, right, node=1, start=0, end=-1)
        return the partial min of the array.
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
            tree[node] = start
            return tree[node]
        mid = (start + end) // 2
        left = self.init(tree, start, mid, node * 2)
        right = self.init(tree, mid + 1, end, node * 2 + 1)
        if self.array[left] < self.array[right]:
            tree[node] = left
        else:
            tree[node] = right
        return tree[node]

    def min(self, left, right, node=1, start=0, end=-1):
        '''
        Parameters
        ----------
        left : int
            start index of the part [left, left+1, left+2 .. right-2, right-1, right]
        right : int
            end index of the part [left, left+1, left+2 .. right-2, right-1, right]
        
        Returns
        -------
        int
            a minimum value of the part of the array. min([left, left+1, left+2 .. right-2, right-1, right])
        '''
        if end == -1:
            end = self.last_index        
        if left > end or right < start:
            return -1
        if left <= start and end <= right:
            return self.tree[node]
        left_index = self.min(left, right, node*2, start, (start+end)//2)
        right_index = self.min(left, right, node*2+1, (start+end)//2+1, end)
        if left_index == -1 and right_index == -1:
            return -1
        elif left_index == -1:
            return right_index
        elif right_index == -1:
            return left_index
        else:
            if self.array[left_index] < self.array[right_index]:
                return left_index
            return right_index



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
    a = [3, -1, 6, 7, 2, -2, 4, 5, 2, 8, 1, 5]

    segment = Segment_Min_Tree(a)
    print(segment.min(0, 11))
