# -*- coding: utf-8 -*-

"""75. 颜色分类(https://leetcode-cn.com/problems/sort-colors/solution/yan-se-fen-lei-by-leetcode/)
"""

import unittest
from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        curr = 0
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


class TestCase(unittest.TestCase):

    def test_sortColors(self):
        inputs = [
            [2, 0, 2, 1, 1, 0],
            [1, 0, 0, 1, 1, 0]
        ]
        outputs = [
            [0, 0, 1, 1, 2, 2],
            [0, 0, 0, 1, 1, 1]
        ]
        [Solution().sortColors(v) for v in inputs]
        self.assertSequenceEqual(inputs, outputs)


if __name__ == '__main__':
    unittest.main()
