# -*- coding: utf-8 -*-

"""105. 从前序与中序遍历序列构造二叉树(https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
"""

import unittest
from typing import List, Optional

from utils import TreeNode


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root

    def buildTree_Loop(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not (preorder and inorder):
            return
        root = TreeNode(preorder[0])
        stack: List[TreeNode] = [root]
        index = 0
        for v in preorder[1:]:
            node = TreeNode(v)
            top = stack[-1]
            if top.val != inorder[index]:
                top.left = node
            else:
                while stack and stack[-1].val == inorder[index]:
                    top = stack.pop()
                    index += 1
                top.right = node
            stack.append(node)
        return root


class TestCase(unittest.TestCase):

    def test_buildTree(self):
        inputs = [
            [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
            [[3, 9, 8, 5, 4, 10, 20, 15, 7], [4, 5, 8, 10, 9, 3, 15, 20, 7]]
        ]
        T1 = TreeNode(3)
        T1.left = TreeNode(9)
        T1.right = TreeNode(20)
        T1.right.left = TreeNode(15)
        T1.right.right = TreeNode(7)

        T2 = TreeNode(3)
        T2.left = TreeNode(9)
        T2.right = TreeNode(20)
        T2.left.left = TreeNode(8)
        T2.left.left.left = TreeNode(5)
        T2.left.left.right = TreeNode(10)
        T2.left.left.left.left = TreeNode(4)
        T2.right.left = TreeNode(15)
        T2.right.right = TreeNode(7)

        outputs = [T1, T2]
        result = [Solution().buildTree(*v) for v in inputs]
        result_loop = [Solution().buildTree_Loop(*v) for v in inputs]
        self.assertEqual(result, outputs)
        self.assertEqual(result_loop, outputs)


if __name__ == '__main__':
    unittest.main()
