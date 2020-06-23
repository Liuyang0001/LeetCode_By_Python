#
# @lc app=leetcode.cn id=1000006 lang=python3
#
# [1000006] one-away-lcci
#
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        len1, len2 = len(first), len(second)
        # dp[i][j] - 字符串first[:i]和字符串second[:j]的编辑距离
        dp = [[float("inf")] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if first[i - 1] == second[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        # print(dp)
        return dp[len1][len2] == 0 or dp[len1][len2] == 1

# @lc code=end