#
# @lc app=leetcode.cn id=1000017 lang=python3
#
# [1000017] factorial-zeros-lcci
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while(n > 0):
            result += n // 5
            n //= 5
        return result
# @lc code=end