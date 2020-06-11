#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] sort-list
#
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 特判
        if not head or not head.next: return head
        pre, slow, fast = None, head, head
        # 快指针走两步，慢指针走一步
        # 找到中点，切成两个链表【归并排序】
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        # 继续拆分
        left = self.sortList(head)
        right = self.sortList(slow)
        # 开始合并
        return self.mergeTwoLists(left,right)
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


# @lc code=end