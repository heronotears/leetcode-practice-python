# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Dict, List, Optional


class TreeNode:
    """树节点"""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other: TreeNode) -> bool:
        return (self.val == other.val and self.left == other.left and
                self.right == other.right)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.val})'


class ListNode:
    """链表节点"""

    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

    def __eq__(self, other: ListNode) -> bool:
        return self.val == other.val and self.next == other.next

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
