#
# @lc app=leetcode.cn id=100185 lang=python3
#
# [100185] rotate-matrix-lcci
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [list(x)[::-1] for x in zip(*matrix)]
# @lc code=end