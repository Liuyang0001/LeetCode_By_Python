#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] course-schedule
#
class Solution:
    # 思想：该方法的每一步总是输出当前无前趋（即入度为零）的顶点
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 课程的长度
        clen = len(prerequisites)
        # 没有课程，当然可以完成课程的学习
        if clen == 0: return True
        # 入度数组，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表
        adj = [set() for _ in range(numCourses)]

        # 想要学习课程 0 ，你需要先完成课程 1 ，
        # 我们用一个匹配来表示他们: [0,1]
        # [0,1] 表示 1 在先，0 在后
        # 注意：邻接表存放的是后继 successor 结点的集合
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        # print("in_degrees", in_degrees)
        # 首先遍历一遍，把所有入度为 0 的结点加入队列
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        counter = 0
        while queue:
            top = queue.pop(0)
            counter += 1
            for successor in adj[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)

        return counter >= numCourses

# @lc code=end