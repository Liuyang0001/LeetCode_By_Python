#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
from typing import List
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        nums.sort()
        for i in range(0,n-1,2):
            if nums[i] == nums[i + 1]: continue
            else: return nums[i]
        return nums[-1]
# @lc code=end

