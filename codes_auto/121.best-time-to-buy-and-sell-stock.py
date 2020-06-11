#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] best-time-to-buy-and-sell-stock
#
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [0]*(n)
        cur_min=nums[0]
        for i in range(1,n):
            if nums[i]>=cur_min:
                dp[i]=nums[i]-cur_min
            else:
                cur_min = nums[i]
        # print(dp)
        return max(dp)
            
# @lc code=end