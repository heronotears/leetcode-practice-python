# -*- coding: utf-8 -*-

"""19. 删除链表的倒数第N个节点(https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)
"""

from typing import Optional

from utils import ListNode, list2node, node2list


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        """双指针解法"""
        if not head:
            return
        slow = fast = head
        while fast.next:
            fast = fast.next
            if n > 0:
                n -= 1
            else:
                slow = slow.next
        # 考虑长度大于或者等于链表长度的情况
        if n > 0:
            T = head.next
            head = T
        else:
            T = slow.next
            slow.next = T.next
        del T
        return head

    def removeNthFromEnd_Dummy(self, head: ListNode, n: int) -> Optional[ListNode]:
        """双指针解法: 哑节点"""
        if not head:
            return
        dummy: ListNode = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while fast:
            fast = fast.next
            if n >= 0:
                n -= 1
            else:
                slow = slow.next
        T = slow.next.next
        slow.next = T
        del T
        return dummy.next

    def removeNthFromEnd_Dummy2(self, head: ListNode, n: int) -> Optional[ListNode]:
        """双指针解法: 哑节点"""
        if not head:
            return
        dummy: ListNode = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while n >= 0:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        T = slow.next.next
        slow.next = T
        del T
        return dummy.next


if __name__ == '__main__':
    inputs = [
        # [list2node([]), 1],
        # [list2node([1]), 1],
        # [list2node([1, 2]), 2],
        [list2node([1, 2, 3, 4, 5]), 2],
    ]
    for h, n in inputs:
        # r1 = Solution().removeNthFromEnd(h, n)
        r2 = Solution().removeNthFromEnd_Dummy2(h, n)
        # print(f'{node2list(r1)} ==> {r1}')
        print(f'{node2list(r2)} ==> {r2}')
        print('#' * 80)
