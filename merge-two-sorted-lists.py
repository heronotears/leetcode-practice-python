# -*- coding: utf-8 -*-

"""21. 合并两个有序链表(https://leetcode-cn.com/problems/merge-two-sorted-lists/)
"""

from utils import ListNode, list2node, node2list


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy: ListNode = ListNode(0)
        prev = dummy
        while l1 or l2:
            if not l1:
                prev.next = l2
                break
            if not l2:
                prev.next = l1
                break
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        return dummy.next


if __name__ == '__main__':
    inputs = [
        [list2node([1, 2, 4]), list2node([1, 3, 4])]
    ]
    for v in inputs:
        r = Solution().mergeTwoLists(*v)
        print(f'{node2list(r)}')
