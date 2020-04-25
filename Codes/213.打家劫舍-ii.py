#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n < 4: return max(nums)
        # dp
        def helper(nums):
            nums[2]+= nums[0]
            for i in range(3,n-1):
                nums[i] += max(nums[i - 2], nums[i - 3])
            return max(nums[-2:])
        # 首尾只能取一个
        return max(helper(nums[1:]),helper(nums[:-1]))
# @lc code=end