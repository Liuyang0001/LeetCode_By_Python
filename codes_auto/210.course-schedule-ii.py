#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] course-schedule-ii
#
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = len(prerequisites)
        if n == 0: return [i for i in range(numCourses)]
        in_degrees = [0] * numCourses
        adj = [set() for _ in range(numCourses)]
        # 有向图
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)
        que, res = [], []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                que.append(i)
        while que:
            cur = que.pop(0)
            res.append(cur)
            for i in adj[cur]:
                in_degrees[i] -= 1
                if in_degrees[i] == 0:
                    que.append(i)
        return res if len(res)==numCourses else []

# @lc code=end