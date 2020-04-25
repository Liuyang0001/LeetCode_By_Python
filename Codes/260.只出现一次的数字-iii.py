#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)<=2: return nums
        d = sorted(Counter(nums).items(), key=lambda x: x[1])
        res = [d[0][0], d[1][0]]
        return res
# @lc code=end

