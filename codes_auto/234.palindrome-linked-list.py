#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] palindrome-linked-list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        mid,fast = head,head
        dummyHead = ListNode(None)
        while fast and fast.next:
            # 快指针走两步        
            fast = fast.next.next
#             翻转前部分链表
            save = mid.next
            mid.next = dummyHead.next
            dummyHead.next = mid
            mid = save
        head.next = None
        if fast: mid = mid.next
        p = dummyHead.next
        while p and mid and p.val==mid.val:
            p = p.next
            mid = mid.next
        return p==mid==None
        
# @lc code=end