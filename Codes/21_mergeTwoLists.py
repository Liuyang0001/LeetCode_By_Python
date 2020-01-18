'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)  #合并后的新的头结点
        # 分别创建三个链表的指针
        l1_p, l2_p, l3_p = l1, l2, l3
        # 两指针所指不完全为空
        while l1_p and l2_p:
            # 将较小的那个结点接到l3的尾端
            if l1_p.val < l2_p.val:
                l3_p.next=l1_p
                l1_p= l1_p.next
            else:
                l3_p.next=l2_p
                l2_p=l2_p.next
            l3_p = l3_p.next
        # 将剩余的部分复制给l_others，均为空则为None
        l_others = l1_p if l1_p else l2_p
        l3_p.next = l_others
        # 返回除了头指针之外的结点
        return l3.next

# 递归解法
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 先考虑递归边界问题
        if l1 == None:
            return l2
        elif l2==None:
            return l1
        # 最后会返回l1，l2中较小的为头结点
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1 
        elif l1.val>=l2.val:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
            