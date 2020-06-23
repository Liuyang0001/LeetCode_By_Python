#
# @lc app=leetcode.cn id=100188 lang=python3
#
# [100188] sum-lists-lcci
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 特判 其中一个为空
        if not l1: return l2
        if not l2: return l1
        dummyHead = ListNode(None)
        rear = dummyHead
        carry = 0
        while l1 or l2 or carry:
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            newNode = ListNode(num%10)
            rear.next = newNode
            rear = newNode
            carry= num//10
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummyHead.next
# @lc code=end