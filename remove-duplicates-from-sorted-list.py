# -*- coding: utf-8 -*-

"""83. 删除排序链表中的重复元素(https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)
"""

from typing import Optional

from utils import ListNode, list2node, node2list


class Solution:

    def deleteDuplicates(self, head: ListNode) -> Optional[ListNode]:
        if not head:
            return
        flag = set()
        ptr = prev = head
        while ptr:
            if ptr.val in flag:
                prev.next = ptr.next
            else:
                prev = ptr
                flag.add(ptr.val)
            ptr = ptr.next
        return head


if __name__ == '__main__':
    inputs = [
        list2node([]),
        list2node([1]),
        list2node([1, 1]),
        list2node([1, 1, 1]),
        list2node([1, 1, 2]),
        list2node([1, 1, 2, 3, 3]),
    ]
    for v in inputs:
        r = Solution().deleteDuplicates(v)
        print(f'{node2list(r)}')
