# -*- coding: utf-8 -*-

"""86. 分隔链表(https://leetcode-cn.com/problems/partition-list/)
"""

from utils import ListNode, list2node, node2list


class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        pa = after = ListNode(0)
        pb = before = ListNode(0)
        while head:
            if head.val < x:
                pb.next = head
                pb = pb.next
            else:
                pa.next = head
                pa = pa.next
            head = head.next

        pa.next = None
        pb.next = after.next
        return before.next


if __name__ == '__main__':
    inputs = [
        [list2node([1, 4, 3, 2, 5, 2]), 3]
    ]
    for v in inputs:
        r = Solution().partition(*v)
        print(f'{node2list(r)}')
