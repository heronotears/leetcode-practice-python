# -*- coding: utf-8 -*-

"""88. 合并两个有序数组(https://leetcode-cn.com/problems/merge-sorted-array/)
"""

import unittest
from typing import List


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        last = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[last] = nums2[p2]
                p2 -= 1
            else:
                nums1[last] = nums1[p1]
                p1 -= 1
            last -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]


class TestCase(unittest.TestCase):

    def test_merge(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        inputs = [
            [nums1, 3, [1, 2, 3], 3]
        ]
        outputs = [1, 2, 3, 4, 5, 6]
        [Solution().merge(*v) for v in inputs]
        self.assertEqual(nums1, outputs)


if __name__ == '__main__':
    unittest.main()
