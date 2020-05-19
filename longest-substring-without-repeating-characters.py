# -*- coding: utf-8 -*-

"""3. 无重复字符的最长子串(https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        left = 0
        answer = 0
        for i, c in enumerate(s):
            if c in index:
                left = max(left, index[c] + 1)
            answer = max(answer, i - left + 1)
            index[c] = i
        return answer


if __name__ == '__main__':
    input = ['abaab', 'abcabcbb', 'pwwkew', 'bbbbb']
    for v in input:
        output = Solution().lengthOfLongestSubstring(v)
        print(f'{v}: {output}')
