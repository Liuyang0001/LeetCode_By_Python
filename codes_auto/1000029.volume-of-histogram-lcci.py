#
# @lc app=leetcode.cn id=1000029 lang=python3
#
# [1000029] volume-of-histogram-lcci
#
class Solution:
    def trap(self, height: [int]) -> int:
        size = len(height)
        if size < 3: return 0
        left, right = 0, size - 1
        left_max, right_max = height[left], height[right]
        res = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res
# @lc code=end