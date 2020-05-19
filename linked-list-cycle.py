# -*- coding: utf-8 -*-

"""141. 环形链表(https://leetcode-cn.com/problems/linked-list-cycle/)
"""

from typing import Set

from utils import ListNode


class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        """集合解法"""
        if not head:
            return False
        flag: Set[ListNode] = set()
        while head:
            if head in flag:
                return True
            flag.add(head)
            head = head.next
        return False

    def hasCycleWithPointer(self, head: ListNode) -> bool:
        """双指针解法"""
        if not head:
            return False
        slow: ListNode = head
        fast: ListNode = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


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
        r1 = Solution().hasCycle(v)
        r2 = Solution().hasCycleWithPointer(v)
        print(f'{r1} ==> {r2}')
