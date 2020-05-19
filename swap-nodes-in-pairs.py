# -*- coding: utf-8 -*-

"""24. 两两交换链表中的节点(https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
"""

from utils import ListNode, list2node, node2list


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        dummy: ListNode = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            mid, back = current.next, current.next.next
            mid.next, current.next = back.next, back
            current = back.next = mid
        return dummy.next


if __name__ == '__main__':
    inputs = [
        list2node([1, 2, 3]),
        list2node([1, 2, 3, 4]),
        list2node([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ]
    for v in inputs:
        r = Solution().swapPairs(v)
        print(f'{node2list(r)}')
