#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#
from collections import Counter
# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        elif n==1: return 10
        dp = [1, 10] + [0] * (n - 1)
        mul = 9
        for i in range(2, min(11, n + 1)):
            mul *= 11-i
            dp[i] = dp[i-1] + mul
        # print(dp)
        return dp[-1]
# @lc code=end

