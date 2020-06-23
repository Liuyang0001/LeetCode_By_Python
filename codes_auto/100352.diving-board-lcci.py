#
# @lc app=leetcode.cn id=100352 lang=python3
#
# [100352] diving-board-lcci
#
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0: return []
        elif shorter == longer: return [k*shorter]
        return list(range(shorter*k, longer*k + 1, (longer-shorter)))
# @lc code=end