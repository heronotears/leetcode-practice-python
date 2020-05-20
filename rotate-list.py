# -*- coding: utf-8 -*-

"""61. 旋转链表(https://leetcode-cn.com/problems/rotate-list/)
"""

from typing import Optional

from utils import ListNode, list2node, node2list


class Solution:

    def rotateRight(self, head: ListNode, k: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head

        n = 1
        old = head
        while old.next:
            n += 1
            old = old.next
        old.next = head

        ptr = head
        pos = n - k % n - 1
        for i in range(pos):
            ptr = ptr.next
        new_head = ptr.next
        ptr.next = None
        return new_head


if __name__ == '__main__':
    inputs = [
        [list2node([1, 2, 3, 4, 5]), 11],
        [list2node([1, 2, 3, 4, 5]), 5],
        [list2node([1, 2, 3, 4, 5]), 4],
        [list2node([1, 2, 3, 4, 5]), 3],
        [list2node([1, 2, 3, 4, 5]), 2],
        [list2node([1, 2, 3, 4, 5]), 1],
        [list2node([0, 1, 2]), 4],
        [list2node([0, 1, 2]), 3],
        [list2node([0, 1, 2]), 2],
        [list2node([0, 1, 2]), 1],
    ]
    for h, n in inputs:
        r = Solution().rotateRight(h, n)
        print(f'{n} ==> {node2list(r)} ==> {r}')
