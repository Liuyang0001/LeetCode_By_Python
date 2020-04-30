#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#
from leetcode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummyHead1 = ListNode(-1)
        dummyHead2 = ListNode(-1)
        p = dummyHead1 # 奇链表的表尾
        q = dummyHead2 # 偶链表的表尾
        cur,cnt = head, 1
        while cur:
            if cnt % 2 == 1:
                p.next = cur
                p = p.next
            else:
                q.next = cur
                q = q.next
            cur = cur.next
            cnt += 1
        # 两个链表拼接
        p.next = dummyHead2.next
        q.next = None
        return dummyHead1.next
# @lc code=end

