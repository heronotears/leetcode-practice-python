# -*- coding: utf-8 -*-

"""148. 排序链表(https://leetcode-cn.com/problems/sort-list/)
"""

import unittest

from utils import ListNode, list2node, node2list


class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        dummy = ListNode(0)
        dummy.next = head
        pivot = curr = head
        while curr.next:
            c_next = curr.next
            if curr.next.val < pivot.val:
                curr.next = curr.next.next
                c_next.next = dummy.next
                dummy.next = c_next
            else:
                curr = c_next
        right = self.sortList(pivot.next)
        pivot.next = None
        left = self.sortList(dummy.next)
        pivot.next = right
        return left


class TestSolution(unittest.TestCase):

    def test_sortList(self):
        inputs = [
            list2node([6, 4, 1, 5, 8, 7, 9, 3])
        ]
        outputs = [
            [1, 3, 4, 5, 6, 7, 8, 9]
        ]
        result = [node2list(Solution().sortList(v)) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
