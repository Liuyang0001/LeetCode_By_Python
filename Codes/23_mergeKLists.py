'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 暴力法
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        new_List = ListNode(None)
        p = new_List
        nodes = []
        # 将每个结点的值都加入列表中
        for l in lists:
            while l != None:
                nodes.append(l.val)
                l = l.next
        # 对列表进行排序，依次生成结点加入新链表
        for node in sorted(nodes):
            p.next=ListNode(node)
            p=p.next
        return new_List.next


# 解法2:利用优先级队列
from Queue import PriorityQueue

class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                # 根据结点的数据域val为优先级加入队列
                q.put((l.val, l))
        # 每次取出最小的数据域的结点，
        # 再将取出的结点后继加入队列。
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

