# -*- coding: utf-8 -*-

"""2. 两数相加(https://leetcode-cn.com/problems/add-two-numbers/)
"""

from typing import List, Optional


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f'{self.__class__.__name__}({self.val})'


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result: Optional[ListNode] = None
        prev: Optional[ListNode] = None
        carry = 0
        while l1 or l2 or carry:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            sum = l1v + l2v + carry
            if sum >= 10:
                carry, sum = divmod(sum, 10)
            else:
                carry = 0
            n = ListNode(sum)
            if result:
                prev.next = n
                prev = prev.next
            else:
                result = prev = n
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result


def create_singly_linked_list(data: List[int]) -> Optional[ListNode]:
    r: ListNode = ListNode(data[0])
    p: ListNode = r
    for v in data[1:]:
        p.next = ListNode(v)
        p = p.next
    return r


def node2list(node: ListNode) -> List:
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    return ret


if __name__ == '__main__':
    L1 = create_singly_linked_list([2, 4, 3])
    L2 = create_singly_linked_list([5, 6, 4])
    result = Solution().addTwoNumbers(L1, L2)
    print(f'{node2list(L1)} + {node2list(L2)} = {node2list(result)}')

    L1 = create_singly_linked_list([2, 4, 3])
    L2 = create_singly_linked_list([5, 6, 7, 9])
    result = Solution().addTwoNumbers(L1, L2)
    print(f'{node2list(L1)} + {node2list(L2)} = {node2list(result)}')
