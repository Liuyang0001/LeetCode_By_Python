#
# @lc app=leetcode.cn id=1000021 lang=python3
#
# [1000021] smallest-k-lcci
#
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]
# @lc code=end