#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
import functools
class Solution:
    @functools.lru_cache(None)
    def minCut(self, s: str) -> int:
        if s == s[::-1]: return 0
        res = float("inf")
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                res = min(self.minCut(s[i:]) + 1, res)
        return res
# @lc code=end

