#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
from typing import List
# @lc code=start


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_x, zero_y = [], []
        # 遍历矩阵找到需要变0的行和列
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    zero_x.append(x)
                    zero_y.append(y)
        # 对应位置变零
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if x in zero_x or y in zero_y:
                    matrix[x][y] = 0
        # print(matrix)
# @lc code=end
