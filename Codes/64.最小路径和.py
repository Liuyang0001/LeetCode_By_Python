#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from typing import List
# @lc code=start


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        if m == 1:  # 只有一行
            return sum(grid[0])
        if n == 1:  # 只有一列
            return sum(list(*zip(*grid)))
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[0][j-1] + grid[0][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][0] + grid[i][0]
                else:
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == "__main__":
    grid = [[1, 2, 5], [3, 2, 1]]
    S = Solution()
    res = S.minPathSum(grid)
    print(res)
# @lc code=end
