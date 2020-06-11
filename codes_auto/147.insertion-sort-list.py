#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] insertion-sort-list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummyHead = ListNode(float("-inf"))
        tail = dummyHead
        cur = head 
        while cur:
            # 大于当前排好部分的尾结点
            if tail.val <= cur.val:
                tail.next = cur
                tail = cur
                cur = cur.next
            else:
                # 保存下一个待插入结点
                save = cur.next
                tail.next = save
                # 上面判断过了，
                # 所以一定能找到插入的位置
                p = dummyHead
                while p.next and p.next.val < cur.val:
                    p = p.next
                cur.next = p.next
                p.next = cur

                # 下一个结点
                cur = save
        return dummyHead.next

# @lc code=end