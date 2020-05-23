# -*- coding: utf-8 -*-

"""56. 合并区间(https://leetcode-cn.com/problems/merge-intervals/)
"""

import unittest
from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        merged = []
        prev = intervals[0]
        for v in intervals[1:]:
            if prev[1] < v[0]:
                merged.append(prev)
                prev = v
            else:
                prev = [prev[0], max(prev[1], v[1])]
        merged.append(prev)
        return merged


class TestCase(unittest.TestCase):

    def test_merge(self):
        inputs = [
            [[1, 4], [2, 3]],
            [[1, 4], [4, 5]],
            [[1, 3], [15, 18], [8, 10], [2, 6]]
        ]
        outputs = [
            [[1, 4]],
            [[1, 5]],
            [[1, 6], [8, 10], [15, 18]]
        ]
        result = [Solution().merge(v) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
