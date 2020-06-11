#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] reconstruct-itinerary
#
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
        tickets.sort()
        for tic in tickets:
            graph[tic[0]].append(tic[1])
        res = []
        def helper(cur):
            while graph[cur]:
                nxt = graph[cur].pop(0)
                helper(nxt)
            res.insert(0,cur)
        helper('JFK')
        return res
# @lc code=end

# @lc code=end