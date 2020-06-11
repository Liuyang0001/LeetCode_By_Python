#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] valid-palindrome
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tem = ""
        for i in s.lower():
            if "0"<=i<="9" or "a"<=i<="z":
                tem+=i
        return tem==tem[::-1]
# @lc code=end