# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Using extra space for dict
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     valuesA = {}
    #     while headA:
    #         valuesA[headA] = True
    #         headA = headA.next

    #     while headB:
    #         if headB in valuesA:
    #             return headB
    #         headB = headB.next

    #     return None

    # Smart way to traverse through lists several times
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1
