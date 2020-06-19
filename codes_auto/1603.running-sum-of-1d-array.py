#
# @lc app=leetcode.cn id=1603 lang=python3
#
# [1603] running-sum-of-1d-array
#
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        tem = 0
        for i in nums:
            tem += i
            res.append(tem)
        return res
# @lc code=end