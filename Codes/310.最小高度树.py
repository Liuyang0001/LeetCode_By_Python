#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#
from typing import List
# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]
        # 创建邻接表
        neighbors = [set() for _ in range(n)]
        for edge in edges:
            neighbors[edge[0]].add(edge[1])
            neighbors[edge[1]].add(edge[0])
        print(neighbors)
        # 入度为1的加进队列
        que = [i for i in range(n) if len(neighbors[i]) == 1]
        while n > 2:
            n -= len(que)
            nxt_que = []
            for cur in que:
                # 无向图两个点的邻接表都要删除对应点
                # 与叶子节点相连的点找到
                adj = neighbors[cur].pop()
                # 相连的点删去这个叶子节点
                neighbors[adj].remove(cur)
                if len(neighbors[adj]) == 1:
                    nxt_que.append(adj)
            que = nxt_que
        return que
# @lc code=end