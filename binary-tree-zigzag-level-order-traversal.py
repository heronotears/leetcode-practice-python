# -*- coding: utf-8 -*-

"""103. 二叉树的锯齿形层次遍历(https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)
"""

import unittest
from typing import Generator, List

from utils import TreeNode, list2tree


class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        return list(self.__zigzagLevelOrder(root))

    def __zigzagLevelOrder(self, root: TreeNode) -> Generator[List[int], None, None]:
        stack: List[TreeNode] = [root]
        level: List[int] = []
        reverse = 0
        while stack:
            size = len(stack)
            for _ in range(size):
                node = stack.pop(0)
                level.append(node.val)
                node.left and stack.append(node.left)
                node.right and stack.append(node.right)
            if level:
                if reverse:
                    level.reverse()
                yield level
                level = []
            reverse ^= 1


class TestSolution(unittest.TestCase):

    def test_zigzagLevelOrder(self):
        inputs = [
            list2tree([3, 9, 20, None, None, 15, 7]),
            list2tree([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])
        ]
        outputs = [
            [[3], [20, 9], [15, 7]],
            [[0], [4, 2], [1, 3, -1], [8, 6, 1, 5]]
        ]
        result = [Solution().zigzagLevelOrder(v) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
