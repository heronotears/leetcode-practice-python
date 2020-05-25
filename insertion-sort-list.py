# -*- coding: utf-8 -*-

"""147. 对链表进行插入排序(https://leetcode-cn.com/problems/insertion-sort-list/)
"""

import unittest

from utils import ListNode, list2node, node2list


class Solution:

    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(float('-inf'))
        prev = tail = dummy
        current = head
        while current:
            c_next = current.next
            if current.val >= tail.val:
                tail.next = current
                tail = current
            else:
                tail.next = c_next
                while prev.next and prev.next.val < current.val:
                    prev = prev.next
                current.next = prev.next
                prev.next = current
                prev = dummy
            current = c_next
        return dummy.next


class TestCase(unittest.TestCase):

    def test_insertionSortList(self):
        inputs = [
            list2node([4, 2, 1, 3]),
            list2node([-1, 5, 3, 4, 0])
        ]
        outputs = [
            [1, 2, 3, 4],
            [-1, 0, 3, 4, 5]
        ]
        result = [node2list(Solution().insertionSortList(v)) for v in inputs]
        self.assertSequenceEqual(result, outputs)


if __name__ == '__main__':
    unittest.main()
