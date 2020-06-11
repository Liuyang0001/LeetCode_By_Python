#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] intersection-of-two-linked-lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        A = set()
        while headA:
            A.add(headA)
            headA = headA.next
        while headB:
            if headB in A:
                return headB
            headB = headB.next
        return None
        
# @lc code=end