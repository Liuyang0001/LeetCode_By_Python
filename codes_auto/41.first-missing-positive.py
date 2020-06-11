#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] first-missing-positive
#
from typing import List


class Solution:
    # 3 应该放在索引为 2 的地方
    # 4 应该放在索引为 3 的地方
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                # self.__swap(nums, i, nums[i] - 1)
                nums[nums[i]-1], nums[i] = nums[i],nums[nums[i]-1]

        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1

        return size + 1

# @lc code=end