#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] power-of-four
#
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        n = len(bin(num))
        return bin(num)=="0b1"+(n-3)*"0" and n%2==1
# @lc code=end