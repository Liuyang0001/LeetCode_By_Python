#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] number-of-1-bits
#
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
# @lc code=end