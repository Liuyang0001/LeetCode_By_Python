#
# @lc app=leetcode.cn id=100163 lang=python3
#
# [100163] remove-duplicate-node-lcci
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        pre = head
        p = head.next # 遍历指针
        dic = {head.val:1}
        while p:
            if dic.get(p.val,0)==0:
                dic[p.val]=1
                pre.next = p
                pre = p
            p = p.next
        pre.next = None
        return head

            
# @lc code=end