#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
from typing import List
# @lc code=start
class Solution:
    # 思想：该方法的每一步总是输出当前无前趋（即入度为零）的顶点
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 课程的长度
        n = len(prerequisites)
        # 没有课程，当然可以完成课程的学习
        if n == 0: return True
        # 入度数组，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表
        adj = [set() for _ in range(numCourses)]

        # 想要学习课程 0 ，你需要先完成课程 1 ，
        # 我们用一个匹配来表示他们: [0,1]
        # [0,1] 表示 1 在先，0 在后
        # 注意：邻接表存放的是后继 i 结点的集合
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        # print("in_degrees", in_degrees)
        # 首先遍历一遍，把所有入度为 0 的结点加入队列
        que = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                que.append(i)
        counter = 0
        while que:
            top = que.pop(0)
            counter += 1
            for i in adj[top]:
                in_degrees[i] -= 1
                # 入度为0，加进que
                if in_degrees[i] == 0:
                    que.append(i)

        return counter == numCourses

# @lc code=end

# 拓扑排序。
# 构建的邻接表就是我们通常认识的邻接表，每一个结点存放的是后继结点的集合。
# 该方法的每一步总是输出当前无前趋（即入度为零）的顶点。
# 为避免每次选入度为0的顶点时扫描整个存储空间，
# 可设置一个队列暂存所有入度为0的顶点。

# 具体做法如下：
# 1、在开始排序前，扫描对应的存储空间，将入度为0的顶点均入队列。
# 2、只要队列非空，就从队首取出入度为 0的顶点，将这个顶点输出到结果集中，
# 并且将这个顶点的所有邻接点的入度减1，在减1以后，发现这个邻接点的入度为0，就继续入队。
# 最后检查结果集中的顶点个数是否和课程数相同即可。