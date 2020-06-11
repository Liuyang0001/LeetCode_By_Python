#
# @lc app=leetcode.cn id=390 lang=python3
#
# [390] elimination-game
#
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n < 2: return n
        return 2*(n//2+1-self.lastRemaining(n//2))
# @lc code=end