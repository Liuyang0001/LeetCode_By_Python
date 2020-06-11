#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] merge-two-sorted-lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(None)
        rear = dummyHead
        p1,p2 = l1,l2
        while p1 and p2:
            if p1.val<=p2.val:
                rear.next = p1
                p1 = p1.next
            else:
                rear.next = p2
                p2 = p2.next
            rear = rear.next
        if p2: p1=p2
        rear.next = p1
        return dummyHead.next
# @lc code=end