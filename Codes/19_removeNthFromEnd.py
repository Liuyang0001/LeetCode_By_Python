'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 设置双指针
        pre, p = head,head
        # 只有一个结点的情况
        if head.next==None:
            return None
        # p先向后移动n个位置
        for _ in range(n):
            p=p.next
        # 此时p为空，说明要删除的为头结点
        if not p:
            return head.next
        # 删除位置不为首尾结点，同步向后移动，直到p指向最后一结点
        while p.next:
            p=p.next
            pre=pre.next
        # 删除结点
        pre.next = pre.next.next
        # 返回头结点
        return head