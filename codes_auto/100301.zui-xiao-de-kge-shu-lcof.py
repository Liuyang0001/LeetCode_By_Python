#
# @lc app=leetcode.cn id=100301 lang=python3
#
# [100301] zui-xiao-de-kge-shu-lcof
#
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr: return []
        arr.sort()
        return arr[:k]

# @lc code=end