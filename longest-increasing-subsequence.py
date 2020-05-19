# -*- coding: utf-8 -*-

"""300. 最长上升子序列(https://leetcode-cn.com/problems/longest-increasing-subsequence/)
"""

import bisect
from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = [nums[0]]
        for i in nums[1:]:
            if i > seq[-1]:
                seq.append(i)
            else:
                j = bisect.bisect_left(seq, i)
                if j == len(seq) - 1:
                    seq[j] = i
        return len(seq)


    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    inputs = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        # [10, 9, 2, 5, 3, 7, 101, 18, 4, 19],
        # [10, 9, 2, 5, 3, 7, 101, 18, 4, 19, -99, -88, -77, -66, -55, -44, -33],
    ]
    for nums in inputs:
        r = Solution().lengthOfLIS_dp(nums)
        print(f'{nums}  ==> {r}')
