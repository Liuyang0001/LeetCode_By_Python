#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1)%9+1 if num!=0 else 0
# @lc code=end

# 数学归纳法：
# k=x
# k+1=x+1 当x=9时：k+1=1
# k+2=x+2 或 2
# 显然 k%9可以推测，根据0-9调整表达式