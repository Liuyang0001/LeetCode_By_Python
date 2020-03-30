#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p = head
        p1 = head1 = ListNode(-1)
        p2 = head2 = ListNode(-1)
        while p != None:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p1.next = head2.next
        p2.next = None # 尾边界
        del head2
        return head1.next
# @lc code=end

