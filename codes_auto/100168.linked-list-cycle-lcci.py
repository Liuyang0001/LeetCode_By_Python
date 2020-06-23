#
# @lc app=leetcode.cn id=100168 lang=python3
#
# [100168] linked-list-cycle-lcci
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dic = {}
        while head:
            if dic.get(head,0)==0:
                dic[head]=1
                head = head.next
            else:
                return head
        return None

# @lc code=end