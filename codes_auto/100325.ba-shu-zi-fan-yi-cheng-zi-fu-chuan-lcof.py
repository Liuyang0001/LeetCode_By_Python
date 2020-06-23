#
# @lc app=leetcode.cn id=100325 lang=python3
#
# [100325] ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
#
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        if not num: return 0

        dp = [1] * len(num)     # 初始状态设置 dp[0]=1
        for i in range(1, len(num)):
            # 当前数字和后一个数字可以组合
            if num[i - 1] == '1' or num[i - 1] == '2' and '0' <= num[i] < '6':
                dp[i] = dp[i-1] + dp[i-2]
            else:   # 当前数字必需独立编码
                dp[i] = dp[i - 1]

        return dp[-1]
# @lc code=end