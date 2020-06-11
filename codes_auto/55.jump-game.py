#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] jump-game
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<=1: return True
        # dp 到位置能到达的最远距离
        for i in range(1, n):
            if nums[i-1]>=i:
                nums[i] = max(nums[i-1], i+nums[i])
            else: # 到达不了位置i
                return False
        return True
# @lc code=end