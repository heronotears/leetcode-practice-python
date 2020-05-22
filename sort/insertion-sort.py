# -*- coding: utf-8 -*-

"""912. 排序数组(插入排序)(https://leetcode-cn.com/problems/sort-an-array/)
"""

import unittest
from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        self.insertionSort(nums)
        return nums

    def insertionSort(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(1, n):
            while i > 0:
                if nums[i] >= nums[i - 1]:
                    break
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1


class TestSolution(unittest.TestCase):

    def test_sortArray(self):
        input = [
            [78, 17, 39, 26, 72, 94, 21, 12, 23, 68],
            [1, 4, 6, 3, 8, 2],
            [2, 8, 4, 1, 3, 5, 6, 7]
        ]
        output = [sorted(v) for v in input]
        result = [Solution().sortArray(list(v)) for v in input]
        self.assertSequenceEqual(result, output)


if __name__ == '__main__':
    unittest.main()
