#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] unique-paths
#
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         # 初始化DP数组为第一行第一列均为1，其余为0
#         dp=[[1]*n]+[[1]+[0]*(n-1) for _ in range(m-1)]
#         for i in range(1,m):
#             for j in range(1,n):
#                 dp[i][j]=dp[i-1][j]+dp[i][j-1]
#         return dp[-1][-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j]+=cur[j-1]
        return cur[-1]
# @lc code=end