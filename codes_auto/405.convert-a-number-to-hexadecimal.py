#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] convert-a-number-to-hexadecimal
#
class Solution:
    def toHex(self, num: int) -> str:
        num &= 0xFFFFFFFF
        s = "0123456789abcdef"
        res = ""
        mask = 0b1111
        while num > 0:
            # 每次取后四位
            res += s[num & mask]
            num >>= 4
        return res[::-1] if res else "0"
# @lc code=end