# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        r = head

        # Find nth next element
        ltr_distance = 0
        while ltr_distance < n:
            r = r.next
            ltr_distance += 1

        # if right is tail.next, we need to remove head
        if r == None:
            return head.next

        # Move both pointers until right is tail
        while r.next:
            l = l.next
            r = r.next

        # Remove left's next element
        l.next = l.next.next

        return head
