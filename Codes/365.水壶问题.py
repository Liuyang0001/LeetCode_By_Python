#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#
import  math
# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # 两个桶一共都没有z升水，不可能实现
        if x + y < z: return False
        # 其中一个为0，特判
        if x == 0 or y == 0:
            return z == 0 or z == x + y
        # z = ax+by
        # z 对 x，y的最大公约数取余
        return z % math.gcd(x, y) == 0
# @lc code=end