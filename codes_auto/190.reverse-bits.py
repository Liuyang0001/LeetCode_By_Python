#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] reverse-bits
#
class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:]
        res = ("0"*(32-len(bin_n))+bin_n)[::-1]
        return int(res,base=2)
# @lc code=end