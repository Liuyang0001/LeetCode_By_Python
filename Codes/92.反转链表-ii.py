#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
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
class Solution():
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        # 找到翻转链表部分的前一个节点
        for _ in range(m-1):
            pre = pre.next
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
        # 拼接
        rear2.next = cur_node
        rear1.next = dummy2.next
        # head结点可能已经改变，返回头结点的下一节点
        return dummy.next

# @lc code=end

if __name__ == "__main__":
    S = Solution()
    ls = [1, 2]
    H = ListNode(-1)
    p = H
    for i in ls:
        p.next = ListNode(i)
        p = p.next
    head = H.next
    res = S.reverseBetween(head,1,2)
    while res:
        print(res.val)
        res = res.next