#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] product-of-array-except-self
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        cur = 1
        cur_back = 1
        for i in range(n - 1):
            cur *= nums[i]
            cur_back *= nums[n - i - 1]
            res[i + 1] *= cur
            res[n - i - 2] *= cur_back

        return res
# @lc code=end