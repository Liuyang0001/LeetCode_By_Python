#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] search-a-2d-matrix-ii
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        row,col = len(matrix), len(matrix[0])
        # index = [[0, 0] for _ in range(row)]
        # for i in range(row):
        #     index[0] = matrix[i][0]
        #     index[1] = matrix[i][-1]
        for i in range(row):
            ind = bisect_left(matrix[i], target)
            if ind>=col: continue
            if matrix[i][ind] == target:
                return True
        return False
# @lc code=end