#
# @lc app=leetcode.cn id=100171 lang=python3
#
# [100171] route-between-nodes-lcci
#
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        # 构建邻接表
        link_table = [[] for _ in range(n)]
        for i, j in graph:
            link_table[i].append(j)
        visted = [0]*n # 访问数组
        # BFS
        que = [start]
        while que:
            cur_node = que.pop(0)
            if target in link_table[cur_node]: return True
            for node in link_table[cur_node]:
                if visted[node]==0:
                    que.append(node)
            visted[cur_node] = 1
        return False
# @lc code=end