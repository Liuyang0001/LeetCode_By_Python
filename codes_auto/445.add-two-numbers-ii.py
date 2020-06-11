#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] add-two-numbers-ii
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1,num2 = "",""
        while l1:
            num1+=str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        res = int(num1)+int(num2)
        dummyHead = ListNode(-1)
        rear = dummyHead
        for i in str(res):
            newNode = ListNode(int(i))
            rear.next = newNode
            rear = newNode
        return dummyHead.next
# @lc code=end