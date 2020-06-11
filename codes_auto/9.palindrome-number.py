#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] palindrome-number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x)==str(x)[::-1] else False
    
# @lc code=end