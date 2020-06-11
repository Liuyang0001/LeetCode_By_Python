#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] reverse-linked-list-ii
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution():
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        # 找到翻转链表部分的前一个节点, 1->2->3->4->5->NULL, m = 2, n = 4 指的是 节点值为1
        for _ in range(m-1):
            pre = pre.next
        # 用双指针,进行链表翻转
        # print("pre:", pre.val)
        rear1 = pre # 翻转部分的前一个结点
        rear2 = pre.next # 翻转部分的第一个结点，翻转后为尾结点
        cur_node = pre.next
        # 翻转部分的头结点
        dummy2 = ListNode(-1)
        for _ in range(n-m+1):
            # 头插法翻转链表
            save_node = cur_node.next
            cur_node.next = dummy2.next
            dummy2.next = cur_node
            cur_node = save_node
        # 将翻转部分 和 原链表拼接
        rear2.next = cur_node
        rear1.next = dummy2.next
        return dummy.next

# @lc code=end