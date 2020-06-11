#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] minimum-cost-for-tickets
#
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        # dp[i] 为 0 表示当天不旅行，为 -1 表示当天旅行
        for i in days:    dp[i] = -1
        for i in range(1, days[-1] + 1):
            # 若当天不旅行，花费不变
            if dp[i] == 0:    dp[i] = dp[i - 1]
            else:
            # 若当天旅行，分别看
            # 1.当天买日票；2.一周前买周票；3.一月前买月票
            # 三种情况哪一个最便宜
                dp[i] = min(
                    # 按照理解，一周前和一月前应该分别是
                    # dp[i - 7] + costs[1],
                    # dp[i - 30] + costs[2]
                    # 加 max 是为了预防新年第一周时 i-7<0、第一月内 i-30<0
                    dp[i - 1] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2]
                )
        return dp[-1]
# @lc code=end