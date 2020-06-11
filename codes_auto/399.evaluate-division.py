#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] evaluate-division
#
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        variables = set()
        ans = [0] * len(queries)
        graph = creategraph(equations,values,variables)

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
            if queries[i][0] not in variables or queries[i][1] not in variables:
                ans[i] = -1
            elif queries[i][0] == queries[i][1]:
                ans[i] = 1
            else:
                ans[i] = dfs(queries[i][0],queries[i][1],graph)
        return ans

def creategraph(equations,values,variables):
    graph = defaultdict(set)
    for i in range(len(equations)):
        variables.add(equations[i][0])
        variables.add(equations[i][1])
        graph[equations[i][0]].add((equations[i][1],values[i]))
        graph[equations[i][1]].add((equations[i][0],1/values[i]))
    return graph

# @lc code=end