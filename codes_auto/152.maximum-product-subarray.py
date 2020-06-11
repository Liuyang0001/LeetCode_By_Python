#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] maximum-product-subarray
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        # dp = [到当前位置的最大乘积,到当前位置的最小乘积]
        dp = [nums[0],nums[0]]
        res = nums[0]
        for i in range(1,n):
            tem1 = dp[0]*nums[i]
            tem2 = dp[1]*nums[i]
            # 更新dp数组
            dp[0],dp[1]=max(tem1,tem2,nums[i]),min(tem1,tem2,nums[i])
            # res = max(res, 到当前的最大值)  
            res = max(res, dp[0])
        return res
# @lc code=end