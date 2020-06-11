#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] set-matrix-zeroes
#


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_x, zero_y = set(), set()
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    zero_x.add(x)
                    zero_y.add(y)
        # print(zero_x)
        # print(zero_y)
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if x in zero_x or y in zero_y:
                    matrix[x][y] = 0
        # print(matrix)
# @lc code=end