'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 非递归解法
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        # 创建一个不含任何信息的头结点，并添加到原链表的前面
        H = ListNode(None)
        H.next = head
        rear =H #指向已完成交换部分的尾结点，初始为头结点H
        pre,p = head,head.next #分别指向要交换的两个结点
        while p:
            # 重新调整结点位置
            pre.next = p.next
            p.next = pre
            rear.next = p
            # 更新指针
            rear = pre
            pre = pre.next
            p = pre.next if pre else None
        return H.next


# 递归解法
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 结点数为0或1时
        if head == None or head.next == None:
            return head
        # 每次处理两个结点，head和N
        N = head.next
        # head处理后变为后面的结点，
        # 需要和后面递归的首元素连接起来
        head.next = self.swapPairs(N.next)
        # 原来后面的元素放到前面
        N.next = head
        # 最后返回的是N（后面的变到了前面）
        return N