#
# @lc app=leetcode.cn id=100164 lang=python3
#
# [100164] palindrome-linked-list-lcci
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        tem = []
        while head:
           tem.append(head.val)
           head=head.next
        return tem==tem[::-1]
# @lc code=end