#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] coin-change
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]+[float("inf")] * amount
        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1]!=float("inf") else -1
# @lc code=end