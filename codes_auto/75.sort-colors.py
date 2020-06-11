#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] sort-colors
#
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c_nums = Counter(nums)
        index = 0
        for i in range(3):
            for _ in range(c_nums[i]):
                nums[index] = i
                index += 1


# @lc code=end