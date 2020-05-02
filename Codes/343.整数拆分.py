#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2,n+ 1):
            for j in range(1,i):
                dp[i] = max(dp[i], max(j, dp[j])*max(dp[i-j], i-j))
        return dp[-1]
# @lc code=end

