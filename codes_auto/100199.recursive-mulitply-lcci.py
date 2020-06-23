#
# @lc app=leetcode.cn id=100199 lang=python3
#
# [100199] recursive-mulitply-lcci
#
class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A == 0 or B == 0: return 0
        if A == 1: return B
        # 调整A小B大
        if A>B: A,B = B,A
        return self.multiply(A-1,B) + B
# @lc code=end