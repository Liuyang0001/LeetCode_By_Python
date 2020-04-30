#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
from typing import List
# @lc code=cur
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # 排序 使得同一key的value有序
        tickets.sort() 
        for tic in tickets:
            graph[tic[0]].append(tic[1])
        res = []
        def helper(cur):
            while graph[cur]:
                nxt = graph[cur].pop(0)
                helper(nxt)
            # 一定可以有一条路径使得图全空
            # 有一条走通就返回
            res.insert(0,cur)
        helper('JFK')
        return res
# @lc code=end
