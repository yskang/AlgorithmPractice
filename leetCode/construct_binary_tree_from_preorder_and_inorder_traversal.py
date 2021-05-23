# Title: Construct Binary Tree from Preorder and Inorder Traversal
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from libs.leet_code_utils import Codec, TreeNode
from collections import defaultdict


class Problem:
    def __init__(self) -> None:
        self.preorder = []
        self.inorder = []
        self.len = 0
        self.get_idx = defaultdict(lambda: None)

    def buildTree_1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        idx = inorder.index(preorder[0])
        return TreeNode(preorder[0], self.buildTree(preorder[1:1+idx], inorder[:idx]), self.buildTree(preorder[1+idx:], inorder[idx+1:]))

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        self.preorder = preorder
        self.inorder = inorder
        self.len = len(preorder)

        for i, num in enumerate(inorder):
            self.get_idx[num] = i

        return self.build_tree(0, self.len-1, 0, self.len-1)
    
    def build_tree(self, pre_l: int, pre_r: int, in_l: int, in_r: int) -> TreeNode:
        if pre_r < pre_l or pre_l >= self.len:
            return None
        idx = self.get_idx[self.preorder[pre_l]] - in_l
        return TreeNode(self.preorder[pre_l], self.build_tree(pre_l+1, pre_l+idx, in_l, idx+in_l-1), self.build_tree(pre_l+idx+1, pre_r, idx+in_l+1, in_r))


def solution():
    preorder = [1, 2, 3, 4]
    inorder = [1, 2, 3, 4]
    problem = Problem()
    return problem.buildTree(preorder, inorder)


def main():
    codec = Codec()
    print(codec.serialize(solution()))


if __name__ == '__main__':
    main()