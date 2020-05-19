# -*- coding: utf-8 -*-

"""1. 两数之和(https://leetcode-cn.com/problems/two-sum/)
"""

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, n in enumerate(nums):
            another = target - n
            if another in mapping:
                return [mapping[another], i]
            else:
                mapping[n] = i
