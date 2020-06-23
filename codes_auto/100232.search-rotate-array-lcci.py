#
# @lc app=leetcode.cn id=100232 lang=python3
#
# [100232] search-rotate-array-lcci
#
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        try:
            return arr.index(target)
        except:
            return -1
# @lc code=end