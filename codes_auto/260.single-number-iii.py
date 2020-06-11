#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] single-number-iii
#
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)<=2: return nums
        d = sorted(Counter(nums).items(), key=lambda x: x[1])
        res = [d[0][0], d[1][0]]
        return res
# @lc code=end