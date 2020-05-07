#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#
import bisect
from typing import List
# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        # 相当于建了一个排序队列,[(值:(对应坐标))]
        que = [(matrix[0][0], (0, 0))]
        visited = set(((0,0))) # 访问过得结点
        self.cnt = 0 # 计数
        while que:
            # 弹出最小的key值，取其对应坐标
            x, y = que.pop(0)[1]
            self.cnt += 1 # 计数
            if self.cnt == k: return matrix[x][y]
            # 当前的右方和下方元素入队（二分法插入）
            for x_off, y_off in [(0, 1),(1, 0)]:
                i, j = x + x_off, y + y_off
                # print(i, j,visited)
                if 0 <= i < row and 0 <= j < col and (i, j) not in visited:
                    bisect.insort(que, (matrix[i][j],(i,j)))
                    visited.add((i,j))
# @lc code=end