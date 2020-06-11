#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] move-zeroes
#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, cnt = 0, 0
        for num in nums:
            if num != 0:
                nums[slow] = num
                slow += 1
            else: cnt += 1
        nums[:] = nums[:slow]+[0]*cnt
# @lc code=end