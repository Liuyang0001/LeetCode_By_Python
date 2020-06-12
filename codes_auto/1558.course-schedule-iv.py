#
# @lc app=leetcode.cn id=1558 lang=python3
#
# [1558] course-schedule-iv
#
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], q: List[List[int]]) -> List[bool]:
        if n == 0: return []
        # 邻接表
        adj = [set() for _ in range(n)]
        
        @functools.lru_cache(None)
        def dfs(cur,node):
            adj[cur].add(node)
            for i in adj[node]:
                dfs(cur,i)
        
        for first,sec in prerequisites:
            dfs(sec,first)

        # print(adj)
        res = []
        for fro,cur in q:
            if fro in adj[cur]:
                res.append(True)
            else:
                res.append(False)
        return res
# @lc code=end