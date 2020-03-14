#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None or k == 0:
            return head
        p = head  # 指针
        len_ListLink = 1
        # 遍历计算链表长度
        while p.next:
            len_ListLink += 1
            p = p.next
        # 找到原表尾的位置
        rear = p
        # 转折点位置
        t = len_ListLink - (k % len_ListLink)
        if t == len_ListLink:
            return head
        p = head  # 第二次遍历指针
        while t > 1:
            t -= 1
            p = p.next
        newRear = p
        newHead = p.next
        # 重新构建链表
        newRear.next = None
        rear.next = head
        return newHead
# @lc code=end
