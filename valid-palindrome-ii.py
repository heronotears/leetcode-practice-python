# -*- coding: utf-8 -*-

"""680. 验证回文字符串 Ⅱ(https://leetcode-cn.com/problems/valid-palindrome-ii/)
"""

class Solution:

    def __init__(self):
        self.delete = 0

    def validPalindrome(self, s: str) -> bool:
        """子循环解法"""
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return (self.sub_validPalindrome(s, left + 1, right) or
                        self.sub_validPalindrome(s, left, right - 1))
        return True

    @staticmethod
    def sub_validPalindrome(s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome_recursion(self, s: str) -> bool:
        """递归解法"""
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if self.delete == 0: # 修改此处可实现最多删除 N 个字符 判断是否能够成为会问字符串
                    self.delete += 1
                    return (self.validPalindrome_recursion(s[left + 1: right + 1]) or
                            self.validPalindrome_recursion(s[left: right]))
                return False
        return True


if __name__ == '__main__':
    inputs = [
        'aba',
        'abca',
        'abdca',
        'eeccccbebaeeabebccceea',
        'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga'
    ]
    for v in inputs:
        r1 = Solution().validPalindrome(v)
        r2 = Solution().validPalindrome_recursion(v)
        print(f'{v} ==> {r1} ==> {r2}')
