# -*- coding: utf-8 -*-

"""82. 删除排序链表中的重复元素 II(https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)
"""

import unittest

from utils import ListNode, list2node, node2list


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = current = head
        prev = dummy
        repeated = 0
        while current and current.next:
            if current.val == current.next.val:
                repeated = 1
            else:
                if repeated:
                    prev.next = current.next
                else:
                    prev = current
                repeated = 0
            current = current.next
        if repeated:
            prev.next = None
        return dummy.next


class TestSolution(unittest.TestCase):

    def test_deleteDuplicates(self):
        def func(v):
            return node2list(Solution().deleteDuplicates(list2node(v)))

        inputs = [
            [1, 1, 2, 4],
            [1, 1, 2, 4, 4],
            [1, 2, 3, 3, 4, 4, 5],
            [1, 1, 1, 2, 3, 3],
        ]
        outputs = [
            [2, 4],
            [2],
            [1, 2, 5],
            [2],
        ]
        result = [func(v) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
