#
# @lc app=leetcode.cn id=100203 lang=python3
#
# [100203] bianry-number-to-string-lcci
#
class Solution:
    def printBin(self, num: float) -> str:
        res, len_ = "0.", 2
        while num > 0 and len_<32:
            num *= 2
            if num >= 1:
                res += '1'
                num -= 1
            else:
                res += '0'
            len_ += 1
        return res if not num else "ERROR"
# @lc code=end