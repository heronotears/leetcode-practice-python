# -*- coding: utf-8 -*-

"""912. 排序数组(归并排序)(https://leetcode-cn.com/problems/sort-an-array/)
"""

import unittest
from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def mergeSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        mid = n // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        ret = []
        while left and right:
            if left[0] <= right[0]:
                ret.append(left.pop(0))
            else:
                ret.append(right.pop(0))
        left and ret.extend(left)
        right and ret.extend(right)
        return ret


class TestSolution(unittest.TestCase):

    def test_sortArray(self):
        inputs = [
            [78, 17, 39, 26, 72, 94, 21, 12, 23, 68],
            [1, 4, 6, 3, 8, 2],
            [2, 8, 4, 1, 3, 5, 6, 7]
        ]
        outputs = [sorted(v) for v in inputs]
        result = [Solution().sortArray(list(v)) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
