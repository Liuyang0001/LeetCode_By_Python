#
# @lc app=leetcode.cn id=1000011 lang=python3
#
# [1000011] robot-in-a-grid-lcci
#
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if not obstacleGrid: return []
        if obstacleGrid[0][0]==1: return []
        row,col = len(obstacleGrid),len(obstacleGrid[0])
        if row==col==1: return [[0,0]]
        self.res = []
        visited = {}
        def dfs(cur_x,cur_y,tem):
            if cur_x>=row or cur_y>=col:
                return
            if not tem or obstacleGrid[cur_x][cur_y]==1:
                return
            if cur_x==row-1 and cur_y==col-1:
                self.res =  tem
                return
            if visited.get((cur_x,cur_y),0)==0:
                visited[(cur_x,cur_y)] = 1
            else:
                return
            dfs(cur_x,cur_y+1,tem+[[cur_x,cur_y+1]])
            dfs(cur_x+1,cur_y,tem+[[cur_x+1,cur_y]])

        dfs(0,0,[[0,0]])
        return self.res
# @lc code=end