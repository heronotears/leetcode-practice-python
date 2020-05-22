# -*- coding: utf-8 -*-

"""912. 排序数组(桶排序)(https://leetcode-cn.com/problems/sort-an-array/)
"""

import unittest
from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bucketSort(nums, 10)

    def bucketSort(self, nums: List[int], size: int) -> List[int]:
        if len(nums) <= 1:
            return nums
        n_min = min(nums)
        n_max = max(nums)
        n = (n_max - n_min) // size + 1
        bucket = [[] for _ in range(n)]
        for v in nums:
            i = (v - n_min) // size
            bucket[i].append(v)

        ret = []
        for b in bucket:
            if not b:
                continue
            if len(b) == 1:
                ret.extend(b)
            else:
                if n == 1:
                    size -= 1
                ret.extend(self.bucketSort(b, size))
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
