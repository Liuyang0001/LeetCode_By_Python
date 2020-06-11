#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] linked-list-cycle
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        s = set()
        while head:
            if head in s: return True
            s.add(head)
            head = head.next
        return False
        
# @lc code=end