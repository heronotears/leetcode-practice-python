# -*- coding: utf-8 -*-

"""20. 有效的括号(https://leetcode-cn.com/problems/valid-parentheses/)
"""

import unittest
from typing import List


class Solution:

    def isValid(self, s: str) -> bool:
        parentheses = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack: List[str] = []
        for c in s:
            if c in parentheses.values():
                stack.append(c)
            elif c in parentheses.keys() and not (stack and parentheses[c] == stack.pop()):
                return False
        return not stack


class TestSolution(unittest.TestCase):

    def test_isValid(self):
        inputs = [
            '()[]{}',
            '(]'
        ]
        outputs = [
            True,
            False
        ]
        result = [Solution().isValid(v) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
