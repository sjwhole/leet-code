from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        node = head
        while node:
            nodes.append(node)
            node = node.next

        nodes.sort(key=lambda x: x.val)

        root = ListNode()
        cur = root
        for node in nodes:
            cur.next = node
            cur = cur.next

        cur.next = None

        return root.next
