#
# @lc app=leetcode.cn id=100240 lang=python3
#
# [100240] magic-index-lcci
#
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i==num:
                return i
        return -1

# @lc code=end