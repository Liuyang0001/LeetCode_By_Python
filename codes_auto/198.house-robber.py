#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] house-robber
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n<3: return max(nums)
        dp = nums[:2]+[0]*(n-2)
        dp[2]=nums[0]+nums[2]
        for i in range(3,n):
            dp[i] = nums[i]+max(dp[i-2],dp[i-3])
        # print(dp)
        return max(dp[-2:])
# @lc code=end