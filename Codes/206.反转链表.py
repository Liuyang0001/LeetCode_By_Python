#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        dummyHead = ListNode(1)
        dummyHead.next = head
        cur = dummyHead
        while cur:
            save = cur.next
            cur.next = dummyHead.next
            dummyHead.next = cur
            cur = save
        head.next = None
        return dummyHead.next
# @lc code=end

