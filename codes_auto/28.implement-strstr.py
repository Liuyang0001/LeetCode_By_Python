#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] implement-strstr
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else: return -1
# @lc code=end