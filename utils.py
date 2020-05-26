# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Dict, List, Optional


class TreeNode:
    """树节点"""

    def __init__(self, x):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __repr__(self):
        return f'{self.__class__.__name__}({self.val})'


class ListNode:
    """链表节点"""

    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

    # def __eq__(self, other: ListNode) -> bool:
    #     return self.val == other.val and self.next == other.next

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
    """链表转列表"""
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    return ret


def list2tree(nums: List[int]) -> TreeNode:
    """列表转二叉树"""
    tree: List[TreeNode] = []
    for i, v in enumerate(nums):
        tree.append(None if v is None else TreeNode(v))

    nt = len(tree)
    j = 0
    for i in range(nt):
        if tree[i]:
            left, right = j * 2 + 1, j * 2 + 2
            if right >= nt:
                break
            tree[i].left = tree[left]
            tree[i].right = tree[right]
            j += 1
    return tree[0]
