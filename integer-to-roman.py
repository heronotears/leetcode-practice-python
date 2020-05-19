# -*- coding: utf-8 -*-

"""12. 整数转罗马数字(https://leetcode-cn.com/problems/integer-to-roman/)
"""


class Solution:

    def intToRoman(self, num: int) -> str:
        number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        bucket = []
        for i, n in enumerate(number):
            if num < n:
                continue
            r, num = divmod(num, n)
            if r:
                bucket.append(roman[i] * r)
            if num == 0:
                break
        return ''.join(bucket)


if __name__ == '__main__':
    print(Solution().intToRoman(3))
    print(Solution().intToRoman(4))
    print(Solution().intToRoman(9))
    print(Solution().intToRoman(58))
    print(Solution().intToRoman(1900))
    print(Solution().intToRoman(1994))
