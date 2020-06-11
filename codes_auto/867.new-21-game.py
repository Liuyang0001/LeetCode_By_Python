#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] new-21-game
#
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0 for _ in range(K + W)]
        for i in range(K, K + W):
            if i <= N:
                dp[i] = 1
        for i in range(K - 1, -1, -1):
            if i == K - 1:
                s = 0
                for j in range(1, W + 1):
                    s += dp[i + j]
            dp[i] = s / W
            s += dp[i]
            s -= dp[i+W]
        return dp[0]
# @lc code=end