#
# @lc app=leetcode.cn id=100304 lang=python3
#
# [100304] lian-xu-zi-shu-zu-de-zui-da-he-lcof
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        for i in range(1,n):
            nums[i] += max(nums[i-1],0)
        return max(nums)
# @lc code=end