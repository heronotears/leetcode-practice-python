# -*- coding: utf-8 -*-

"""145. 二叉树的后序遍历(https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)
"""

import unittest
from typing import Generator, List

from utils import TreeNode


class Solution:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return list(self.__postorderTraversal(root))

    def __postorderTraversal(self, root: TreeNode) -> Generator[int, None, None]:
        stack: List[TreeNode] = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left or root.right
            elif stack:
                n = stack.pop()
                yield n.val
                root = stack[-1].right if stack and stack[-1].left == n else None


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
            [9, 15, 7, 20, 3]
        ]
        result = [Solution().postorderTraversal(v) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
