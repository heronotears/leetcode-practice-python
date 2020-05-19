# -*- coding: utf-8 -*-

"""5. 最长回文子串(https://leetcode-cn.com/problems/longest-palindromic-substring/)
"""

from typing import Tuple


class Solution:

    def longestPalindrome(self, s: str) -> str:
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


if __name__ == '__main__':
    print(Solution().longestPalindrome(''))
    print(Solution().longestPalindrome('a'))
    print(Solution().longestPalindrome('ac'))
    print(Solution().longestPalindrome('kk'))
    print(Solution().longestPalindrome('cbbd'))
    print(Solution().longestPalindrome('babad'))
    print(Solution().longestPalindrome('wwabcdefgfedcbavv'))
    print(Solution().longestPalindrome('abcdefg'))
