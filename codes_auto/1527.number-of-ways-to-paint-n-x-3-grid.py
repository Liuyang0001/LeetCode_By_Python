#
# @lc app=leetcode.cn id=1527 lang=python3
#
# [1527] number-of-ways-to-paint-n-x-3-grid
#
class Solution:
    def numOfWays(self, n: int) -> int:
        x, y, mod = 6, 6, 1000000007
        for i in range(1, n):
            prex, prey = x, y
            x = (3 * prex + 2 * prey) % mod
            y = (2 * prex + 2 * prey) % mod
        return (x + y) % mod
# @lc code=end