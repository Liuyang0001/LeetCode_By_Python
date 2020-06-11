#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] add-two-numbers
#
# 官方解法
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0) # 建立一个头结点
        curr, carry = dummyHead, 0 #curr表当前结点；carry表进位
        while l1 or l2: # 不全为空
            sum = 0
            if l1: # l1非空
                sum += l1.val
                l1 = l1.next
            if l2: # l2非空
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
        if carry > 0: # 需要进位，使得链表加长
            curr.next = ListNode(1)
        return dummyHead.next; #返回除头结点之后链表
# @lc code=end