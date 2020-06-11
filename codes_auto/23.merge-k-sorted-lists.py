#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] merge-k-sorted-lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummyHead = ListNode(None)
        p = dummyHead
        nodes = []
        for l in lists:
            while l != None:
                nodes.append(l.val)
                l = l.next
        for node in sorted(nodes):
            p.next=ListNode(node)
            p=p.next
        return dummyHead.next
# @lc code=end