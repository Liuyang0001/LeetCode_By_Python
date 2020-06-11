#
# @lc app=leetcode.cn id=1514 lang=python3
#
# [1514] minimum-value-to-get-positive-step-by-step-sum
#
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [0]*n
        # dp[0] = nums[0] if nums[0]>0 else 1-nums[0]
        start = 1 if nums[0]>0 else 1-nums[0]
        res = start
        for i in range(n):
            res+=nums[i]
            if res<1:
                start+= 1-res
                res=1
        return start
            
# @lc code=end