# -*- coding: utf-8 -*-

"""5. 最长回文子串(https://leetcode-cn.com/problems/longest-palindromic-substring/)
"""

import unittest
from typing import Tuple


class Solution:

    def longestPalindrome(self, s: str) -> str:
        """中心扩展解法"""
        pos = (0, 0)
        j = 0
        n = len(s)
        while j < n:
            p1 = self.expand_around_center(s, j - 1, j + 1)
            p2 = self.expand_around_center(s, j, j + 1)
            d1 = p1[1] - p1[0]
            d2 = p2[1] - p2[0]
            if d2 or d1:
                x = p2 if d2 > d1 else p1
                if (pos[1] - pos[0]) < (x[1] - x[0]):
                    pos = x
            j += 1
        return s[pos[0]: pos[1] + 1]

    @staticmethod
    def expand_around_center(s: str, left: int, right: int) -> Tuple[int, int]:
        L, R = 0, 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            L, R = left, right
            left -= 1
            right += 1
        return L, R

    def longestPalindrome_dp(self, s: str) -> str:
        """动态规划解法"""
        ls = len(s)
        dp = [[0] * ls for i in range(ls)]
        for i in range(ls):
            dp[i][i] = 1

        for j in range(ls):
            for i in range(j):
                dp[i][j] = int(s[i] == s[j])
                if j - i > 1:
                    dp[i][j] &= int(dp[i + 1][j - 1])

        ret = [0, 0]
        for i, arr in enumerate(dp):
            for j, r in enumerate(arr):
                if r and (j - i) > (ret[1] - ret[0]):
                    ret = [i, j]
        return s[ret[0]:ret[1] + 1]


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.inputs = [
            ['', ''],
            ['a', 'a'],
            ['ac', 'a'],
            ['kk', 'kk'],
            ['cbbd', 'bb'],
            ['babad', 'bab'],
            ['wwabcdefgfedcbavv', 'abcdefgfedcba']
        ]

    def test_longestPalindrome(self):
        for k, v in self.inputs:
            self.assertEqual(Solution().longestPalindrome(k), v)

    def test_longestPalindrome_dp(self):
        for k, v in self.inputs:
            self.assertEqual(Solution().longestPalindrome_dp(k), v)


if __name__ == '__main__':
    unittest.main()
