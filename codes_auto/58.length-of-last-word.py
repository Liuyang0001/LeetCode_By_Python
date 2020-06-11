#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] length-of-last-word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.strip().split(" ")
        return len(res[-1])
# @lc code=end