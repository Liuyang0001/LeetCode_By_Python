#
# @lc app=leetcode.cn id=1000007 lang=python3
#
# [1000007] kth-node-from-end-of-list-lcci
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        dummyHead = ListNode(None)
        dummyHead.next = head
        fast = slow = dummyHead
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val
# @lc code=end