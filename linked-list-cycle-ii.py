# -*- coding: utf-8 -*-

"""142. 环形链表 II(https://leetcode-cn.com/problems/linked-list-cycle-ii/)
"""

from typing import Optional, Set

from utils import ListNode


class Solution:

    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        """集合解法"""
        if not head:
            return
        flag: Set[ListNode] = set()
        while head:
            if head in flag:
                return head
            flag.add(head)
            head = head.next

    def detectCycleWithPointer(self, head: ListNode) -> Optional[ListNode]:
        """双指针解法"""
        point = self.meet(head)
        if not point:
            return
        p1 = head
        p2 = point
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    @staticmethod
    def meet(head: ListNode) -> Optional[ListNode]:
        if not head:
            return
        slow: ListNode = head
        fast: ListNode = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow


if __name__ == '__main__':
    from utils import list2node

    inputs = [
        list2node([], -1),
        list2node([1, 0]),
        list2node([1, 0], 0),
        list2node([3, 2, 0, 4]),
        list2node([3, 2, 0, 4], 1),
        list2node(list(range(-3, 5))),
        list2node(list(range(-3, 5)), 3),
    ]
    for v in inputs:
        r1 = Solution().detectCycle(v)
        r2 = Solution().detectCycleWithPointer(v)
        print(f'{r1} ==> {r2}')
