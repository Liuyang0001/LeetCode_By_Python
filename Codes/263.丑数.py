#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0: return False
        for tem in [2, 3, 5]:
            while num % tem == 0:
                num //= tem
        return num == 1
# @lc code=end