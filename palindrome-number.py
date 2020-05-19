# -*- coding: utf-8 -*-

"""9. 回文数(https://leetcode-cn.com/problems/palindrome-number/)
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev_num = 0
        while x > rev_num:
            x, q = divmod(x, 10)
            rev_num = rev_num * 10 + q
        return x == rev_num or x == rev_num // 10

    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        dq = []
        while x:
            x, q = divmod(x, 10)
            dq.append(q)
        while dq and len(dq) > 1:
            if dq.pop(0) != dq.pop():
                return False
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(10))
    print(Solution().isPalindrome(123456754321))
