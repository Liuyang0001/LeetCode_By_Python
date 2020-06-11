#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] reverse-integer
#
class Solution:
    def reverse(self, x: int) -> int:
        flag=1 if x>0 else -1
        x = int(str(abs(x))[::-1])*flag
        return x if -2**31<=x<=2**31-1 else 0
# @lc code=end