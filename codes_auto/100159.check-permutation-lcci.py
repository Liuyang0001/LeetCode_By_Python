#
# @lc app=leetcode.cn id=100159 lang=python3
#
# [100159] check-permutation-lcci
#
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1)==sorted(s2)
# @lc code=end