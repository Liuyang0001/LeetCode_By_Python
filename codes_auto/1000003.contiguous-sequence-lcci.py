#
# @lc app=leetcode.cn id=1000003 lang=python3
#
# [1000003] contiguous-sequence-lcci
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # res = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i],nums[i]+nums[i-1])
            # res = max(res,nums[i])
        return max(nums)
# @lc code=end