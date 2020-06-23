#
# @lc app=leetcode.cn id=100258 lang=python3
#
# [100258] swap-numbers-lcci
#
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[0]+numbers[1]
        numbers[1] = numbers[0]-numbers[1]
        numbers[0] = numbers[0]-numbers[1]
        return numbers
# @lc code=end