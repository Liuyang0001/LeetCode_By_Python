#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] number-of-islands
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) < 1: return 0
        res = 0
        rows, cols = len(grid),len(grid[0])
        visit = [[0]*cols for _ in range(rows)]

        def dfs(i, j):
            # 越界不再遍历
            if i < 0 or i > rows - 1 or \
                j < 0 or j > cols-1 or \
                    visit[i][j] == 1 or grid[i][j] == '0':
                return
            visit[i][j] = 1
            # DFS：二维矩阵的上下左右
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visit[i][j] == 0:
                    dfs(i, j)
                    res += 1
        return res
# @lc code=end