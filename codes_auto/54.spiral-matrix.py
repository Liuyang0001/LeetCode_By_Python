#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] spiral-matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res
# @lc code=end