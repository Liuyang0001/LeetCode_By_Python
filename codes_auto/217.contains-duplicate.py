#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] contains-duplicate
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)
# @lc code=end