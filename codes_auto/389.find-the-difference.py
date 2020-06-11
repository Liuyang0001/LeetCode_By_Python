#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] find-the-difference
#
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord,t))-sum(map(ord,s)))
# @lc code=end