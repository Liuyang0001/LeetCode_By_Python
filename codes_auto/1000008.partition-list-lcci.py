#
# @lc app=leetcode.cn id=1000008 lang=python3
#
# [1000008] partition-list-lcci
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyHead1 = ListNode(None)
        dummyHead2 = ListNode(None)
        rear1,rear2 = dummyHead1,dummyHead2
        while head:
            # print(head.val)
            if head.val<x:
                rear1.next = head
                rear1 = head
            else:
                rear2.next = head
                rear2 = head
            head = head.next
        rear2.next = None
        if rear1:
            rear1.next = dummyHead2.next
        else:
            return dummyHead2.next
        return dummyHead1.next
# @lc code=end