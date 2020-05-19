# -*- coding: utf-8 -*-

from typing import Dict, List, Optional


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

    def __repr__(self):
        return f'ListNode({self.val})'


def list2node(data: List, pos: int = None) -> Optional[ListNode]:
    """列表转链表 如果指定 pos 表示有环"""
    if not data:
        return
    index: Dict[int, ListNode] = {}
    head: Optional[ListNode] = None
    current: Optional[ListNode] = None
    for i, v in enumerate(data):
        n = ListNode(v)
        index[i] = n
        if head:
            current.next = n
            current = current.next
        else:
            head = current = n
    if pos is not None:
        current.next = index[pos]
    return head


def node2list(node: ListNode) -> List:
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    return ret
