#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from bisect import bisect_right
        # 使用二分法寻找右边界
        # 使用双指针寻找答案
        left, right = 0, min(len(numbers) - 1, bisect_right(numbers, target))  # 最大右边界
        while left <= right:  # 闭合都无所谓，因为有答案
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
# @lc code=end

