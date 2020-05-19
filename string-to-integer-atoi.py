# -*- coding: utf-8 -*-

"""8. 字符串转换整数 (atoi)(https://leetcode-cn.com/problems/string-to-integer-atoi/)
"""


class Solution:

    def myAtoi(self, s: str) -> int:
        n = 0
        b = ord('0')
        digit = False
        negative = None
        prev = ''
        empty = ['', ' ']
        for c in s:
            if c == ' ':
                if prev not in empty:
                    break
            elif c in ['-', '+']:
                if prev not in empty:
                    break
                if negative is not None:
                    break
                negative = c == '-'
                prev = c
            elif '0' <= c <= '9':
                prev = c
                if c == '0' and not digit:
                    continue
                digit = True
                ch = ord(c) - b
                n = n * 10 + ch
            else:
                break
        if negative:
            n = max(-n, -2 ** 31)
        else:
            n = min(n, 2 ** 31 - 1)
        return n


if __name__ == '__main__':
    print(Solution().myAtoi('0-1'))
    print(Solution().myAtoi('   +0 123'))
    print(Solution().myAtoi('   +041 123'))
    print(Solution().myAtoi('-000000000000001'))
    print(Solution().myAtoi('  0000000000012345678'))
    print(Solution().myAtoi('+1'))
    print(Solution().myAtoi('+01234'))
    print(Solution().myAtoi('   +004500'))
    print(Solution().myAtoi('888'))
    print(Solution().myAtoi('   -42'))
    print(Solution().myAtoi('   --42'))
    print(Solution().myAtoi('4193 with words'))
    print(Solution().myAtoi('words and 987'))
    print(Solution().myAtoi('-91283472332'))
