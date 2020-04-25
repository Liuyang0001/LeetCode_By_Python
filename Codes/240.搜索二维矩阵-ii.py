#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# import bisect
from bisect import bisect_left
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        row,col = len(matrix), len(matrix[0])
        for i in range(row):
            ind = bisect_left(matrix[i], target)
            if ind>=col: continue
            if matrix[i][ind] == target:
                return True
        return False
# @lc code=end

