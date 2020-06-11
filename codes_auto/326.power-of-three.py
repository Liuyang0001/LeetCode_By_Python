#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] power-of-three
#
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
        
# @lc code=end