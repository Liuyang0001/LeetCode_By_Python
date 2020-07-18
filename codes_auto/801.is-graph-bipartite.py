#
# @lc app=leetcode.cn id=801 lang=python3
#
# [801] is-graph-bipartite
#
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dye = defaultdict(int)
        def DFS(s, color):
            dye[s] = color
            for i in graph[s]:
                # 已经上色了，如果和我一样表示不行
                if dye[i] == color:
                    return False
                # 没上色就染成和我相反的
                if not dye[i]:
                    if not DFS(i, -color):
                        return False
            return True
        for i in range(len(graph)):
            # 没被染色的就继续染色
            if not dye[i]:
                if not DFS(i, 1):
                    return False
        return True
# @lc code=end