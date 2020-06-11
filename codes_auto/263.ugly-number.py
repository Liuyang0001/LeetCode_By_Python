#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] ugly-number
#
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0: return False
        for e in [2, 3, 5]:
            while num % e == 0:
                num //= e
        return num == 1
# @lc code=end