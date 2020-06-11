#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] remove-duplicates-from-sorted-list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head and head.next:
            pre = head
            p = head.next
        else:
            return head
        while p:
            if pre.val == p.val:
                pre.next = p.next
                p = p.next
            else:
                pre = pre.next
                p = p.next
        return head
# @lc code=end