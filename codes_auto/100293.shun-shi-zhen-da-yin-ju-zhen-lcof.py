#
# @lc app=leetcode.cn id=100293 lang=python3
#
# [100293] shun-shi-zhen-da-yin-ju-zhen-lcof
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res
# @lc code=end