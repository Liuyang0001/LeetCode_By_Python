#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] make-two-arrays-equal-by-reversing-sub-arrays
#
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(arr)==sorted(target)
# @lc code=end