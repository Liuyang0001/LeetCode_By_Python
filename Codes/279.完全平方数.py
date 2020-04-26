#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        tem = n**0.5
        if tem == int(tem): return 1
        # dp初始都为1构成的路径
        # 自底向上进行更新最短的路径
        dp = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            # 可选的路径点为（1，i^½+1)
            for j in range(1,int(i**(0.5))+1):
                dp[i] = min(dp[i], dp[i-j*j] + 1)
        return dp[-1]
            
# @lc code=end

