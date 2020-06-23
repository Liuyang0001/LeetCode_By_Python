#
# @lc app=leetcode.cn id=1000012 lang=python3
#
# [1000012] sorted-merge-lcci
#
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        if n==0: return
        A[:] = A[:-n]+B
        A.sort()
# @lc code=end