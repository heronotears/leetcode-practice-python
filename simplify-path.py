# -*- coding: utf-8 -*-

"""71. 简化路径(https://leetcode-cn.com/problems/simplify-path/)
"""

import unittest
from typing import List


class Solution:

    def simplifyPath(self, path: str) -> str:
        stack: List[str] = []
        p = filter(None, path.split('/'))
        for v in p:
            if v == '.':
                continue
            if v == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(v)
        return '/' + '/'.join(stack)


class TestSolution(unittest.TestCase):

    def test_simplifyPath(self):
        inputs = [
            '/home/',
            '/../',
            '/home//foo/',
            '/a/./b/../../c/',
            '/a/../../b/../c//.//',
            '/a//b////c/d//././/..'
        ]
        outputs = [
            '/home',
            '/',
            '/home/foo',
            '/c',
            '/c',
            '/a/b/c'
        ]
        result = [Solution().simplifyPath(v) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
