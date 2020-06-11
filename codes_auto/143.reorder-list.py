#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] reorder-list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        from collections import deque
        if not head or not head.next: return
        nodes = deque()
        p = head
        while p:
            nodes.append(p)
            p = p.next
        rear = None
        while len(nodes) > 1:
            cur = nodes.popleft()
            next_node = nodes.pop()
            cur.next = next_node
            if rear: rear.next = cur
            rear = next_node
        if nodes:
            cur = nodes.pop()
            rear.next = cur
            rear = cur
        rear.next = None


# @lc code=end