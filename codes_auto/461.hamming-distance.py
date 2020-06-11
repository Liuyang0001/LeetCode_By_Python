#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] hamming-distance
#
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count("1")
        
# @lc code=end