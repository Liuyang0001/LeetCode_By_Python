#
# @lc app=leetcode.cn id=1574 lang=python3
#
# [1574] maximum-product-of-two-elements-in-an-array
#
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        nums.sort()
        res = max((nums[0]-1)*(nums[1]-1),(nums[-1]-1)*(nums[-2]-1),(nums[0]-1)*(nums[-1]-1))
        return res
# @lc code=end