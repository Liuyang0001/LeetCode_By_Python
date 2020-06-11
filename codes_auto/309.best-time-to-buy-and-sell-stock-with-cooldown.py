#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] best-time-to-buy-and-sell-stock-with-cooldown
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0, 0] for _ in range(n+1)]
        dp[0][1] = float('-inf')
        dp[1][1] = -prices[0]
        for i in range(2, n + 1):
            # 因为下面有i-2所以从2开始, 自行去填0-1的base case
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i-1])
        return dp[-1][0]
        
# @lc code=end