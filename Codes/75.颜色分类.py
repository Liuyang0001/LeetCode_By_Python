#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
from typing import List
# @lc code=start
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 调用Counter()进行统计每个数字的个数
        c_nums = Counter(nums)
        index = 0
        # 重新对原数组进行覆盖
        for i in range(3):
            for _ in range(c_nums[i]):
                nums[index] = i
                index += 1


# @lc code=end
