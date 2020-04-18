#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        # 0,1分别存储最小值和最大值
        dp = [[0, 0] for _ in range(n)]
        # 初始化
        dp[0] = [nums[0],nums[0]]
        self.res = nums[0]
        for i in range(1, n):
            tem0 = dp[i - 1][0] * nums[i]
            tem1 = dp[i - 1][1] * nums[i]
            dp[i][0] = max(tem0, tem1, nums[i])
            dp[i][1] = min(tem0, tem1, nums[i])
            if dp[i][0] > self.res:
                self.res = dp[i][0]
        return self.res
# @lc code=end

