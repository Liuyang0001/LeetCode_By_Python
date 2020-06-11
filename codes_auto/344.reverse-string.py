#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] reverse-string
#
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]
# @lc code=end