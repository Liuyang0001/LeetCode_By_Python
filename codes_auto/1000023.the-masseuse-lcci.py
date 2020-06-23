#
# @lc app=leetcode.cn id=1000023 lang=python3
#
# [1000023] the-masseuse-lcci
#
class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n<3: return max(nums)
        nums[2]+=nums[0]
        for i in range(3,n):
            nums[i] += max(nums[i-2],nums[i-3])
        return max(nums[-2:])
# @lc code=end