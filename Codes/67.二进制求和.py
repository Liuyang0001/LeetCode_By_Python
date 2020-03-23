#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = int(a, base=2) + int(b, base=2)
        return bin(res)[2:]
# @lc code=end
