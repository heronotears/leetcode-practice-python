# -*- coding: utf-8 -*-

"""102. 二叉树的层序遍历(https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
"""

import unittest
from typing import Generator, List

from utils import TreeNode, list2tree


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        return list(self.__levelOrder(root))

    def __levelOrder(self, root: TreeNode) -> Generator[List[int], None, None]:
        stack: List[TreeNode] = [root]
        level: List[int] = []
        while stack:
            size = len(stack)
            for _ in range(size):
                node = stack.pop(0)
                level.append(node.val)
                node.left and stack.append(node.left)
                node.right and stack.append(node.right)
            if level:
                yield level
                level = []


class TestSolution(unittest.TestCase):

    def test_levelOrder(self):
        inputs = [
            list2tree([3, 9, 20, None, None, 15, 7]),
            list2tree([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])
        ]
        outputs = [
            [[3], [9, 20], [15, 7]],
            [[0], [2, 4], [1, 3, -1], [5, 1, 6, 8]]
        ]
        result = [Solution().levelOrder(v) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
