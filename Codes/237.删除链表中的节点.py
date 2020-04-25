#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#
from leetcode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node: 'ListNode') -> None:
        while node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None
# @lc code=end

