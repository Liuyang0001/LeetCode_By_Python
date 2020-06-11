#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] valid-anagram
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
# @lc code=end