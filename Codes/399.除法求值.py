#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 顶点表
        nodes = set()
        res = [0] * len(queries)
        # 构建图【邻接表】
        # {node1：(node2, 结点值得商),(..., ...)}
        graph = defaultdict(set)
        for i in range(len(equations)):
            nodes.add(equations[i][0])
            nodes.add(equations[i][1])
            graph[equations[i][0]].add((equations[i][1],values[i]))
            graph[equations[i][1]].add((equations[i][0], 1 / values[i]))
        print(graph)
        # 深度优先查找
        def dfs(start, end, graph):
            for node in graph[start]:
                if node[0] == end:
                    return node[1]
                elif node[0] not in visited:
                    visited.add(node[0])
                    v = dfs(node[0],end,graph)
                    if v != -1:
                        return node[1] * v
            return -1

        for i in range(len(queries)):
            visited = set()
            if queries[i][0] not in nodes or queries[i][1] not in nodes:
                res[i] = -1
            elif queries[i][0] == queries[i][1]:
                res[i] = 1
            else:
                res[i] = dfs(queries[i][0],queries[i][1],graph)
        return res

# @lc code=end

