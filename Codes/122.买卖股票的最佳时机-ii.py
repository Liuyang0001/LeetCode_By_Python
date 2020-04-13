#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit
# @lc code=end

