#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
from typing import List
# @lc code=start
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

# 受启发自精选题解 一个方法团灭 6 道股票问题
# 穷举，你有再多的状态，要做的就是一把梭全部列举出来。
# 这个问题的「状态」有三个，第一个是天数，第二个是允许交易的最大次数，
# 第三个是当前的持有状态（即之前说的 rest 的状态，
# 我们不妨用 1 表示持有，0 表示没有持有）。
# 然后我们用一个三维数组就可以装下这几种状态的全部组合：

# dp[i][k][0 or 1]
# 0 <= i <= n-1, 1 <= k <= K
# n 为天数，大 K 为最多交易数

# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
#               max(   选择 rest  ,             选择 sell      )

# 解释：今天我没有持有股票，有两种可能：
# 要么是我昨天就没有持有，然后今天选择 rest，所以我今天还是没有持有；
# 要么是我昨天持有股票，但是今天我 sell 了，所以我今天没有持有股票了。

# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
#               max(   选择 rest  ,           选择 buy         )

# 解释：今天我持有着股票，有两种可能：
# 要么我昨天就持有着股票，然后今天选择 rest，所以我今天还持有着股票；
# 要么我昨天本没有持有，但今天我选择 buy，所以今天我就持有股票了。
# dp[-1][k][0] = 0
# 解释：因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0 。
# dp[-1][k][1] = -infinity
# 解释：还没开始的时候，是不可能持有股票的，用负无穷表示这种不可能。
# dp[i][0][0] = 0
# 解释：因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0 。
# dp[i][0][1] = -infinity
# 解释：不允许交易的情况下，是不可能持有股票的，用负无穷表示这种不可能。



# 把上面的状态转移方程总结一下：

# base case：
# dp[-1][k][0] = dp[i][0][0] = 0
# dp[-1][k][1] = dp[i][0][1] = -infinity

# 状态转移方程：
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])


# 本题因为不限制买卖次数, 所以k这个维度可以省去. 状态转移即变为

# dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
# dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i-1])
