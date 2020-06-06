#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = {}
        res = 0
        for num in nums:
            if num not in lookup:
                # 判断左右是否可以连起来
                left = lookup[num - 1] if num - 1 in lookup else 0
                right = lookup[num + 1] if num + 1 in lookup else 0
                # 记录当前能够延展的最大长度
                cur_len = left + right + 1
                lookup[num] = cur_len
                # 更新查找表
                lookup[num - left] = cur_len
                lookup[num + right] = cur_len
                res = max(res, cur_len)
        return res
# @lc code=end

