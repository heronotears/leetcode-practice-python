# -*- coding: utf-8 -*-

"""912. 排序数组(快速排序)(https://leetcode-cn.com/problems/sort-an-array/)
"""

import random
import unittest
from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return
        mid = self.partition(nums, left, right)
        self.quickSort(nums, left, mid - 1)
        self.quickSort(nums, mid + 1, right)

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]
        i = left - 1
        for j in range(left, right):
            if nums[j] < nums[right]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i


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
