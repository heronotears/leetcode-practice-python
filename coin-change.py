# -*- coding: utf-8 -*-

"""322. 零钱兑换(https://leetcode-cn.com/problems/coin-change/)
"""

import unittest
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float('inf')
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == inf else dp[amount]


class TestSolution(unittest.TestCase):

    def test_coinChange(self):
        self.assertEqual(Solution().coinChange([2], 3), -1)
        self.assertEqual(Solution().coinChange([1, 2, 5], 11), 3)


if __name__ == '__main__':
    unittest.main()
