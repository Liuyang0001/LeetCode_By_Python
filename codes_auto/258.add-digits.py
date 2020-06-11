#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] add-digits
#
class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1)%9+1 if num!=0 else 0
# @lc code=end