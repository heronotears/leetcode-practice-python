# -*- coding: utf-8 -*-

"""179. 最大数(https://leetcode-cn.com/problems/largest-number/)
"""

import unittest
from typing import List


class LargerNumKey(str):

    def __lt__(x, y) -> bool:
        return x + y > y + x


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return largest_num.lstrip('0') or '0'


class TestSolution(unittest.TestCase):

    def test_largestNumber(self):
        inputs = [
            [10, 2],
            [3, 30, 34, 5, 9]
        ]
        outputs = [
            '210',
            '9534330'
        ]
        result = [Solution().largestNumber(v) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
