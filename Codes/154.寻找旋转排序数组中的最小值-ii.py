#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:  # mid == right
            # 出现重复值，使其向左靠拢
                right -= 1
        return nums[left]
# @lc code=end

