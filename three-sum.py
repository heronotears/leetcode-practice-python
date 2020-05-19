# -*- coding: utf-8 -*-

"""15. 三数之和(https://leetcode-cn.com/problems/3sum/)
"""

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)
        if n < 3:
            return answer

        nums.sort()
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L, R = i + 1, n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                else:
                    answer.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
        return answer


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, 0, 0]))
    print(Solution().threeSum([-2, 0, 0, 2, 2]))
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
