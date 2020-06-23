#
# @lc app=leetcode.cn id=100242 lang=python3
#
# [100242] sparse-array-search-lcci
#
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        try:
            return words.index(s)
        except:
            return -1
# @lc code=end