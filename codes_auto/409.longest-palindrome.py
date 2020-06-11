#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] longest-palindrome
#
class Solution:
    def longestPalindrome(self, s: str) -> int:
        return len(s) - max(0,sum([s.count(i)%2 for i in set(s)])-1)
# @lc code=end