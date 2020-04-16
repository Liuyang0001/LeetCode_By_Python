#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        nums.sort()
        for i in range(0,n-1,3):
            if nums[i] == nums[i + 1] == nums[i + 2]:
                continue
            else: return nums[i]
        return nums[-1]
# @lc code=end

