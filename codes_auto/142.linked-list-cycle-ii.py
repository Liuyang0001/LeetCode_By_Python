#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] linked-list-cycle-ii
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = {}
        count = 0
        while head:
            if head not in nodes:
                nodes[head] = count
                count += 1
            else:
                return head
            head = head.next
        return None
        
        
# @lc code=end