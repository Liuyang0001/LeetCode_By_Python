#
# @lc app=leetcode.cn id=100231 lang=python3
#
# [100231] coin-lcci
#
class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [1]+[0]*n
        for coin in [1,5,10,25]:
            for offset in range(n-coin+1):
                dp[coin+offset] += dp[offset]
        return dp[n]%1000000007
# @lc code=end