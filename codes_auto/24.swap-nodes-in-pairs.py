#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] swap-nodes-in-pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        sec = head.next
        save = head.next.next
        
        head.next = self.swapPairs(save)
        sec.next = head
        
        return sec
# @lc code=end