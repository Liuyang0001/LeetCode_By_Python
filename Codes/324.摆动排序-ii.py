#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#
from typing import List
# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        # 穿插排列
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
# @lc code=end

# 先对数组排序，分为大数部分和小数部分，再穿插排序。 
# 注意顺序，例如[1，2，4，4，4，6]这个数组，通过降序穿插得到[4,6,2,4,1,4]。
# 如果顺序排列，则会得到[1,4,2,4,4,6]不满足要求。 
# 这里是因为我们想尽量将小数部分的最大数放在边上，
# 这样只用靠近一个大数部分的最大数。