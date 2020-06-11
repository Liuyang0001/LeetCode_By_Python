#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] factorial-trailing-zeroes
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n >= 5:
            n = n // 5
            res += n
        return res
# @lc code=end