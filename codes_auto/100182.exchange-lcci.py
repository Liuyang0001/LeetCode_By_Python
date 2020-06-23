#
# @lc app=leetcode.cn id=100182 lang=python3
#
# [100182] exchange-lcci
#
class Solution:
    def exchangeBits(self, num: int) -> int:
        # 对于奇数位，使用 101010（即 0xAA）作为掩码，提取奇数位，并把它们右移一位；
        # 对于偶数位，使用 010101（即 0x55）作为掩码，提取偶数位，并把它们左移一位。
        # num的范围在[0, 2^30-1]之间，不会发生整数溢出。
        return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)
# @lc code=end