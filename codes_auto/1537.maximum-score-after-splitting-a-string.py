#
# @lc app=leetcode.cn id=1537 lang=python3
#
# [1537] maximum-score-after-splitting-a-string
#
class Solution:
    def maxScore(self, s: str) -> int:
        if not s: return 0
        res = 0
        for i in range(1,len(s)):
            s1 = s[:i].count("0")
            s2 = s[i:].count("1")
            res = max(res,s1+s2)
        return res
# @lc code=end