#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.income = 0
        for i in range(len(prices)-1):
            buy = prices[i]
            max_income = max(prices[i+1:]) - buy
            if max_income > self.income:
                self.income = max_income
        return self.income
# @lc code=end

