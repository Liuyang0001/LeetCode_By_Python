#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] combination-sum-iv
#
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        # print(dp)
        return dp[target]
                    
# @lc code=end