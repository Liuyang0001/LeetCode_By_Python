#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] single-number
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums: a^=i
        return a
# @lc code=end