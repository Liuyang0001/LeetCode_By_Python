#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in [0, 1, 4]: return True
        x = num // 2
        # 牛顿逼近法
        while x * x > num:
            x = (x + num // x) // 2
        return x**2==num
            
# @lc code=end

# 二分法
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in [0, 1, 4]: return True
        left, right = 3, 46340
        while left <= right:
            mid = (left + right) // 2
            tem = mid*mid
            if tem == num: return True
            elif tem < num:
                left += 1
            else:
                right -= 1
        return False