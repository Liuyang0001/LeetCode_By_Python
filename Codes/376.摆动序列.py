#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#
from typing import List
# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        up, down = 1,1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                # 这次上升=到上次下降+1
                up = down + 1
            elif nums[i] < nums[i - 1]:
                # 这次下降=到上次上升+1
                down = up + 1
        return max(up,down)
# @lc code=end