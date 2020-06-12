#
# @lc app=leetcode.cn id=1580 lang=python3
#
# [1580] shuffle-the-array
#
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if n<2: return nums
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res
# @lc code=end