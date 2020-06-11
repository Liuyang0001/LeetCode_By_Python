#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] power-of-two
#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # print(bin(-16)[2:])
        return bin(n)[2:].count("1")==1 if n>=0 else False
# @lc code=end