#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        dummyHead = ListNode(-1)
        dummyHead.next = head
        fast, slow = dummyHead.next, dummyHead
        while fast:
            if fast.val == val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
        return dummyHead.next

# @lc code=end

