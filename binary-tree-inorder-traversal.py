# -*- coding: utf-8 -*-

"""94. 二叉树的中序遍历(https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
"""

import unittest
from typing import Generator, List

from utils import TreeNode


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return list(self.__inorderTraversal(root))

    def __inorderTraversal(self, root: TreeNode) -> Generator[int, None, None]:
        stack: List[TreeNode] = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                node = stack.pop()
                yield node.val
                root = node.right

    def __inorderTraversal_2(self, root: TreeNode) -> List[int]:
        """优化右节点的出入栈次数"""
        stack: List[TreeNode] = []
        while root or stack:
            if root:
                if root.left:
                    stack.append(root)
                    root = root.left
                else:
                    yield root.val
                    root = root.right
                continue
            if stack:
                node = stack.pop()
                yield node.val
                root = node.right


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
            [9, 3, 15, 20, 7]
        ]
        result = [list(Solution().inorderTraversal(v)) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
