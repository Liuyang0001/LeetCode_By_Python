#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:

        flag = True if n > 0 else False
        res, n = 1, abs(n)
        while n:
            # 每次取得最后一位
            if n & 0x01:
                res *= x
            x *= x
            n >>= 1
        return res if flag else 1/res
# @lc code=end
