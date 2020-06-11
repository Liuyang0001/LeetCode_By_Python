#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] valid-number
#
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            res = float(s.strip())
            return True
        except:
            return False
# @lc code=end