# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.is_visited = False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Extra array
        # silly = []
        # while head:
        #     if head.next in silly:
        #         return True
        #     silly.append(head.next)
        #     head = head.next
        # return False

        # Tortoise and hare
        try:
            tortoise = head
            hare = head.next
            while tortoise != hare:
                tortoise = tortoise.next
                hare = hare.next.next
            return True
        except:
            return False


print(Solution().hasCycle(ListNode(0)))
