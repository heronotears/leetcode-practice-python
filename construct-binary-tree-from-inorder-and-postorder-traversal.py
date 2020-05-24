# -*- coding: utf-8 -*-

"""106. 从中序与后序遍历序列构造二叉树(https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
"""

import unittest
from typing import List, Optional

from utils import TreeNode


class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        return root


class TestCase(unittest.TestCase):

    def test_buildTree(self):
        inputs = [
            [[9, 3, 15, 20, 7], [9, 15, 7, 20, 3]]
        ]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        outputs = [root]
        result = [Solution().buildTree(*v) for v in inputs]
        self.assertEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
