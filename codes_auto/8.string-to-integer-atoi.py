#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] string-to-integer-atoi
#
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
# @lc code=end