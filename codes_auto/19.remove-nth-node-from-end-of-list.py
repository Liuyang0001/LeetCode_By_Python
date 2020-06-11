#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] remove-nth-node-from-end-of-list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        
        prefast,preslow=dummyHead,dummyHead
        fast,slow = head,head
        while n>0:
            prefast = prefast.next
            fast = fast.next
            n-=1
        while fast:
            fast = fast.next
            slow = slow.next
            prefast = prefast.next
            preslow = preslow.next
        preslow.next=slow.next
        del slow
        return dummyHead.next
# @lc code=end