#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] kth-smallest-element-in-a-sorted-matrix
#
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        # [ (值:(坐标)) ]
        dic = [(matrix[0][0],(0, 0))]
        visited = set(((0,0)))
        self.cnt = 0
        while dic:
            # print(dic)
            # print(matrix[x][y])
            x, y = dic.pop(0)[1]
            # visited.add((x, y))
            self.cnt += 1
            if self.cnt == k: return matrix[x][y]
            for x_off, y_off in [(0, 1),(1, 0)]:
                i, j = x + x_off, y + y_off
                # print(i, j,visited)
                if 0 <= i < row and 0 <= j < col and (i, j) not in visited:
                    bisect.insort(dic, (matrix[i][j],(i,j)))
                    visited.add((i,j))
# @lc code=end