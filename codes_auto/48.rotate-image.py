#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] rotate-image
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [i[::-1] for i in zip(*matrix)]
# @lc code=end