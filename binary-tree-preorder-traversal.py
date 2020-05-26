# -*- coding: utf-8 -*-

"""144. 二叉树的前序遍历(https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)
"""

import unittest
from typing import Generator, List

from utils import TreeNode


class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return list(self.__preorderTraversal(root))

    def __preorderTraversal(self, root: TreeNode) -> Generator[int, None, None]:
        stack: List[TreeNode] = []
        while root:
            yield root.val
            if root.right:
                stack.append(root.right)
            root = root.left
            if not root and stack:
                root = stack.pop()


class TestSolution(unittest.TestCase):

    def test_preorderTraversal(self):
        T1 = TreeNode(3)
        T1.left = TreeNode(9)
        T1.right = TreeNode(20)
        T1.right.left = TreeNode(15)
        T1.right.right = TreeNode(7)
        inputs = [
            T1
        ]
        outputs = [
            [3, 9, 20, 15, 7]
        ]
        result = [Solution().preorderTraversal(v) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
