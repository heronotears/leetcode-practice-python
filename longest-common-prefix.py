# -*- coding: utf-8 -*-

"""14. 最长公共前缀(https://leetcode-cn.com/problems/longest-common-prefix/)
"""

from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = []
        for v in zip(*strs):
            if len(set(v)) == 1:
                answer.append(v[0])
        return ''.join(answer)


if __name__ == '__main__':
    input = [['flower','flow','flight'], ['dog','racecar','car']]
    for v in input:
        output = Solution().longestCommonPrefix(v)
        print(f'{v} ==> {output}')
