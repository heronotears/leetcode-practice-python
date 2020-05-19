# -*- coding: utf-8 -*-

"""4. 寻找两个正序数组的中位数(https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)
"""

import sys
from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        k1, k2 = (l1 + l2 + 1) // 2, (l1 + l2 + 2) // 2
        n1 = self.findMinK(nums1, nums2, k1)
        n2 = self.findMinK(nums1, nums2, k2)
        return (n1 + n2) / 2.0

    @classmethod
    def findMinK(cls, nums1: List[int], nums2: List[int], k: int) -> int:
        while True:
            if k == 1:
                return min(cls.check(nums1, 0), cls.check(nums2, 0))
            n = k // 2
            x1 = cls.check(nums1, n - 1)
            x2 = cls.check(nums2, n - 1)
            if x1 < x2:
                nums1 = nums1[n:]
            else:
                nums2 = nums2[n:]
            k -= n

    @staticmethod
    def check(a, i):
        return a[i] if len(a) > i else sys.maxsize


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1], [2, 3, 4, 5, 6]))
    print(Solution().findMedianSortedArrays([1, 3], [2]))
