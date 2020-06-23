#
# @lc app=leetcode.cn id=100181 lang=python3
#
# [100181] convert-integer-lcci
#
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        # A与B转成32位二进制，两者进行异或操作，不同则产生1
        # 最后数“1”即可
        return bin((A & 0xffffffff) ^ (B & 0xffffffff)).count('1')
# @lc code=end