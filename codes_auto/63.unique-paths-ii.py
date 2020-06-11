#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] unique-paths-ii
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:#空
            return 0
        # 起点或者终点存在障碍
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(1,n):
            if(obstacleGrid[0][i]!=1):
                dp[0][i]=dp[0][i-1]
        for j in range(1,m):
            if(obstacleGrid[j][0]!=1):
                dp[j][0]=dp[j-1][0]
        for x in range(1,m):
            for y in range(1,n):
                if(obstacleGrid[x][y]!=1):
                    dp[x][y]=dp[x-1][y]+dp[x][y-1]
        return dp[-1][-1]

# @lc code=end