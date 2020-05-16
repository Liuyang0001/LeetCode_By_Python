#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
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
# 库函数
# return hex(num & 0xFFFFFFFF)[2:]