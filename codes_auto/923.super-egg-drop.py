#
# @lc app=leetcode.cn id=923 lang=python3
#
# [923] super-egg-drop
#
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # floor:N层  鸡蛋：K个
        # 特判
        if K == 1 or N == 1: return N
        dp = [0]*(K+1)
        res = 0
        # K个鸡蛋扔x次可以覆盖多少楼层
        while dp[0] < N:
            for k in range(0, K):
                dp[k] = dp[k]+dp[k+1]+1
            print(dp)
            res += 1
        return res

# @lc code=end