#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
from typing import List
# @lc code=start
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
# 回溯超时
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.cnt = 0
        nums.sort()
        def helper(target):
            if target == 0:
                self.cnt += 1
                return
            if target < 0: return
            for i in nums:
                helper(target - i)
        helper(target)
        return self.cnt