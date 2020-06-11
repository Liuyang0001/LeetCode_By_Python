#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] maximum-subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp = [float("-inf")]*len(nums)
        # dp[0]=
        for i in range(1,len(nums)):
            nums[i]=max(nums[i],nums[i-1]+nums[i])
        return max(nums)
# @lc code=end