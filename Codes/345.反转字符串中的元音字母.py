#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # a e i o u
        def exchange(s, i, j):
            return s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
        n = len(s)
        left, right = 0, n-1
        while left < right:
            while s[left].lower() not in "aeiou" and left<right:
                left += 1
            while s[right].lower() not in "aeiou" and left< right:
                right -= 1
            # print(left,right)
            if left < right:
                s = exchange(s, left, right)
                left,right = left+1,right-1
        return s
# @lc code=end

