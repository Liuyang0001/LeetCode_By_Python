#
# @lc app=leetcode.cn id=100160 lang=python3
#
# [100160] string-to-url-lcci
#
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ","%20")
# @lc code=end