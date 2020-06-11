#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] valid-perfect-square
#
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in [0, 1, 4]: return True
        x = num // 2
        # 牛顿逼近法
        while x * x > num:
            x = (x + num // x) // 2
        return x**2==num
            
# @lc code=end