#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] excel-sheet-column-number
#
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        base = 26
        for i,letter in enumerate(s[::-1]):
            res += (ord(letter)-64)*(base**i)
        return res
# @lc code=end