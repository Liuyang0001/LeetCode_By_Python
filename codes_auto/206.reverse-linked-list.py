#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] reverse-linked-list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next: return head
#         dummyHead = ListNode(None)
#         cur = head
#         while cur:
#             save = cur.next
#             cur.next = dummyHead.next
#             dummyHead.next = cur
#             cur=save
#         head.next = None
#         return dummyHead.next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tail
# @lc code=end