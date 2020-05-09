#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#
import random
from leetcode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        self.head = head
    
    # 蓄水池抽样算法(k=1)
    # 到第i个被留下的概率为1/i
    def getRandom(self) -> int:
        count = 0
        reserve = 0
        cur = self.head
        while cur:
            count += 1
            rand = random.randint(1,count)
            if rand == count:
                reserve = cur.val
            cur = cur.next
        return reserve



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

